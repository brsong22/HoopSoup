from mongoengine.fields import DictField, FloatField, IntField, StringField

TOTALS_METRIC = 'totals'
PER_G_METRIC = 'per_g'
PER_M_METRIC = 'per_m'
PER_P_METRIC = 'per_p'
ADV_METRIC = 'adv'
# PBP_METRIC = 'pbp'
# SHOOTING_METRIC = 'shooting'
# ADJ_SHOOTING_METRIC = 'adj_shooting' # idk what's up with bbref's seasonal adj shooting page. beautifulsoup can't find the table by id

METRICS_CATEGORIES = {
    TOTALS_METRIC: {
        # 'data_id': 'totals',
        'fullname': 'Totals',
        'table_id': 'totals_stats',
        'url_name': 'totals'
    },
    PER_G_METRIC: {
        # 'data_id': 'per_g',
        'fullname': 'Per Game',
        'table_id': 'per_game_stats',
        'url_name': 'per_game'
    },
    PER_M_METRIC: {
        # 'data_id': 'per_minute_36',
        'fullname': 'Per 36 Minutes',
        'table_id': 'per_minute_stats',
        'url_name': 'per_minute'
    },
    PER_P_METRIC: {
        # 'data_id': 'per_poss',
        'fullname': 'Per 100 Possessions',
        'table_id': 'per_poss_stats',
        'url_name': 'per_poss'
    },
    ADV_METRIC: {
        # 'data_id': '',
        'fullname': 'Advanced',
        'table_id': 'advanced_stats',
        'url_name': 'advanced'
    },
    # PBP_METRIC: {
    #     # 'data_id': 'pbp',
    #     'fullname': 'Play-by-Play',
    #     'table_id': 'pbp_stats',
    #     'url_name': 'play-by-play'
    # },
    # SHOOTING_METRIC: {
    #     # 'data_id': 'shooting',
    #     'fullname': 'Shooting',
    #     'table_id': 'shooting_stats',
    #     'url_name': 'shooting'
    # },
    # ADJ_SHOOTING_METRIC: {
    #     # 'data_id': 'adv_shooting',
    #     'fullname': 'Adjusted Shooting',
    #     'table_id': 'adj-shooting',
    #     'url_name': 'adj_shooting'
    # }
}

