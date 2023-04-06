# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
pizzaprice = 0
if size == "S":
    pizzaprice = 15      
elif size == "M":
    pizzaprice = 20
else:
    pizzaprice = 25
if add_pepperoni == "Y":
    if size == "S":
        pizzaprice +=2
    else:
        pizzaprice += 3
if extra_cheese == "Y":
    pizzaprice +=1
print(f"Your final bill is: ${pizzaprice}.")
   

 

     
            
        
   

        
