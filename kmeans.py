#5/4/2020
#K - Mean nearest neighbour Algorithem
#this code can use on small data sets. Need to optimize to use in large data sets 
#Only 2 dimention for presentation
#Scalable for any dmentionality
#Scalable to any K value
#Current Version 1.0 

import numpy as np
import csv
import matplotlib
from matplotlib import pyplot as plt
import sys
import time


#Data Loading -----------------------------
#readig csv file
csv_file = open("D:/Projects/K Means/Book1.csv")
reader = csv.reader(csv_file)

#Intializing input fields
inputFild = []
XDimWise = []
newlist = []
distancesFromOneDataPoint = []


#List of list of input varialbles
for row in reader:
	line = list(map(int,row))  # One line of code to Map all string values in the list to Int
	inputFild.append(line)

numberOfDataPoints = len(inputFild)
dimentions = len(inputFild[0])

#Dimentionwise data list
for j in range(0,dimentions):
	for i in range(0,numberOfDataPoints):
		newlist.append(inputFild[i][j])
	print(newlist)
	print("**")
	XDimWise.append(newlist)
	newlist = []
	print(XDimWise)
	print("--")
	


inputArray = np.array(inputFild)
XDimWiseArray = np.array(XDimWise)


#-------------------------------------------

#Asignemnt of Cluster-----------------------
k = [[25,100],[170,25]]
kx = [k[0][0], k[1][0]]
ky = [k[0][1], k[1][1]]
k0Values = []
k1Values = []




plt.plot(XDimWise[0], XDimWise[1], 'ro',color ='y')
plt.plot(k[0][0], k[0][1], 'ro', color ='r',marker = "x")
plt.plot(k[1][0], k[1][1], 'ro', color ='b',marker = "x")
plt.axis([0, 200, 0, 200])
plt.show()


for p in range(0,50):
	time1 = time.time()

	for i in  range(0,numberOfDataPoints):
		a = inputArray[i]
		for j in range(0,dimentions):
			b = k[j]
			dist = np.linalg.norm(a-b) # Norm of a A- b matrix gives the same clculation to find dist	
			distancesFromOneDataPoint.append(dist)
			#print(dist)
		minDimIndex = distancesFromOneDataPoint.index(min(distancesFromOneDataPoint))
		minDist = min(distancesFromOneDataPoint) 
		#print(distancesFromOneDataPoint)
		#print(minDist)
		#print(minDimIndex)
		#print(inputArray[i])
		#print("------")
		if minDimIndex == 0:
			plt.plot(a[0],a[1],'ro',color='r')
			k0Values.append(inputArray[i])
		else:
			plt.plot(a[0],a[1],'ro',color='b')
			k1Values.append(inputArray[i])
		distancesFromOneDataPoint.clear()


	k0ValuesArray = np.array(k0Values)
	k1ValuesArray = np.array(k1Values)

	k[0] =  np.mean(k0ValuesArray, axis = 0)
	k[1] =  np.mean(k1ValuesArray, axis = 0)

	k0Values.clear()
	k1Values.clear()

	plt.plot(k[0][0], k[0][1], 'ro', color ='r',marker = "x")
	plt.plot(k[1][0], k[1][1], 'ro', color ='b',marker = "x")

	#print(k)

	#plt.pause(0.01)
	print(time.time()- time1)

plt.show()









#print(dir(name_of the var))   See what you can do with the var  Ex: count
#print(help(name_of the var.count))   See what you can do methods 
#print(type(name_of the var))  Get the type of th var

