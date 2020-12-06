# jobcoin-mixer
An application for mixing Jobcoin transactions. If you are interviewing with Gemini and looking for examples of their take-home project, this is it. 

## Instructions
The containers can be run separately or they can be run as a group, using `Docker`/`docker-compose`.    


#### Prerequesites
You will need both `docker` and `docker-compose` installed on your machine.

#### Commands

Within the repository folder (`/jobcoin-mixer`), run:      
`docker-compose up`

Depending on your OS, you may need to use `sudo` with the `docker-compose` command. If you don't want to see output, add the `-d` flag. 

The app will then be available at [http://localhost:80/](http://localhost:80/).

## Components

### Web App
The web app is a simple create-react-app that has been modified to facilitate the transfer of Jobcoins.
Users put in the following information into the app:     
**1:** A list of addresses     
**2:** A number of transactions (OPTIONAL)        
**3:** A timeout for the transactions (OPTIONAL)

The web app then makes a call to the flask app, which provides the web app with a random, unique UUID to deposit coins to.

Once coins have been deposited via [the Jobcoin UI](https://jobcoin.gemini.com/headache-joyfully), the user confirms in the web app that coins have been deposited, and the coins are then mixed via the flask app. A list of the transactions is then provided to the user.

The UI has some form validation and can check the Jobcoin API for deposited coins, but is otherwise very straight-forward.

### Flask App
The flask app is a python-based API with business logic to handle the mixing of coins.
The app has two endpoints:

#### '/get_address'
The `/mix_coins` endpoint is a `POST` for double-checking the list of provided addresses. The API then provides back the random, unique deposit address.

#### '/mix_coins'
The `/check_deposit` endpoint does both a `POST` and a `GET`.

The `GET` allows the user to tell the API that coins have been deposited at the generated address. If coins have not been deposited, a balance of `0` is passed back to the web app. Otherwise, the balance amount is returned. 

The `POST` allows the user to then send the address list, the number of transactions, and the timeout length to the flask app for mixing the coins.

## Considerations
Some of the aspects of my mixer were meant to be demonstrational, but don't necessarily make a difference in the way my mixer works.        

**1:** The mixer takes coins out of the unique address and places them in a pool, and then coins are distributed from the pool. If 'coins' themselves were unique/trackable, this would be helpful - but in the context of my mixer, it really makes little difference.          
**2:** The ability to add delay to your transactions is meant to spread them across the network to add anonymity. However, since there aren't that many transactions happening on the network at once, it really makes no difference in the end in this example.         
**3:** Because I didn't implement some type of queue/threading for my app, delaying the transactions means waiting until the API calls are finished. Because of this, I made them intentionally very, very short, so as not to delay the app for minutes on end.
   

## Other
If you'd like to view more detailed information about the separate projects, please view their READMEs. 

A note: If you're poking around through the git history and you notice there seems to be some gaps, I originally started this project as two separate repositories and then combined them. You can see the [flask-app](https://github.com/nldoty/gemini-coinmixer-challenge) and [web-app](https://github.com/nldoty/gemini-mixer-react-app) here if you'd like a better picture. Please forgive my poor naming structures. 
