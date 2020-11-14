# This Python Script collects data from a website and converts into a JSON file.
# In this example I am collecting data regarding Covid cases around the world
# from a table on Wikipedia.
from bs4 import BeautifulSoup
import requests
import json

# URL to be scanned
url = "https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html Page content
soup = BeautifulSoup(html_content, "html.parser")

# Print Page title
print("Page Title:\n" + soup.title.text + "\n")

# Get Reference to Table
covid_table = soup.find('table', attrs={'class': 'wikitable'})
# Get Reference to "World" data (First row of the table)
world_data = covid_table.find('tr', attrs={'class': 'sorttop'})
world_data_columns = world_data.find_all('th')
# Get Reference to all other rows in the table
rows = covid_table.tbody.find_all('tr')

# Create Json data object
json_data = {'covid_cases': []}

# Add World data to my object
json_data['covid_cases'].append({
    'location': 'World',
    'cases': world_data_columns[2].text.replace('\n', ''),
    'deaths': world_data_columns[3].text.replace('\n', ''),
    'recoveries': world_data_columns[4].text.replace('\n', '')
})

# Add data from all other rows in my object (Countries, Cases, Deaths and Recoveries)
for row in rows:
    th_tags = row.find_all('th')
    td_tags = row.find_all('td')
    if len(th_tags) == 2:
        json_data['covid_cases'].append({
            'location': th_tags[1].a.text,
            'cases': td_tags[0].text.replace('\n', ''),
            'deaths': td_tags[1].text.replace('\n', ''),
            'recoveries': td_tags[2].text.replace('\n', '')
        })

# Print Json Object
print("Json Object:")
print(json_data)

# Export Json file
with open('data.json', 'w') as outfile:
    json.dump(json_data, outfile)
