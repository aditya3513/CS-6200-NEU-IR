import pandas as pd
import numpy as np
import collections
import os
import operator
import math



invertedIndexFile = open("invertedIndex/1Gram.txt", "r")
corpusList = open("corpusList.txt", "r")
docLengthFile = open("docLenFile.txt", "w")
unigram = eval(invertedIndexFile.read())
docLenList = {}
C = 0
u = 1500

docIDs = corpusList.readlines()
for filename in docIDs:
	docID = filename.rstrip("\n")
	#read file
	docFile = open("corpus/"+docID+".txt", "r").read()

	lendoc = len(docFile.split())
	if docID not in docLenList:
		docLenList[docID] = lendoc
		C += lendoc
	else:
		docLenList[docID] += lendoc
		C += lendoc


columnNames = ["query_id", "Q0", "doc_id", "rank", "LMDirichlet_score", "system_name"]
rankDF = pd.DataFrame(list(range(1,1001)), columns = ["rank"])
Queries = ["carbon emission", "cutting carbon emission", "flexible dieting", 
	"flexible dieting and vegetarianism", "information on pest control in greenhouse", 
	"pest control greenhouse", "greenhouse apples apple", "green house apples apple"]
# Queries = ["carbon emission"]
#first we iterate the queries and go trhough each query string
for query, query_id in zip(Queries, range(len(Queries))):
	resultDF = pd.DataFrame(columns = columnNames)
	#iterate through each document
	for docID, indexVal in zip(docIDs, range(len(docIDs))):
		
		docID = docID.rstrip("\n")
		docScore = 0
		#we run the sustem on each dpcument for all query words
		#splitting query into words
		for word in query.split():
			unigramSection = unigram[word]

			# now we calculate fqi and cqi
			fqi = 0
			cqi = 0
			for uniGramdocID, termCount in unigramSection:
				#its the coutn across all docs
				cqi += termCount
				#only when its present in document else its zero
				if uniGramdocID == docID:
					fqi += termCount
			
			#now we compute teh value using the formula
			D = docLenList[docID]
			term1 = fqi + (u * (cqi/C))
			term2 = D + u
			score = term1/term2
			docScore += math.log(score)
		# newData = pd.DataFrame([query_id, "Q0", docID, 0, docScore, "LMDirichlet"], columnNames)
		resultDF.loc[len(resultDF)] = [query_id+1, "Q0", docID, 0, docScore, "LMDirichlet"]
	# print(len(resultDF), len(rankDF))
	resultDF = resultDF.sort_values('LMDirichlet_score', ascending=False)
	
	resultDF['rank'] = rankDF['rank'].values
	np.savetxt('results/task2/'+query_id+".txt", resultDF.values[:100], fmt='%s')


	