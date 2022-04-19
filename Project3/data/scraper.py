from bs4 import BeautifulSoup
import requests as req
import csv
import os

baseUrl = 'https://transcripts.foreverdreaming.org/viewforum.php?f=890'

startValues = [0, 25, 50, 75, 100, 125, 150, 175]
urls = []
for value in startValues:
	episodeDoc = req.get(baseUrl + '&start=' + str(value))
	epSoup = BeautifulSoup(episodeDoc.text, 'html.parser')

	tempUrls = []
	aList = epSoup.find_all('a', href=True, class_='topictitle')
	for a in aList:
		link = a['href']
		tempUrls.append('https://transcripts.foreverdreaming.org' + link[1:])

	tempUrls = tempUrls[1:]
	urls = urls + tempUrls

rows = []
for url in urls:
	print(url)
	html_doc = req.get(url)
	if html_doc:
		S = BeautifulSoup(html_doc.content, 'html.parser')
		headerDiv = S.find_all('div', class_='boxheading')[1]
		header = headerDiv.find_all('h2')[0].get_text()
		seasonNumber = header.split('-')[0].strip().split('x')[0]
		episodeNumber = header.split('-')[0].strip().split('x')[1]

		textDiv = S.find_all('div', class_='postbody')[0]
		pList = textDiv.find_all('p')
		for p in pList:
			text = p.get_text()
			if ':' in text:
				if '--Cut' not in text:
					textSplit = text.split(':')
					character = textSplit[0].strip().upper()
					if '(' in character:
						character = character.split('(')[0].strip()
					if '[' in character:
						character = character.split('[')[0].strip()
					if character == 'GREG HOUSE':
						character = 'HOUSE'
					if character == 'JAMES WILSON':
						character = 'WILSON'
					if character == 'ROBERT CHASE':
						character = 'CHASE'
					if character == 'ERIC FOREMAN':
						character = 'FOREMAN'
					if character == 'LAWRENCE KUTNER':
						character = 'KUTNER'
					if character == 'CHRIS TAUB':
						character = 'TAUB'
					if character == 'AMBER VOLAKIS':
						character = 'AMBER'
					if character == 'LISA CUDDY':
						character = 'CUDDY'
					if character == '"THIRTEEN"':
						character = 'THIRTEEN'
					line = textSplit[1].strip().lower().replace('<br>', '')
					rows.append([character, line, seasonNumber, episodeNumber])
	else:
		print('Failed to retrieve ' + url)

os.chdir('C:/workdir/visual-interfaces/Project3/data') # Desktop
# os.chdir('C:/Users/sethc/Desktop/visual-interfaces/Project3/data') # Laptop

with open('showData.csv', 'w', newline='', encoding='utf-8-sig') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerow(['Character', 'Line', 'Season', 'Episode'])
    for row in rows:
        writer.writerow(row)