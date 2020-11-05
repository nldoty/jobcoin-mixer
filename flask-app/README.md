# Coin Mixer Flask App

This is my API/business-logic implementation for the coinmixer challenge.

## MVP   

##### This is the basic MVP process:    
**1.** A service provides the addresses (a<sub>1</sub>, a<sub>2</sub>, ... a<sub>n</sub>) that they'd like their mixed coins sent to (currently max 5). The mixer returns a unique address (b) to the user to send coins to. 
**2.** The user sends the coins they want mixed to (b). A service checks the Jobcoin API to determine if coins were sent to (b).     
**3.** Once the coins are sent to (b), the mixer then sends coins in equal increments to (a<sub>1</sub>, a<sub>2</sub>, ... a<sub>n</sub>).
     

##### Improving the anonymity:      
 
**1.** Instead of divvying up coins equally to the supplied addresses, make the division random.         
**2.** Make the number of divisions/transactions more than the number of supplied addresses, so some addresses will have multiple transactions. The user can also set this value.
**3.** The ability to send transactions at random intervals adds anonymity by potentially spreading them out with other transactions on the network.


##### Great to haves:     
     
**1.** A persistence database to track if Jobcoin transactions fail, and the ability to resolve those transactions later.
  
  
## Instructions: 

#### Using Python    
To start with the app you'll need to create a virtual environment.      
```
python3 -m venv venv      
source venv/bin/activate      
pip install -r requirements.txt        
```

To start the service, simply run
`python app.py`

#### Using Docker
To run the app using Docker, run the following commands: 

`docker build -t flask-app .`
`docker run --name mixer-flaskapp -p 5000:5000 flask-app`

## Assumptions       
These are just some general assumptions I'm making moving forward. These might change.
     
**1.** A minimum number of Jobcoins need to be in the mixer to "mix" with.
  **a.** I do not know how many. At this point I've chosen 50.
**2.** All transactions will be rounded to 8 decimal places. 
**a.** Doing financial transactions is a bad idea using floating point. I get around this by doing integer math, converting small coins into large int values, doing calculations, and then changing them back to their original value as strings. This is kind of how other coins transactions work (like Bitcoin ==  100,000,000 Satoshi)

## Issues
This is a non-exhaustive list of issues with the application as it currently stands.

**1.** The `MIXER_POOL_ADDRESS` is hard-coded in `config.py`. This isn't a good practice. This would be better off placed in something like a `.env` file, and not committed to the project in a public way.         
**2.** Because of the way the containers are hosted, I run into CORS issues. This is expected hosting the app on the same source but in an enterprise application should be resolved. 
**3.** Not an issue, but although I implemented the ability to capture fees, I don't. The fee address is also too obvious. 