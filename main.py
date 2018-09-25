from numpy import *

dataset = genfromtxt('data.csv', delimiter=',')
print dataset

newM = 0

#Hyper Parameters
learningRate = 0.0001
trainingSteps = 1000
startingM = 1

def errorRate(data, m):
        a = 0.0
        for points in data:
                x = points[0]
                y = points[1]
                a = a + ((y-(x**m))**2)
        a = a/len(data)
        return(a)

def delta(data, m):
	a = 0.0
	for points in data:
		x = points[0]
		y = points[1]
		a = a + -2 * (x**m) * log(x) * (y-x**m)
	a = a/len(data)
	a = a*learningRate
	return(a)

deriv=delta(dataset, startingM)
print("Derivitive: ")
print(deriv)
print("Error Rate: ")
print(errorRate(dataset, startingM))
newM = startingM - deriv
print("Error Rate after Delta 1: ")
print(errorRate(dataset, newM))

for i in xrange(trainingSteps):
        newM = newM - delta(dataset, newM)
print("Error Rate after " + str(trainingSteps) + " Trainings")
print(errorRate(dataset, newM))
print("New M")
print(newM)

