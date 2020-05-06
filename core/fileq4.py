# Python program to read last n lines of a file.
f= open('./read_this_file_entire.txt','r')
arr = f.readlines()
newarr= []
for i in arr:
    newarr.append(i.rstrip('\n'))
no_of_lines = int(input("Enter last lines no : "))
if no_of_lines > len(newarr):
    print("wrong")
else:
    i=0
    while(no_of_lines):
        print(newarr[len(newarr)-1-i])
        i+=1
        no_of_lines-=1