import requests 
import bs4 
import csv 

url_addr = "https://www.zoomit.ir/2019/3/9/313732/national--symbol-introduced/"

response = requests.get(url_addr)

soup = bs4.BeautifulSoup(response.text, 'html.parser')  

title = soup.findAll('h1', attrs={'itemprop': 'headline'})

news_link = soup.findAll('a', attrs={'itemprop': 'url'})[0]['href']

news_summary = soup.findAll('div', attrs={'class': 'article-summery'})[0].text

comment_number = soup.findAll('span', attrs={'class': 'total-count'})[0].text


