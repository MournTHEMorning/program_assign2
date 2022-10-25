class Product:
    def __init__(self, product_code, product_name, product_price, product_cost, product_stock, product_monthUnit):
        self.code=product_code
        self.name=product_name
        self.price=product_price
        self.cost=product_cost
        self.stock=product_stock
        self.monthly_unit=product_monthUnit
    
    def getCode(self):
        return self.code
