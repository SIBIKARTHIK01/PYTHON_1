

# a= input("enter your password")
# if a == "password":
#     print("true")
# else:
#     print("false")

# a="Hello sibi"
# print(a)
#
# a='sibi'
# b=123
# # ab=[a+b,a-b,a*b,a/b,a%b]
# # print(ab)
#
# # a=input("enter the first value")
# # b=input("enter the second value")
# ab=a+str(b)
# print(ab)

# a=int(input("enter the value"))
# b=int(input("enter the value"))
# if(a>b):
#     print("a is less than b")
# else:
#     print("b is greater than a")

# a=int(input("enter the value"))
# if(a==1):
#     print("Hai")
# elif(a==2):
#     print("Hello")
# elif(a==3):
#     print("Sk")
# else:
#     print("ok")

# a=int(input("enter the first value"))
# b=int(input("enter the second value"))
# c=int(input("enter the third value"))
# if(a>=b):
#     print("a is greater than b")
# elif(b>=c):
#     print("b is greater than a")
# elif(c>=a):
#     print("c is greater than a")
# else:
#     print("undefined")

# a = int(input("Enter the first value: "))
# b = int(input("Enter the second value: "))
# c = int(input("Enter the third value: "))
#
# if a > c and b > c:
#     print("Both a and b are greater than c, b and c are greater than a, c and a are greater than b")
# elif a > b and a > c:
#     print("a is the greatest")
# elif b > a and b > c:
#     print("b is the greatest")
# elif c > a and c > b:
#     print("c is the greatest")
# else:
#     print("undefined")


# a=50
# b=90
# c=100
# if(a==b==c):
#     print("a,b,c are equal")
# else:
#     if(a>b):
#         if(a>c):
#             print("a is greater")
#         else:
#             print("c is greater")
#     else:
#         if(b>c):
#             print("b is greater")
#         else:
#             print("c is greater")
#
# a=input("enter one value:")
# a=int(a)
# print(type(a))

# a=30
# b=20
# c=10
# if not (a>b):
#     print("hellow")
# else:
#     print("hai")

# if (a>b) or (a>c):
#     print("a")
# else:
#     print("b,c")

# if(a>b) and (b>c):
#     print("a")
# else:
#     print("b,c")
##for loop
# a=5
# for i in range(a,20,1):
#     print(i)
##while loop        a+=1 (increment operators)  a-= (drecrement operators)
# a=5
# while (a<10):
#     print(a)
#     a += 10


# a=1
# b=10
# while (a<=10):
#     print(a,"x",b,"=",a*b)
#     a+=1

# for i in range (a,11,1):
#     print(a,"x",b,"=",a*b)
#     a+=1



# senders = []
# receivers = []
# amounts = []
#
# def get_senders():
#     for i in range(5):
#         sender_name = input(f"Enter the name of sender {i+1}: ")
#         sender_amount = int(input(f"Enter the amount for sender {i+1}: "))
#         senders.append(sender_name)
#         amounts.append(sender_amount)
#
#
# def get_receivers():
#     for i in range(5):
#         receiver_name = input(f"Enter the name of receiver {i+1}: ")
#         receivers.append(receiver_name)
#
# def show_details():
#     for i in range(5):
#         print(f"Transaction {i+1}:")
#         print(f"Sender: {senders[i]}")
#         print(f"Receiver: {receivers[i]}")
#         print(f"Amount: {amounts[i]}")
#         print("-" * 20)
#
#
# get_senders()
# get_receivers()
#
# show_details()


##append,extend,insert

# list1=[]
# # print(list1)
# list1.append(10)
# # print(list1)
# list1.extend([20,30,40,50])
# # print(list1)
# # print(list1)
# list1.insert(3,35)
# print(list1)
#
# ##deleting elements from list
#
# del list1[3]
# print(list1)



