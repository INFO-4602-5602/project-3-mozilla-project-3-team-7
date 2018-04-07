import csv
from collections import defaultdict
from bokeh.plotting import figure, output_file, show

#These are the possible ratings for 

deviceNum = []
SafetyRating = []
SecurityRating = []
PrivacyRating = []
saAverages=[0]*10
seAverages=[0]*10
pAverages=[10]*10
p = figure(title='Avg. # of Devices Vs. Safety, Security, and Privacy')


with open('Num_Vs_Safe_Sec_Priv_Compact.csv')  as d:
	reader = csv.DictReader(d)
	rownum = 0
	for row in reader:
		testString = ''
		counter = 0
		if row['WiFi_Router'] == "WiFi Router":
			counter +=1
		if row['Laptop_Computer'] == "Laptop computer":
			counter +=1
		if row['Smart_Phone'] == "Smart phone":
			counter +=1
		if row['Smart_TV'] == "Smart TV":
			counter +=1
		if row['Activity_Tracker'] == "Activity Tracker (ex: Fitbit or Apple Watch)":
			counter +=1
		if row['Smarthome_Hub'] == "Smarthome Hub (ex. Amazon Echo, Google Alexa)":
			counter +=1
		if row['Internet_Connected_Car'] == "Car that connects to the internet":
			counter +=1
		if row['Smart_Thermostat'] == "Smart Thermostat (ex: Nest)":
			counter +=1
		if row['Smart_Appliance'] == "Smart Appliance (ex. Coffeemaker, Refrigerator, Oven, Fridge)":
			counter +=1
		if row['Smart_Doors'] == "Smart Door Locks (ex. Door locks for your home you can open via bluetooth)":
			counter +=1
		if row['Smart_Lighting'] == "Smart Lighting (ex. Connected lighting switches, dimmers, or bulbs)":
			counter +=1
			
		saR = row['Safety']
		if saR=='' or saR ==' ':
			saR=0
		seR = row['Security']
		if seR=='' or seR==' ':
			seR = 0
		pR = row['Privacy']
		if pR==''or pR==' ':
			pR=0
		deviceNum.append(counter)
		SafetyRating.append(int(saR))
		SecurityRating.append(int(seR))
		PrivacyRating.append(int(pR))
saC=0
saDA=0
seC=0
seDA=0
pC=0
pDA=0
for i in range(1,11):
	for j in range(len(deviceNum)):
		if i == SafetyRating[j]:
			saC+=1
			saDA += deviceNum[j]
		if i == SecurityRating[j]:
			seC+=1
			seDA += deviceNum[j]
		if i == PrivacyRating[j]:
			pC+=1
			pDA += deviceNum[j]
	if saC !=0:
		saDA=saDA/saC
	else:
		saDa = 0
	if seC !=0:
		seDA=seDA/seC
	else:
		seDA=0
	if pC !=0:
		pDA=pDA/pC
	else:
		pDA=0
	
	saAverages[i-1] = saDA
	seAverages[i-1] = seDA
	pAverages[i-1] = pDA
		
		
p.circle([1,2,3,4,5,6,7,8,9,10],pAverages,size=5,fill_color='blue',alpha=.5)
p.circle([1,2,3,4,5,6,7,8,9,10],saAverages,size=5,fill_color='green',alpha=.5)
p.circle([1,2,3,4,5,6,7,8,9,10],seAverages,size=5,fill_color='orange',alpha=.5)

p.legend.location = "top_right"
p.legend.click_policy='hide'	
	
output_file("scatter.html")
show(p)