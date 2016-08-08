from bs4 import BeautifulSoup as bs
import urllib2
import unicodecsv as csv

# pagenums = 40
pagenums_for_wifi = 5

names = []
addresses = []
cuisines = []
costfor2 = []
timings = []
ratings = []

for pagenum in range(1,pagenums+1) :
	print pagenum

	html = urllib2.urlopen('https://www.zomato.com/ncr/noida-restaurants?page='+str(pagenum))
	# html = urllib2.urlopen('https://www.zomato.com/ncr/noida-restaurants?wifi=1&page='+str(pagenum))
	soup = bs(html.read())

	a_tags = soup.find_all('a',class_="result-title hover_feedback zred bold ln24   fontsize0 ")
	names = names + [tag.string.strip() for tag in a_tags]

	div_tags = soup.find_all('div', class_="col-m-16 search-result-address grey-text nowrap ln22")
	addresses = addresses + [tag.string.strip() for tag in div_tags]

	span_tags = soup.find_all('span', class_="col-s-11 col-m-12 nowrap pl0")
	
	for tag in span_tags :
		cuisines.append(', '.join(map(lambda tag: tag.string.strip(), tag.find_all('a'))))

	span_tags = soup.find_all('span', class_="col-s-11 col-m-12 pl0")
	costfor2 = costfor2 + [tag.string.strip() for tag in span_tags]

	div_tags = soup.find_all('div', class_="res-timing clearfix")
	timings = timings + [tag['title'].strip() for tag in div_tags]

	div_tags = soup.find_all('div', class_="rating-popup")
	ratings = ratings + [tag.string.strip() for tag in div_tags]


print names
print addresses
print cuisines
print costfor2
print timings
print ratings

rows = zip(names, addresses, cuisines, costfor2, timings, ratings)

with open('wifi_restaurants.csv','w') as outfile :
	csv_out = csv.writer(outfile)
	csv_out.writerow(['name','address','cuisines','cost for 2','timings','rating'])

	for row in rows :
		csv_out.writerow(row)