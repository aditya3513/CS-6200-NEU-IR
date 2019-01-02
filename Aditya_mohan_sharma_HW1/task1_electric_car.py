#for parsing html
from bs4 import BeautifulSoup
#for connections and downloading pages
from urllib.request import urlopen
#regular expressions
import re
import time

#given input to us
origin = "https://en.wikipedia.org/wiki/Electric_car"
max_depth = 6
max_links = 1000
start = 0
base_url = "https://en.wikipedia.org"

visited_link_file = open("visited_link_file_q1_electric_car.txt","w+")


def getChildLinks(parent):
	#we open a connection to download the whole page
	req = urlopen(parent)

	#reading the page to get its content into the memory.
	downloaded_page = req.read();

	#close the connection
	req.close()

	#now we will parse the html, to get different tags.
	html_content = BeautifulSoup(downloaded_page, "html.parser")

	#removing https://
	file_name = parent.replace("https://", "")
	#replacing slashes with _
	file_name = file_name.replace("/", "_")

	#file name update with correct path
	file_name = "html_files_q1_electric_car/" + file_name + ".txt"
	current_page_file = open(file_name,"w+")
	current_page_file.write(str(html_content))
	current_page_file.close()
	# print(html_content.a) just an example for my notes.

	#list of child links, this maintains all unique child to be traversed.
	child_link_list = []

	#pattern to look for is ^/wiki/
	pattern = re.compile("^/wiki/")
	all_a_tags = html_content.find_all("a",href=pattern)

	for a_tag in all_a_tags:
		link = a_tag["href"]
		#get link without the #, so to the the page itself rather than the section of the page.
		if(":" not in link):
			if "#" in link :
				#get part before # tag.
				url = link [: link.index('#')]
				child_link = base_url + url
				if child_link not in child_link_list:
					child_link_list.append(child_link)
			else:
				child_link = base_url + link
				if child_link not in child_link_list:
					child_link_list.append(child_link)

	return child_link_list


Queue = [] #prefer to say it a Queue rather than Frontier
Visited_url = [] #list of all visited urls
depth = 1 # it is one for origin
child_nodes = []

#adding origin i.e the first link to the queue.
Queue.append(origin)

while len(Queue) > 0 and len(Visited_url) < max_links and depth < max_depth:

	current_node = Queue.pop(0)
	next_nodes = getChildLinks(current_node)

	if len(next_nodes) > 0:
		Visited_url.append(current_node)
		visited_link_file.write(current_node+"\n")
		for node in next_nodes:
			if node not in child_nodes and node not in Visited_url:
				child_nodes.append(node)
		time.sleep(1)

	if len(Queue) == 0:
		depth += 1
		Queue = list(set(child_nodes))
		child_nodes = []

visited_link_file.close()
print("depth reached in the end : ", depth)
print("number of url visited : ", len(Visited_url))
print("all links added to file: visited_link_file_q1_electric_car.txt in this folder")










