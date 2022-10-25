import product, random
#assignment 2 created

def simulate(rand):
    #effect MEASURES HOW rand VARIABLE EFFECTS THE MONTH
    effect=random.randint(0,1)

    #returns a positive value
    if(effect):
        return rand
    
    #returns a negative value, which is the complement of the original rand
    else:
        rand-=10
        return rand


#player assigning values
print("Welcome to Programming Principles Product Inventory")
userCode=input("Please enter the Product Code: ")
userName=input("Please enter the Product Name: ")
userStock=int(input("Please enter the Current Stock: "))
userPrice=float(input("Please enter the Product Sale Price: "))
userCost=float(input("Please enter the Product Manufacture Cost: "))
userMonthlyProduction=int(input("Please enter estimated monthly production: "))


item=product.Product(userCode,userName,userStock,userPrice,userCost,userMonthlyProduction)
#print(item.getCode(), item.getName(), item.getStock(),item.getPrice(),item.getCost(), item.getMonthly_Unit())

print("\n"," * "*7,"Programming Principles Stock Statement"," * "*7)
print("\nProduct Code: {}\nProduct Name: {}\n\nSale Price: {} CAD\nManufacture Cost: {} CAD \nMonthly Production: {} units (Approx.)".format(userCode,userName,userPrice,userCost,userMonthlyProduction))

#print("simVal: ", simVal)

totalManufactured=0
totalSold=0

for month in range(1,13):
    simVal=simulate(random.randint(0,10))
    totalManufactured+=userMonthlyProduction
    totalSold+=userMonthlyProduction+simVal
    if(simVal<0):
        userStock+=(simVal%20)
    else:
        userStock-=simVal
    #note: if you lose product, or random value = -, then you add that value to your stock. from observations . Fix this 
    print("\nMonth {}:\n\tManufactured: {} units\n\tSold: {} units\n\tStock: {} units\n".format(month,userMonthlyProduction,(userMonthlyProduction+simVal),userStock))

    print(simVal,userStock, totalManufactured, totalSold)
    input(" INPUT TO CONTINUE: ")

# print((totalSold*userPrice))
# print(totalManufactured*userCost)
print("\n\nNet Profit: $",(totalSold*userPrice)-(totalManufactured*userCost), "CAD")



#(Total Units Sold * Sale Price) - (Total Units Manufactured * Manufacture Cost)
#(totalSold*userPrice)-(totalManufactured*userCost)

