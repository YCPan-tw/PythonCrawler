
# coding: utf-8

# In[15]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
from random import randint
#code modify from https://medium.com/@danielcimring/downloading-historical-data-from-coinmarketcap-41a2b0111baf
#https://coinmarketcap.com/methodology/#market-data
#https://coinmarketcap.com/faq/


# In[16]:


url_list ={"ETH": "https://coinmarketcap.com/currencies/ethereum/historical-data/?start=20130428&end=20190228"
,"BTC": "https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428&end=20190228"
,"LTC":"https://coinmarketcap.com/currencies/litecoin/historical-data/?start=20130428&end=20190228"
,"XRP":"https://coinmarketcap.com/currencies/ripple/historical-data/?start=20130428&end=20190228"
,"XMR":"https://coinmarketcap.com/currencies/monero/historical-data/?start=20130428&end=20190228"
,"DASH":"https://coinmarketcap.com/currencies/dash/historical-data/?start=20130428&end=20190228"  
,"EOS":"https://coinmarketcap.com/currencies/eos/historical-data/?start=20130428&end=20190228"
,"ADA":"https://coinmarketcap.com/currencies/cardano/historical-data/?start=20130428&end=20190228"        
,"TRON":"https://coinmarketcap.com/currencies/tron/historical-data/?start=20130428&end=20190228"
          }

for key,value in url_list.items():
    print(key,value)


# In[17]:


def getdata(urldict):
    for key,value in urldict.items():
        content = requests.get(value).content
        soup = BeautifulSoup(content,'html.parser')
        table = soup.find('table', {'class': 'table'})
        data = [[td.text.strip() for td in tr.findChildren('td')] 
            for tr in table.findChildren('tr')]
        df = pd.DataFrame(data)
        df.drop(df.index[0], inplace=True) # first row is empty
        df[0] =  pd.to_datetime(df[0]) # date
        for i in range(1,7):
            df[i] = pd.to_numeric(df[i].str.replace(",","").str.replace("-","")) # some vol is missing and has -
        df.columns = ['Date','Open','High','Low','Close','Volume','Market Cap']
        df.set_index('Date',inplace=True)
        df.sort_index(inplace=True)
        filename = "Data_"+str(key)+".csv"
        df.to_csv(filename)
        
        #sleep a while in order to prevent from
        t = randint(1,5)
        time.sleep(t)
        print("take a rest(",t,")second!")


# In[20]:


if __name__ == '__main__':
    getdata(url_list)

