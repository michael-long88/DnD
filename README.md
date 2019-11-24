# DnD
Project to hold current and future Dnd-related scripts. 

## tavern.py
Calculates success rate of selling a premium ale at the player-owned tavern based on the DC, the cost of the premium ale, 
and the cost of a regular ale.  

r = 1d20 - DC  
*r >= DC  
c = cost - base ale price  
*c >= base ale price  
r + (100 - (10 * c)) = chance of success  

Example:  
DC = 10  
r = 9  
cost = 12  
base ale price = 6  
c = 6  
9 + (100 - (10 * 6)) = 49% chance of success
