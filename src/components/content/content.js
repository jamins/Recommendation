import React from 'react';
import './content.css';

const Content = () => {
    return (
        <div className="container">
            <div className="login">
                <input />
                <button>Логин</button>
            </div>
            <div className="recommendation">
                <div className="string-recommendation">
                    <h2>Книги</h2>
                    <p>Текст</p>
                </div>
                <div className="string-recommendation">
                    <h2>Книги</h2>
                    <p>Текст</p>
                </div>
                <div className="string-recommendation">
                    <h2>Книги</h2>
                    <p>Текст</p>
                </div>
            </div>
        </div>
    );
};

export default Content;