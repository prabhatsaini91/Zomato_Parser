from bs4 import BeautifulSoup as bs
import requests
import re
import unicodecsv as csv

url = "http://www.zomato.com/ncr/restaurants"
request = requests.get(url,params={})
soup = bs(request.text,'html.parser')

result = soup.find_all('div',{'class':re.compile(r'\bsearch-snippet-card\b')})

all_addresses = []
all_locations = []
all_names = []
all_cuisines = []
cost_for_2 = []
all_ratings = []

for res in result :
	names = res.find_all('a',{'class':re.compile(r'\bresult-title')})
	for name in names :
		all_names.append(name.string.strip())

	locations = res.find_all('a',{'class':re.compile(r'\bsearch-page-text\b')})
	for location in locations :
		all_locations.append(location.string)
		
	addresses = res.find_all('div',{'class':re.compile(r'\bsearch-result-address\b')})
	for address in addresses :
		all_addresses.append(address.string)

	cuisines = res.find_all('span',{'class':re.compile(r'\bcol-s-11\b')})
	temp = cuisines[0].find_all('a')
	fubar = ''
	for foo in temp :
		fubar = foo.string + " " + fubar

	all_cuisines.append(fubar)

	cost_for_2.append(cuisines[1].string)

	ratings = res.find_all('div',{'class':re.compile(r'\brating-popup\b')})
	for rating in ratings :
		all_ratings.append(rating.string.strip())


output_to_csv = []
for i in range(0,len(all_ratings)) :
	output_to_csv.append((all_names[i],all_locations[i],all_addresses[i],all_cuisines[i],cost_for_2[i],all_ratings[i]))

with open('restaurants.csv','w') as outfile :
	csv_out = csv.writer(outfile)
	csv_out.writerow(['name','location','address','cuisines','cost for 2','rating'])

	for row in output_to_csv :
		csv_out.writerow(row)
