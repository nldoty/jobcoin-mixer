import React from 'react';
import Jumbotron from 'react-bootstrap/Jumbotron';
import Loader from 'react-loader-spinner';


class Loading extends React.Component {
    render() {
        return (
            <div style={{width: '600px'}}>
                <Jumbotron>
                    <Loader type="TailSpin" color="#00BFFF" height={300} width={300} />
                    <div id="hi" style={{display: "flex", marginLeft: '200px', marginRight: '200px'}}>
                        <h3>Loading</h3><Loader style={{marginTop: '12px'}} type="ThreeDots" color="#000000" height={20} width={30} />
                    </div>
                </Jumbotron>
            </div>
        )
    }
}


export default Loading;
