class Medicine:
    def __init__ (self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity
    
    def restock(self, amount):
        self.quantity += amount
        return f"Restrocked{amount} units of {self.name}"

    def sell(self, amount):
        if amount > self.quantity:
            return "Insufficient stock"

        self.quantity -= amount
        return f"Sold {amount} units of {self.name}"

medicine= Medicine("Paracetamol", 20, 100)

print("Total stock value:", medicine.total_value())

print(medicine.restock(50))
print("Quantity:", medicine.quantity)

print(medicine.sell(30))
print("Quntity:", medicine.quantity)

print(medicine.sell(200))
print("Quantity:", medicine.quantity)
