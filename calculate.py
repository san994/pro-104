import csv
from collections import Counter

with open('C:\\Users\\user\\desktop\\pythonProject\\pro 104\\heightweight.csv',newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data=[]

for i in range(len(file_data)):
    num = file_data[i][2]
    new_data.append(float(num))

def mean(data):
    n = len(data)
    total = 0

    for x in new_data:
        total+=x

    mean = total/n

    return mean

def median(data):
    n = len(data)
    data.sort()

    if n%2==0:
        median1 = float(data[n//2])
        median2 = float(data[n//2-1])

        median = (median1+median2)/2
    else:
        median = data[n//2]

    return median

def mode(data):
    new_data = Counter(data)
    mode_data_for_range = {'50-60':0,'60-70':0,'70-80':0}

    for weight,occurence in new_data.items(): 
        if(50<float(weight)<60):
            mode_data_for_range['50-60']+=occurence
        elif(60<float(weight)<70):
            mode_data_for_range['60-70']+=occurence
        elif(70<float(weight)<80):
            mode_data_for_range['70-80']+=occurence

    mode_range,mode_occurence = 0,0

    for range,occurence in mode_data_for_range.items():
        if(occurence>mode_occurence):
            mode_range,mode_occurence=[int(range.split("-")[0]),int(range.split("-")[1])],occurence

    mode = float((mode_range[0]+mode_range[1])/2)
    
    return mode

mode = mode(new_data)
median = median(new_data)
mean = mean(new_data)

inp = input("enter what you want(mean,median,mode): ")

if(inp=="mean"):
    print("mean = ",mean)
elif(inp=="median"):
    print("median = ",median)
elif(inp=="mode"):
    print(f"mode is {mode:2f}")
else:
    print("plz enter a valid thing")
