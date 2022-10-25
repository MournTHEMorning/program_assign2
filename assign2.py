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

print(" * "*7,"Programming Principles Stock Statement"," * "*7)
print("Product Code: {}\nProduct Name: {}\n\nSale Price: {} CAD\nManufacture Cost: {} CAD \nMonthly Production: {} units (Approx.)".format(userCode,userName,userStock,userPrice,userCost,userMonthlyProduction))

simVal=simulate(random.randint(0,10))
print("simVal: ", simVal)

print("Month ###:\n\tManufactured: {} units\n\tSold: {} units\n\tStock: {} units".format(userMonthlyProduction,(userMonthlyProduction+simVal),userStock-(simVal%20)))