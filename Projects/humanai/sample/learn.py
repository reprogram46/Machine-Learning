# code to append data to the datafile #

from pickle import dump


df_loc = 'datasets/small_dataset.dat'
df_dir = 'datasets'
df_name = 'small_dataset.dat'
# above three vars must correlate for efficient exception handling..
df_handle = None

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
	if 'exit' in i.lower():
		print('[ EXIT ]')
		exit()
	else:
		add()



def add():
	f_1 = valid('\nIntelligence %: ')
	f_2 = valid('Agression %: ')
	f_3 = valid('Humour %: ')
	lbl = str(input('Finally, is (s)he trustable: '))
	try:
		dump([[f_1,f_2,f_3], lbl], df_handle)
	except:
		print(' ## Some error occurred in adding data ## ')
		exit()
	resume(': ')




def main():
	global df_handle
	global df_loc, df_name, df_dir
	try:
		df_handle = open(df_loc, 'ab')
	except FileNotFoundError:
		print(' ## No dataset found. Creating a new dataset.')
		from os import system as cmd
		cmd("mkdir {} && touch {}".format(df_dir, df_name))
		# now, file is made #
		write_once = open(df_loc, 'wb')
		# write_once.dump([], df_handle)
		write_once.close()
		del write_once
		df_handle = open(df_loc, 'ab')
	add()
	print('\nAll values are to be on a scale of 0 to 100 (both inclusive).')
	print("Type 'exit' anytime to quit from the program.\n")
	
if __name__ == '__main__':
	main()