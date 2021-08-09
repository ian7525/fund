import requests
from bs4 import BeautifulSoup
import csv
import datetime

fundName = '貝萊德美國特別時機基金A2美元'

netWorth = requests.get(
    'https://www.moneydj.com/funddj/yp/yp010001.djhtm?a=SHZ12')
soup = BeautifulSoup(netWorth.text, "html.parser")
today = soup.findAll("table",  {'class': 't01'})
# print(today)

todayNetWorth = []
for table_row in today[0].findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    todayNetWorth.append(output_row)
# print(todayNetWorth)

lastTenDays = []
for table_row in today[1].findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    lastTenDays.append(output_row)
# print(lastTenDays)

csvFileName = fundName+'_'+str(datetime.date.today())+'.csv'
with open(csvFileName, 'w+', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(todayNetWorth)
    writer.writerows('\n')
    writer.writerows(lastTenDays)
