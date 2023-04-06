# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

hundreadmultiple = year%100
fourmultiple = year%4
fourhundreadmultiple = year%400

if fourmultiple == 0 and hundreadmultiple != 0:
    print('Leap year.')
elif fourhundreadmultiple == 0:
    print('Leap year.')
else:
    print('Not leap year.')

    
  
