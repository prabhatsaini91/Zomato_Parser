# Zomato_Parser
Parses data of restaurants from Zomato and stores them in a .csv file

### Installing Dependencies

```pip install beautifulsoup```
```pip install unicodecsv```

1. Run the file parser.py to get restaurants.csv
2. Make changes as listed in the file
3. Run the file parser.py to get wifi_restaurants.csv
4. Open Terminal and Run: 
        ```
        grep -xvFf wifi_restaurants.csv restaurants.csv > no_wifi_restaurants.csv
        ```
5. Restaurants with no wifi are stored in no_wifi_restaurants.csv
        
