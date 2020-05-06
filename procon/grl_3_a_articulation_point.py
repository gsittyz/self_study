# Python program to find articulation points in an undirected graph

# #This class represents an undirected graph
# #using adjacency list representation
# class Graph:

# 	def __init__(self,vertices):
# 		self.V= vertices #No. of vertices
# 		self.graph = defaultdict(list) # default dictionary to store graph
# 		self.Time = 0

# 	# function to add an edge to graph
# 	def addEdge(self,u,v):
# 		self.graph[u].append(v)
# 		self.graph[v].append(u)

# 	'''A recursive function that find articulation points
# 	using DFS traversal
# 	u --> The vertex to be visited next
# 	visited[] --> keeps tract of visited vertices
# 	disc[] --> Stores discovery times of visited vertices
# 	parent[] --> Stores parent vertices in DFS tree
# 	ap[] --> Store articulation points'''
# 	def APUtil(self,u, visited, ap, parent, low, disc):

# 		#Count of children in current node
# 		children =0

# 		# Mark the current node as visited and print it
# 		visited[u]= True

# 		# Initialize discovery time and low value
# 		disc[u] = self.Time
# 		low[u] = self.Time
# 		self.Time += 1

# 		#Recur for all the vertices adjacent to this vertex
# 		for v in self.graph[u]:
# 			# If v is not visited yet, then make it a child of u
# 			# in DFS tree and recur for it
# 			if visited[v] == False :
# 				parent[v] = u
# 				children += 1
# 				self.APUtil(v, visited, ap, parent, low, disc)

# 				# Check if the subtree rooted with v has a connection to
# 				# one of the ancestors of u
# 				low[u] = min(low[u], low[v])

# 				# u is an articulation point in following cases
# 				# (1) u is root of DFS tree and has two or more chilren.
# 				if parent[u] == -1 and children > 1:
# 					ap[u] = True

# 				#(2) If u is not root and low value of one of its child is more
# 				# than discovery value of u.
# 				if parent[u] != -1 and low[v] >= disc[u]:
# 					ap[u] = True

# 				# Update low value of u for parent function calls
# 			elif v != parent[u]:
# 				low[u] = min(low[u], disc[v])


# 	#The function to do DFS traversal. It uses recursive APUtil()
# 	def AP(self):

# 		# Mark all the vertices as not visited
# 		# and Initialize parent and visited,
# 		# and ap(articulation point) arrays
# 		visited = [False] * (self.V)
# 		disc = [float("Inf")] * (self.V)
# 		low = [float("Inf")] * (self.V)
# 		parent = [-1] * (self.V)
# 		ap = [False] * (self.V) #To store articulation points

# 		# Call the recursive helper function
# 		# to find articulation points
# 		# in DFS tree rooted with vertex 'i'
# 		for i in range(self.V):
# 			if visited[i] == False:
# 				self.APUtil(i, visited, ap, parent, low, disc)

# 		for index, value in enumerate (ap):
# 			if value == True: print index,


timer = 0


def find_articulation(node, visited, disc, low, parent, ap, tonodes):
    global timer
    children = 0
    visited[node] = True
    disc[node] = low[node] = timer
    timer += 1
    for nextnode in tonodes[node]:
        if not visited[nextnode]:
            parent[nextnode] = node
            children += 1
            find_articulation(nextnode, visited, disc, low, parent, ap, tonodes)
            low[node] = min(low[node], low[nextnode])
            if parent[node] is None and children > 1:
                # ルートで子供がいる
                ap[node] = True
            if parent[node] is not None and low[nextnode] >= disc[node]:
                # nextnodeから後ろのnodeには遡ることができない
                ap[node] = True
        elif nextnode != parent[node]:
            low[node] = min(low[node], disc[nextnode])


def articulation(tonodes, v):
    visited = [False for _ in range(v)]
    disc = [float("inf") for _ in range(v)]  # 発見の順番を記憶する
    low = [float("inf") for _ in range(v)]  # uの子孫から遡ることができて、prenumが一番小さいuの先祖
    parent = [None for _ in range(v)]  # 深さ優先探索における親
    ap = [False for _ in range(v)]  # 関節点を記録する
    global timer
    timer = 0
    for i in range(v):
        if not visited[i]:
            find_articulation(i, visited, disc, low, parent, ap, tonodes)
    for i in range(v):
        if ap[i]:
            print(i)


def main():
    ve = input().split()
    v, e = tuple(map(int, ve))
    tonodes = [[] for _ in range(v)]
    for _ in range(e):
        st = input().split()
        s, t = tuple(map(int, st))
        tonodes[s].append(t)
        tonodes[t].append(s)
    articulation(tonodes, v)


if __name__ == "__main__":
    main()
