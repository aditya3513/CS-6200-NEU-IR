import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import collections
import string
import os
import operator
import re
import ast

def encode(arr):
	encoded_array = []
	for i in range(len(arr)):
		if i == 0:
			encoded_array.append(arr[i])
		else:
			val = arr[i] - arr[i-1]
			encoded_array.append(val)
	return encoded_array



if not os.path.exists("invertedIndex"):
	os.makedirs("invertedIndex")

# https://stackoverflow.com/questions/11026959/writing-a-dict-to-txt-file-and-reading-it-back
unigramWordsFile = eval(open("unigramWordsFile.txt", "r").read())
uniGramContentFile = eval(open("uniGramContentFile.txt", "r").read())

invertedPosIndexFile = open("invertedIndex/1GramPositionInvertedIndex.txt", "w")

pos_index = {}
for docID, terms in unigramWordsFile.items():
	for term in set(terms):
		#we find position of word in the whole corpus of the docID
		#reference from: https://stackoverflow.com/questions/4664850/find-all-occurrences-of-a-substring-in-python
		positions = [pos.start() for pos in re.finditer(term, uniGramContentFile[docID])]
		
		if term not in pos_index:
			pos_index.update({term:{docID : positions}})
		elif docID not in pos_index[term]:
			pos_index[term].update({docID:positions})
		else:
			pos_index[term][docID] += positions



print("created dict, now encoding it")
for term, docID_posns in pos_index.items():
	for docID, posns in docID_posns.items():
		encoded_val = encode(posns)
		pos_index[term][docID] = encoded_val
		invertedPosIndexFile.write(str(term)+" "+str(docID)+" "+str(encoded_val)+"\n")

raw_file = open("raw_position_index.txt", "w")
raw_file.write(str(dict(pos_index)))

print("done")








