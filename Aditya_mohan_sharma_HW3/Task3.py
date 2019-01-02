import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import collections
import string
import os
import operator
import re

#this one uses raw file generated from task2d.py, this one I copied bfore formatting the file fo soleve this part.
#as this process takes long and is slow.
pos_index_file = open("raw_position_index.txt", "r")
task3_result_file = open("task3_result_file.txt", "w")

pos_index = eval(pos_index_file.read())

def decode(arr):
	decoded_arr = []
	for i in range(len(arr)):
		if i == 0:
			decoded_arr.append(arr[i])
		else:
			decoded_val = arr[i]+decoded_arr[i-1]
			decoded_arr.append(decoded_val)
	return(decoded_arr)


def pos_index_search(keyword1, keyword2, k):
	doc_list = []
	val1 = pos_index[keyword1]
	val2 = pos_index[keyword2]

	common_docID = set(val1.keys()) & set(val2.keys())

	for docID in common_docID:
		posn1 = decode(val1[docID])
		posn2 = decode(val2[docID])

		for p1 in posn1:
			for p2 in posn2:
				if abs(p1-p2) <= k:
					doc_list.append(docID)
	
	task3_result_file.write("for keywords: "+ keyword1+ " " +keyword2+"\n")
	task3_result_file.write("documents list: "+ str(doc_list) +"\n")
	task3_result_file.write("------------------------------------------\n")
	print("----------------------------")
	print("K = ", k)
	print("keywords = ", keyword1, keyword2)
	print("documnet ids = ", str(doc_list))






pos_index_search('carbon', 'emission', 5)
pos_index_search('carbon', 'emission', 10)
pos_index_search('greenhouse', 'emission', 6)
pos_index_search('greenhouse', 'emission', 12)

