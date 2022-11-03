"""assign2.py MODULE: Where the main code runs, user interaction, and the program logic"""
#imports random module (python library) and product (user created)
import product, random

#for each simulation, it recieves a random value and determines a gain [+]or loss[-] 
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


#Welcome statement
print("Welcome to Programming Principles Product Inventory")

#nameLoop determines if the VARiables have to LOOP again
varLoop=True

#player assigning values
while (varLoop):
    try:
        code=int(input("Please enter the Product Code: "))
        name=input("Please enter the Product Name: ")
        stock=int(input("Please enter the Current Stock: "))
        price=float(input("Please enter the Product Sale Price: "))
        cost=float(input("Please enter the Product Manufacture Cost: "))
        monthProduction=int(input("Please enter estimated monthly production: "))
        #ends loop
        varLoop=False

    #if data is invalid type, the loop reruns
    except ValueError:
        print("Incorrect value type. Please try again.\n")

#creating object item
item=product.Product(code,name,stock,price,cost,monthProduction)

#variables for object item's getter methods
userCode=item.getCode()
userName=item.getName()
userStock=item.getStock()
userPrice=item.getPrice()
userCost=item.getCost()
userMonthlyProduction=item.getMonthly_Unit()

#print statements
print("\n"," * "*7,"Programming Principles Stock Statement"," * "*7)
print("\nProduct Code: {}\nProduct Name: {}\n\nSale Price: {} CAD\nManufacture Cost: {} CAD \nMonthly Production: {} units (Approx.)".format(userCode,userName,userPrice,userCost,userMonthlyProduction))

#establishing variables that will be printed at end. 
#totalManufactured will count how many manufactured
totalManufactured=0
#totalSold will count sales
totalSold=0

#loop for the monthly report
for month in range(1,13):
    #see simulate() for details, butbasically changes sold via +/- stock
    simVal=simulate(random.randint(0,10))
    totalManufactured+=userMonthlyProduction
    totalSold+=userMonthlyProduction+simVal

    #if the val is a loss, then add the extra product to the stock
    if(simVal<0):
        userStock+=(simVal%20)

    #if there is a higher demand, use  the stock
    else:
        userStock-=simVal

    #print statement for monthly report
    print("\nMonth {}:\n\tManufactured: {} units\n\tSold: {} units\n\tStock: {} units\n".format(month,userMonthlyProduction,(userMonthlyProduction+simVal),userStock))

#Formula from assignment: (Total Units Sold * Sale Price) - (Total Units Manufactured * Manufacture Cost)

#end net profit
print("\n\nNet Profit: $",(totalSold*userPrice)-(totalManufactured*userCost), "CAD")