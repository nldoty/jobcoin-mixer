import React from 'react';
import Form from 'react-bootstrap/Form'
import Jumbotron from 'react-bootstrap/Jumbotron';
import Button from 'react-bootstrap/Button';
import {getUniqueMixerAddress} from "../api";


class GetAddresses extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            advanced: false,
            advanced_text: 'Show Advanced',
            showAddressList: true,
            formValues: {
                address0: "",
                address1: "",
                address2: "",
                address3: "",
                address4: "",
                transactions: "",
                timeout: "",
            },
            addressList: [
                'address0'
            ]
        }
    }

    showAdvanced = () => {
        if (this.state.advanced){
            this.setState({
                advanced: false,
                advanced_text: 'Show Advanced'
            });
        } else {
            this.setState({
                advanced: true,
                advanced_text: 'Hide Advanced'
            });
        }
    };

    addAddress = () => {
        const numAddresses = this.state.addressList.length;
        const newInput = `address${numAddresses}`;
        this.setState(prevState => ({
            addressList: prevState.addressList.concat(newInput),
            showAddressList: numAddresses !== 4
        }));
    };

    submitRequest = async () => {
        const formValid = !this.validateForm();

        if (formValid) {
            const formValues = this.state.formValues;
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
                addresses: addressList,
            }

            const response = await getUniqueMixerAddress(body);
            const mixer_unique_address = response['deposit_address'];

            if (mixer_unique_address) {
                this.props.history.push({pathname: '/mix', address: mixer_unique_address, formValues: this.state.formValues})
            }
        }
    }

    validateForm = () => {
        let errors = false;
        let errorString = "";
        const formValues = this.state.formValues;
        const addresses = [
            formValues.address0.trim(),
            formValues.address1.trim(),
            formValues.address2.trim(),
            formValues.address3.trim(),
            formValues.address4.trim()
        ];

        const transactions = formValues.transactions;
        const timeout = formValues.timeout;

        const trimmed_addresses = addresses.filter((item) => {
            return item !== '';
        });

        const num_trimmed_addresses = trimmed_addresses.length

        if (num_trimmed_addresses === 0) {
            errors = true;
            errorString += 'A minimum of one address must be defined.\n';
        }

        if (transactions !== "") {
            if (isNaN(transactions)) {
                errors = true;
                errorString += 'The transactions field must be a number.\n';
            }
            else {
                if (transactions > 20) {
                    errors = true;
                    errorString += 'The max number of transactions is 20.\n';
                }
                if (parseFloat(transactions) % 1 !== 0) {
                    errors = true;
                    errorString += 'The value for transactions must be an integer.\n';
                }
                if (num_trimmed_addresses > transactions) {
                    errors = true;
                    errorString += 'The number of transactions must be more than the number of addresses.\n';
                }
            }
        }

        if (timeout !== "") {
            console.log(timeout)
            if (isNaN(timeout)) {
                errors = true;
                errorString += 'The timeout field must be a number.\n';
            } else {
                if (timeout > 3) {
                    errors = true;
                    errorString += 'The max timeout time is 3 seconds.\n';
                }
                if (parseFloat(timeout) % 1 !== 0) {
                    errors = true;
                    errorString += 'The value for timeout must be an integer.\n';
                }
            }
        }

        if (errors) {
            window.alert(errorString);
        }

        return errors;
    };


    updateField = (item, value) => {
        const subState = Object.assign({}, this.state.formValues);
        subState[item] = value;
        this.setState({
            formValues: subState
        });
    };


    onFieldChange = (event) => {
        const id = event.target.id;
        const value = event.target.value;

        this.updateField(id, value);
    };


    render() {
        return (
            <div className="mixer_request" style={{width: '600px'}} >
                <Jumbotron>
                    <h1>Jobcoin Mixer</h1>
                    <p>
                        This is a simple user interface for making Jobcoin Mixer requests.
                    </p>
                    <Form>
                       <div id='dynamicAddressList'>
                           <Form.Group>
                               <Form.Label>Address</Form.Label>
                           <Form.Text className="text-muted">
                               The number of address fields to split your coins to. Max five addresses, one required.
                           </Form.Text>
                           {this.state.addressList.map((input, index) => (
                               <Form.Control className="mt-3" type="addresses"  placeholder={'Address ' + (index + 1)}
                                             onChange={(e) => this.onFieldChange(e)}
                                             key={input} id={input}/>
                           ))}
                           </Form.Group>
                       </div>
                    </Form>
                    {this.state.advanced ?
                        (<div>
                            <Form>
                                <Form.Group>
                                    <Form.Label>Total Transactions</Form.Label>
                                    <Form.Control type="transactions" onChange={(e) => this.onFieldChange(e)}
                                                  placeholder="Enter the total # of transactions (MAX 20)"
                                                  key='transactions' id='transactions'/>
                                    <Form.Text className="text-muted">
                                        This can spread out your transactions into multiple calls per address, randomly.
                                    </Form.Text>
                                </Form.Group>
                                <Form.Group>
                                    <Form.Label>Max Timeout</Form.Label>
                                    <Form.Control type="timeout" onChange={(e) => this.onFieldChange(e)}
                                                  placeholder="Enter the max timeout in seconds (MAX 3)"
                                                  key='timeout' id='timeout'/>
                                    <Form.Text className="text-muted">
                                        This allows us to spread out transactions randomly over a given period of time.
                                    </Form.Text>
                                    <Form.Text className="text-muted">
                                        This is intentionally short for demonstration purposes.
                                    </Form.Text>
                                </Form.Group>
                            </Form>
                        </div>)
                    : null}

                    <Button variant="secondary" className="mr-3" disabled={!this.state.showAddressList} onClick={this.addAddress}>Add address</Button>
                    <Button variant="secondary" className="mr-3" onClick={this.showAdvanced}>{this.state.advanced_text}</Button>
                    <br />
                    <br />
                    <Button variant="success" onClick={this.submitRequest}>Mix Coins</Button>
                </Jumbotron>
            </div>
        )
    }
}

export default GetAddresses;