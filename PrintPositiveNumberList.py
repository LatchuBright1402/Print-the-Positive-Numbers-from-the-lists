# Python program to print positive Numbers in a List

# list of numbers
list1 = [12,-7,5,64,-14]
list2 = [12,14,-95,3]
PList1 = []
PList2 = []

# iterating each number in list
for num1 in list1:

    # checking condition
    if num1 >= 0:

        #print(num1, end=" ")

        PList1.append(num1)
print(PList1)


for num2 in list2:

    # checking condition
    if num2 >= 0:

        #print(num2, end=" ")
        PList2.append(num2)
print(PList2)



