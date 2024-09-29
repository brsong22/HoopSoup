import json
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import EmbeddedDocumentField, FloatField, ListField, StringField
from constants.metrics import TOTALS_METRIC, PER_G_METRIC, PER_M_METRIC, PER_P_METRIC, ADV_METRIC #, PBP_METRIC, SHOOTING_METRIC, ADJ_SHOOTING_METRIC, METRICS_STATS

def create_stats_models(metric, model_name):
    model_fields = {
        'meta': {'collection': metric},
        'season': FloatField(),
        'ranker': FloatField(),
        'name_display': StringField(),
        'age': FloatField(),
        'team_name_abbr': StringField(),
        'pos': StringField(),
        'games': FloatField(),
        'games_started': FloatField(),
        'mp': FloatField(),
        'awards': ListField(StringField())
    }

    with open('constants/stat_defs.json', 'r') as stat_def_file:
        stat_defs = json.load(stat_def_file)
    model_fields = {**model_fields, **{key: FloatField() if value['type'] == 'float' else StringField() for key, value in stat_defs[metric].items()}}
    print(model_fields)
    return type(model_name, (Document,), model_fields)

TotalsStatsModel = create_stats_models(TOTALS_METRIC, 'PlayerTotalsStats')
PerGStatsModel = create_stats_models(PER_G_METRIC, 'PlayerPerGStats')
PerMStatsModel = create_stats_models(PER_M_METRIC, 'PlayerPerMStats')
PerPStatsModel = create_stats_models(PER_P_METRIC, 'PlayerPerPStats')
AdvStatsModel = create_stats_models(ADV_METRIC, 'PlayerAdvStats')