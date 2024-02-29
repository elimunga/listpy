#Create an empty list called my_list
my_list=[]
print("Empty List: ",my_list)

#Appending 10,20,30 and 40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("Appended List: ",my_list)

#Inserting 15 at the second position in my_list
my_list.insert(1,15)
print("Inserted element(15): ",my_list)

#Extending my list with [50,60,70]
my_list.extend([50,60,70])
print("Extended List: ",my_list)

#Removing the last element from my_list
my_list.remove(my_list[-1])
print("Removed element(last): ",my_list)

#sorting my_list in ascending order
my_list.sort()
print("Sorted in ascending: ",my_list)

#Finding index of 30 in my_list
index=my_list.index(30)
print("Index of 30: ",index)