import React from 'react';
import './header.css';

const Header = () => {
    return (
        <div className='header'>
            <h1>Информация</h1>
            <p>
                Для получения блока рекомендаций необходима авторизация. Введя свой логин в соотвутствующее поле, вы получите рекомендации, основанные на ваших предпочтениях
            </p>
        </div>
    );
};

export default Header;