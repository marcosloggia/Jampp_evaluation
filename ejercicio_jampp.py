#Import random package
import random 
#Define the function weighted_random
def weighted_random(values, weights):     
 #create new variable total_weight that is equal to the addition of the total weights in the list
 total_weight = sum(weights)     
 #create a new variable acum_weights that is equal to the iteration of each value in weights list divided by the total_weight
 acum_weights = [w / total_weight for w in weights[:]]     
 #Iterate between every value of the list weights, to sum all the acum_weights
 for i in range(len(weights)):
	acum_weights[i] += acum_weights[i]     
 #create then variable rand that is equal to a random number generated with the package random
 rand = random.random()     
 for value, weight in zip(values, acum_weights):         
	# if the value of the list is bigger than the random value generated in rand then return the value.
	if weight > rand:             
		return value
#The problem that I see here is that the function only returns one value when it should return all the values of the list values, and all the values of the list weights
#I've tried to modify it but I can't find the error, besides add weights after the value in return.
		
