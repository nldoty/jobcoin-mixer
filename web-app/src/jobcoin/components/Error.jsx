import React from 'react';
import Jumbotron from 'react-bootstrap/Jumbotron';
import { Link } from "react-router-dom";
import Button from "react-bootstrap/Button";


class Error extends React.Component {


    render() {
        return (
            <div className="mixer_request" style={{width: '600px'}} >
                <Jumbotron>
                    <h1>Uh oh! Page not found :'(</h1>
                    <p>Looks like you've been poking around where you shouldn't be.</p>
                    <p> To go home, click the link below.</p>
                    <Link to='/'><Button>Home</Button></Link>
                </Jumbotron>
            </div>
        )
    }
}

export default Error;
