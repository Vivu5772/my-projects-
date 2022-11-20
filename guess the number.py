print("GUESS THE NUMBER GAME:")
print("you have to guess the hidden number.")
print("you have only 5 chances")
print("The number is of 2 digits")
n=45
i=0
c="congrats you guess right no."
w="you won"
l11="you move some forward"
l10="you move forward"
l12="few forward"
l13="just reached"
l14="very close"
l15="you move some backward"
l16="you move backward"
while(True):
    ui= int(input("guess number "))
    if ui==45:
        print(c,w)

        break
    elif ui<10:
        print(l10)
    elif ui<20:
        print(l11)
    elif ui<30:
        print(l12)
    elif ui<40:
        print(l13)
    elif ui<45:
        print(l14)
    elif ui<50:
        print(l14)
    elif ui<60:
        print(l15)
    elif ui<100:
        print(l16)
    print("you have now only 4 chances")
    break
while(True):
    ui = int(input("guess number "))
    if ui == 45:
        print(c,w)
        break
    elif ui < 10:
        print(l10)
    elif ui < 20:
        print(l11)
    elif ui < 30:
        print(l12)
    elif ui < 40:
        print(l13)
    elif ui < 45:
        print(l14)
    elif ui < 50:
        print(l14)
    elif ui < 60:
        print(l15)
    elif ui < 100:
        print(l16)
    print("now you have only 3 chance left")
    break
while(True):
    ui= int(input("guess number "))
    if ui==45:
        print(c,w)
        break
    elif ui<10:
        print(l10)
    elif ui<20:
        print(l11)
    elif ui<30:
        print(l12)
    elif ui<40:
        print(l13)
    elif ui<45:
        print(l14)
    elif ui<50:
        print(l14)
    elif ui<60:
        print(l15)
    elif ui<100:
        print(l16)
    print("now you have only 2 chance left")
    break
while(True):
    ui = int(input("guess number "))
    if ui == 45:
        print(c,w)
        break
    elif ui < 10:
        print(l10)
    elif ui < 20:
        print(l11)
    elif ui < 30:
        print(l12)
    elif ui < 40:
        print(l13)
    elif ui < 45:
        print(l14)
    elif ui < 50:
        print(l14)
    elif ui < 60:
        print(l15)
    elif ui < 100:
        print(l16)
    print("you have now last chance left")
    break
while(True):
    ui = int(input("guess number "))
    if ui == 45:
        print(c,w)
        break
    elif ui < 10:
        print(l10)
    elif ui < 20:
        print(l11)
    elif ui < 30:
        print(l12)
    elif ui < 40:
        print(l13)
    elif ui < 45:
        print(l14)
    elif ui < 50:
        print(l14)
    elif ui < 60:
        print(l15)
    elif ui < 100:
        print(l16)
    print("Game over you loose")
    break

print("i hope you will enjoy it")
print("made by vivu")





