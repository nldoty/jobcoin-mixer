# jobcoin-mixer
An application for mixing Jobcoin transactions

## Components

### Web App
The web app is a simple create-react-app that has been modified to facilitate the transfer of Jobcoins.
Users put in the following information into the app:     
**1:** A list of addresses     
**2:** A number of transactions (OPTIONAL)
**3:** TODO: A timeout for the transactions (OPTIONAL)

The web app then makes a call to the flask app, which provides the web app with a random, unique UUID to deposit coins to.

Once coins have been deposited via [the Jobcoin UI](https://jobcoin.gemini.com/headache-joyfully), the user confirms in the web app that coins have been deposited, and the coins are then mixed via the flask app. A list of the transactions is then provided to the user.

The UI has some form validation and can check the Jobcoin API for deposited coins, but is otherwise very straight-forward.

### Flask App
The flask app is a python-based API with business logic to handle the mixing of coins.
The app has two endpoints:

#### '/mix_coins'
The `/mix_coins` endpoint is a `POST` for double-checking the list of provided addresses. The API then provides back the random, unique deposit address.

#### '/check_deposit'
The `/check_deposit` endpoint does both a `POST` and a `GET`.

The `GET` allows the user to tell the API that coins have been deposited at the generated address. If coins have not been deposited, a balance of `0` is passed back to the web app. Otherwise, the balance amount is returned. 

The `POST` allows the user to then send the address list, the number of transactions, and the timeout length to the flask app for mixing the coins.

## Current Issues
Issues currently within the app as a whole:      
**1:** I have not tested sending partial coins. I'm fairly certain it works, but need to test it.    
**2:** As separate parts, the apps work just fine. Together, the docker-compose doesn't allow the two to communicate, and I cannot figure out why.       
**3:** The time delay is not currently implemented. I realized in doing so that it could delay the front-end for up to 2 minutes, meaning there would be a lot of down time. I figured I could lower it to 10 seconds for just demonstration purposes, but otherwise have not implemented it yet.        
**4:** I have not yet added in any tests.     
**5:** Although optional, I did not implement the ability to take in a fee. As it was part of the prompt, I may want to implement that. 

## Other
If you'd like to view more detailed information about the separate projects, please view their READMEs. 