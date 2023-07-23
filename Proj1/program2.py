# Author: Scott Normore
#
# A program for One Stop Insurance analyzing sales
#

import matplotlib.pyplot as plt
# Our array with all the months
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
# Our Empty Sales Array
sales = []

# We fill our sales array with numbers
sales.append(float(input("Enter total sales for January: ")))
sales.append(float(input("Enter total sales for February: ")))
sales.append(float(input("Enter total sales for March: ")))
sales.append(float(input("Enter total sales for April: ")))
sales.append(float(input("Enter total sales for May: ")))
sales.append(float(input("Enter total sales for June: ")))
sales.append(float(input("Enter total sales for July: ")))
sales.append(float(input("Enter total sales for August: ")))
sales.append(float(input("Enter total sales for September: ")))
sales.append(float(input("Enter total sales for October: ")))
sales.append(float(input("Enter total sales for November: ")))
sales.append(float(input("Enter total sales for December: ")))

# We remove unused months
for i in range(len(sales)-1,0,-1):
    if sales[i]==0:
        sales.pop()
        months.pop()
    else:
        break;
# We ask for the year for title purposes
year = input("Enter the current year: ")

# We plot our graph
plt.title("Insurance Sales for "+year)
plt.plot(months, sales, color='blue', marker='o')

plt.xlabel("Month")
plt.ylabel("Total Sales ($)")

plt.show()