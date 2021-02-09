import matplotlib.pyplot as pl
import random
import csv


def neural(x, w, b):
    return w * x + b


def cost_per_element(y, p):
    return (p - y) ** 2


def dc_dw(p, w, x, y):
    '''derivative of cost wrt w'''
    return 2 * (p - y) * x


def dc_db(p, y):
    '''derivative of cost wrt b'''
    return 2 * (p - y)


dataset_in = open(r'.\datasets\swedish insurance', 'r', newline='\n')

x = []  # no. of claims
y = []  # payout
alfa = 0.000001  # learning rate
w = random.choice(range(100))  # random parameters for w and b
b = random.choice(range(100))

print(w, b)

# reading the file as CSV and storing in x and y
rdr = csv.reader(dataset_in)
dataset_in.seek(0)
for oro in rdr:
    x.append(int(oro[0]))
    y.append(float(oro[1]))
print(x, y, sep='/n')

dataset_in.close()

# creating testing set
test_x = []
test_y = []
for i in range(10):
    n = random.choice(range(62-i))
    test_x.append(x.pop(n))
    test_y.append(y.pop(n))

for i in range(500000):  # main loop to adjust w and b
    sigma_w = 0  # sum of dc_dw
    sigma_b = 0  # sum of dc_dw
    for a in range(len(x)):
        p = neural(x[a], w, b)
        sigma_w += dc_dw(p, w, x[a], y[a])
        sigma_b += dc_db(p, y[a])
    w = w - alfa * sigma_w
    b = b - alfa * sigma_b
    iter_info = 'iteration no. ' + str(i).ljust(7) + str(b).ljust(10) + '  ' + str(w).ljust(10)  # str for iter information
    print(iter_info, end='')
    # getch = input()
    print('\b' * len(iter_info), end='', flush=True)
    pass
print(iter_info, end='')

file_out = open(r'.\datasets\para_out', 'w')  # output of parameters
file_out.write('b = ' + str(b) + '\n')
file_out.write('w = ' + str(w) + '\n')
file_out.close()

dataset_out = open(r'.\datasets\data_out', 'w')  # output of the pred. data

result_y = []
for i in range(10):  # to store all the predicted test set in a file
    result_y.append(w * test_x[i] + b)
    dataset_out.write(f'{test_x[i]},{result_y[i]}\n')

for i in range(len(x)):  # to store all the predicted set in a file
    dataset_out.write(f'{x[i]},{w * x[i] + b}\n')

dataset_out.close()

pl.plot(x, y, '*', markersize='3.7', markeredgecolor='#F30C46')  # plotting points of x, y (pink star)
pl.plot(test_x, test_y, 'r+')  # plotting the test set (red plus)
pl.plot(test_x, result_y, '#0CF3B9', linewidth=2)  # plotting the predicted test result (cyan line)
pl.show()

getch = input()
