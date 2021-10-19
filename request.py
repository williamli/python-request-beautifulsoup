import requests
from bs4 import BeautifulSoup

page = requests.get('https://en.wikipedia.org/wiki/Usage_share_of_web_browsers')
# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
rows = soup.table.find_all('tr')
# print(rows.td)
# print(BeautifulSoup(soup.table.tr.string, 'html.parser').td)
data = []

for tr in rows:
  tds = tr.find_all('td')
  if tds:
    # print(tds)
    data.append({
      "browser": tds[0].a.string.rstrip(),
      "stat-counter": tds[1].string.rstrip(),
      "netmarket": tds[2].string.rstrip(),
      "wikimedia": tds[3].string.rstrip()
    })

print(data)