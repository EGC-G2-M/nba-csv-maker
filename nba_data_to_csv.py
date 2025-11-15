from bs4 import BeautifulSoup
import urllib.request
from tkinter import *
from tkinter import messagebox
import re, os, shutil
from datetime import datetime
from datetime import datetime
import locale
import os, ssl
from nba_teams_dic import NBA_TEAMS_CODE, get_info_by_abbr

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

def obtain_players_data(team_abbr, year, playoffs=False):
    team_code, url_name, team_name= get_info_by_abbr(team_abbr)
    if not check_parameters(team_abbr, year, playoffs, team_code, url_name):
        return
    if year == 2025:
        uri = "https://www.proballers.com/es/baloncesto/equipo/" + str(team_code) + "/" + url_name
    else :
        uri = "https://www.proballers.com/es/baloncesto/equipo/" + str(team_code) + "/" + url_name + "/" + str(year)
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
    'Referer': 'https://www.google.com/' # O el dominio principal 'https://www.proballers.com'
    }
    req=urllib.request.Request(uri , headers=headers) 
    f = urllib.request.urlopen(req) 
    s = BeautifulSoup(f, 'lxml')

    if playoffs: 
        if  s.find("span", class_="generic-section-subtitle", string="NBA Playoffs"):
            playoff_span = s.find("span", class_="generic-section-subtitle", string="NBA Playoffs")
            stats_container = playoff_span.find_parent("section", class_="home-team__content__roster-statistics__content mb-5")
        else : 
            print (f"No data found. Are you sure {team_abbr} played the playoffs of {year}-{(year+1)%100:02d} season?")
            return
    else: 
        stats_container = s.find("section", class_="home-team__content__roster-statistics__content mb-5" )
    players_table = stats_container.find("tbody")
    players_info = players_table.find_all("tr")
    res = []
    for p in players_info:
        name_td, height_td, age_td = p.find_all("td", class_="left")[0:3]    
        name = name_td.text.strip()
        height = height_td.text.strip()
        age = age_td.text.strip() 
        games = p.select_one('td[class="right"]').text.strip() 
        ppg_td, apg_td, rpg_td = p.find_all("td", class_="right")[0:3]
        ppg = ppg_td.text.strip()
        apg = apg_td.text.strip()
        rpg = rpg_td.text.strip()
        player_info = (name, height, age, games, ppg, apg, rpg)
        res.append(player_info)
        # print(player_info)
    return res

def check_parameters(team_abbr, year, playoffs, team_code, url_name):
    res = True
    if team_abbr is None or team_abbr not in NBA_TEAMS:
        print("Team not found")
        res = False
    elif not team_code or not url_name:
        print("Team information is incomplete")
        res = False 
    elif playoffs:
        if year < 1996 or year > 2024:
            print("Year out of range for playoffs, we only have playoffs data from 1996 to 2024")
            res = False
    elif year < 1975 or year > 2025:
        print("Year out of range, we only have data from 1975 to 2025")
        res = False
    return res
    
NBA_TEAMS = [ "ATL", "BOS", "NOP", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", "HOU",
            "IND", "LAC", "LAL", "MIA", "MIL", "MIN", "BKN", "NYK", "ORL", "PHI",
            "PHX", "POR", "SAC", "SAS", "TOR", "UTA", "MEM", "WAS", "CHA", "OKC" ]

if __name__ == '__main__':
    # read_data()
    obtain_players_data("CHI", 2026, playoffs=False)