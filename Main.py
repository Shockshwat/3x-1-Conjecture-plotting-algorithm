# importing libraries
import numpy as np
import matplotlib.pyplot as plt
import sys
import time

# Taking Input from user
try:
    a = int(input("Enter the number to check for the 3x+1 conjecture: "))
except ValueError:
    print("Please enter a number")
    time.sleep(5)
    sys.exit()

# Algorithm
final = np.array([a])

while a != 1:
    if a % 2 == 0:
        a = a / 2
    else:
        a = 3 * a + 1
    final = np.append(final, a)
counter = np.arange(1, len(final) + 1)

# Plotting
print("It falls under the 3x+1 conjecture.")
plt.figure("3x+1 Iteration")
plt.title("Line graph")
plt.xlabel("Number Height")
plt.ylabel("Iteration")

plt.plot(counter, final, color="green")
plt.show()
