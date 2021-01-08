import requests
url='https://cyncs-mobile.technopro.com/eg/'
#url='https://www.yahoo.co.jp'
html=requests.get(url)
print(html.text)
