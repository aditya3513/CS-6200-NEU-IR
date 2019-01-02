import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import collections
import string
import os
import operator
import re

#tf files
# 1gram_doc_freq = open("1gram_doc_freq.txt", "w")
# 1gram_term_freq = open("1gram_term_freq.txt", "w")

if not os.path.exists("invertedIndex"):
	os.makedirs("invertedIndex")

unigramWordsFile = open("unigramWordsFile.txt", "w")
uniGramContentFile = open("uniGramContentFile.txt", "w")
docTermCountTable = open("invertedIndex/docTermCountTable.txt", "w")
threshold_values = [35, 5, 2]
for n in [1,2,3]:
	
	corpusListFile = open("corpusList.txt", "r")

	nGram_invertedIndex_file = open("invertedIndex/"+str(n)+"Gram.txt", "w")

	content = {}
	words = {}

	for fileName in corpusListFile.readlines():
		docID = fileName.strip("\n")

		corpus = open("corpus/"+docID+".txt", "r").read()

		#adding corpus to dict with docID as the key
		content[docID] = corpus
		#adding words of corpus to dict with docID as key
		words[docID] = corpus.split()



	#now since we have a dict with all files and words we can count and calculate nterms.
	nterms = {}
	for docID, word in words.items():
		# print(docID, words)
		#following method counts the number of termms in the corpus
		termCounts = {}
		for i in range(len(word)-n+1):
			val = ' '.join(word[i:i+n])
			if val not in termCounts:
				termCounts[val] = 1
			else:
				termCounts[val] += 1
		nterms[docID] = len(set(termCounts))


	#now tf is calculates, similar to above method, first we generate terms and term counts
	#then we count how many times each term is occuring and 
	#then we add values to Inverted list
	invertedList = {}
	for docID, word in words.items():
		# print(docID, words)
		#following method counts the number of termms in the corpus
		termCounts = {}
		for i in range(len(word)-n+1):
			val = ' '.join(word[i:i+n])
			if val not in termCounts:
				termCounts[val] = 1
			else:
				termCounts[val] += 1
		tf = {}
		#counting teh number of times a term is present in all docs to get freq.
		for term, count in termCounts.items():
			if term not in tf:
				tf[term] = count
			else:
				tf[term] += count
		tf = sorted(tf.items(), key=lambda kv: kv[1], reverse=True)
		
		for term, freq in tf:
			if term not in invertedList:
				invertedList[term] = [(docID, freq)]
			else:
				invertedList[term].append((docID, freq))


	#writing all data to file

	#writing term frequency, format: term and tern-freq
	stop_list = []
	for term, item in invertedList.items():
		nGram_invertedIndex_file.write(str(term)+" "+str(item)+"\n")
		threshold_value = threshold_values[n-1]


	doc_term_freq_table = {}
	for docID, term in words.items():
		if docID not in doc_term_freq_table:
			doc_term_freq_table[docID] = len(set(term))
		else:
			doc_term_freq_table[docID] += len(set(term))

	for docID, freq in doc_term_freq_table.items():
		docTermCountTable.write(str(docID)+" "+str(freq))


	#generating positional index for unigrams
	if n == 1:
		#saving them to be used by positional index code
		unigramWordsFile.write(str(words))
		uniGramContentFile.write(str(content))






'''
pos_index_file = open("invertedIndex/1gram_position_index.txt", "w")
		pos_index = {}
		for docID, wordlist in words.items():
			for word in wordlist:
				# print(wordlist.find(word))
				#taken from https://stackoverflow.com/questions/4664850/find-all-occurrences-of-a-substring-in-python
				position = [m.start() for m in re.finditer(word, content[docID])]
				if word not in pos_index:
					doc_word_count = {docID: position}
					pos_index[word] = doc_word_count
				else:
					if docID not in pos_index[word]:
						pos_index[word] = {docID: position}
					else:
						pos_set = pos_index[word][docID] + position
						# print(pos_set)
						pos_index[word][docID] = pos_set
						
		

		for word, item in pos_index.items():
			pos_index_file.write(str(word)+" "+str(item)+"\n")
'''





			