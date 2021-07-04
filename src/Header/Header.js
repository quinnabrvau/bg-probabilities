import React from 'react';
import classes from './Header.module.css';

const Header = (props) => {
    return (
        <div>
            <div className={classes.Logos}>
                <a target="_blank" href="https://github.com/quinnabrvau/sbb-probabilities" rel="noopener noreferrer">
                    <img className={classes.Logo} src={require('../assets/github.png')} alt="Page's source code"/>
                </a>
            </div>
            <div>
                <div className={classes.Title}>
                    <h2>QuinnAbr's Hearthstone Battlegrounds Probability Calculator</h2>
                </div>
            </div>
        </div>
    );
}

export default Header;
