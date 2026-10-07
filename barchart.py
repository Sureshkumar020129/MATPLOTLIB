import matplotlib.pyplot as plt
product=["laptop","mobile","tablet", "earbuds","camera","printer"]
sales=[100,200,300,400,500,600]
plt.bar(product,sales,color='orange')
plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.barh(product,sales,color='green')
plt.show()