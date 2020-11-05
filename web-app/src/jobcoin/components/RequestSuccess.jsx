import React from 'react';
import Jumbotron from 'react-bootstrap/Jumbotron';
import {Link} from "react-router-dom";
import Button from "react-bootstrap/Button";

class RequestSuccess extends React.Component {

    render() {
        return (
            <div className="mixer_request" style={{width: '600px'}} >
                <Jumbotron>
                    <h1>Success!</h1>
                    <h4>You should see the following transactions:</h4>
                    {this.props.location.transactions.map((transaction) => (
                        <p>{transaction}</p>
                    ))}
                    <Link to='/'><Button>Home</Button></Link>
                </Jumbotron>
            </div>
        )
    }
}

export default RequestSuccess;
