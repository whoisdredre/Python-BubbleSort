#Python Bubble Sort Alorithm
import random

jockey_list = []
	#for loop will populate a new list to sort
for count in range(0,101):
	jockey_list.append(random.randint(0,100001))
	#test print original list after populating 100 items
print jockey_list
	#bubble sort action . . .
for i in range(len(jockey_list)-1):
	for b in range(len(jockey_list)-1):
		if jockey_list[b] > jockey_list[b+1]:
			temp = jockey_list [b+1]
			jockey_list[b+1] = jockey_list[b]
			jockey_list[b] = temp
			#un-comment below to see sorting in process.... 
			#print jockey_list
print jockey_list