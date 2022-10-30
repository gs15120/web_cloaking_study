from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests,re,os
from urllib.request import urlretrieve

html = requests.get('https://search.naver.com/search.naver?query=날씨')
#pprint(html.text)

soup = bs(html.text,'html.parser')
html.close()
#pprint(soup)
datal=soup.find('div',{'class':'_today'})
#pprint(datal)
data2=datal.findAll('div');
#pprint(data2[0])


#today weather
find=data2[0].find('span',{'class':'blind'}).text
#print(find)


#webtoon page
html= requests.get("https://comic.naver.com/webtoon/weekday")
soup=bs(html.text,'html.parser');
html.close()


#webtoon momday
data1=soup.find('div',{'class':'col_inner'})
#pprint(data1)

#coode incluoding title
data2=data1.findAll('a',{'class':'title'})
#pprint(data2)

#print titles
titles=[]
for t in data2:
    titles.append(t.text)
#pprint(titles)





#webtoon for 1 week
data1_list=soup.findAll('div',{'class':'col_inner'})

week_titles=[]

for data1 in data1_list:
#code including titles
    data2=data1.findAll('a',{'class':'title'})
#pprint(data2)

#add titles
    titles=[]
    for t in data2:
        titles.append(t.text)
        #pprint(titles)
    week_titles.append(titles)
#print all titles
#pprint(week_titles)


#source of webpage
html=requests.get("https://comic.naver.com/webtoon/weekday")
soup=bs(html.text,'html.parser')
html.close()

#webtoons
data1_list=soup.findAll('div',{'class':'col_inner'})

#range of thumbnails+titles
list=[]
for data1 in data1_list:
    list.extend(data1.findAll('li'))

#pprint(list)



try:
    if not (os.path.isdir('image')):
        os.makedirs(os.path.join('image'))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 생성 실패!")
        exit()
#all titles+thumbnailes
for i in list:
    img=i.find('img')
    title=img['title']
    img_src=img['src']
    #print(title,img_src)
    title=re.sub('[^0-9a-zA-Zㄱ-힗]',' ',title)
    urlretrieve(img_src,'./image/'+title+'.jpg')