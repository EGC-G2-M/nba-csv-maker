import csv
import os

from nba_data_to_csv import obtain_players_data
from nba_teams_dic import NBA_TEAMS_CODE, NBA_TEAMS

def export_to_csv(team_abbr, year, playoffs=False, name_type='short', custom_folder_name=None):
    players_data = obtain_players_data(team_abbr, year, playoffs)
    if not players_data:
        print("No player data to export.")
        return
    filename = create_filename(team_abbr, year, playoffs=playoffs, name_type=name_type, custom_folder_name=custom_folder_name)
    header = ["Name", "Height", "Age", "Games", "Points per game", "Assists per game", "Rebounds per game"]

    ask_about_overwrite(filename)

    try:
        directory = os.path.dirname(filename)

        if directory and not os.path.exists(directory):
            try:
                os.makedirs(directory, exist_ok=True)
            except OSError as e:
                print(f"Error creating directory'{directory}': {e}")
                return
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(header)
            writer.writerows(players_data)
        print(f"{filename} exported successfully.")
        
    except Exception as e:
        print(f"Error exporting to CSV: {e}")

def ask_about_overwrite(filename):
    if os.path.exists(filename):
        while True :
            choice = input(f"The file '{filename}' already exists. Do you want to overwrite it? (Y/n): ").strip().lower()
            if choice == 'y':
                print(f"Overwriting '{filename}'...")
                break  
            elif choice == 'n':
                print("Export cancelled by the user.")
                return 
            else:
                print("Invalid input. Please enter 'Y' or 'n'.")


def create_filename(team_abbr, year, playoffs=False, name_type='short', custom_folder_name=None):
    """ 
        - 'short' (default): Short name (e.g., milwaukee or lakers).
        - 'abbr': Abbreviature (e.g., MIL).
        - 'url': Uses the name that appears in the url (e.g., milwaukee-bucks).
    """

    if name_type == 'abbr':
        team_name = team_abbr
    elif name_type == 'url':
        team_name = NBA_TEAMS_CODE[team_abbr][1]
    else: # 'short'
        team_name = NBA_TEAMS_CODE[team_abbr][2]

    season= f"{year}-{(year+1)%100:02d}"

    if custom_folder_name is None:
        if playoffs:
            path_prefix = "playoffs"
            filename_suffix = f"_playoffs_{season}.csv"
        else:
            path_prefix = "season"
            filename_suffix = f"_{season}.csv"
        res = f"data/{path_prefix}-{season}/{team_name}{filename_suffix}"

    else:
        filename_suffix = f"_{season}.csv"
        path_prefix = "depot"
        res = f"data/{custom_folder_name}/{team_name}{filename_suffix}"
        
    return res

def create_several_csv_loop(team_abbrs, years, playoffs=False, name_type='short', custom_folder_name=None):
    for team_abbr in team_abbrs:
        for year in years:
            export_to_csv(team_abbr, year, playoffs=playoffs, name_type=name_type, custom_folder_name=custom_folder_name)

def create_several_csv_pairs (pair_list, playoffs=False, name_type='short', custom_folder_name=None):
    for pair in pair_list:
        team_abbr = pair[0]
        year = pair[1]
        export_to_csv(team_abbr, year, playoffs=playoffs, name_type=name_type, custom_folder_name=custom_folder_name)

if __name__ == '__main__':
    # teams = [ "ATL", "BOS", "NOP", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", "HOU",
    #         "IND", "LAC", "LAL", "MIA", "MIL", "MIN", "BKN", "NYK", "ORL", "PHI",
    #         "PHX", "POR", "SAC", "SAS", "TOR", "UTA", "MEM", "WAS", "CHA", "OKC" ]
    # years = list(range(2022, 2025))
    # create_several_csv_loop(teams, years, playoffs=False)

    # pairlist = [("NYK", 2016), ("NYK", 2017), ("CHA", 2017), ("CHA", 2018), ("CHA", 2019),("NOP", 2020), ("NOP", 2021), ("NOP", 2022)]
    # custom_folder_name = "Willy-Hernangomez-teams"
    # create_several_csv_pairs(pairlist, custom_folder_name=custom_folder_name)
    # custom_folder_name = "Willy-Hernangomez-playoffs-teams"
    # create_several_csv_pairs(pairlist, playoffs=True, custom_folder_name=custom_folder_name)

    # custom_folder_name = "spurs-ring-winners"
    # create_several_csv_pairs(pairlist_spurs_championships, playoffs=True, custom_folder_name=custom_folder_name)
    pairlist_random_selection_old = [
    # --- 
    ("SAC", 1999),
    ("PHI", 1999),
    
    # --- Año 2001 (Temporada 2001-02) ---
    ("BKN", 2001),   # Finalistas del Este (como Nets)
    ("DAL", 2001),
    ("GSW", 2001),
    
    # --- Año 2004 (Temporada 2004-05) ---
    ("DET", 2004),   # Finalistas
    ("CLE", 2004),   # Un año de juventud de LeBron
    ("OKC", 2004),   # Seattle Supersonics (ahora OKC)
]

    custom_folder_name = "Random-NBA-Rosters-1990-2004"
    create_several_csv_pairs(pairlist_random_selection_old)