# list1 = []
# list1.append(10)
# list1.extend([20, 30, 40, 50])
# list1.insert(3, 35)
#
# print(list1)
# ##deleting elements from list
# del list1[:]
# print(list1)

# l1=[10,20,30,40,50]
# z=0
# x=max(l1)
# print(x)
# x=int(input("enter searching value:"))
# for i in l1:
#     if i==x:
#         z=1
# if z==1:
#     print("value is available")
# else:
#     print("value is not available")

# a=[10,15,25,29,35,42]
# x=int(input("enter the number to remove: "))
# if x in a:
#     a.remove(x)
#     print(a)
# else:
#     print("number is not found")



# a = [10, 15, 25, 29, 35, 42]
# x = int(input("Enter the number to remove: "))
#
# if x in a:
#     index = a.index(x)  # Find the index of the element
#     del a[index]  # Delete the element by index
#     print(a)
# else:
#     print("Number is not found")

##removing the numbers from list

# a=int(input("enter the number to remove: "))
# z=[10,20,30,40,50]
# b=0
# for i in z:
#     if i ==a:
#         b=1
#     #     break
#     # else:
#     #     b=0
# if b==1:
#     index = z.index(a)
#     z.remove(a)
#     print(z)
# else:
#     print("number is not found")


##removing duplicates

# a=[11,15,20,10,19,24,26,19,26,10,20]
# #removing duplicates from original preseving
# z = []
# for i in a:
#     if i not in z:
#         z.append(i)
# a.clear()
# a=z.copy()
# print(z)
# print(a)


# n=5
# for i in range(1,5,1):
#     j=0
#     while(j<i):
#         print("$",end=" ")
#         j+=1
#     print("\n")
#
# for i in range(1,6,1):
#     j=5
#     while(j>i):
#         print("#",end=" ")
#         j-=1
#     print("\n")


# a = [11, 5, 12, 9, 7, 10, 22]
#
# # Finding the smallest number
# x = max(a)
#
# print("x:",x)



##finding the greater number using for loop
# a = [11, 5, 12, 9, 7, 10, 22]
#
# x = a[0]
#
# for number in a:
#     if number > x:
#         x = number
#
# print("x:", x)

##finding the greater and smaller number using for loop

# l=[10,30,60,20,12,40,4,12,40,50,1]
# x = l[0]
# for number in l:
#     if number > x:
#         x = number
#
# print("x:", x)
#
# for number in l:
#     if number < x:
#         x = number
#
# print("x:", x)

##print characters
# a="HELLO WORLD"
# b=a[0]
# for i in range (len(a)):
#     for j in range(i + 1):
#         print(a[j], end= ' ')
#     print("\n")

# for i in range(a):
#     for b in range(i+1):
#         print(a[b], end= ' ')
#     print("\n")


##print charaters
# x = "hello world"
#
# z = list(x)
#
# for char in z:
#     print(char)

##sorting the list
# a=[10,9,30,20,45]
# # print(a.sort())
# print(a.sort(reverse=True))
# b=a.copy()
# print(a)
# print(b)

###TUPLES#####

# a=[10,9,30,20,45]
# b=(10,20,30,58,34,12)
# a[2]=20
# print(a)
# # b[2]=10
# print(b)
#
# ##tuple()
# a=tuple(x*2 for x in range(1,10,1))
# print(a)
#
# ##changing elements in tuples
# c=list(b)
# print(c)
# c[3]=79
# c=tuple(c)
# print(c)
#
# ##accessing single element in tuple
#
# print(c[4])
#
# a=(11,12,13,14)
# d=a+b
# print(d)

##unpacked tuples

a=(10,20,30)
(b,c,d)=(10,20,30)
print(a,'\n',b,'\n',c,'\n',d)

## count() index(),min() and max() in tuple

##minimum value
x = min(a)
print("x:", x)

##maximum value
x = max(a)
print("x:", x)

x= a.count(10)
print("x:",x)

x=a[2]
print("x:",x)


