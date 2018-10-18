#!/usr/bin/env python3

#dictionary of favorite things
myFavDict = {"tree": "redwood", "musical":"Hamilton", "book":"python for biologists!","food":"ramen", "husband":"Gerald"}
print (myFavDict)

print(myFavDict['book'])

fav_thing = 'book'
print(myFavDict[fav_thing])

print(myFavDict['tree'])

myFavDict['organism'] = 'giardia'

fav_thing = 'organism'
print (myFavDict[fav_thing])

inputFavThing = input("Name a category and I'll tell you my favorite thing in that category:")

print ("My favorite",inputFavThing, "is", myFavDict[inputFavThing])

myFavDict[fav_thing] = "manatee"
print ("New fav organism:",myFavDict[fav_thing])

inputFavSugg = input("But what do you think my favorite "+ inputFavThing+" should be?")

print("OK, my favorite", inputFavThing, "is now", inputFavSugg)

for item in myFavDict:
	print ((item, myFavDict[item]))
