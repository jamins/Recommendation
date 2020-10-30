import React from 'react';
import './app.css';
import Header from '../header';
import Content from '../content';
import Footer from '../footer';

const App = () => {
    return (
        <div className='app'>
            <Header />
            <Content />
            <Footer />
        </div>
    );
};

export default App;