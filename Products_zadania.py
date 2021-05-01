# Zadanie - Products

class Products:
    def __init__(self, name, description, price, quantity):
        if price < 0.01:
            raise ValueError(f"Attribute '{price}' doesn't carry the value")

        if not type(price) == float:
            raise ValueError(f"Attribute '{price}' isn't float")

        if not type(name) == str:
            raise ValueError(f"Attribute '{price}' isn't a string")

        if not type(quantity) == int or quantity < 0:
            raise ValueError(f"Attribute '{quantity}' isn't int")

        self.quantity = quantity
        self.price = price
        self.description = description
        self.name = name
        self._id = id(self)

    @property
    def idid(self):
        return self._id

    def get_total_sum(self):
        return self.price * self.quantity


def main():
    f = Products('Jabko', 'Owoc', 100.00, 10)
    g = Products('Jabko', 'Owoc', 9.99, 2)
    h = Products('Jabko', 'Owoc', 5.65, 1)
    i = Products('Jabko', 'Owoc', 10.0, 5)

    print(f.get_total_sum())
    print(g.get_total_sum())
    print(h.get_total_sum())
    print(i.get_total_sum())

if __name__ == '__main__':
    main()
