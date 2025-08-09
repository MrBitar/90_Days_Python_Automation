# test with https://quotes.toscrape.com
import requests 
from bs4 import BeautifulSoup as bs
url = "https://quotes.toscrape.com" # video link
response = requests.get(url) # the response of the url 
if response.status_code == 200: # the response is ok

    soup = bs(response.text, 'html.parser') #html.parser is the default parser you use to help BeautifulSoup “read” the webpage’s HTML text so you can work with it easily in Python
    title = soup.find('a')
    print("Website title is: "+title.text)

    quotes = soup.find_all('div', class_="quote")
    for quote in quotes:
        text = quote.find('span',class_='text')
        author = quote.find('small',class_='author')
        link = quote.find('a')
        link = link.get('href')
        sentence = "-----------------------\n"+text.text+"\nBy "+author.text+" his biograpghy link  "+ f'| URL:https://quotes.toscrape.com{link} '
        print(sentence)
    credits = soup.find('p', class_='text-muted')
    ref = credits.find('a').get('href')
    for a_tag in credits.find_all('a'):
       a_tag.extract()
    text ="==================\n"+ credits.get_text(strip = True)
    print(text+ f'{ref}')
    copyright = soup.find('p', class_='copyright')
    refz = copyright.find('a').get('href')
    for a_tag in copyright.find_all('a'):
       a_tag.extract()
    for span_tag in copyright.find_all('span'):
       span_tag.extract()
    text2 = copyright.get_text(strip=True)
    print(text2+ f'{refz}')

else:
    print("ERROR!!")