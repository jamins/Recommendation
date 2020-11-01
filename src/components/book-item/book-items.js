import React from 'react';
import './book-item.css';

const BookItem = ({ data }) => {
    const { age_rating, author, name, year } = data;
    return (
        <div>
            <div className="books">
                <p>{author}</p>
                <p>{name}</p>
                <p>Возраст: для {age_rating}-летних</p>
                <p>Год: {year}</p>
            </div>
        </div>
    );
};

export default BookItem;