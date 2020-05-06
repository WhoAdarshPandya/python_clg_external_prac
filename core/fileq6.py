list= ["\nthis is append1","\nthis is append2","\nthis is append3"]
file = open('./read_this_file_entire.txt','r')
# file.writelines(list)
data= file.readlines()
n = int(input("Enter random line no : "))
print(data[n-1])