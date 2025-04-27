import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random
style.use("ggplot")

# X_data = np.random.random(50)*100
# Y_data = np.random.random(50)*100
# plt.scatter(X_data, Y_data, c= "#00f", marker = "*", alpha = 0.5, s = 100)
# plt.title("Scatter Plot Example")
# plt.show()

# years= [2200, 2001, 2002, 2003, 2004, 2005]
# weights = [100, 52, 67, 48, 89, 80]
# plt.plot(years, weights, color = "green", marker = "o", alpha = 0.5, linewidth = 2, linestyle = "dashed")
# plt.title("Line Plot Example")
# plt.xlabel("Years")
# plt.ylabel("Weights")
# plt.show()

# x = ["c", "c++", "java", "python", "javascript"]
# y = [145, 250, 300, 400, 55]
# plt.bar(x, y, color = "green", alpha = 0.5, width = 0.3, align = "center", edgecolor = "blue")
# plt.pie(y,labels = x, colors = ['red', 'blue', 'green', 'yellow', 'orange'], startangle = 90, shadow = True, explode = (0.1, 0.1, 0.1, 0.4, 0.1), autopct = "%.2f%%", pctdistance=0.6, radius = 1.2)
# plt.legend(x, loc = "upper right")
# plt.show()

# years = [2014, 2015, 2016, 2017, 2018, 2019]
# income = [20, 30, 40, 55, 60, 25]
# print(income)
# income_ticks = list(range(20,120,5))
# plt.plot(years, income, color = "green", marker = "o", alpha = 0.5, linewidth = 2, linestyle = "dashed")
# plt.yticks(income_ticks, [f"${i}K" for i in income_ticks])
# plt.title("Income vs Years", fontsize = 20, fontname = "Serif", color = "blue")
# plt.legend("Income", loc = "lower right")
# plt.xlabel("Years")
# plt.ylabel("Income")    
# plt.show()

# x1, y1 = np.random.rand(100), np.random.rand(100)
# x2, y2 = np.arange(100), np.random.rand(100)
# plt.figure(1)
# plt.plot(x1, y1)
# plt.figure(2)
# plt.scatter(x2, y2, color = "red", marker = "o", alpha = 0.5, linewidth = 2, linestyle = "dashed")
# plt.show()

# x = np.arange(111)
# fig , axis = plt.subplots(2, 2)
# axis[0,0].plot(x, np.sin(x))
# axis[0,0].set_title("Sine")
# axis[0,1].plot(x, np.cos(x))
# axis[0,1].set_title("Cosine")
# axis[1,0].plot(x, np.tan(x))
# axis[1,0].set_title("Tangent")
# axis[1,1].plot(x, np.log(x))
# axis[1,1].set_title("Logarithm")
# plt.show()
# plt.savefig("sine.png", dpi = 300, bbox_inches = "tight", transparent = False, pad_inches = 0.1)
# plt.suptitle("Sine and Cosine")

# ax = plt.axes(projection = "3d")
# x = np.arange(0,50, 0.1)
# y = np.arange(0,50, 0.1)
# z = np.cos(x+y)
# ax.scatter3D(x, y, z, color = "red", marker = "*", alpha = 0.5)
# ax.set_xlabel("X-axis")
# ax.set_ylabel("Y-axis")
# ax.set_zlabel("Z-axis")
# plt.title("3D Scatter Plot Example")

# x = np.arange(-5, 5, 0.1)
# y = np.arange(-5, 5, 0.1)
# x, y = np.meshgrid(x, y)   
# z = np.sin(x) * np.cos(y)
# ax.plot_surface(x, y, z, cmap = "Spectral", edgecolor = "none", alpha = 0.5)
# ax.view_init(azim = 30, elev = 20)
# plt.show()

heads_tails = [0, 0]
for i in range(100):
    heads_tails[random.randint(0, 1)] += 1
    plt.bar(["Heads", "Tails"], heads_tails, color = ["blue", "red"], alpha = 0.5, width = 0.3, align = "center", edgecolor = "black")
    plt.pause(0.01)
plt.show()
