import requests
from bs4 import BeautifulSoup

import re

def extract_year(movie):
    match = re.search(r'\((\d+)\)', movie)
    if match:
        return int(match.group(1))
    else:
        return None

def extract_poem_details(soup):
    section = soup.find_all('table', class_ = 'mdetails')
    poem_details = [detail.get_text() for detail in section[0].find_all('td')]

    poem_details_dict = {}

    for i in range(0,len(poem_details),2):
        poem_details_dict[poem_details[i]] = poem_details[i+1]

    return poem_details_dict

def extract_poem(soup):
    return [line.text.strip() for line in soup.find_all('table',id = "tbllyrics")]


# URL of the webpage containing the poem lines
url = 'https://www.malayalachalachithram.com/song.php?i=13178'

#url = input("Enter Url")
# Send a GET request to the webpage URL and retrieve the HTML content
response = requests.get(url)
html_content = response.content

# Use Beautiful Soup to parse the HTML content and extract the poem lines
soup = BeautifulSoup(html_content, 'html.parser')
#print(soup)
#print(soup.prettify())

#Get the poem details
poem_details = extract_poem_details(soup)
#print(poem_details)

# poet = poem_details_dict['Lyrics']
# print("Poet: ",poet)

# movie = poem_details_dict['Movie']
# year = extract_year(movie)

# print('Year: ',year)

full_lyrics = soup.find_all('table',id = "tbllyrics")
#print(full_lyrics)
for lyrics in full_lyrics:
    l = lyrics.find_all('td')
    #print(l[1].text)
#print(soup.get_text())
lines = [lyrics.find_all('td') for lyrics in full_lyrics]
#print(lines[0][1].text)

poem_lines = lines[0][1].text

#poem_lines = [line.text.strip() for line in soup.find_all('table',id = "tbllyrics")]

# Print the extracted poem lines
print(poem_lines)
#This code should extract all the poem lines from the webpage and print them to the console. However, the specific HTML elements and class names used to extract the poem lines may vary depending on the webpage you're scraping.






