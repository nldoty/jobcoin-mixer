
# Gemini Coin Web App

This is my front end implementation for the coinmixer challenge.

## MVP   

##### This is the basic MVP process:    
**1.** A user opens the app and enters some information about the mix they want to do:       
  **a.** A list of addresses to send the mixed coins to.       
  **b.**(OPTIONAL) The number of transactions they'd like to take place.        
  **c.**(OPTIONAL) The max time length to delay transactions by.        
**2.** After submitting, the app displays a unique, random address to send coins to.    
**3.** Once the coins are sent to the address, the UI displays the transactions that the user should see.


## Pages
#### GetAddresses.jsx
This is the main entry file, hosted at `/`. It allows you to enter addresses to send to, as well as optional values for the number of transactions, and a time delay on transactions.

#### MixCoins.jsx
This page provides you with a unique address to send your coins to, and a button to mix your coins. It checks that coins have been added to the address before mixing and alerts you if the balance is `0`. 

#### RequestSuccess.jsx
This page is shown if your transactions were successful, and it lists out the transactions that were made.

#### RequestFailed.jsx
This page I made to show request failures. I never implemented its use.

#### Loading.jsx
This page is the loading page while waiting for your transactions to take place. If you have very few transactions and no timeout, it's likely you will not see it.

#### Error.jsx
This page is shown if you go poking around to a react route that does not exist. 
  
## Instructions:  

#### Using yarn   
Starting the app requires that you have yarn.

To setup and start the app, run:     
`yarn install`        
`yarn start`

The app will then be available at [http://localhost:3000/](http://localhost:3000/).

#### Using Docker
To start the app using docker, you must build and then run the container. 
`docker build -t web-app .`      
`docker run --name mixer-webapp -p 80:3000 web-app`

The app will then be available at [http://localhost:80/](http://localhost:80/).
