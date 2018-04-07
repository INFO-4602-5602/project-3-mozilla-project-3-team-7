#Project 3
#Information Visualization
#Group 7
#Guillermo
#Matt
#Spring 2018


import csv
from collections import defaultdict
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource

privacyFocused = {'Average User':0,'Technically Savvy':0, 'Ultra Nerd':0,'Luddite':0}
priceFocused = {'Average User':0,'Technically Savvy':0, 'Ultra Nerd':0,'Luddite':0}

# Using a cleaned up csv with only the columns we want, we read it in as a dictionary format
with open('techprivacyprice.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        # With each row, we determine if the data we are looking for exists, if it does increment the sum by the value of the row
        try:
            if int(row['PrivacyFocused']) == 1:
                privacyFocused[row['TechLevel']] = int(privacyFocused[row['TechLevel']])+int(row['PrivacyFocused'])
            if int(row['PriceFocused']) == 1:
                priceFocused[row['TechLevel']] = int(priceFocused[row['TechLevel']])+int(row['PriceFocused'])
        except KeyError as name: # This captures any csv errors when the key cannot be found in the dictionary
            pass




# Y Axis for Bokeh
techTypes = ['Average User','Technically Savvy','Ultra Nerd','Luddite']
# Create two empty lists which will be used to graph the summed values
price = []
privacy = []

# We use this to correctly sort the sum dictionaries to a column format that Bokeh can understand (basically lists)
for techType in techTypes:
    price.append(priceFocused[techType])
    privacy.append(privacyFocused[techType])

print(priceFocused)
print(techTypes)
print(price)
print('\n\n')
print(privacyFocused)
print(techTypes)
print(privacy)

# Create an HTML file
output_file("privacyVis.html")

# Create Plot with Title, Size, and the X Axis
p = figure(title="Examing the Tech Levels of Users and Price vs Privacy Concerns when purchasing", x_axis_label='Tech Level', y_axis_label='Price vs. Privacy Preference', x_range=techTypes,plot_width=940,plot_height=500)

# Add Lines of our data
p.line(techTypes, price, legend="Privacy Focused", line_width=2)
p.line(techTypes, privacy, legend="Price Focused", color='red', line_width=2)

# Show the Visualization
show(p)