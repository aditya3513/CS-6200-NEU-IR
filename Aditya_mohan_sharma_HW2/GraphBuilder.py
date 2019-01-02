#for parsing html
from bs4 import BeautifulSoup
#for connections and downloading pages
from urllib.request import urlopen
#regular expressions
import re
import time
import os
from collections import defaultdict

#read bfs link file
file = open("link1.txt","r")
graphFile =open("G1.txt", "w")
report_file = open("G1_report.txt", "w")

#get documents for collected files in last assignment
saved_file_val = "en.wikipedia.org_wiki_"

linkUrls = set()

graph = defaultdict(list)

for linkUrl in file.readlines():
	fileName = linkUrl.replace("https://", "").replace("/", "_").rstrip('\n')
	docID = fileName.replace(saved_file_val, "").replace(".txt","")

	#this maintains a runnig list of all documents that we got during bfs crawl, used later to create graph
	linkUrls.add(docID)
	
	#read content of files
	file = open("link1_files/"+fileName+".txt", "r")
	html_content = BeautifulSoup(file, "html.parser")
	bodyContent = html_content.find(id="bodyContent")

	outlinks = set()

	for a_tags in bodyContent.find_all("a"):
		link = a_tags.get("href")

		#check for external links, internal maps using #

		#this time i used match instead of containes as suggested in feedback comments
		if link != None and re.match('/wiki/.*', link) != None and re.match('/wiki/(.*)#(.*)', link) == None and re.match('/wiki/(.*):(.*)', link) == None:
			outlinks.add(link.replace("/wiki/", ""))

	for oLinks in outlinks:
		if oLinks != docID:
			graph[oLinks].append(docID)



for docID, links in graph.items():
	graphFile.write(docID)
	for link in links:
		graphFile.write(' '+link)
	graphFile.write('\n')

#report generation part
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
P = [] #documents

#creting dict of inlinks
for docID, links in graph.items():
	M[docID] = links

#creating set of documents
P = M.keys()

#creating set of outlinks
for docID in P:
	for inlink in M[docID]:
		if inlink not in L:
			L[inlink] = 1.0
		else:
			L[inlink] += 1.0


#creating sink array
for p in P:
	if p not in L:
		S.add(p)
S = list(S)


#finding sources
Sources = set()
for p in P:
	if p not in M:
		Sources.add(p)

#finding max in-degree
maxInDeg = 0
for docID in P:
	deg = len(M[docID])
	if deg > maxInDeg:
		maxInDeg = deg

#finding max out degree
maxOutDeg = 0
for p in L:
	if L[p] > maxOutDeg:
		maxOutDeg = L[p]


#writing results in file
report_file.write("Graph G1"+"\n")
report_file.write("Number of pages with no in-links = "+ str(len(Sources))+"\n")
report_file.write("Number of pages with no out-links = "+ str(len(S))+"\n")
report_file.write("Max In degree = "+ str(maxInDeg)+"\n")
report_file.write("Max Out degree = "+ str(maxOutDeg)+"\n")



	


