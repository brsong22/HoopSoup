from mongoengine import Document
from mongoengine.fields import (
    DictField, IntField, StringField,
)

class PlayerTotalsStats(Document):
    meta = {'collection': 'totals'}
    season = IntField()
    name = StringField()
    position = StringField()
    stats = DictField()

class PlayerPerGStats(Document):
    meta = {'collection': 'per_g'}
    season = IntField()
    name = StringField()
    position = StringField()
    stats = DictField()

class PlayerPerMStats(Document):
    meta = {'collection': 'per_m'}
    season = IntField()
    name = StringField()
    position = StringField()
    stats = DictField()

class PlayerPerPStats(Document):
    meta = {'collection': 'per_p'}
    season = IntField()
    name = StringField()
    position = StringField()
    stats = DictField()

class PlayerAdvStats(Document):
    meta = {'collection': 'adv'}
    season = IntField()
    name = StringField()
    position = StringField()
    stats = DictField()

class PlayerPBPStats(Document):
    meta = {'collection': 'pbp'}
    season = IntField()
    name = StringField()
    position = StringField()
    stats = DictField()

class PlayerShootingStats(Document):
    meta = {'collection': 'shooting'}
    season = IntField()
    name = StringField()
    position = StringField()
    stats = DictField()

class PlayerAdvShootingStats(Document):
    meta = {'collection': 'adv_shooting'}
    season = IntField()
    name = StringField()
    position = StringField()
    stats = DictField()