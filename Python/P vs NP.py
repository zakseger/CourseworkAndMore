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
for line in lines:                      ## O(N)
    x += 1                              
    All_Students.append(line)           

random.shuffle(All_Students)

## The Whitelist is all the pairs that aren't allowed.
## This is a list of 20 not allowed pairs, or 40% of the
## total maximum pairs. With thes sizes the program
## completes itself in about 0.3s minute total. As you add
## more exceptions to this program the literal time it takes
## to complete will grow very slowly
    
Whitelist = [[ 'GRAVES\n', 'MURRAY'],[ "JONES\n", "COBB\n" ],
             [ "MILLER\n", "FLOWERS\n"], ['JIMENEZ\n', 'MURRAY'],
             ['CHAVEZ\n', 'MONTGOMERY\n'], ['JONES\n', 'COBB\n'],
             ['GONZALEZ\n', 'NEWTON\n'], ['HORTON\n', 'GOMEZ\n'],
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
## of our data, based on joining the list from end to end, and allows
## us to create many initial sets that will end up qualifying as
## allowed sets. For the purpose of solving the problem, it does
## not matter whether or not this data is sorted.
## Time Complexity: O(n)

x = 0
for student in All_Students:                    ## O((logN) 
        
    lastS = int(len(All_Students) - 1)
        
    if student == All_Students[0]: 	
        Housing_List.append([student,  All_Students[lastS]])
            
    elif x > int(lastS / 2) :
        Housing_List.append([student, 0])
        break

    else:
        Housing_List.append([student,  All_Students[lastS - x]])
        x  +=  1

## In this next loop we will be comparing each sublist in our Housing List,
## with each sublist in our Whitelist. We say for every sublist in in our
## randomly generated Housing List, check every sublist in our Whitelist
## to see whether or not it should be there. If the match is not allowed,
## add it to another list, called  deleted list, as single values
## once again, then delete it from the Housing List. 

                                                ## O((N*N+N)/2) = O((N^2)/2)
n = 0
for set1 in Housing_List:
    for set2 in Whitelist:
            Backset = [[set2[0], set2[1]]]
            if set1 == set2 or set1 == Backset:
                    del_list.append(set1)
                    Housing_List.remove(set1)
              
    n += 1

## Now, since we have the values we want to use still at our disposal, we need
## to turn them into a random set of new lists to pull from again.

y = 0 
for set1 in del_list:                       ## O(N)
    new_list.append(set1[0])
    print(set1[0])
    new_list.append(set1[1])
        
    del del_list[y]
    y += 1
del_list = []

print("Housing List: ", Housing_List,
      "\n\nWhitelist: ", Whitelist,"\n\nNew List: ", new_list)

time_now = time.time()

## The following line deletes all duplicates from our list.

if new_list is not None:
    new_list = list(dict.fromkeys(new_list))

print("Housing List Length:", len(Housing_List))
print("New List Length:", len(new_list))

## Finally, the meat of the operation. We start comparing the lists and
## eliminating what we dont want and then repurposing it into what we do
## want. First we compare every value set in the new_list which we've
## created all the value sets in our Whitelist. The Whitelist is the
## value sets that are not allowed. If the two sets are equal then we go
## ahead and add the value set to a list called deleted list, and further
## actually remove the option from new_list altogether. We also take into
## account that the set we are comparing too could be a backwards pair
## of what we don't want, so we scrape the data, turn it backwards, and
## compare it as a new list as well. 
        
for set1 in new_list:                       ## O((N*N+N+N)/2) = O((N^2)/2)
    for set2 in Whitelist:
        Backset = [[set2[0], set2[1]]]
        if set1 == set2 or set1 == Backset:
                del_list.append(set1)
                new_list.remove(set1)

## In this next loop we structure the exact same way, but this time we are
## comparing our Housing_List with Whitelist. In the end here, we see the 
## same action type. This time what is different is that we are actually 
## doing is removing the bad value set from the Housing_List itself,  
## cleaning it out in the process.

for set1 in Housing_List:                   ## O((N*N+N)/2) = O((N^2)/2))
    for set2 in Whitelist:
        Backset = [[set2[0], set2[1]]]
        if set1 == set2 or set1 == Backset:
                del_list.append(set1)
                Housing_List.remove(set1)

## Now those data sets we deleted are turned into individual strings,
## in reverse order to help randomization, and appended to into the the 
## new_list list. Once we have completed that task we then need to clean
## up all our trash, so we just reset the deleted list, del_list, to
## and empty list structure.

for set1 in del_list:                       ## O(N)
    new_list.append(set1[1])
    new_list.append(set1[0])
        
del_list = []

## So at this point we have taken out the garbage, done the rest of our chores,
## and actually get to start having fun. As it turns out, since there are such an
## insane number of combinations that do not conform to the rules, our new list
## stays comparatively tiny compared to the rest of our lists. It also turns out to
## be a useless set no matter how many times you shuffle it, so we can throw it out
## too at this point.

new_list = []

print("Housing List Length w/ Errors =", len(Housing_List), '\n')

## Last and most important we are going to check out list for all the types of sets
## We aren't allowing. We say that if the nested list contains the same name in both
## locations, we can throw it out, because you cant be your own roommate. Then, if
## there is a name set that only contains one name, and a zero value in its other
## container, this is dues to our elif method above, and we can throw it out as well.
## Our 3rd method below here is to make sure that no student is inside of more than
## one pair in the list. We keep count for each student in the list, and if they
## appear a second time the list they appear in secoond is deleted.

for setN in Housing_List:
    if setN[0] == setN[1]:
        Housing_List.remove(setN)

for setN in Housing_List:                   ## O(N+N) = O(N)
    if setN[1] == 0:
        Housing_List.remove(setN)
        
for student in All_Students:                ## O(N*N+N+N) = O(N^2)
    s = 0
    for setN in Housing_List:
        if student == setN[0] or student == setN[1]:
            s += 1            
        if s == 2:
            Housing_List.remove(setN)

## This method tests whether or not we actually have a dataset that does not include
## any names within the whitelist. As you can see after running this program, the
## P = NP is now proven.

def passFail(list1, list2):                 ## O(N*N+N) = O(N^2)
    for x in list1:
        for y in list2:
            if x == y:
                print("FAIL")
                return
    print("Success!!")    
    
passFail(Housing_List, Whitelist)
print(len(Housing_List), 'Unique Combinations Created!\n')

print("Final Housing List: ", Housing_List,)

## Final Thoughts:
## O(N^2) is better than polynomial my freinds..
## I am curious if my math is right for the O(N) = (N^2) / 2
## I believe it is if you graph all values from of N 0..10000 you get 5 * 10^7 max = 50,000,000
##                                         doing so with n^2 gets you 1 * 10^8 max = 100,000,000
## I say it is /2 because all variables are made into tuples, and iterated to in
## one step. Therefore, 1step/2data is where I get the /2 from.
## Too Easy..
## I Think I'll go solve Sodoku now..

    
