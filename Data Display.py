import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import csv

#https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot
SMALL_SIZE = 18
MEDIUM_SIZE = 20
BIGGER_SIZE = 20

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title



def find_name(list, name):
    for item in range(len(list)):
        if list[item] == name:
            return item

def display_wireframe(X,Y,Z):
    fig = plt.figure()
    plt.rcParams.update({'font.size': 42})
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X[0], Y[0], Z[0], zdir='z', s=180, color='green', label='Start')
    ax.scatter(X[len(X)-1], Y[len(Y)-1], Z[len(Z)-1], zdir='z', s=180, color='red', label='End')
    Z = (Z,Z)
    ax.plot_wireframe(np.array(X),np.array(Y),np.array(Z))
    plt.show()

def display_pie(tags,mouse_clicks):
    labels = tags
    sizes = mouse_clicks
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%.0f%%')
    plt.show()

#Main Program
with open('Trial_test_data.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    X = []
    Y = []
    Z = []
    mouse_clicks = []

    firstpast = True
    labels = ""

    index_coords = 0
    index_clicks = 0
    for row in csvReader:
        if firstpast == True:
            index_coords = find_name(row,"X")
            index_clicks = find_name(row,"Button_active")
            firstpast = False
            pass
        else:
            X.append((float(row[index_coords])))
            Y.append((float(row[index_coords+1])))
            Z.append((float(row[index_coords+2])))
            mouse_clicks.append(row[index_clicks])

    #Actual tagging system for mouseclicks
    filtered_clicks = []
    mouse_click_per_tag = []

    for item in mouse_clicks:
        if item == "":
            item = "No action"
        if item not in filtered_clicks:
            filtered_clicks.append(item)



    counter = 0
    for item in filtered_clicks:

        for tag in mouse_clicks:
            if tag == item:
                try:
                    mouse_click_per_tag[counter] += 1
                except:
                    mouse_click_per_tag.append(1)
        counter += 1


    #Comment out to see either the pie chart or the linear chart versions
    display_pie(filtered_clicks,mouse_click_per_tag)
    #display_wireframe(X,Y,Z)



