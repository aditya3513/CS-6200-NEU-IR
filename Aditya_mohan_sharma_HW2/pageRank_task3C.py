from math import log
import operator
from collections import defaultdict
import numpy as np
file_name = input("enter file name : ")
file_name = file_name.replace(".txt", "")
results_file = open(file_name+"_results.txt", "w")

def l1Norm(PR, newPR):
	norm = 0.0
	for p in PR:
		norm += abs(newPR[p] - PR[p])
	return norm

def sumNewPR():
	sum = 0.0
	for p in newPR:
		sum += newPR[p]
	return sum

'''
We have a graph in G and we traverse it to find nodes and classify them into 
-Sink (that dont have any out links) represented by S
-Inlinks (nodes that get you to the page) represented by M
-outlinks (nodes that take you out of the page) represented by L
-PR is page rank dictionary that stores, docID as key rank as value
-newPR is page rank dictionary that stores, docID as key rank as value for temporary purpose and L1 norm
-N is total no of documents or pages in this case.
-d is damping factor
-P is the documents which is nothing but key values of M
'''
S = set() #sink
M = {} #inlinks
L = {} #outlinks
PR = {} #page rank
newPR = {} #temp page rank
d = 0.55

#initialization
# graph = open("test.txt","r") #run this to test for ungraded part, works exactly as asked
graph = open(file_name+".txt","r")

#creating inlinks dictionary and document dict and N
for line in graph.readlines():
	row = line.replace("\n", "").split(' ')
	#document id is first element in list
	docID = row[0]
	#rest of items are inlinks
	inlinks = row[1:]
	#we setup inlink dictionary
	M[docID] = inlinks

#documents list
P = M.keys()

#size of documents
N = float(len(P))

#setting up oulinks
for p in P:
	#iterating through inlinks of the document
	for inlink in M[p]:
		if inlink not in L:
			L[inlink] = 1.0
		else:
			L[inlink] += 1.0

#setting up sink list
for p in P:
	if p not in L:
		S.add(p)
S = list(S)

#setting up Page rank dict
for p in P:
	PR[p] = 1.0/N #initial values for PR


norm_value = 0.0
iterations = 0
convergence_step = 0
#running algo till convergence
while convergence_step < 4:
	sinkPR = 0
	for p in S:
		sinkPR += PR[p]
	for p in M:
		newPR[p] = (1-d)/N
		newPR[p] += d*sinkPR/N
		for q in M[p]:
			if q in PR:
				newPR[p] += (d*PR[q]/L[q])
	new_norm_value = l1Norm(PR, newPR)
	diff = abs(new_norm_value - norm_value)
	if diff < 0.001:
		convergence_step += 1
	else:
		convergence_step = 0

	norm_value = new_norm_value

	#here we write all info to file for results
	results_file.write("\n------------------------------------\n")
	results_file.write("Iteration = "+str(iterations)+"\n")
	results_file.write("L1 norm value = "+str(norm_value)+"\n")
	results_file.write("Convergence Step = "+str(convergence_step)+"\n")
	results_file.write("newPR sum = "+str(sumNewPR())+"\n")


	for p in P:
		PR[p] = newPR[p]

	iterations += 1

	# print("iter = ",iterations)
	# print("norm = ",norm_value )
	# print("diff = ", diff)
	# print("step = ", convergence_step)


#sorting page rank
#refered to https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
inlinkSorted = {}
for p in P:
	inlinkSorted[p] = len(M[p])

sortedPR = sorted(inlinkSorted.items(), key=lambda kv: kv[1],reverse=True)


#sorting page ranks in decreasing order
rankResults = open(file_name+"_ranks.txt", "w")
limit = 50
if(len(sortedPR) < 50):
	limit = len(sortedPR)

for i in range(0,limit):
	rank = sortedPR[i]
	rankResults.write(str(rank) + "\n")


print("results have been generated and files are saved, look for these files:")
print("all ranks in "+file_name+"_ranks.txt")
print("results in "+file_name+"_results.txt")





