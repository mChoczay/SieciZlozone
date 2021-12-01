import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = 'https://pl.wikipedia.org/wiki/Reprezentacja_Polski_w_pi%C5%82ce_no%C5%BCnej_m%C4%99%C5%BCczyzn#Od_2018'
r = requests.get(URL)
if r.status_code == 200:
    soup = BeautifulSoup(r.content, 'html.parser')
    wiki_tables = pd.read_html(r.text, attrs={"class": "wikitable"})
wiki_list = list(wiki_tables)
team = wiki_list[2]
team.to_excel('represented.xlsx')

