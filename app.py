class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot to be negative.")

        self.__price = value


# product = Product(-50)

# This implementation is not pythonic, which means we don't use python features and in this case we can use Property:


class Product1:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot to be negative.")

        self.__price = value

    # after define set and get, we define a property called price using the property function that takes four optional parameters.
    price = property(get_price, set_price)


product = Product1(50)
# now we have a price property with dot notion
# product.price = -1
# print(product.price)

# in this solution we can access to get and set methods with dont notation and they make the product1 class polluted, we can make them private or we can use a better solution using decorators:


class Product2:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot to be negative.")

        self.__price = value


product = Product2(50)
print(product.price)
product.price = -1
print(product.price)
