import statistics
import matplotlib.pyplot as plt
import numpy as np


def predict(hours):
    return (m * hours) + c


hours_spent_driving_x = [10, 9, 2, 15, 10, 16, 11, 16]
risk_score_y = [95, 80, 10, 50, 45, 98, 38, 93]

x_mean = statistics.mean(hours_spent_driving_x)
y_mean = statistics.mean(risk_score_y)

x_deviation_square_sum = sum((i - x_mean) ** 2 for i in hours_spent_driving_x)

xy_deviation_product_sum = 0
for i, j in zip(hours_spent_driving_x, risk_score_y):
    xy_deviation_product_sum += (i - x_mean) * (j - y_mean)

m = xy_deviation_product_sum / x_deviation_square_sum
c = y_mean - m * x_mean

print('slope(m): ', m)
print('intercept(c): ', c)
print('prediction(y) : ', predict(16))

plt.scatter(x=hours_spent_driving_x, y=risk_score_y)

x1 = np.linspace(0, 20)
y1 = m * x1 + c
plt.plot(x1, y1)
plt.show()
