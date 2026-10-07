import matplotlib.pyplot as plt
sales = [100, 200, 300, 400, 150, 250, 350, 450, 500, 600, 700]
years = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
plt.pie(sales, labels=years, autopct='%1.1f%%')
plt.title('Sales Data by Year')
plt.show()