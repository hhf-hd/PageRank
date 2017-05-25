from pygraph.classes.digraph import digraph
import sys
import re
import urllib
from bs4 import BeautifulSoup

class PRIterator:
	__doc__ = '''cal''' 

	def __init__(self, dg):
		self.damping_factor = 0.85  
		self.max_iterations = 100  
		self.min_delta = 0.00001 
		self.graph = dg

	def page_rank(self):
		for node in self.graph.nodes():
			if len(self.graph.neighbors(node)) == 0:
				for node2 in self.graph.nodes():
					digraph.add_edge(self.graph, (node, node2))

		nodes = self.graph.nodes()
		graph_size = len(nodes)

		if graph_size == 0:
			return {}
		page_rank = dict.fromkeys(nodes, 1.0 / graph_size)  
		damping_value = (1.0 - self.damping_factor) / graph_size

		flag = False
		for i in range(self.max_iterations):
			change = 0
			for node in nodes:
				rank = 0
				for incident_page in self.graph.incidents(node):
					rank += self.damping_factor * \
					(page_rank[incident_page] / len(self.graph.neighbors(incident_page)))
				rank += damping_value
				change += abs(page_rank[node] - rank) 
				page_rank[node] = rank

		return page_rank

def Is_Key_Words_In(url,Key_Words):
	Page =urllib.urlopen(url)
	soup = BeautifulSoup(Page,"html.parser")
	for p_tag in soup.find_all('p'):
		Str = p_tag.get_text()
		Is_In = re.compile(r'([\s\S]*)%s([\s\S]*)'%(Key_Words),re.S)
		matchObj = Is_In.search(Str)
		if matchObj:
			return 1
	return 0
def Get_Node(url):
	Res = re.search(r'http://www.personalwebhhf.cn/PageRank/Page(.*).html',url,re.M|re.I)
	if Res:
		#print Res.group(1)
		return Res.group(1)
def Get_Graph(Key_Words):
	Node_List = []
	Url_List = []
	Eage_List = []
	url = "http://www.personalwebhhf.cn/PageRank/PageB.html"
	node1 = Get_Node(url)
	#start from PageA
	if Is_Key_Words_In(url,Key_Words):
		node = Get_Node(url)
		Node_List.append(node)
		#print Node_List
	Page =urllib.urlopen(url)
	soup = BeautifulSoup(Page,"html.parser")
	for Link in soup.find_all('a'):
		Link_Url = Link.get("href")
		
		Url_List.append(Link_Url)
	#start page to his link
	for Link_Url in Url_List:
		#print Link_Url
		if Is_Key_Words_In(Link_Url,Key_Words) and Is_Key_Words_In(url,Key_Words):
			node = Get_Node(Link_Url)
			Eage_List.append((node1,node))
			

	#start from Url_List
	for Link_Url in Url_List:
		
		if Is_Key_Words_In(Link_Url,Key_Words):
			node = Get_Node(Link_Url)
			Node_List.append(node)
		#print Node_List
		Page =urllib.urlopen(Link_Url)
		soup = BeautifulSoup(Page,"html.parser")
		for Link in soup.find_all('a'):
			href = Link.get("href")
			
			if (href in Url_List)==False and href!=url:
				Url_List.append(href)
				#print "add"
			if Is_Key_Words_In(href,Key_Words) and Is_Key_Words_In(Link_Url,Key_Words):
				node1 = Get_Node(Link_Url)
				node2 = Get_Node(href)
				Eage_List.append((node1,node2))
	return Node_List,Eage_List
	

if __name__ == '__main__':
	
	Node_List=[]		 
	Edge_List = []		 
	Key_Words = sys.argv[1]  #get parameter from PageRank.php
	#print Key_Words
	Node_List,Edge_List=Get_Graph(Key_Words)  #get the node and the edge of the node
	#print Node_List,Edge_List
	dg = digraph()
	dg.add_nodes(Node_List)
	for Edge in Edge_List:
		dg.add_edge(Edge)
	pr = PRIterator(dg)
	page_ranks = pr.page_rank()
	page_ranks = sorted(page_ranks.items(),key=lambda item:item[1],reverse=True)
	#print("The final page rank is\n", page_ranks)
	for i in range(len(page_ranks)):
		url = "http://www.personalwebhhf.cn/PageRank/Page"+page_ranks[i][0]+".html"
		print url











