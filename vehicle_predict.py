# python-3.6.3
# code to predict a vehicle type based on mileage and weight #

## each element of features[] is [km-per-litre, weight] ##

from sklearn import tree

def main():
	clf = tree.DecisionTreeClassifier()
	features = [[60, 500], [30, 600], [10, 2000], [30, 1800], [20, 800], [3, 1600]]
	labels = ['bike', 'bike', 'car', 'car', 'bike', ''car]
	mileage = float(input('Kilometres per litre: '))
	weight = float(input('Heaviness (in kg): '))
	print('Vehicle is more likely to be a {}'.format(clf.predict([[mileage, weight]])))

if __name__ == '__main__':
	main()
