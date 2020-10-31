import React, { useState } from 'react';
import './content.css';

const Content = () => {

    const [login, setLogin] = useState('');

    console.log(login);

    const Choice = () => {

        const authorization = (
            <div className="authorization">
                    <p>
                    Вам необходима авторизация
                    </p>
                </div>
        );
          
        const recommendation = (
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
        );

        if (login === '') {
            return (
                authorization
            );
        } else if (login !== '') {
            return (
                recommendation
            );
        };
    };

    return (
        <div className="container">
            <div className="left-column">
                <div className="login">
                    <input type='text' id='login' />
                    <button form='login' onClick={setLogin}>Логин</button>
                </div>
                <div className="information">
                    <p>Некоторая информация</p>
                </div>
            </div>
            <Choice />
        </div>
    );
};

export default Content;