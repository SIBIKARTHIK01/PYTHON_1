

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



senders = []
receivers = []
amounts = []

def get_senders():
    for i in range(5):
        sender_name = input(f"Enter the name of sender {i+1}: ")
        sender_amount = int(input(f"Enter the amount for sender {i+1}: "))
        senders.append(sender_name)
        amounts.append(sender_amount)


def get_receivers():
    for i in range(5):
        receiver_name = input(f"Enter the name of receiver {i+1}: ")
        receivers.append(receiver_name)

def show_details():
    for i in range(5):
        print(f"Transaction {i+1}:")
        print(f"Sender: {senders[i]}")
        print(f"Receiver: {receivers[i]}")
        print(f"Amount: {amounts[i]}")
        print("-" * 20)


get_senders()
get_receivers()

show_details()































