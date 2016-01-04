# converts the datasets in tab-deliminated text to csv's for GEPHI
filename1 = 'danishrecipes_FIXED.txt'
filename2 = 'kaggle_test_FIXED.txt'
filename3 = 'kaggle_train_FIXED.txt'
filename4 = 'scirep-cuisines-detail/allr_recipes_FIXED.txt'
filename5 = 'scirep-cuisines-detail/epic_recipes_FIXED.txt'
filename6 = 'scirep-cuisines-detail/menu_recipes_FIXED.txt'
filename7 = 'all_FIXED.txt'

# all by filename 5
with open(filename7) as f:
	for line in f:
		a = line.strip().split('\t')

		for j in range(len(a)):
			for k in range(j+1, len(a)):
				print a[j] + "," + a[k]
'''

# filename 5
lines = open(filename5).read().splitlines()
for line in lines:
	a = line.strip().split('\t')

	for j in range(len(a)):
		for k in range(j+1, len(a)):
			print a[j] + "," + a[k]

'''
