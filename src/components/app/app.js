import React from 'react';
import './app.css';
import Header from '../header';
import Content from '../content';

const App = () => {
    return (
        <div className='app'>
            <Header />
            <Content />
        </div>
    );
};

export default App;