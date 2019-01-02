2) To run task 1, include the task1.java in a project along with the jars mentioned in the HW and run the code. Then enter location of idea and position of file, press Q and the 	inter the query. if you terminate the don't add html files again else the results has repeated files in hits.
	All results are stored in "results/task1/" folder.

3) To tun task 2, in case you don't have the unigram run the GenerateInvertedLists.py [python GenerateInvertedLists.py] and it will generate all the inverted index needed.
	Now run Task2.py [python Task2.py] and it will automatically run for all queries that are asked in the HW. in case you want to change add queries to "Queries" variable in 	the code. It will generate the results in "results/task2/" folder. 

4) Implementations:
	a) task1:
		- I changed the number of documents from 3 to 100 and ran the code. then copied the result into test files.

	b) task2:
		- First generated the unigram as a son that can be read.
		- Then created a doc length list to have a dict of lengths of documents where docID is key and length is value. sum of all length hives us corpus length
		- For each query string, split into words, then for each words get query word frequency in document (fqi) and query word frequency in corpus(cqi)
		- Now we put everything in formula and calculate score for each word of string and add them up.
		- add final score to data frame and in the end sort the data frame and put into file.

5) Top 5 result comparisons are saved in "results/Top5Comparison.txt"

6) Consecutive results in "results/consecutiveResult.txt"