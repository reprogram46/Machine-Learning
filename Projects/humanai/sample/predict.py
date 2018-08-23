
# Loads the datafile. Inputs, and predicts.


from pickle import load
try:
	from sklearn import tree
except ImportError:
	print('Install the required libraries using:\n')
	print('\tpip3 install scipy')
	print('\tpip3 install sklearn\n')
	print('and restart the application.')
	exit()



def load_all_data(reader_handle):
	storage_list = []
	reader_handle.seek(0)	## reset file pointer ##
	while True:
		try:
			storage_list.append(load(reader_handle))
		except:
			return storage_list


# def valid(msg):
# 	while True:
# 		try:
# 			i = float(input(msg))
# 			if 'exit' in i.lower():
# 				print('[ EXIT ]')
# 				exit()
# 			if i<0 and i>100:
# 				print('Scale your values between 0 and 100')
# 			else:
# 				return i
# 		except:
# 			print('Only decimals and integers are allowed.')
# this was older...had errors


def valid(msg):
	while True:
		try:
			i = input(msg)
			if 'exit' in i.lower():
				print('[ EXIT ]')
				exit()
			i = float(i)
			if i<0 or i>100:
				print('Scale your values between 0 and 100')
			else:
				return i
		except:
			print('Only decimals and integers are allowed.')



def resume(msg):
	i = input(msg)
	if 'exit' in i:
		print('[ EXIT ]')
		exit()
	else:
		__predict__()



def __predict__():
	f_1 = valid('\nIntelligence level: ')
	f_2 = valid('Agression %: ')
	f_3 = valid('Humour %: ')
	print('\nBased on the data you provided, the prediction is: ')
	print(cfr.predict([[f_1, f_2, f_3]]))
	resume('\n: ')


datafile_loc = 'datasets/small_dataset.dat'
cfr = None
features, labels = [], []
DATA = []

def init_once():
	global cfr, features, labels, DATA
	global datafile_loc		## does not run without setting global
	cfr = tree.DecisionTreeClassifier()
	try:
		datafile = open(datafile_loc, 'rb')
		DATA = load_all_data(datafile)
		datafile.close()
		del datafile
		del datafile_loc
	except IOError:
		print('No dataset found. It was perhaps deleted.')
		print('\n\tRUN \'learn.py\' TO CREATE A NEW ONE\n')
		exit()

	for i in range(len(DATA)):
		features.append(DATA[i][0])
		labels.append(DATA[i][1])

	cfr = cfr.fit(features, labels)



def main():
	print('\nAll values are to be on a scale of 0 to 100 (both inclusive).')
	print("Type 'exit' anytime to quit from the program.\n")
	init_once()
	__predict__()


main()
# ALL ai VARIABLES:
#  
# cfr	
# features	
# labels
# datafile
# DATA

# features = [[0,3], [3,5], [6.4], [3,8]]
# labels = ['apple', 'orange', 'apple', 'orange']
# print cfr.predict([[inp_1, inp_2, inp_3]])
# combined = [
#                 [[0,3],'apple'],
#                 [[3,5],'orange'],
#                 [[6,4],'apple'],
#                 [[3,8],'orange']
#            ]
#
# combined[i] is a row;
# combined[i][0] is a set of features;
# combined[i][1] is the label;
# SUMMARY:
#   len(combined[i]) always returns 2 (features and labels)
#   len(combined) returns the number of rows
#   len(combined[i][j]) returns:
#       feature_count, if j == 0
#       bytes in the label string, if j == 1 



# """
# dataset looks like:
# [[1,5,4,7], 'fair'], []]
# """

def free_memory(elem_1, elem_2, elem_3):
	remove = [elem_1, elem_2, elem_3]
	for _ in range(len(remove)):
		del remove[_]
