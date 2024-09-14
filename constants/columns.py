METRICS_CATEGORIES = {
    'totals': {
        'identifier': 'totals',
        'name': 'totals'
    },
    'per_g': {
        'identifier': 'per_game',
        'name': 'per_game'
    },
    'per_m': {
        'identifier': 'per_minute',
        'name': 'per_minute'
    },
    'per_p': {
        'identifier': 'per_poss',
        'name': 'per_poss'
    },
    'adv': {
        'identifier': 'advanced',
        'name': 'advanced'
    },
    'pbp': {
        'identifier': 'pbp',
        'name': 'play-by-play'
    },
    'shooting': {
        'identifier': 'shooting',
        'name': 'shooting'
    },
    'adv_shooting': {
        'identifier': 'adv_shooting',
        'name': 'adv_shooting'
    }
}

METRICS_STATS_HEADERS = {
    METRICS_CATEGORIES['totals']['name']: {
        'name': 'Totals',
        'description': 'Season Totals',
        'stats': {
            'fg': {
                'name': 'Field Goals',
                'abbreviation': 'FG',
                'description': 'Field Goals made'
            },
            'fga': {
                'name': 'Field Goal Attempts',
                'abbreviation': 'FGA',
                'description': 'Field Goals attempted'
            },
            'fg_pct': {
                'name': 'Field Goal Percentage',
                'abbreviation': 'FG%',
                'description': 'Percent of Field Goals made'
            },
            'fg3': {
                'name': '3-Point Field Goals',
                'abbreviation': '3P',
                'description': '3-Point Field Goals made'
            },
            'fg3a': {
                'name': '3-Point Field Goal Attempts',
                'abbreviation': '3PA',
                'description': '3-Point Field Goals attempted'
            },
            'fg3_pct': {
                'name': '3-Point Field Goal Percentage',
                'abbreviation': '3P%',
                'description': 'Percent of 3-Point Field Goals made'
            },
            'fg2': {
                'name': '2-Point Field Goals',
                'abbreviation': '2P',
                'description': '2-Point Field Goals made'
            },
            'fg2a': {
                'name': '2-Point Field Goal Attempts',
                'abbreviation': '2PA',
                'description': '2-Point Field Goals attempted'
            },
            'fg2_pct': {
                'name': '2-Point Field Goal Percentage',
                'abbreviation': '2P%',
                'description': 'Percent of 2-Point Field Goals made'
            },
            'efg_pct': {
                'name': 'Effective Field Goal Percentage',
                'abbreviation': 'eFG%',
                'description': 'Weighted combined Field Goal Percentage between 3 and 2-Pointers'
            },
            'ft': {
                'name': 'Free Throws',
                'abbreviation': 'FT',
                'description': 'Free Throws made'
            },
            'fta': {
                'name': 'Free Throw Attempts',
                'abbreviation': 'FTA',
                'description': 'Free Throws attempted'
            },
            'ft_pct': {
                'name': 'Free Throw Percentage',
                'abbreviation': 'FT%',
                'description': 'Percent of Free Throws made'
            },
            'orb': {
                'name': 'Offensive Rebounds',
                'abbreviation': 'ORB',
                'description': 'Rebounds while on offense'
            },
            'drb': {
                'name': 'Defensive Rebounds',
                'abbreviation': 'DRB',
                'description': 'Rebounds while on defense'
            },
            'trb': {
                'name': 'Total Rebounds',
                'abbreviation': 'TRB',
                'description': 'Total Rebounds made'
            },
            'ast': {
                'name': 'Assists',
                'abbreviation': 'AST',
                'description': 'Passes made that led to a made basket'
            },
            'stl': {
                'name': 'Steals',
                'abbreviation': 'STL',
                'description': 'Balls taken from offensive team'
            },
            'blk': {
                'name': 'Blocks',
                'abbreviation': 'BLK',
                'description': 'Shots blocked while on defense'
            },
            'tov': {
                'name': 'Turnovers',
                'abbreviation': 'TOV',
                'description': 'Balls lost to defensive team'
            },
            'pf': {
                'name': 'Personal Fouls',
                'abbreviation': 'PF',
                'description': 'Fouls committed'
            },
            'pts': {
                'name': 'Points',
                'abbreviation': 'PTS',
                'description': 'buckets.'
            }
        }
    },
    METRICS_CATEGORIES['per_g']['name']: {
        'name': 'Per Game',
        'description': 'Per Game Averages',
        'stats': {
            'fg_per_g': {
                'name': 'Field Goals',
                'abbreviation': 'FG',
                'description': 'Field Goals made'
            },
            'fga_per_g': {
                'name': 'Field Goal Attempts',
                'abbreviation': 'FGA',
                'description': 'Field Goals attempted'
            },
            'fg_pct': {
                'name': 'Field Goal Percentage',
                'abbreviation': 'FG%',
                'description': 'Percent of Field Goals made'
            },
            'fg3_per_g': {
                'name': '3-Point Field Goals',
                'abbreviation': '3P',
                'description': '3-Point Field Goals made'
            },
            'fg3a_per_g': {
                'name': '3-Point Field Goal Attempts',
                'abbreviation': '3PA',
                'description': '3-Point Field Goals attempted'
            },
            'fg3_pct': {
                'name': '3-Point Field Goal Percentage',
                'abbreviation': '3P%',
                'description': 'Percent of 3-Point Field Goals made'
            },
            'fg2_per_g': {
                'name': '2-Point Field Goals',
                'abbreviation': '2P',
                'description': '2-Point Field Goals made'
            },
            'fg2a_per_g': {
                'name': '2-Point Field Goal Attempts',
                'abbreviation': '2PA',
                'description': '2-Point Field Goals attempted'
            },
            'fg2_pct': {
                'name': '2-Point Field Goal Percentage',
                'abbreviation': '2P%',
                'description': 'Percent of 2-Point Field Goals made'
            },
            'efg_pct': {
                'name': 'Effective Field Goal Percentage',
                'abbreviation': 'eFG%',
                'description': 'Weighted combined Field Goal Percentage between 3 and 2-Pointers'
            },
            'ft_per_g': {
                'name': 'Free Throws',
                'abbreviation': 'FT',
                'description': 'Free Throws made'
            },
            'fta_per_g': {
                'name': 'Free Throw Attempts',
                'abbreviation': 'FTA',
                'description': 'Free Throws attempted'
            },
            'ft_pct': {
                'name': 'Free Throw Percentage',
                'abbreviation': 'FT%',
                'description': 'Percent of Free Throws made'
            },
            'orb_per_g': {
                'name': 'Offensive Rebounds',
                'abbreviation': 'ORB',
                'description': 'Rebounds while on offense'
            },
            'drb_per_g': {
                'name': 'Defensive Rebounds',
                'abbreviation': 'DRB',
                'description': 'Rebounds while on defense'
            },
            'trb_per_g': {
                'name': 'Total Rebounds',
                'abbreviation': 'TRB',
                'description': 'Total Rebounds made'
            },
            'ast_per_g': {
                'name': 'Assists',
                'abbreviation': 'AST',
                'description': 'Passes made that led to a made basket'
            },
            'stl_per_g': {
                'name': 'Steals',
                'abbreviation': 'STL',
                'description': 'Balls taken from offensive team'
            },
            'blk_per_g': {
                'name': 'Blocks',
                'abbreviation': 'BLK',
                'description': 'Shots blocked while on defense'
            },
            'tov_per_g': {
                'name': 'Turnovers',
                'abbreviation': 'TOV',
                'description': 'Balls lost to defensive team'
            },
            'pf_per_g': {
                'name': 'Personal Fouls',
                'abbreviation': 'PF',
                'description': 'Fouls committed'
            },
            'pts_per_g': {
                'name': 'Points',
                'abbreviation': 'PTS',
                'description': 'buckets.'
            }
        }
    }
}