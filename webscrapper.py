import requests
from bs4 import BeautifulSoup

# URL of the webpage containing the poem lines
url = 'https://www.poetryfoundation.org/poems/46473/the-road-not-taken'

# Send a GET request to the webpage URL and retrieve the HTML content
response = requests.get(url)
html_content = response.content

# Use Beautiful Soup to parse the HTML content and extract the poem lines
soup = BeautifulSoup(html_content, 'html.parser')
poem_lines = [line.text.strip() for line in soup.find_all('div', class_='c-feature-bd')]

# Print the extracted poem lines
print(poem_lines)
#This code should extract all the poem lines from the webpage and print them to the console. However, the specific HTML elements and class names used to extract the poem lines may vary depending on the webpage you're scraping.






