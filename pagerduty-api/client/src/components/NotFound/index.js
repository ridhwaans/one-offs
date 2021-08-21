import React, { useEffect } from 'react';
import logo from '../../assets/logo.svg';
import '../../assets/App.css';

function NotFound() {
    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <p>
                Not found. Please go to /users
                </p>
            </header>
        </div>
    )
}

export default NotFound;
