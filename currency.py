from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import datetime
import os

url="https://x-rates.com/table/?from=INR&amount=1"

#open connection to the webpage and download it
uClient=uReq(url)

#the page is read and contents are placed in page_html
page_html=uClient.read()

#close connection
uClient.close()

#parsing html
page_soup=soup(page_html,"html.parser")
container=page_soup.find("table",{"class":"ratesTable"})

filename = input('Enter file name: ')

try:
    f = open(filename,"r",encoding="utf-8")
except IOError:
    f = open(filename,'w',encoding="utf-8")

if os.stat(filename).st_size==0:
    #creating a csv format file
    f=open(filename,"w",encoding="utf-8")
    headers="Date,US Dollar,Euro,BritishPound,Australian Dollar,Canadian Dollar,Singapore Dollar,Swiss Franc,Malaysian Ringgit,Japanese Yen,Chinese Yuan Renminbi\n"
    f.write(headers)


f = open(filename, "a", encoding="utf-8")
#appending values in csv file
rateval=container.findAll("td",{"class":"rtRates"})
d=container.find("span",{"class":"ratesTimestamp"})
print(d)
print(rateval)
print(len(rateval))
price=str(datetime.datetime.now())
for rates in  range(0,len(rateval)):
    if (rates%2!=0):
        price=price+","+rateval[rates].text
price=price+"\n"
print(price)
f.write(price)
f.close()



#plotting values on graph
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

a,b,c,d,e,f,g,h,i,j,k=np.genfromtxt(filename,dtype=None,unpack=True,delimiter=",",encoding="UTF-8")

x=np.delete(a,0)

y=np.delete(b,0)
z=np.delete(c,0)
print(x)
print(y)
print(z)




y1=y.astype(np.float)

plt.plot(x,y1)
plt.ylabel("Rate")
plt.xlabel("Date")
plt.plot_date(x,y1)
plt.gcf().autofmt_xdate()
for a,b in zip(x, y1):
    plt.text(a, b, str(b))
plt.show()
plt.show()
