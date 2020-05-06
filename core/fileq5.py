f=open('./read_this_file_entire.txt','r')
# get no of lines
data = f.read()
data = data.split('\n')
print(len(data))