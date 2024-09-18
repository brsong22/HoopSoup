from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import EmbeddedDocumentField, IntField, StringField
from constants.columns import TOTALS_METRIC, PER_G_METRIC, PER_M_METRIC, PER_P_METRIC, ADV_METRIC, PBP_METRIC, SHOOTING_METRIC, ADV_SHOOTING_METRIC, METRICS_STATS

def create_stats_embedded_document_class(metric):
    class_fields = {key: value['type'] for key, value in METRICS_STATS[metric].items()}
    return type('Stats', (EmbeddedDocument,), class_fields)

TotalsStats = create_stats_embedded_document_class(TOTALS_METRIC)
PerGStats = create_stats_embedded_document_class(PER_G_METRIC)
PerMStats = create_stats_embedded_document_class(PER_M_METRIC)
PerPStats = create_stats_embedded_document_class(PER_P_METRIC)
AdvStats = create_stats_embedded_document_class(ADV_METRIC)
PbpStats = create_stats_embedded_document_class(PBP_METRIC)
ShootingStats = create_stats_embedded_document_class(SHOOTING_METRIC)
AdvShootingStats = create_stats_embedded_document_class(ADV_SHOOTING_METRIC)

class PlayerTotalsStats(Document):
    meta = {'collection': 'totals'}
    season = IntField()
    name = StringField()
    position = StringField()
    stats = EmbeddedDocumentField(TotalsStats)

class PlayerPerGStats(Document):
    meta = {'collection': 'per_g'}
    season = IntField()
    name = StringField()
    position = StringField()
    stats = EmbeddedDocumentField(PerGStats)

class PlayerPerMStats(Document):
    meta = {'collection': 'per_m'}
    season = IntField()
    name = StringField()
    position = StringField()
    stats = EmbeddedDocumentField(PerMStats)

class PlayerPerPStats(Document):
    meta = {'collection': 'per_p'}
    season = IntField()
    name = StringField()
    position = StringField()
    stats = EmbeddedDocumentField(PerPStats)

class PlayerAdvStats(Document):
    meta = {'collection': 'adv'}
    season = IntField()
    name = StringField()
    position = StringField()
    stats = EmbeddedDocumentField(AdvStats)

class PlayerPbpStats(Document):
    meta = {'collection': 'pbp'}
    season = IntField()
    name = StringField()
    position = StringField()
    stats = EmbeddedDocumentField(PbpStats)

class PlayerShootingStats(Document):
    meta = {'collection': 'shooting'}
    season = IntField()
    name = StringField()
    position = StringField()
    stats = EmbeddedDocumentField(ShootingStats)

class PlayerAdvShootingStats(Document):
    meta = {'collection': 'adv_shooting'}
    season = IntField()
    name = StringField()
    position = StringField()
    stats = EmbeddedDocumentField(AdvShootingStats)