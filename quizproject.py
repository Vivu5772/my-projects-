import random
print()
wel="▁ ▂ ▄ ▅ ▆ ▇ █ 【ＷＥＬＣＯＭＥ　ＴＯ　ＧＡＭＥ　ＯＦ　ＱＵＩＺ】 █ ▇ ▆ ▅ ▄ ▂ ▁"
cr="Created by .."
print(wel.center(100,' '))
print(" ")
print(cr.center(200," "))
print(" ")
ins="Instructions-"
print(ins.center(50," "))
print(" ")
print("* You have 5 questions to answer.")
print("* For each correct answer you get 1 point.")
print("* In answer you have to only type 'T/F'.")
print(" ")
print("Quiz started -")
count=0
def q(que,ans):
   


    if (ui)==ans:
        print()
        print("(っ◔◡◔)っ ♥ YOU ARE RIGHT ♥")

        global count
        count+=1






    else:
        print()
        print("ＯＯＰＳ！ ＹＯＵ ＡＲＥ ＷＲＯＮＧ")

    print("★ your score is-",count,"★")
    print()
qt=[["# python is low level language(T/F)","F"],["# True is boolean value(T/F)","T"],["# Pyhton is using compiler to compile the code(T/F)","T"],
    ["# '[]' is use to define tuppel(T/F)","F"],["# 5.0 is float(T/F)","T"],["# Import maths is use for importing maths library(T/F)","F"],
    ["# Python is developed by Guido van Rossum(T/F)","T"],["# Print is keyword in python(T/F)","F"],]

for z in range(0,5):


    s=random.choice(qt)
    qt.remove(s)

    v=s[0]
    i=s[1]

    print(v)
    u=input("Your answer- ")
    ui=u.upper()
    q(v,i)

print()
print("Your final score is-","◦•●◉✿",count,"✿◉●•◦")
print()
th=" ░T░H░A░N░K░ ░Y░O░U░ "
print(th.center(100,"*"))
