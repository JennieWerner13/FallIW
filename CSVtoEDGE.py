import pickle

all_edges_count = {}

with open('all.csv') as f:
	for line in f:
		a = line.strip().split(',')
		if a[0].startswith('"') and a[0].endswith('"'):
			a[0] = a[0][1:-1]
		if a[1].startswith('"') and a[1].endswith('"'):
			a[1] = a[1][1:-1]

		key = min(a) + " " + max(a)
		if key in all_edges_count:
			all_edges_count[key] = all_edges_count[key] + 1
		else:
			all_edges_count[key] = 1

all_edges = []
for i in all_edges_count:
	to_add = i + " " + str(all_edges_count[i])
	all_edges.append(to_add)

# saves the list for network
pickle.dump( all_edges, open( "ingredients.edgelist", "wb" ) )
print "saved to file   ingredients.edgelist"
