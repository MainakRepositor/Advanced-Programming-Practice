'''Given an array of names of candidates in an election. A candidate name in the array
represents a vote cast to the candidate. Print the name of candidates received Max vote. If
there is tie, print a lexicographically smaller name. Input = ['john','johnny','jackie','johnny', 
'john','jackie','jamie','jamie', john','johnny','jamie','johnny', 'john']. Output : john'''


from collections import Counter 

def winner(input): 

	
	votes = Counter(input) 
	
 
	dict = {} 

	for value in votes.values(): 

		dict[value] = [] 

	for (key,value) in votes.items(): 
		dict[value].append(key) 


	maxVote = sorted(dict.keys(),reverse=True)[0] 


	if len(dict[maxVote])>1: 
		print (sorted(dict[maxVote])[0]) 
	else: 
		print (dict[maxVote][0]) 


if __name__ == "__main__": 
	input =['john','johnny','jackie','johnny', 
			'john','jackie','jamie','jamie', 
			'john','johnny','jamie','johnny', 
			'john'] 
	winner(input) 

    