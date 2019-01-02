- to run this code, you just need the html files saved in HTML_pages_Task1, it has all webpages downloaded during HW1.
- next thing you need is "crawledList.txt" it has links to all l=files that were crawled, they work as index while initial corpus creation and code maps 	files  hsing these links.
- Task 1
	- To run this task, python Task1.py
	- it generates a file "corpus.txt" which has list of all file names in corpus folder
	- corpus/ folder has all corpus files with same name as article

- Task2 (part a,b,c):
	- to run this python Task2.py
	- it places all the results in folder invertedIndex/
	- it has 5 files: 1Gram.txt, 2Gram.txt, 3Gram.txt, 1GramPositionInvertedIndex, docTermCountTable.txt. these tables are inveted index for n=1,2,3, 	  	positional index for 1Gram and docTermCountTable.
	- it also generates the files uniGramContentFile.txt and unigramWordsFile.txt that are used by Task2d.py to create 1GramPositionInvertedIndex

- Task2 (part d):
	-to run this python Task2d.py
	- you need to run Task2.py to use this, if the two files mentioned above are not generated.
	- once you run this, it will give you 1GramPositionInvertedIndex.txt which has positional inverted index for 1 gram.

- Task3
	- to run this python Task3.py
	- it takes raw_position_index.txt which is craeted by Task2d.py. i had to do this to save time as re runnig was really slow, this allows it to read a 	dict from a file.
	- it will craete a file task3_result_file.txt which has resulst for Task3

-Task4
	- to run this python task4.py
	- it generates results in freq/ folder.
	- it gives 6 files asked in the questions, they are names as nGram_doc_freq_file or nGram_term_freq_file where n is 1 or 2 or 3
	- part c:
		- explanationa nd stop list are in stoplist_task4_c/stoplists.txt
		refer to see the stoplist and explanation.
		
