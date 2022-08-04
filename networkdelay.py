import heapq as hq
class Solution:
	def adjacency_ls(times):
		# create a dictionary with the neighbor nodes and the weight.
		adjacency_ls = {}
		for node in times:
			if node[0] not in adjacency_ls.indices:
				adjacency_ls[node[0]] = [(node[1], node[2])]
			elif node[0] in adjacency_ls.indices:
				adjacency_ls[node[0]].append([(node[1], node[2])])
		return adjacency_ls
# TODO: table with high numbers assigned at the beginning
    def networkdelay(self, times, n, k):
    	priorityq = [k]
    	adjacency_ls = adjacency_ls(times)
    	while priorityq:
    		cur_node = hq.heappop(priorityq)
            adjacent, weight = adjacency_ls[cur_node]
            for i in cur_node_adjacent:
            	if weight + cur_weight > cur_weight:
            		cur_node = adjacent
            		cur_cost = weight + cur_weight
            	else:
            		continue




