#importing the necessary modules
import os
import numpy as np
import pandas as pd
import requests
import seaborn as sns
from bs4 import BeautifulSoup 


from datetime import date

path = "E:\github projects\Footistics\Players data"    #path where you want to save
os.chdir(path)
    

path = os.getcwd()  


# function to read fbref website

def readfromhtml(filepath):
    print(filepath)
    response = requests.get(filepath).text.replace('<!--', '').replace('-->', '')
    df = pd.read_html(response, header=1)[-1]
    df = df[df['Rk'].ne('Rk')]
    df = df.apply(pd.to_numeric, errors='ignore')
    return df


#function to save the cvs
def save_all_csvs(base_url='https://fbref.com/en/comps/676/European-Championship-Stats',
                  filepath=path):

    req = requests.get(base_url)
    parse_soup = BeautifulSoup(req.content, 'lxml')
    scripts = parse_soup.find_all('ul')
    url_list = scripts[4]
    urls = []
    for url in url_list.find_all('a', href=True):
        urls.append(url['href'])
    urls = [base_url[:17] + url for url in urls]
    for url in urls:
        df = readfromhtml(url)
        filename = url.split('/')[6]
        try:
            df.to_csv(filepath + '//' + filename + '.csv', encoding='utf-8-sig')
            print("saved")
        except:
            print('An error occurred in saving the file')
        else:
            print('File has been saved as {0} at {1} in format YYYY-MM-DD '.format(filename, filepath))

save_all_csvs()