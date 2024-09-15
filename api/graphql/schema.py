import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from ..models import PlayerTotalsStats as PlayerTotalsStatsModel
from ..models import PlayerPerGStats as PlayerPerGStatsModel
from ..models import PlayerPerMStats as PlayerPerMStatsModel
from ..models import PlayerPerPStats as PlayerPerPStatsModel
from ..models import PlayerAdvStats as PlayerAdvStatsModel
from ..models import PlayerPBPStats as PlayerPBPStatsModel
from ..models import PlayerShootingStats as PlayerShootingStatsModel
from ..models import PlayerAdvShootingStats as PlayerAdvShootingStatsModel

class PlayerTotalsStats(MongoengineObjectType):

    class Meta:
        model = PlayerTotalsStatsModel
        interfaces = (Node,)

class PlayerPerGStats(MongoengineObjectType):

    class Meta:
        model = PlayerPerGStatsModel
        interfaces = (Node,)

class PlayerPerMStats(MongoengineObjectType):

    class Meta:
        model = PlayerPerMStatsModel
        interfaces = (Node,)

class PlayerPerPStats(MongoengineObjectType):

    class Meta:
        model = PlayerPerPStatsModel
        interfaces = (Node,)

class PlayerAdvStats(MongoengineObjectType):

    class Meta:
        model = PlayerAdvStatsModel
        interfaces = (Node,)

class PlayerPBPStats(MongoengineObjectType):

    class Meta:
        model = PlayerPBPStatsModel
        interfaces = (Node,)

class PlayerShootingStats(MongoengineObjectType):

    class Meta:
        model = PlayerShootingStatsModel
        interfaces = (Node,)

class PlayerAdvShootingStats(MongoengineObjectType):

    class Meta:
        model = PlayerAdvShootingStatsModel
        interfaces = (Node,)

class Query(graphene.ObjectType):
    node = Node.Field()
    all_totals = MongoengineConnectionField(PlayerTotalsStats)
    all_per_g = MongoengineConnectionField(PlayerPerGStats)
    all_per_m = MongoengineConnectionField(PlayerPerMStats)
    all_per_p = MongoengineConnectionField(PlayerPerPStats)
    all_adv = MongoengineConnectionField(PlayerAdvStats)
    all_pbp = MongoengineConnectionField(PlayerPBPStats)
    all_shooting = MongoengineConnectionField(PlayerShootingStats)
    all_adv_shooting = MongoengineConnectionField(PlayerAdvShootingStats)

schema = graphene.Schema(query=Query, types=[PlayerTotalsStats, PlayerPerGStats, PlayerPerMStats, PlayerPerPStats, PlayerAdvStats, PlayerPBPStats, PlayerShootingStats, PlayerAdvShootingStats])