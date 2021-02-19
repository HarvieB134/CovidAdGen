import random
ca1=("the communities we serve","our extended family","our team and valued customers")
ca2=("challenging times","uncertain times","unprecedented times","difficult times","trying times")
ca3=("protecting the communities we serve","serving the communities we protect","America")
ca4=("staying safe","at home","waiting this out","America")
ca5=("with you","here for you","here to help","all ","America")
ca5A=("in this together","grateful to ")
ca5Ab=("the heroes","the medical professionals","the people who keep working for us","America")
ca6=("we will get through this","we can help save ")
ca6A=("restaurants","bars","book stores","America")
ca7=("our values","our heroes","America")
cchoice1=random.choice(ca1)
cchoice2=random.choice(ca2)
print("To " + cchoice1 + " in these " + (cchoice2) + ":")
cchoice3=random.choice(ca3)
print("Our top priority is " + cchoice3 + ".")
cchoice4=random.choice(ca4)
cchoice5=random.choice(ca5)
if(cchoice5=="all "):
    csub5=random.choice(ca5A)
    if(csub5=="grateful to "):
        calt5=random.choice(ca5Ab)
        cres5=(cchoice5+csub5+calt5)
else:
    cres5=cchoice5
print("But, while we are " + cchoice4 + ", we are also " + cres5 + ".")
cchoice6=random.choice(ca6)
if(cchoice6=="we can help save "):
    csub6=random.choice(ca6A)
    cres6=(cchoice6+csub6)
else:
    cres6=cchoice6
print("Together, " + cres6 + ".")
cchoice7=random.choice(ca7)
print("Now, more than ever, we must stay faithful to " + cchoice7 + ".")