f = open('./read_this_file_entire.txt','r')
num_lines = int(input("Enter number of lines : "))
for i in range(num_lines):
    line = f.readline()
    print(line,end="")
