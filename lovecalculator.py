# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lowername1 = name1.lower()
lowername2 = name2.lower()
tcount = lowername1.count("t")+lowername2.count("t")
rcount = lowername1.count("r")+lowername2.count("r")
ucount = lowername1.count("u")+lowername2.count("u")
ecount = lowername1.count("e")+lowername2.count("e")

truecount = tcount + rcount + ucount +ecount

lcount = lowername1.count("l")+lowername2.count("l")
ocount = lowername1.count("o")+lowername2.count("o")
vcount = lowername1.count("v")+lowername2.count("v")
ecount = lowername1.count("e")+lowername2.count("e")

lovecount = lcount + ocount + vcount + ecount

score = int(str(truecount) + str(lovecount))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")


