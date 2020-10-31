import React from 'react';
import './content.css';

const Content = () => {

    const fetchData = async () => {
        const response = await fetch('https://culture-recommendation-service.herokuapp.com/recommendations/1');
        const data = await response.json();
        console.log(data);
    };

    fetchData();

    return (
        <div className="container">
            <div className="left-column">
                <div className="login">
                    <input type='text' id='login'/>
                    <button form='login'>Логин</button>
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