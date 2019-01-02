import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from collections import defaultdict
import string
import os

#read link file for all urls
linkFile = open("crawledList.txt", "r")
saved_file_val = "en.wikipedia.org_wiki_"
corpusList = open("corpusList.txt", "w")
# crawledList = [:1]
for link in linkFile.readlines():
	linkName = link.strip("\n").replace("https://", "").replace("/", "_")
	docID = linkName.replace(saved_file_val, "").replace(".txt","")
	if not os.path.exists("corpus"):
		os.makedirs("corpus")
	corpus_file_name = "corpus/"+docID+".txt"
	corpus_file = open(corpus_file_name, "w")
	corpusList.write(docID+"\n")
	#open HTML files
	htmlFileName = "HTML_pages_Task1/"+linkName+".txt"
	#open file
	htmlFile = open(htmlFileName, "r").read()
	# we need to remove see also section, so we get everything before it as it contains References and Notes
	if htmlFile.find('<span class="mw-headline" id="See_also">') != -1:
		htmlFile = htmlFile[:htmlFile.find('<span class="mw-headline" id="See_also">')]
	#incase see also it not present, removing references
	if htmlFile.find('<span class="mw-headline" id="References">') != -1:
		htmlFile = htmlFile[:htmlFile.find('<span class="mw-headline" id="References">')]
	#incase see also it not present, removing Notes
	if htmlFile.find('<span class="mw-headline" id="Notes">') != -1:
		htmlFile = htmlFile[:htmlFile.find('<span class="mw-headline" id="Notes">')]
	html_content = BeautifulSoup(htmlFile, "html.parser")
	if html_content.find('div', id='toc') != None:
		print("tokenizing :",docID)
		html_content.find('div', id='toc').decompose()
	bodyContent = html_content.findAll('div', attrs={'id':'bodyContent'})
	content = ""
	#title
	content += html_content.find('title').getText().lower()
	content += html_content.find('h1').getText().lower()
	#now we get all tags and start collecting all text from it
	#this way we get all div text, span text and text in anchors.
	for data in bodyContent:
		content += data.getText().lower()

	#removing punctuations
	punctuations = set(string.punctuation)
	content_without_punctuation = ""

	for ch, i in zip(content, range(len(content)-1)):
		# print(ch)
		if ch not in punctuations:
			content_without_punctuation += ch
		else:
			if content[i-1] in string.digits and content[i+1] in string.digits and ch in ",.":
				content_without_punctuation += ch

	corpus_file.write(content_without_punctuation)


print("corpus has been generated and saved in corpus/")



	

	

		




	

	


