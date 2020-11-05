import React from 'react';
import Jumbotron from 'react-bootstrap/Jumbotron';
import Button from 'react-bootstrap/Button'
import { checkMixerDepositAddress, mixCoinsFromAddress } from "../api";

class MixCoins extends React.Component {

    checkMixer = async () => {
        const mixer_address = this.props.location.address;

        const response = await checkMixerDepositAddress(mixer_address);

        const balance = parseInt(response['balance']);

        if (balance === 0) {
            const str = "No coins at address " + mixer_address + " found.\n Are you sure you sent coins to the address?";
            window.alert(str)
        } else {
            this.props.history.push({pathname: '/loading'})
            const formValues = this.props.location.formValues;

            const addressListAll = [
                formValues.address0.trim(),
                formValues.address1.trim(),
                formValues.address2.trim(),
                formValues.address3.trim(),
                formValues.address4.trim()
            ];

            const addressList = addressListAll.filter((item) => {
                return item !== '';
            });

            const body = {
                'addresses': addressList,
                'transactions': formValues.transactions,
                'timeout': formValues.timeout
            }


            const mix_response = await mixCoinsFromAddress(mixer_address, body);
            const mixer_transactions = mix_response['transactions'];
            this.props.history.push({pathname: '/success', transactions: mixer_transactions})

        }
    }

    render() {
        return (
            <div className="mixer_request" style={{width: '600px'}} >
                <Jumbotron>
                    <h1>Send Coins</h1>
                    <p>Please send us your coins to the following address, so they can be mixed:</p>
                    <br />
                    <h4>{this.props.location.address}</h4>
                    <p>When your coins are sent, click the Mix Coins button below to begin the mixing process.</p>
                    <p className='text-warning'>WARNING: Please only send coins with 8 significant digits. Otherwise,
                    the remainder will be lost in mixing!</p>
                    <Button onClick={this.checkMixer}>Mix Coins</Button>
                </Jumbotron>
            </div>
        )
    }
}

export default MixCoins;