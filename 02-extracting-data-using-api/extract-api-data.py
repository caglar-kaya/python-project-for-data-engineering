import requests
import pandas as pd
import json

# Using the requests library call the endpoint and save the text
url = "http://api.exchangeratesapi.io/v1/latest?base=EUR&access_key=379a8db70ecfd0bc7108832fd7a84151"

response = requests.get(url)

text_content = response.text

parse_text_content = json.loads(text_content)

formatted_text_content = json.dumps(parse_text_content, indent=4)

print(formatted_text_content)

# Turn the data into a dataframe
data = response.json()

rates = data.get('rates', {})

df = pd.DataFrame.from_dict(rates, orient='index', columns=['Rate'])

df.index.name = 'Currency'

print(df)

# Drop unnescessary columns
df.drop(columns=df.columns.difference(['Rate']), inplace=True)

print(df)

# Save the Dataframe
df.to_csv('exchange_rates_1.csv')
