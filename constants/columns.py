from mongoengine.fields import DictField, FloatField, IntField, StringField

TOTALS_METRIC = 'totals'
PER_G_METRIC = 'per_g'
PER_M_METRIC = 'per_m'
PER_P_METRIC = 'per_p'
ADV_METRIC = 'adv'
PBP_METRIC = 'pbp'
SHOOTING_METRIC = 'shooting'
ADV_SHOOTING_METRIC = 'adv_shooting'

METRICS_CATEGORIES = {
    TOTALS_METRIC: {
        'identifier': 'totals',
        'name': 'totals'
    },
    PER_G_METRIC: {
        'identifier': 'per_game',
        'name': 'per_game'
    },
    PER_M_METRIC: {
        'identifier': 'per_minute',
        'name': 'per_minute'
    },
    PER_P_METRIC: {
        'identifier': 'per_poss',
        'name': 'per_poss'
    },
    ADV_METRIC: {
        'identifier': 'advanced',
        'name': 'advanced'
    },
    PBP_METRIC: {
        'identifier': 'pbp',
        'name': 'play-by-play'
    },
    SHOOTING_METRIC: {
        'identifier': 'shooting',
        'name': 'shooting'
    },
    ADV_SHOOTING_METRIC: {
        'identifier': 'adv_shooting',
        'name': 'adv_shooting'
    }
}

METRICS_STATS = {
    TOTALS_METRIC: {
        'fg': { 'type': IntField() },
        'fga': { 'type': IntField() },
        'fg_pct': { 'type': FloatField() },
        'fg3': { 'type': IntField() },
        'fg3a': { 'type': IntField() },
        'fg3_pct': { 'type': FloatField() },
        'fg2': { 'type': IntField() },
        'fg2a': { 'type': IntField() },
        'fg2_pct': { 'type': FloatField() },
        'efg_pct': { 'type': FloatField() },
        'ft': { 'type': IntField() },
        'fta': { 'type': IntField() },
        'ft_pct': { 'type': FloatField() },
        'orb': { 'type': IntField() },
        'drb': { 'type': IntField() },
        'trb': { 'type': IntField() },
        'ast': { 'type': IntField() },
        'stl': { 'type': IntField() },
        'blk': { 'type': IntField() },
        'tov': { 'type': IntField() },
        'pf': { 'type': IntField() },
        'pts': { 'type': IntField() }
    },
    PER_G_METRIC: {
        'fg': { 'type': FloatField() },
        'fga': { 'type': FloatField() },
        'fg_pct': { 'type': FloatField() },
        'fg3': { 'type': FloatField() },
        'fg3a': { 'type': FloatField() },
        'fg3_pct': { 'type': FloatField() },
        'fg2': { 'type': FloatField() },
        'fg2a': { 'type': FloatField() },
        'fg2_pct': { 'type': FloatField() },
        'efg_pct': { 'type': FloatField() },
        'ft': { 'type': FloatField() },
        'fta': { 'type': FloatField() },
        'ft_pct': { 'type': FloatField() },
        'orb': { 'type': FloatField() },
        'drb': { 'type': FloatField() },
        'trb': { 'type': FloatField() },
        'ast': { 'type': FloatField() },
        'stl': { 'type': FloatField() },
        'blk': { 'type': FloatField() },
        'tov': { 'type': FloatField() },
        'pf': { 'type': FloatField() },
        'pts': { 'type': FloatField() }
    },
    PER_M_METRIC: {},
    PER_P_METRIC: {},
    ADV_METRIC: {},
    PBP_METRIC: {},
    SHOOTING_METRIC: {},
    ADV_SHOOTING_METRIC: {}
}