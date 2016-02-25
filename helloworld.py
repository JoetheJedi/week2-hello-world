# Joseph Gonzalez

# write a program that:
# 1. greets the user in English
# 2. asks the user to choose from 1 of 3 spoken languages (pick your favorite languages!) 
# 3. displays the greeting in the chosen language
# 4. exits

# make sure that your code contains comments explaining your logic!



print ('Hello class!')               #Greeting in english
print ('A)French')                   #language choice 1
print ('B)Italian')                  #language choice 2
print ('C)Japanese')                 #language choice 3
question1=input('Type the letter before the language you want to be greeted in!') #giving the user instruction to choose their desired language
if question1 == "A" or question1 == "a":              #making sure both upper and lowercase Letter choices will work
     print('bonjour')
if question1 == "B" or question1 == "b":
     print ('Ciao')
if question1 == "C" or question1 == "c":
     print ('Konnichiwa')
exit
