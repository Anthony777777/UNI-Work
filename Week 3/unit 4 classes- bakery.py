class Bakery():
    """
    A class to store bakery orders.
    """
    def __init__(self, type, quantity, price, date):
        self.type = type
        self.quantity = quantity
        self.price = price
        self.date = date

    def __str__(self):
        return "Order type: " + str(self.type) + "\nPrice: " + str(self.price) + "\nQuantity: " + str(self.quantity)

    def get_invoice(self):
        return self.price * self.quantity

    def update_quantity(self, new_quantity):
        if new_quantity < 0:
            raise ValueError("New quantity cannot be negative.")
        self.quantity = new_quantity

    def get_item(self):
        return self.type

    def get_quantity(self):
        return self.quantity

def invoice_test(invoice : Bakery):
    print(invoice.price)