class Product:
    def __init__(self, product_code, product_name,product_stock, product_price, product_cost, product_monthUnit):
        self.code=product_code
        self.name=product_name
        self.stock=product_stock
        self.price=product_price
        self.cost=product_cost
        self.monthly_unit=product_monthUnit
    
    def getCode(self):
        return self.code

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getCost(self):
        return self.cost

    def getStock(self):
        return self.stock

    def getMonthly_Unit(self):
        return self.monthly_unit