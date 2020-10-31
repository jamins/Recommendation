import React from 'react';
import './content.css';

const Content = () => {
    return (
        <div className="container">
            <div className="left-column">
                <div className="login">
                    <input type='text' placeholder='Например, Sweet_Alcatel'/>
                    <button>Логин</button>
                </div>
                <div className="information">
                    <p>Некоторая информация!</p>
                </div>
            </div>
            <div className="recommendation">
                <div className="string-recommendation">
                    <h2>Мероприятия</h2>
                    <p>Текст</p>
                </div>
                <div className="string-recommendation">
                    <h2>Мероприятия</h2>
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