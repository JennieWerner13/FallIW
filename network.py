import networkx as nx
import pickle
import operator

#################  SETTING UP OF NETWORK  #################

edge_list = pickle.load( open( "ingredients.edgelist", "rb" ) )

G = nx.parse_edgelist(edge_list, nodetype = str, data=(('weight',int),))

#################  INPUTTING RECIPE  #################

print 'Enter ingredients in the recipe'
print 'with the ingredient to substitute FIRST'
print 'and ingredients separated by COMMAS: ',
filename = raw_input()

# get individual ingredients, all separated by a comma
temp_ingreds = filename.split(',')
ingreds = []
for i in temp_ingreds:
	# remove whitespace, replace space with _, make all lowercase
	ingreds.append(i.strip().replace(' ', '_').lower())

#################  ANALYSIS OF NETWORK  #################

### setting up variables ###
# ingredient to substitute
x = ingreds[0]

# potential substitutions
neighbors = G.neighbors(x)

# degree for each ingredient in recipe
ingreds_degree = {}
# Getting the degree with weights for all in ingreds
for i in ingreds:
	total = 0
	if i in G: # checking if i is in network
		for n in G.neighbors(i):
			total = total + G[n][i]['weight']
		ingreds_degree[i] = total

all_potentials = []
#going through all neighbors
for n in neighbors:
	# don't want neighbors that are also ingredients
	if n not in ingreds:
		potential = 0
		#going through all ingredients, except X which is first
		for i in ingreds[1:]:
			if i in G: # checking if i is in network
				if n in G[i]:
					numer = G[n][i]['weight']
				else: # no edge between two
					continue
				denom = ingreds_degree[i]

				# for the first case, but want to keep zero in case never get to inside here
				if potential == 0:
					potential = (numer / float(denom))
				else:
					potential = potential * (numer / float(denom))

		#print n + "," + str(potential)
		all_potentials.append((n, potential))

all_potentialsX = []
# going through relationship to X
for n in neighbors:
	# don't want neighbors that are also ingredients
	if n not in ingreds:
		numer = G[n][x]['weight']
		denom = ingreds_degree[x]
		potentialX = numer / float(denom)
		
		all_potentialsX.append((n, potentialX))
		#print n + "," + str(potentialX)

# sorting
all_potentials.sort(key=operator.itemgetter(1), reverse=True)
all_potentialsX.sort(key=operator.itemgetter(1), reverse=True)

# printing out all options with values in both
final_potentials = []
dict_all = dict(all_potentials)
dict_allX = dict(all_potentialsX)

for i in dict_all:
	if i in dict_allX:
		potential = dict_all[i]
		potentialX = dict_allX[i]
		total_potential = potential + potentialX

		index = [y[0] for y in all_potentials].index(i)
		index_X = [y[0] for y in all_potentialsX].index(i)
		total_index = index + index_X

		#print i, potential, index, potentialX, index_X, total_potential
		final_potentials.append((i, total_index))

final_potentials.sort(key=operator.itemgetter(1))
for i in final_potentials[:10]:
	print str(i[1]) + "\t" + i[0]
