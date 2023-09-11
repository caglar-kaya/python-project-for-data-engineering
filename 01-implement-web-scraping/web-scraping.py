from bs4 import BeautifulSoup
import html5lib
import requests
import pandas as pd

URL = "https://en.wikipedia.org/wiki/List_of_largest_banks"

html_data = requests.get(URL).text

print(html_data[526:549]) # List of largest banks -

soup = BeautifulSoup(html_data, 'html.parser')

data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])

for row in soup.find_all('tbody')[2].find_all('tr'):
    col = row.find_all('td')
    # #Write your code here
    if len(col) == 3:
        Bank_Name = col[1].text.strip()
        Market_Cap = col[2].text.strip()
        data = pd.concat([data, pd.DataFrame({"Name": [Bank_Name], "Market Cap (US$ Billion)": [Market_Cap]})], ignore_index=True)

first_five_rows = data.head(5)

print(first_five_rows)

data.to_json('bank_market_cap.json', orient='records', indent=5)
