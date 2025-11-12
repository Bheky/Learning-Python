import matplotlib.pyplot as plt # import the pyplot module

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25] # list to hold the data

plt.style.use('seaborn-v0_8-darkgrid')

# fig variable represent the entire figure, while ax represent a single plot in the figure. 
fig, ax = plt.subplots() # subplot function to generate one or more plots in the same figure.
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

plt.show()

