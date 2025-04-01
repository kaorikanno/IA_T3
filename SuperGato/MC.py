import numpy as np
import matplotlib.pyplot as plt
import main

MC = 100
y = []

for i in range(MC):
    y.append(main.main())

numerical_data = [0 if value == 'O' else 1 for value in y]

plt.hist(numerical_data, bins=[0, 0.5, 1.0], align='mid', rwidth=0.8)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of List Data')
plt.xticks([0, 1], ['O', 'X'])
plt.show()