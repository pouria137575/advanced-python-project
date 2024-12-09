import requests
import bs4

url = "https://karnameh.com/car-price"

response = requests.get(url)

soup = bs4.BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all("p", attrs={"class": "MuiTypography-root MuiTypography-body1 muirtl-iy5bpq"})
prices = soup.find_all('p', attrs={"class": "MuiTypography-root MuiTypography-body1 muirtl-22intj"})

for title, price in zip(titles, prices):
    print(title.text, '====', price.text) 
