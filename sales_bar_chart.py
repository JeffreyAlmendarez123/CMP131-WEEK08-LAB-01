sales=[]
for store in range(1,6):
    amount=int(input(f"Enter today sale's for store {store}:"))
    while amount < 0: 
        amount=int(input("Error, a negative amount is not found. Try again:"))
    sales.append(amount)

print()
print("Sale's Chart")
print("(Each * = $100)")
for store in range(1,6):
    print(f"Store {store}: ", end="")
    for ast in range(sales[store-1]//100):
        print("*", end="")
    print() 
       