age = int(input("Enter your age :\n "))

if age >= 18:
    print("You can give  Vote")
elif age < 18 and age > 3:
    print("You are in school")
else:
    print("You are a child")
    # if first condition not satisfy you can check the second condition that's the meaning of elif
# else:
#     print ("You Can't give vote")
    print("Thank You!!")