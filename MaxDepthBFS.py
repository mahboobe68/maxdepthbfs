def bfs_edges(G, source, reverse=False, L=0):
    if reverse :#and isinstance(G, nx.DiGraph):
        neighbors = G.predecessors_iter
    else:
        neighbors = G.successors_iter
        #print ("neighbors::: {0}" .format(neighbors))
    visited = set([source])
    del visit_bfs[:]
    visit_bfs.append(source)
    queue = deque([(source, neighbors(source), 0)])
    
    #qqueue = queue
    
    while queue:# and qqueue:
        parent, children, v = queue[0]
        q= children
        #print ("parent::: {0}" .format(parent ))
        #print ("children::: {0}" .format(children ))
        front= queue.popleft()
        #print ("front::: {0}" .format(front ))
        level = front[2]
        #print ("level::: {0}" .format(level ))
        if level >= L:
		      break
        level +=1
        
        for child in children:#while next(q):
            #child = next(children)
            #print ("child::: {0}" .format(child))
            
            if child not in visited:
                yield parent, child
                visited.add(child)
                visit_bfs.append(child)
                queue.append((child, neighbors(child), level))
	