 # This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.class Mathematics:
#largest element in list

#function
def largest(list):
    large= list[0]
    for i in list:
        if i>large:
            large=i
    return large

#list
list=[3, 9, 7, 3, 6, 5, 7, 24, 6]
print("largest in ",list,"is")
print(largest(list))
