import requests
from bs4 import BeautifulSoup
print("films ou series")
choix = input()
if choix == 'films':
 url = "https://www.torrent9.ac/torrents/films"
elif choix == 'series':
 url = "https://www.torrent9.ac/torrents/series"
else:
 url = "https://www.torrent9.ac/recherche/" + choix

response = requests.get(url)
id = 0
links = []
titles = []
nu = 0
if response.ok:
 soup = BeautifulSoup(response.text, 'html5lib')
 nr = soup.find('tbody').findAll('tr')
 for film in  range(len(nr)):
  tr = soup.find('tbody').findAll('tr')[id]
  td = tr.findAll('td')
  a = td[0].contents[2]
  link = "https://www.torrent9.ac" + a['href']
  links.append(link)
  title = a['title']
  size = td[1].contents
  id = id + 1

  print(str(id) + " "+str(title) + " " + str(link) + " " + str(size))
  if id == len(nr):
   print("Faite votre choix")
   choix = input()
   demande = int(choix) -1
   response1 = requests.get(links[int(demande)])
   soup1 = BeautifulSoup(response1.text,'html5lib' )
   for l in range(2):

    div = soup1.findAll('a', {'class': 'btn btn-danger download'})
    a = div[nu]
    print("link or margnet")
    torrentlink = input()
    
    if torrentlink == "link":

     print("https://www.torrent9.ac"+ a['href'])
     print(" ")
    nu = nu + 1
   elif torrentlink == "magnet":
    print(a['href'])





