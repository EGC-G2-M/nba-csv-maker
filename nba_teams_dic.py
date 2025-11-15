NBA_TEAMS = [ "ATL", "BOS", "NOP", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", "HOU",
            "IND", "LAC", "LAL", "MIA", "MIL", "MIN", "BKN", "NYK", "ORL", "PHI",
            "PHX", "POR", "SAC", "SAS", "TOR", "UTA", "MEM", "WAS", "CHA", "OKC" ]

NBA_TEAMS_CODE = {
    "ATL": (100, "atlanta-hawks", "hawks"),
    "BOS": (101, "boston-celtics", "celtics"),
    "NOP": (102, "new-orleans-pelicans", "pelicans"),
    "CHI": (103, "chicago-bulls", "bulls"),
    "CLE": (104, "cleveland-cavaliers", "cavaliers"),
    "DAL": (105, "dallas-mavericks", "mavericks"),
    "DEN": (106, "denver-nuggets", "nuggets"),
    "DET": (107, "detroit-pistons", "pistons"),
    "GSW": (108, "golden-state-warriors", "warriors"), 
    "HOU": (109, "houston-rockets", "rockets"),
    "IND": (110, "indiana-pacers", "pacers"),
    "LAC": (111, "la-clippers", "clippers"),    
    "LAL": (112, "los-angeles-lakers", "lakers"), 
    "MIA": (113, "miami-heat", "heat"),
    "MIL": (114, "milwaukee-bucks", "bucks"),
    "MIN": (115, "minnesota-timberwolves", "timberwolves"),
    "BKN": (116, "brooklyn-nets", "nets"),
    "NYK": (117, "new-york-knicks", "knicks"),  
    "ORL": (118, "orlando-magic", "magic"),
    "PHI": (119, "philadelphia-76ers", "76ers"),
    "PHX": (120, "phoenix-suns", "suns"),
    "POR": (121, "portland-trail-blazers", "trail-blazers"),
    "SAC": (122, "sacramento-kings", "kings"),
    "SAS": (123, "san-antonio-spurs", "spurs"),
    "TOR": (125, "toronto-raptors", "raptors"),
    "UTA": (126, "utah-jazz", "jazz"),
    "MEM": (127, "memphis-grizzlies", "grizzlies"),
    "WAS": (128, "washington-wizards", "wizards"),
    "CHA": (825, "charlotte-hornets", "hornets"),
    "OKC": (1827, "oklahoma-city-thunder", "thunder")
}

def get_all_teams():
    return NBA_TEAMS.keys()

def get_info_by_abbr(abbr):
    upper_abbr = abbr.upper()
    
    if upper_abbr in NBA_TEAMS:
        code, url_name, team_name = NBA_TEAMS_CODE[upper_abbr]
        return code, url_name, team_name
    else:
        return None, None, None

