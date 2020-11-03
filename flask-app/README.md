# Gemini Coin Mixer Challenge

This is my implementation for Gemini's Jobcoin Coinmixer challenge. Ultimately I will do a 
full README write-up but for the time being, I'll be using this as a check-list
for things I'd like to accomplish (to help anyone that happens to look through my Git history).

## To Do
The bulk of to-do items I am logging in [Github Issues](https://github.com/nldoty/gemini-coinmixer-challenge/issues).       

##### The current basic MVP would be this:    
  1. A user gives the addresses (a<sub>1</sub>, a<sub>2</sub>, ... a<sub>n</sub>) that they'd like their mixed coins sent 
  to. The mixer sends a unique address (b) to the user to send coins to. 
  2. The user sends the coins they want mixed to (b). A service polls the Jobcoin API for a period of time to 
  determine if coins were sent to (b).     
    a. If coins are not sent to (b), a new transaction will have to take place to restart the polling service.
  3. Once the coins are sent to (b), the mixer then sends coins in equal increments to (a<sub>1</sub>, a<sub>2</sub>, ... a<sub>n</sub>).
     

##### Functionality to add to improve the anonymity:      
 
  1. Instead of divvying up coins equally to the supplied addresses, make the division random. See [Issue 6](https://github.com/nldoty/gemini-coinmixer-challenge/issues/6).
  2. Make the number of divisions/transactions more than the number of supplied addresses, so some addresses will have multiple transactions. See [Issue 7](https://github.com/nldoty/gemini-coinmixer-challenge/issues/7).
  3. Add the ability to send transactions at random intervals. See [Issue 8](https://github.com/nldoty/gemini-coinmixer-challenge/issues/8).


##### Great to haves:     
     
  1. A Flask API to send mixer requests to.
  2. A React UI for making API mixer requests even easier.
  3. A persistence database to track if Jobcoin transactions fail, and the ability to resolve those transactions later.
  4. Put all these things in a Docker container.
  
  
## Instructions:     
To start with the app you'll need to create a virtual environment.      
```
python3 -m venv venv      
source venv/bin/activate      
pip install -r requirements.txt        
```

## Assumptions       
These are just some general assumptions I'm making moving forward. These might change.
     
     1. A minimum number of Jobcoins need to be in the mixer to "mix" with.
        a. I do not know how many. At this point I've chosen 50.
     2. All transactions will be in whole-coin values. 
        a. Doing financial transactions is a bad idea using floating point. I get around this by doing integer math,
         converting small coins into large int values, doing calculations, and then changing them back to their original
         value as strings. This is kind of how other coins transactions work (like Bitcoin ==  100,000,000 Satoshi)

## Issues
This is a non-exhaustive list of issues with the application as it currently stands.

  1. The `MIXER_POOL_ADDRESS` is hard-coded in `config.py`. This isn't a good practice. This would be better off placed 
  in something like a `.env` file, and not committed to the project in a public way. 
  2. The mixer currently polls the given address for funds for a limited amount of time. This isn't a good practice. The 
  polling service should not run indefinitely, but if someone adds funds after the alloted time the coins become stuck. 
  A more robust solution either tracking these addresses, or a better way to poll the address, or a way to close the address
  would be ideal. 
