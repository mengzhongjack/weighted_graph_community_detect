Detecting Communities in Weighted Graphs
========================================

## Input
 
A weighted graph G. See graph.txt file as a sample for the input graph format. It's a CSV file where each line has the following format: 

	u,v,w 

Above line specifies that there is an edge between node u and v with positive weight w. 
The lowest id should be zero and the nodes id's increase. If you want to used this code for an unweighted graph, 
simply set the weight equal to one on each input line.

## Output

This code runs Girvan-Newman algorithm and returns a list of detected communities with maximum modularity.

## Dependencies

For running the python code, you need to install Python 2.7 and NetworkX package on your machine. Check link below for more details:

	https://networkx.github.io/documentation/latest/install.html

## Girvan-Newman Algorithm Description

You can find the details for how Girvan-Newman algorithm works from the following link: 

	http://www.kazemjahanbakhsh.com/codes/cmty.html

## How to run Python script

	python cmty.py graph.txt

有问题 请找  公众号:
开始倒计时

Technical details:
The implemented algorithm works as follows [1].

Girvan-Newman Alg (Input: A weighted graph G, Output: A list of components of G.)

    BestQ = 0.
    Read the input file (the crawled data) and build the corresponding weighted social graph G.
    Compute the number of components of the graph G (init_ncomp).
    Calculate the weighted version of edge-betweenness for all edges of the graph G.
    Find the edge with the highest betweenness and remove it from G.
    Compute the number of components in G after edge removal (ncomp).
    If ncomp <= init_ncomp go to step 3.
    Compute the modularity of the current version of graph G and store it in Q.
    If Q > BestQ then save the current decomposition of G as the best division in BestComps.
    If there is not any edge left in G return BestComps otherwise go to step 2.
