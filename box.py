import matplotlib.pyplot as plt
data = [100, 200, 300, 400, 150, 250, 350, 450, 500, 600, 70]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov']

plt.boxplot(data)
plt.show()