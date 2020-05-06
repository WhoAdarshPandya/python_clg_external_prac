# h = int(input("Enter h : "))
# b = int(input("Enter b : "))
# area = 0.5 * h *b
# print(area)
# p = int(input("Enter P : "))
# r = int(input("Enter R : "))
# n = int(input("Enter N : "))
# interest = p*r*n/100
# print(interest)

# formate = input("Enter Format (H/mm/) : ")
# if formate == 'H':
#     h = int(input("Enter H : "))
#     m = h*60
#     s = m*60
#     print(s)
# elif formate == "mm":
#     m = int(input("Enter M :"))
#     s = m*60
#     print(s)
# else:
#     print("invalid")


# a = int(input("Enter a"))
# b = int(input("Enter b"))
# print((a+b)**2)

# num = int(input("Enter num to diff 17 : "))
# if num >= 17:
#     main = num-17
#     print(main*2)
# else:
#     print(17-num)

# monthday = {
#     "january":30,
#     "february":28,
#     "march":23
# }
# month = input("Enter name of month : ").lower()
# print(monthday[month])

# num = int(input("enter num : "))
# if num>= 0 and num <=100:
#     print("between 100")
# elif num >100 and num <=1000:
#     print("between 1000")
# elif num > 1000 and num <=2000:
#     print("between 2000")
# else:
#     print("mega")

# n=[]
# pro=1
# elemCount = int(input("Enter Range"))
# for i in range(1,elemCount+1):
#     n.append(int(input(f"Enter num of {i}")))

# for i in n:
#     pro*=i

# print(pro)

# string = input("Enter palin string : ")
# if string == string[::-1]:
#     print("palindrom")

# list1 = [1,2,3,4,36,5,7,0]
# list1.sort()
# print(list1)

list2 = [12,2,3,4,5]
# min max are function
print(min(list2))
print(max(list2))
arr =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
arr.sort()
print(arr)
# for i in list1:
#     if i in list2:
#         print("in",i)
#     else:
#         print("not in list",i)

n = input("Enter anything : ")
if type(n) == type(str):
    print("string")
else:
    print("not string")
