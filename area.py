import matplotlib.pyplot as plt
data = [100, 200, 300, 400, 150, 250, 350, 450, 500, 600, 700]
years = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
plt.fill_between(years, data)
plt.show()