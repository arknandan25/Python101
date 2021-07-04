# TC - O(n) where n is the number of competitions
# SC - O(k) where k is the number of teams


def tournamentWinner(competitions, results):
    # Write your code here.
	# maintain a dict/hash table 
	current_best_team = ""
	score = {current_best_team: 0}
	for i, x in enumerate(competitions):
		winning_team = x[0] if results[i] == 1 else x[1]
		# update the dict score 
		if winning_team not in score:
			score[winning_team] = 0
		# increase score for the winning team by 3
		score[winning_team] += 3
		
		if score[winning_team] > score[current_best_team]:
			current_best_team = winning_team
	
	print(score)
    # return current_best_team

# this solves the problem but there is a problem:
# finding the maximum or minimum in  a dictionary 
# the above approach where we define a dummy entry {"":0} by the current_best_team
# leads to the final score dict with an empty value that should not be there 
# line 17 print: {'': 0, 'C#': 3, 'Python': 6}
# we don't need the "":0

# so another approach should be used for max/min in a dict


def tournamentWinner(competitions, results):
    # Write your code here.
	# maintain a dict/hash table  terminal
	current_best_team = ""
	score = {}
	for i, x in enumerate(competitions):
		winning_team = x[0] if results[i] == 1 else x[1]
		# update the dict score 
		if winning_team not in score:
			score[winning_team] = 0
		# increase score for the winning team by 3
		score[winning_team] += 3
		# find the max value 		
		max_value = max(score.values())
		max_value_key = [k for k, v in score.items() if v == max_value]
    	return max_value_key[0]
