import React from 'react';
import './App.css';
import GetAddresses from './jobcoin/components/GetAddresses'
import Error from './jobcoin/components/Error'
import 'bootstrap/dist/css/bootstrap.min.css';
import { Route, Switch } from 'react-router-dom';
import RequestSuccess from "./jobcoin/components/RequestSuccess";
import RequestFailed from "./jobcoin/components/RequestFailed";
import MixCoins from "./jobcoin/components/MixCoins";

function App() {
  return (
    <div className="App">
        <Switch>
            <Route path='/' component={GetAddresses} exact/>
            <Route path='/mix' component={MixCoins} />
            <Route path='/success' component={RequestSuccess} />
            <Route path='/failure' component={RequestFailed} />
            <Route component={Error} />
        </Switch>
    </div>
  );
}

export default App;
