import torch
from torch import nn
from itertools import zip_longest
import copy



def get_list(n):
    if isinstance(n, (int, float)):
        return [n]
    elif hasattr(n, '__iter__'):
        return list(n)
    raise TypeError('layers configuraiton should be a single number or a list of numbers')

class EmbeddingNet(nn.Module):

    def __init__(self, n_users, n_books,
                 n_factors=50, embedding_dropout=0.02, 
                 hidden=10, dropouts=0.2):
        
        super().__init__()
        hidden = get_list(hidden)
        dropouts = get_list(dropouts)
        n_last = hidden[-1]
        
        def gen_layers(n_in):
            nonlocal hidden, dropouts
            assert len(dropouts) <= len(hidden)
            
            for n_out, rate in zip_longest(hidden, dropouts):
                yield nn.Linear(n_in, n_out)
                yield nn.ReLU()
                if rate is not None and rate > 0.:
                    yield nn.Dropout(rate)
                n_in = n_out
            
        self.u = nn.Embedding(n_users, n_factors)
        self.m = nn.Embedding(n_books, n_factors)
        self.dropout = nn.Dropout(embedding_dropout)
        self.hidden = nn.Sequential(*list(gen_layers(n_factors * 2)))
        self.fc = nn.Linear(n_last, 1)
        self._init()
        
    def forward(self, users, books):
        features = torch.cat([self.u(users), self.m(books)], dim=1)
        x = self.dropout(features)
        x = self.hidden(x)
        out = torch.sigmoid(self.fc(x))
        return out
    
    def _init(self):
        def init(m):
            if type(m) == nn.Linear:
                torch.nn.init.xavier_uniform_(m.weight)
                m.bias.data.fill_(0.01)
                
        self.u.weight.data.uniform_(-0.05, 0.05)
        self.m.weight.data.uniform_(-0.05, 0.05)
        self.hidden.apply(init)
        init(self.fc)



book_weights = torch.load("books_weights.pt", map_location=torch.device('cpu'))

n = 450509
m = 624908

book_net = EmbeddingNet(
    n_users=n, n_books=m, 
    n_factors=25, hidden=[50, 50], 
    embedding_dropout=0.05, dropouts=[0.5, 0.5])

book_net.load_state_dict(book_weights)
book_net.eval()

def predict_book(features):
    tmp_tensor = torch.LongTensor(features)
    return book_net(tmp_tensor[:,0], tmp_tensor[:,1])

"""clf_weights = torch.load("clf_weights.pt", map_location=torch.device('cpu'))

n = 289169
m = 26678

clf_net = EmbeddingNet(
   n_users=n, n_books=m,
   n_factors=50, hidden=[200, 200, 200],
   embedding_dropout=0.05, dropouts=[0.5, 0.5, 0.25])

clf_net.load_state_dict(clf_weights)
clf_net.eval()

def predict_clf(features):
    tmp_tensor = torch.LongTensor(features)
    return clf_net(tmp_tensor[:,0], tmp_tensor[:,1])
"""
