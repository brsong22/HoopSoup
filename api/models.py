import json
from mongoengine import Document
from mongoengine.fields import FloatField, ListField, StringField
from constants.metrics import TOTALS_METRIC, PER_G_METRIC, PER_M_METRIC, PER_P_METRIC, ADV_METRIC

def create_stats_models(metric, model_name):
    model_fields = {
        'meta': {'collection': metric},
    }
    with open('constants/stat_defs.json', 'r') as stat_def_file:
        stat_defs = json.load(stat_def_file)
    for field, value in stat_defs[metric].items():
        if value['type'] == 'float':
            model_fields[field] = FloatField()
            model_fields[f'{field}_lte'] = FloatField()
            model_fields[f'{field}_gte'] = FloatField()
        elif field == 'awards':
            model_fields[field] = ListField(StringField())
        else:
            model_fields[field] = StringField()
    
    return type(model_name, (Document,), model_fields)

TotalsStatsModel = create_stats_models(TOTALS_METRIC, 'PlayerTotalsStats')
PerGStatsModel = create_stats_models(PER_G_METRIC, 'PlayerPerGStats')
PerMStatsModel = create_stats_models(PER_M_METRIC, 'PlayerPerMStats')
PerPStatsModel = create_stats_models(PER_P_METRIC, 'PlayerPerPStats')
AdvStatsModel = create_stats_models(ADV_METRIC, 'PlayerAdvStats')