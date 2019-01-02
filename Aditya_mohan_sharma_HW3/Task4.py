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

if not os.path.exists("freq"):
	os.makedirs("freq")


for n in [1,2,3]:
	
	corpusListFile = open("corpusList.txt", "r")

	nGram_doc_freq_file = open("freq/"+str(n)+"Gram_doc_freq_file.txt", "w")
	nGram_term_freq_file = open("freq/"+str(n)+"Gram_term_freq_file.txt", "w")

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
			nGram_term_freq_file.write(str(term)+" "+str(freq)+"\n")
			if term not in invertedList:
				invertedList[term] = [(docID, freq)]
			else:
				invertedList[term].append((docID, freq))


	#writing all data to file

	#writing doc frequency, format: term, docs, count
	sorted_by_term = sorted(invertedList.items(), key=lambda kv: kv[0])
	for term, item in sorted_by_term:
		doc_ids = []
		for doc_id, tf in item:
			doc_ids.append(doc_id)
		nGram_doc_freq_file.write(str(term)+" "+str(doc_ids)+" "+str(len(doc_ids))+"\n")







			