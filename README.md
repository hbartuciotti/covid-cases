# Covid Cases Script

This Python Script collects data regarding Covid cases in the world from a Wikipedia page and converts it into a JSON file.

# Libraries

This project uses the following library:
- BeautifulSoup4

You should be able to run the "main.py" file with no issues upon clonning this project.
However if for some reason the library is not imported, you can install it by running the following command in your project folder:

For Mac: 
```bash
pip3 install requests beautifulsoup4
```

For Windows: 
```bash
pip install requests beautifulsoup4
```

# Example of the JSON file generated:
```bash
{
  "covid_cases": [
    {
      "location": "United States",
      "cases": "10,810,305",
      "deaths": "247,646",
      "recoveries": "5,885,568"
    },
    {
      "location": "India",
      "cases": "8,728,795",
      "deaths": "128,668",
      "recoveries": "8,115,580"
    }, ...
  ]
}
```
