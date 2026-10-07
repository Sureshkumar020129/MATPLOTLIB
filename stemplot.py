import matplotlib.pyplot as plt
data = [100, 200, 300, 400, 150, 250, 350, 450, 500, 600, 700]
plt.stem(data)
plt.xticks(range(1, len(data) + 1))
plt.show()