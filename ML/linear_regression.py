import statistics
hours_spent_driving_x = [10,9,2,15,10,16,11,16]
risk_score_y = [95,80,10,50,45,98,38,93]

n = len(hours_spent_driving_x)

x_mean = statistics.mean(hours_spent_driving_x)
y_mean = statistics.mean(risk_score_y)

x_deviation_sum = sum(i - x_mean for i in hours_spent_driving_x)
y_deviation_sum = sum(i - y_mean for i in risk_score_y)

x_deviation_square_sum = sum((i - x_mean)**2 for i in hours_spent_driving_x)
y_deviation_square_sum = sum((i - y_mean)**2 for i in risk_score_y)

xy_deviation_sum = 0
for i,j in zip(hours_spent_driving_x,risk_score_y):
    xy_deviation_sum += (i - x_mean) * (j - y_mean)

m = xy_deviation_sum / x_deviation_square_sum
c = y_mean - m * x_mean

def predict(hours):
    return (m * hours) + c

print(m)
print(c)
print(predict(10))