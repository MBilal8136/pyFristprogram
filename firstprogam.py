# name=input("enter your name:")

# print("length of your name is:",len(name))


# marks = int(input("Enter your marks:"))

# if (marks >= 90):
#     print("Grade A")
# elif (marks >= 80 and marks < 90):
#     print("Grade B")
# elif (marks >= 70 and marks < 80):
#     print("Grade C")
# elif (marks >= 60 and marks < 70):
#     print("Grade D")
# else:
#     print("Failed")

# num = int(input("Enter a number:"))

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# a= int(input("Enter a number:"))
# b= int(input("Enter a number:"))
# c= int(input("Enter a number:"))

# if a>b and a>c:
#     print("a is greater" ,a)
# elif b>a and b>c:
#     print("b is greater", b)
# else:
#     print("c is greater", c)

# a= int(input("Enter  number:"))

# if a%7 == 0:
#     print("divisible by 7")
# else:
#     print("not divisible by 7")

# marks = [10, 20, 30, 40, 50]
# print(marks)
# marks.append(60)
# print(marks)
# marks.insert(2, 25)
# for i in marks:
#     print(i)   
# print(marks[2])
# marks.remove(30)



# name = input("Enter moive name:")
# name2 = input("Enter moive name:")
# name3 = input("Enter moive name:")

# list = []
# list.append(name)
# list.append(name2)
# list.append(name3)
# print(list)



# distionary 
# dist = {
#     "name" : "M Bilal",
#     "age" : 23,
#     "city" : "Multan",
#     "country" : "Pakistan",
#     "marks" : [10, 20, 30, 40, 50],
#     "movies" : ["movie1", "movie2", "movie3"]
# }


# print(dist)

# cout = 0
# while cout <= 100:
#     print(cout)
#     cout = cout + 1
#     # print(cout)
# print("End of loop")

# couter
# cout = 100
# while cout >= 1:
#     print(cout)
#     cout = cout - 1
#     # print(cout)
# print("End of loop")

#   n number table
# n= int(input("Enter a number:"))
# i=0
# while i <= 10:
#     print(n, "x", i, "=", n*i)
#     i += 1
# print("End of loop")


num = [1,4,5,6,7,8,9,10,4,45,3,2,1,2,3,4,5,6,7,8,9,10]

for i in range(len(num)):
    print(num[i], end=" ")