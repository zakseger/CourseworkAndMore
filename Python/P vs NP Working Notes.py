## Zackary Seger
## Begin Date & Time: 2/20/2020 at about 9:00PM
## Completion Date & Time: 2/21/2020 at around 1:00AM
## First Draft was written in word and saved that way, lol.
##
##      So What the Heck is P vs NP anyway?
##
##  P:  Solving Problems that have simple alrgorithms and like multiplication.
##  NP: Sovings problems such as a mixed up 10x10 rubic's cube or a 100x100
##      sodoku grid.
##
##      Polynomial Time (P):
##          
##          total steps = function(Nsized)
##          S = f(N)
##
##          This function can contain n, n^2, n^x, but not exponential
##          functions such as 2^n, where the growth rate is too large 
##          for feasible programming speeds.
##
##      Non-Deterministic Polynomial Time (NP):
##          
##          S = P(AreYouKiddingMe)
##
##              We need to take into consideration that this is the maximum
##              number of steps required to solve the problem. In reality, as
##              we explore in this program, it is possible to categorize and
##              manipulate your data that significantly reduces this value.
##
## 
##      quote, "If P = NP, then the world would be a profoundly different place
##              There would be no special value in "creative leaps," no 
##              fundemental gap between solving the solution and recognizing
##              the solution once its found. Everyone who could appreciate a 
##              symphony would be Motzart; everyone who could follow a step-
##              by-step process would be Guass.
##                                                  - Scott Aaronson
##
##
##
##

import time                             ## For this program we require both
import random                           ## the time and random libraries.

start_time = time.time()                ## Creates a base time

file = open("names.txt", "r")           ## This is a list of 400 names
lines = file.readlines()

## This is how we add the names to the first list, All Students. We just
## navigate the text file line by line, and add each word to All Students
## list.
## Time Complexity = O(n)

x = 0
All_Students = [] 
for line in lines:                      
    x += 1                              
    All_Students.append(line)           

## The Whitelist is all the pairs that aren't allowed.
## This is a list of 20 not allowed pairs, or 40% of the
## total maximum pairs. With thes sizes the program
## completes itself in about 1 minute total. As you add
## more exceptions to this program the literal time it takes
## to complete will grow quickly. With only 10 Whitelist
## entries the program will complete itself in about 15 seconds.
    
Whitelist = [[ "WILLIAMS\n", "MOODY"],[ "BROWN\n", "COBB\n" ],
             [ "MILLER\n", "FLOWERS\n"], ["JONES\n", "MOODY"],
             ['CHAVEZ\n', 'MONTGOMERY\n'], ['BAKER\n', 'TODD\n'],
             ['GONZALEZ\n', 'NEWTON\n'], ['NELSON\n', 'ROBBINS\n'],
             ['CARTER\n', 'RODGERS\n'], ['MITCHELL\n', 'HARMON\n'],
             ['PEREZ\n', 'COHEN\n'], ['ROBERTS\n', 'MANNING\n'],
             ['TURNER\n', 'GLOVER\n'], ['PHILLIPS\n', 'VEGA\n'],
             ['CAMPBELL\n', 'AGUILAR\n'], ['PARKER\n', 'DELGADO\n'],
             ['EVANS\n', 'FARMER\n'], ['EDWARDS\n', 'MCGEE\n'],
             ['COLLINS\n', 'DENNIS\n'], ['PALMER\n', 'SILVA\n'],
             ['MILLS\n', 'CARLSON\n'], ['NICHOLS\n', 'HOFFMAN\n'],
             ['GRANT\n', 'BREWER\n'], ['KNIGHT\n', 'FOWLER\n'],
             ['FERGUSON\n', 'MEDINA\n'], ['ROSE\n', 'BOWMAN\n'],
             ['STONE\n', 'MORENO\n'], ['HAWKINS\n', 'MENDOZA\n'],
             ['DUNN\n', 'DAY\n'], ['PERKINS\n', 'HANSON\n'],
             ['HUDSON\n', 'BURKE\n'], ['SPENCER\n', 'FRAZIER\n'],
             ['GARDNER\n', 'LARSON\n'], ['STEPHENS\n', 'WELCH\n'],
             ['PAYNE\n', 'ROMERO\n'], ['PIERCE\n', 'GARRETT\n'],
             ['BERRY\n', 'GILBERT\n'], ['MATTHEWS\n', 'DEAN\n'],
             ['ARNOLD\n', 'LYNCH\n'], ['MATTHEWS\n', 'LYNCH\n']]

Housing_List = []
del_list = []
new_list = []

