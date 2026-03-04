from lib.cash_register import CashRegister

# Create register with 20% discount
register = CashRegister(20)

# Add items
register.add_item("Apple", 10, 2)
print("Total after adding Apples:", register.total)
print("Items:", register.items)

# Apply discount
register.apply_discount()
print("Total after discount:", register.total)

# Void last transaction
register.void_last_transaction()
print("Total after void:", register.total)
print("Items after void:", register.items)