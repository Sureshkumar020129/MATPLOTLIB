import matplotlib.pyplot as plt
x=[1, 2, 3, 4, 5]
y=['A', 'B', 'C', 'D', 'E']
plt.plot(x, y, linestyle='--', marker='o', color='b')
plt.title("new graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.show()
