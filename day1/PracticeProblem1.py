# create a product class with name and price attributes
# also track how mayy products have been created using class variable
# calculate discount using static method with discount percentage as input  
class Product:
    product_count = 0  # class variable to track number of products

    def __init__(self, name, price):  # constructor
        self.name = name
        self.price = price
        Product.product_count += 1  # increment product count on each new product creation

    def product_info(self):  # instance method to get product info
        return f"Product Name: {self.name}, Price: {self.price}"    

    @classmethod
    def get_product_count(cls):  # class method to get product count
        return f"Total products created: {cls.product_count}"   
    @staticmethod
    def calculate_discount(price, discount_percentage):
        return f"Discounted price is: {price - (price * discount_percentage) / 100}"  # static method to calculate discount
# create some product instances
product1 = Product("Laptop", 1000)
product2 = Product("Smartphone", 500)
# print product information
print(product1.product_info())  # using instance method 
print(product2.product_info())  # using instance method
print(Product.get_product_count())  # accessing class variable
# calculate discount for product1
print(product1.calculate_discount(product1.price,10))  # using static method to calculate discount
