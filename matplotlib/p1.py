import matplotlib.pyplot as plt


plt.title("Sales Report")
plt.xlabel("Month")
plt.ylabel("Sales")

x = [1,2,3,4,5]
y = [10,20,30,40,50]

plt.plot(x,y)

plt.show()

x=[1,2,3,4]

python=[10,20,30,40]
django=[15,25,35,45]

plt.plot(x,python)
plt.plot(x,django)

plt.show()

plt.plot(x,python,label="Python")
plt.plot(x,django,label="Django")

plt.legend()