## The following is a for loop that iterates through each student in
## the list we created, and it inserts all of our data into pairs by
## traversing the list from outside in. This is a random distribution
## of our data, which is also in a random order originally, and allows
## us to create many initial sets that will end up qualifying as
## allowed sets. For the purpose of solving the problem, it does
## not matter whether or not this data is sorted.
## Time Complexity: O(n)

x = 0
for student in All_Students:
	
    lastS = int(len(All_Students) - 1)
	
    if student == All_Students[0]: 	
        Housing_List.append([student,  All_Students[lastS]])
            
    elif x > int(lastS / 2) :
        Housing_List.append([student, 0])
        break

    else:
        Housing_List.append([student,  All_Students[lastS - x]])
        x  +=  1

print("first loop complete \n\n")
print(Housing_List)

## In this next loop we will be comparing each sublist in our Housing List,
## with each sublist in our Whitelist. We say for every sublist in in our
## randomly generated Housing List, check every sublist in our Whitelist
## to see whether or not it should be there. If the match is not allowed,
## then delete it from the Housing List, and add it to another list called
## 


n = 0
for set1 in Housing_List:
    for set2 in Whitelist:
            Backset = [[set2[0], set2[1]]]
            if set1 == set2 or set1 == Backset:
                    del_list.append(set1)
                    Housing_List.remove(set1)
              
    n += 1


print("second loop complete \n")
 
y = 0 
for set1 in del_list:
    new_list.append(set1[0])
    new_list.append(set1[1])
	
    del del_list[y]
    y += 1
del_list = []


print("third loop complete \n\nHousing List: ", Housing_List,
      "\n\nWhitelist: ", Whitelist,"\n\nNew List: ", new_list)

time_now = time.time()
q = 0
while q < 500:

    new_list = list(dict.fromkeys(new_list))
        
    
    if len(Housing_List) < 200:
        print(q)
        print("Housing List Length:", len(Housing_List))
        print("New List Length:", len(new_list))
        random.shuffle(new_list)
            
        q += 1
        n = 0	
        for set1 in new_list:
            for set2 in Whitelist:
                Backset = [[set2[0], set2[1]]]
                if set1 == set2 or set1 == Backset:
                        del_list.append(set1)
                        new_list.remove(set1)
            n += 1
        
        for set1 in Housing_List:
            for set2 in Whitelist:
                Backset = [[set2[0], set2[1]]]
                if set1 == set2 or set1 == Backset:
                        del_list.append(set1)
                        Housing_List.remove(set1)
            n += 1
         

        y = 0 
        for set1 in del_list:
            new_list.append(set1[1])
            new_list.append(set1[0])
                
            del del_list[y]
            y += 1
        del_list = []

        x = 0
        for student in new_list:
                
            lastS = int(len(new_list) - 1)
                
            if student == new_list[0]: 	
                Housing_List.append([student,  new_list[lastS]])
                    
            elif x > int(lastS / 2) :
                Housing_List.append([student, 0])
                break

            else:
                Housing_List.append([student,  new_list[lastS - x]])
                x  +=  1
                
        for set1 in Housing_List:
            for set2 in Whitelist:
                Backset = [[set2[0], set2[1]]]
                if set1 == set2 or set1 == Backset:
                        del_list.append(set1)
                        Housing_List.remove(set1)

        for setN in Housing_List:
            if setN[0] == setN[1]:
                Housing_List.remove(setN)

        for setN in Housing_List:
            if setN[1] == 0:
                Housing_List.remove(setN)
                
        for student in All_Students:
            s = 0
            for setN in Housing_List:
                if student == setN[0] or student == setN[1]:
                    s += 1            
                if s == 2:
                    Housing_List.remove(setN)

##

for set1 in Housing_List:
    for set2 in Whitelist:
        Backset = [[set2[0], set2[1]]]
        if set1 == set2 or set1 == Backset:
                del_list.append(set1)
                Housing_List.remove(set1)

for setN in Housing_List:
    if setN[0] == setN[1]:
        Housing_List.remove(setN)

for setN in Housing_List:
    if setN[1] == 0:
        Housing_List.remove(setN)
        
for student in All_Students:
    s = 0
    for setN in Housing_List:
        if student == setN[0] or student == setN[1]:
            s += 1            
        if s == 2:
            Housing_List.remove(setN)
        
print("Complete \n\nHousing List: ", Housing_List,
      "\n\nWhitelist: ", Whitelist)

print(len(Housing_List))
print("Seconds to completion: ", time.time() - start_time)
    
