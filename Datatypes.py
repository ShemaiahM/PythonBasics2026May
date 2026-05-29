from Variables import failed_subjects

print('Data types')
#strings "string this is"
#Booleans True or False
#integer whole number like 1 or 100
#float is a number like 5.0 or 10.0
#camel case myNameIs
#or Undescore my_name_is
#variables so if we have a quotation marks a ="it's" or b = 'it\'s' to ways.
#type() to know what variable it is.

print(type('hello'))
print(type(True))
print(type(False))
print(type(10))
print(type(1.7))
failed_subjects =6
#str to turn integer into a string only for numbers str("failed_subjects")
print("John is failing "+ str(failed_subjects)+" subjects")
#int to turn string into number int("6")
print(int("2" )+2)
print(int(1))
print(int("23"))
print(int(3.3))
print(int(float("3.4")))
## we have to pass a string into an float,
## into a int to get the int
print(type(str(44)))
print(type(str(30)))
print(float("2.2"))
print(float("33"))
print(float(55))

##Exercise
itemName="Hammer"
itemPrice=8.80
itemStock=25
print("We have "+ itemName +" and the price is £" + str(itemPrice) +" and we have " + str(itemStock) +" in stock!")
#Exercise
customerName="John"
numberOfPasses = 10
tokensPerPass = 10
pricePerPass = 5
tokensRequiredPerGame = 5

totalTokens = numberOfPasses * tokensPerPass
print(totalTokens)
totalCost = pricePerPass * numberOfPasses
print(totalCost)
gamesAvailable = totalTokens // tokensRequiredPerGame

print(gamesAvailable)
print("=====ARCADE DAY PASS=====")
print("The customer name is ",customerName, "they have brought " , numberOfPasses, "Passes.")
print("They have a total of ", totalTokens," tokens. ")
print("All of this has costed customer ", customerName, " £"+str(totalCost)+".")
print("They have ",gamesAvailable, " games avaliable to play!")


#note to simple add a number in string use comma(,)
#to get number into string use plus (+)








