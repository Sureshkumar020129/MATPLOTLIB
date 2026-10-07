import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales_2025= [100, 200, 300, 400, 150, 250, 350, 450, 500, 600, 700, 800]
sales_2026= [150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250]
plt.plot(months, sales_2025, linestyle='--', marker='o', color='b', label='Sales 2025')
plt.plot(months, sales_2026, linestyle='--', marker='D', color='g', label='Sales 2026')
plt.title("Sales Comparison 2025 vs 2026")  
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.grid()
plt.show()