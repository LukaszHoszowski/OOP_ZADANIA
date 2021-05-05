import re


class Product:
    """
    Products in the shop.

    :param str          name:       product name
    :param int/float    price:      product price
    """

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if re.match(r"\d\.?", str(price)):
            self._price = price
        else:
            raise ValueError('Price needs to be expressed as integer or float')
        self._id = id(self)


class ShoppingCart:
    """
    Shopping cart for products.
    """

    def __init__(self):
        self.products = {}
        self.quantities = {}

    def add_product(self, product):
        """
        Adds products to cart.

        :param class        product:    class object which contains name and price of products
        """
        self.product = product
        self.products[self.product._id] = self.product
        if self.product._id in self.quantities.keys():
            self.quantities[self.product._id] += 1
        else:
            self.quantities[self.product._id] = 1

    def remove_products(self, product):
        """
        Removes products from cart.

        :param class        product:    class object which contains name and price of products
        """
        self.product = product

        if self.product._id in self.quantities.keys():
            self.products.pop(self.product._id)
            self.quantities.pop(self.product._id)

    def change_product_quantity(self, product, new_quantity):
        """
        Changes quantity of products.

        :param class    product:         class object which contains name and price of products
        :param int      new_quantity:    correct quantity of products
        """

        self.product = product

        if self.product._id in self.quantities.keys():
            if new_quantity > 0:
                self.quantities[self.product._id] = new_quantity
            elif new_quantity == 0:
                self.remove_products(product)
            elif new_quantity < 0:
                raise ValueError("Quantity can't be a negative integer")
            else:
                raise ValueError("Quantity needs to be an integer")

    def get_recipt(self):
        """
        Creates an products list as a bill.

        :return: str    list of products with prices, sums and quantities, if more than 3 products 30% less from total
        """
        recipt = ""
        suma = 0
        for key, value in self.products.items():
            summary = self.quantities[key] * value.price
            if self.quantities[key] >= 3:
                summary *= 0.7
            recipt += f'{value.name} - ilość: {self.quantities[key]}, cena: ' \
                      f'{value.price:.2f} zł, suma: {summary:.2f} zl \n'
            suma += summary
        recipt += f'\nSuma: {suma:.2f} zł'
        return recipt


def main():
    chleb = Product('chleb', 3.67)
    piwo = Product('piwo', 2)
    wodka = Product('wodka', 21.99)
    serek = Product('serek', 2.99)
    woda = Product('woda', 1.39)

    zakupki = ShoppingCart()
    zakupki.add_product(chleb)
    zakupki.add_product(chleb)
    zakupki.add_product(piwo)
    zakupki.add_product(wodka)
    zakupki.add_product(serek)
    zakupki.add_product(woda)

    zakupki.remove_products(serek)

    zakupki.change_product_quantity(piwo, 10)
    zakupki.change_product_quantity(woda, 0)
    print(zakupki.get_recipt())


if __name__ == '__main__':
    main()