# METRICS_STATS = {
#     TOTALS_METRIC: {
#         'fg': {
#             'description': 'Field Goals',
#             'display_name': 'FG',
#             'id': 'fg',
#             'type': IntField()
#         },
#         'fga': {
#             'description': 'Field Goal Attempts',
#             'display_name': 'FGA',
#             'id': 'fga',
#             'type': IntField()
#         },
#         'fg_pct': {
#             'description': 'Field Goal Percentage',
#             'display_name': '',
#             'id': '',
#             'type': FloatField()
#         },
#         'fg3': {
#             'description': '',
#             'display_name': '',
#             'id': '',
#             'type': IntField()
#         },
#         'fg3a': {
#             'description': '',
#             'display_name': '',
#             'id': '',
#             'type': IntField()
#         },
#         'fg3_pct': {
#             'description': '',
#             'display_name': '',
#             'id': '',
#             'type': FloatField()
#         },
#         'fg2': {
#             'description': '',
#             'display_name': '',
#             'id': '',
#             'type': IntField()
#         },
#         'fg2a': {
#             'description': '',
#             'display_name': '',
#             'id': '',
#             'type': IntField()
#         },
#         'fg2_pct': {
#             'description': '',
#             'display_name': '',
#             'id': '',
#             'type': FloatField()
#         },
#         'efg_pct': {
#             'description': '',
#             'display_name': '',
#             'id': '',
#             'type': FloatField()
#         },
#         'ft': {
#             'description': '',
#             'display_name': '',
#             'id': '',
#             'type': IntField()
#         },
#         'fta': {
#             'description': '',
#             'display_name': '',
#             'id': '',
#             'type': IntField()
#         },
#         'ft_pct': {
#             'description': '',
#             'display_name': '',
#             'id': '',
#             'type': FloatField()
#         },
#         'orb': {
#             'description': '',
#             'display_name': '',
#             'id': '',
#             'type': IntField()
#         },
#         'drb': {
#             'description': '',
#             'display_name': '',
#             'id': '',
#             'type': IntField()
#         },
#         'trb': {
#             'description': '',
#             'display_name': '',
#             'id': '',
#             'type': IntField()
#         },
#         'ast': {
#             'description': '',
#             'display_name': '',
#             'id': '',
#             'type': IntField()
#         },
#         'stl': {
#             'description': '',
#             'display_name': '',
#             'id': '',
#             'type': IntField()
#         },
#         'blk': {
#             'description': '',
#             'display_name': '',
#             'id': '',
#             'type': IntField()
#         },
#         'tov': {
#             'description': '',
#             'display_name': '',
#             'id': '',
#             'type': IntField()
#         },
#         'pf': {
#             'description': '',
#             'display_name': '',
#             'id': '',
#             'type': IntField()
#         },
#         'pts': {
#             'description': '',
#             'display_name': '',
#             'id': '',
#             'type': IntField()
#         }
#     },
#     PER_G_METRIC: {
#         'fg': { 'type': FloatField() },
#         'fga': { 'type': FloatField() },
#         'fg_pct': { 'type': FloatField() },
#         'fg3': { 'type': FloatField() },
#         'fg3a': { 'type': FloatField() },
#         'fg3_pct': { 'type': FloatField() },
#         'fg2': { 'type': FloatField() },
#         'fg2a': { 'type': FloatField() },
#         'fg2_pct': { 'type': FloatField() },
#         'efg_pct': { 'type': FloatField() },
#         'ft': { 'type': FloatField() },
#         'fta': { 'type': FloatField() },
#         'ft_pct': { 'type': FloatField() },
#         'orb': { 'type': FloatField() },
#         'drb': { 'type': FloatField() },
#         'trb': { 'type': FloatField() },
#         'ast': { 'type': FloatField() },
#         'stl': { 'type': FloatField() },
#         'blk': { 'type': FloatField() },
#         'tov': { 'type': FloatField() },
#         'pf': { 'type': FloatField() },
#         'pts': { 'type': FloatField() }
#     },
#     PER_M_METRIC: {
#         'fg': { 'type': FloatField() },
#         'fga': { 'type': FloatField() },
#         'fg_pct': { 'type': FloatField() },
#         'fg3': { 'type': FloatField() },
#         'fg3a': { 'type': FloatField() },
#         'fg3_pct': { 'type': FloatField() },
#         'fg2': { 'type': FloatField() },
#         'fg2a': { 'type': FloatField() },
#         'fg2_pct': { 'type': FloatField() },
#         'efg_pct': { 'type': FloatField() },
#         'ft': { 'type': FloatField() },
#         'fta': { 'type': FloatField() },
#         'ft_pct': { 'type': FloatField() },
#         'orb': { 'type': FloatField() },
#         'drb': { 'type': FloatField() },
#         'trb': { 'type': FloatField() },
#         'ast': { 'type': FloatField() },
#         'stl': { 'type': FloatField() },
#         'blk': { 'type': FloatField() },
#         'tov': { 'type': FloatField() },
#         'pf': { 'type': FloatField() },
#         'pts': { 'type': FloatField() }
#     },
#     PER_P_METRIC: {
#         'fg': { 'type': FloatField() },
#         'fga': { 'type': FloatField() },
#         'fg_pct': { 'type': FloatField() },
#         'fg3': { 'type': FloatField() },
#         'fg3a': { 'type': FloatField() },
#         'fg3_pct': { 'type': FloatField() },
#         'fg2': { 'type': FloatField() },
#         'fg2a': { 'type': FloatField() },
#         'fg2_pct': { 'type': FloatField() },
#         'ft': { 'type': FloatField() },
#         'fta': { 'type': FloatField() },
#         'ft_pct': { 'type': FloatField() },
#         'orb': { 'type': FloatField() },
#         'drb': { 'type': FloatField() },
#         'trb': { 'type': FloatField() },
#         'ast': { 'type': FloatField() },
#         'stl': { 'type': FloatField() },
#         'blk': { 'type': FloatField() },
#         'tov': { 'type': FloatField() },
#         'pf': { 'type': FloatField() },
#         'pts': { 'type': FloatField() },
#         'off_rtg': { 'type': IntField() },
#         'def_rtg': { 'type': IntField() }
#     },
#     ADV_METRIC: {
#         'per': { 'type': FloatField() }, # ! CHANGE KEY TO COLUMN NAME AND ADD PROP "ID" SO WE CAN QUERY BY COMMON NAME maybe add "display_name" for capitalization and special characters
#         'ts_pct': { 'type': FloatField() },
#         'fg3a_per_fga_pct': { 'type': FloatField() },
#         'fta_per_fga_pct': { 'type': FloatField() },
#         'fg3a': { 'type': FloatField() },
#         'fg3_pct': { 'type': FloatField() },
#         'fg2': { 'type': FloatField() },
#         'fg2a': { 'type': FloatField() },
#         'fg2_pct': { 'type': FloatField() },
#         'efg_pct': { 'type': FloatField() },
#         'ft': { 'type': FloatField() },
#         'fta': { 'type': FloatField() },
#         'ft_pct': { 'type': FloatField() },
#         'orb': { 'type': FloatField() },
#         'drb': { 'type': FloatField() },
#         'trb': { 'type': FloatField() },
#         'ast': { 'type': FloatField() },
#         'stl': { 'type': FloatField() },
#         'blk': { 'type': FloatField() },
#         'tov': { 'type': FloatField() },
#         'pf': { 'type': FloatField() },
#         'pts': { 'type': FloatField() }
#     },
#     PBP_METRIC: {},
#     SHOOTING_METRIC: {},
#     ADV_SHOOTING_METRIC: {}
# }