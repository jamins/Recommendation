import React, { Component } from 'react';
import './content.css';
import BookItem from '../book-item';
import PropTypes from 'prop-types';

class Content extends Component {
    constructor(props) {
        super(props);
        this.getData = this.getData.bind(this);
    };

    state = {
        value: 0,
        data: []
    };

    PropTypes = {
        value: PropTypes.number
    };

    id = [{id:1}, {id:2}, {id:3}];

    maxId = 4;

    searchInfo = (e) => {
        this.setState({
            value: e.target.value
        });
    };

    getData = async () => {
        await fetch(`https://culture-recommendation-service.herokuapp.com/recommendations/${this.state.value}`)
        .then(response => response.json())
        .then(data => this.setState({
            ...this.state,
            data: data
        }))
        .catch(err => console.log(err));
    };

    componentDidMount() {
        this.getData();
    };

    componentDidUpdate(prevProps) {
        if(this.state.value !== prevProps.value) {
            setTimeout(() => this.getData(), 1000);
        };
    };

    componentWillUnmount() {
        if(this.state.value === null) {
            clearInterval(setTimeout(() => this.getData(), 1000))
        };
    };

    onClick = () => {
        const { value } = this.state;
        this.setState({
            value: value + 1 
        });
    };

    render() {
        const { data, value } = this.state;
        
        return (
            <div className="container">
                <div className="left-column">
                    <div className="id-user">
                        <input type='number' id='search' value={value} onChange={this.searchInfo} disabled/>
                        <button onClick={this.onClick}>+</button>
                    </div>
                    <div className="information">
                        <p>Для нахождения предпочтений пользователя достаточно нажимать кнопку + для увеличения id пользователя</p>
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
                    <div className="string-recommendation-2">
                        <h2>Книги</h2>
                        <ol>
                            <li key={this.id.map((id) => {
                            return id.id
                            })}>
                            {data.map((data) => {
                            return <BookItem key={this.maxId++} data={data}/>
                            })}
                            </li>
                        </ol>
                    </div>
                </div>
            </div>
        );
    }
}


export default Content;