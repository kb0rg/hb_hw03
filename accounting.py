"""
cleaned up code/ made more human-readable
"""

"""
* count up the differerent types of melons that were sold.
"""

print "******************************************"

orders_by_type_file = open("orders_by_type.csv")

# create melon tally dictionary: melon type keys with count values set to zero
melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}

# loop through each line in orders_by_type file
for line in orders_by_type_file:
    # get info re melon type and sales count, put in list
    data = line.split(",")
    melon_type = data[1]
    melon_count = int(data[2])
    # update dict values with count
    melon_tallies[melon_type] += melon_count
orders_by_type_file.close()

"""
* calculate the revenue from those melon tallies.
"""

# create melon prices dictionary
melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }

# initialize total_revenue variable
total_revenue = 0

# loop through each key in melon tally dict
for melon_type in melon_tallies:
    # get value for matching melon type key in prices dict
    price = melon_prices[melon_type]
    # calulate melon type revenue (mult price by count)
    revenue = price * melon_tallies[melon_type]
    # add melon type revenue to total revenue
    total_revenue += revenue
    print "We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue)
    # %0.2f specifices float to two decimals?

"""
* separate sales into online sales and phone sales.
"""

print "******************************************"

orders_with_sales_file = open("orders_with_sales.csv")

# create list of online and phone sales totals, with initial values set to zero
sales = [0, 0]
# set variables to clarify which indices in list refer to which type of sales
# (inferred from print statements)
online_sales = sales[0]
phone_sales = sales[1]

# loop through each line in orders_with_sales file
for line in orders_with_sales_file:
    # break data from line into a list
    data = line.split(",")
    # set variable for sales amount from index[3] in list
    sales_amount = data[3]
    # set variable for salesperson ID number from index[1] in list 
    salesperson_id = data[1]
    # check whether id is zero, indicating online sale
    if salesperson_id == "0":
        # if it's an online sale, add sale amount to online_sales tally
        online_sales += float(sales_amount)
    else:
        # otherwise it's a phone sale, add sale amount to phone_sales tally
        phone_sales += float(sales_amount)

# close file?
orders_with_sales_file.close()

"""
* produce a fancy report to summarize the information for CEO
"""

print "Salespeople generated %0.2f in revenue." % phone_sales
print "Internet sales generated %0.2f in revenue." % online_sales
if phone_sales > online_sales:
    print "Guess there's some value to those salespeople after all."
else:
    print "Time to fire the sales team! Online sales rule all!"

print "******************************************"