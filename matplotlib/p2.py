import matplotlib.pyplot as plt


courses=["Python","Django","AI"]

students=[50,40,60]

plt.bar(courses,students)

plt.show()

plt.barh(courses,students)


data=[40,30,20,10]

labels=["Python","AI","Django","ML"]

plt.pie(data,labels=labels)

plt.show()


plt.pie(
    data,
    labels=labels,
    autopct="%1.1f%%"
)


x=[1,2,3,4,5]

y=[10,15,20,25,30]

plt.scatter(x,y)

plt.show()


marks=[50,60,70,80,90,50,60,70]

plt.hist(marks)

plt.show()


plt.grid()

plt.savefig("chart.png")