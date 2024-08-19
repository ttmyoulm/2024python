from matplotlib import pyplot as plt
 
y = [5, 3, 7, 10, 9, 5, 3.5, 8] #리스트
x = [24,67,34,34,12,34,14]
plt.plot(x, y, color="blue")
plt.bar(x, y, color="red")
plt.show()