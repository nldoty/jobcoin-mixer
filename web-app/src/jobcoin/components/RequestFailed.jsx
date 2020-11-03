import React from 'react';
import Jumbotron from 'react-bootstrap/Jumbotron';
import Button from 'react-bootstrap/Button'
import { Link } from 'react-router-dom';


class RequestFailed extends React.Component {
    render() {
        console.log(this.props);
        return (
            <div className="mixer_request" style={{width: '600px'}} >
                <Jumbotron>
                    <h1>Request Failed</h1>
                    <p>Something went wrong. To go home, click the link below.</p>
                    <Link to='/'><Button>Home</Button></Link>
                </Jumbotron>
            </div>
        )
    }
}

export default RequestFailed;
