#########################################################

To run task 1: python GraphBuilder.py

- run python GraphBuilder.py, it is set to G1.txt right now, so it takes the G1 file. it needs the link1_files (these are files that were downloaded in last assignments crawling. I have used these instead of making requests to download the page.)
- results are saved in results/Task1
	- G1.txt and G2.txt are the graph files for bfs and focused crawl respectively.
	- G1_report.txt and G2_report.txt are report files which have information like: inlink, outlink count, sink and source count.
	- it also has rank and results for the ungraded part that was given.

#########################################################
To run task 2: python pageRank.py
- it will ask for the file name, which is either G1.txt or G2.txt
- it then stores the results in text files and tell you the name of the files.
- results are stored in results/Task2
	- G1_ranks.txt and G2_ranks.txt have top 50 ranks on basis of page rank at d =0.85
	- G1_results.txt and G2_results.txt have info about L1 value, iterations and newPR summations.

#########################################################
To run task 3: 
	->Task A
		- run by doing python pageRank_task3A.py
		- it will ask for file name which will be G1.txt or G2.txt, then it will ask for d value which will be 0.5 or 0.65.
		- it will generate results that are stored results/Task3/A
		- G1_ranks_taskA_0.5.txt and G2_ranks_taskA_0.5.txt have top 50 ranks on basis of page rank at d =0.5
		- G1_ranks_taskA_0.65.txt and G2_ranks_taskA_0.65.txt have top 50 ranks on basis of page rank at d =0.65
		- G1_results_taskA_0.5.txt and G2_results_taskA_0.5.txt have top 50 ranks on basis of page rank at d =0.5
		- G1_results_taskA_0.65.txt and G2_results_taskA_0.65.txt have top 50 ranks on basis of page rank at d =0.65
		- explanation is in result_explanation.txt

	->Task B
		- run by doing python pageRank_task3B.py
		- it will ask for the file name, which is either G1.txt or G2.txt
		- it then stores the results in text files and tell you the name of the files.
		- results are stored in results/Task3/B
			- G1_ranks.txt and G2_ranks.txt have top 50 ranks on basis of page rank for 4 iterations
			- G1_results.txt and G2_results.txt have info about L1 value, iterations and newPR summations.
			- explanation is in result_explanation.txt

	->Task C
		- run by doing python pageRank_task3C.py
		- it will ask for the file name, which is either G1.txt or G2.txt
		- it then stores the results in text files and tell you the name of the files.
		- results are stored in results/Task3/C
			- G1_ranks.txt and G2_ranks.txt have top 50 ranks on basis of inlink count.
			- G1_results.txt and G2_results.txt have info about L1 value, iterations and newPR summations.
			- explanation is in result_explanation.txt

#references:
youtube:
	-https://www.youtube.com/watch?v=u8HtO7Gd5q0
stackoverflow:
	- numpy, sorts for list usinf operators.