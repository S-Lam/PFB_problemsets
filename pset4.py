#pset 4 script that splits a string into a list
#! /usr/bin/env python3
species = "sapiens, erectus, neanderthalensis"
print (species)
species_list = species.split(",")
print (species_list)
alpha_species = sorted(species_list)
print (alpha_species)
print (sorted(alpha_species,key=len))


#print numbers 1 to 100 with while loop

count = 1
while count <101:
	print (count)
	count += 1

#while loop to calculate factorial of 1000

count = 1
product = 1
while count <1001:
	product = product*count
	count += 1
print ("factorial of 1000:",product)
#iterating through a list and only printing even numbers
my_list = [101,2,15,22,95,33,2,27,72,15,52]
for num in my_list:
	if num%2 ==0:
		print (num)

#sorting elements of above list and iterating through each element, printing, calculating cumulative sums

sort_list = sorted(my_list)
even_sum = 0
odd_sum = 0
for num in sort_list:
	print (num)
	if num % 2 == 0:
		even_sum += num
	else:
		odd_sum += num

print ("Sum of even numbers:", even_sum, "\nSum of odds:", odd_sum)

#(range) in for loop to print every number btwn 1-100 

for num in range(1,101):
	print (num)

#list comprehension to print number btwn 1:100

my_list = [num for num in range(1,101)]

for item in my_list:
	print (item)
