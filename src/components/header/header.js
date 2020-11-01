import React from 'react';
import './header.css';

const Header = () => {
    return (
        <div className='header'>
            <h1>Информация</h1>
            <p>
                Для получения блока рекомендаций необходим id. Изменяя id в соотвутствующеv поле, вы получите рекомендации
            </p>
        </div>
    );
};

export default Header;