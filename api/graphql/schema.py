import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from rapidfuzz import process
from unidecode import unidecode
from ..models import TotalsStats as TotalsStatsModel
from ..models import PerGStats as PerGStatsModel
from ..models import PlayerTotalsStats as PlayerTotalsStatsModel
from ..models import PlayerPerGStats as PlayerPerGStatsModel
from ..models import PlayerPerMStats as PlayerPerMStatsModel
from ..models import PlayerPerPStats as PlayerPerPStatsModel
from ..models import PlayerAdvStats as PlayerAdvStatsModel
from ..models import PlayerPbpStats as PlayerPbpStatsModel
from ..models import PlayerShootingStats as PlayerShootingStatsModel
from ..models import PlayerAdvShootingStats as PlayerAdvShootingStatsModel

class TotalStats(MongoengineObjectType):
    class Meta:
        model = TotalsStatsModel
        interfaces = (Node,)

class PerGStats(MongoengineObjectType):
    class Meta:
        model = PerGStatsModel
        interfaces = (Node,)

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
        model = PlayerPbpStatsModel
        interfaces = (Node,)

class PlayerShootingStats(MongoengineObjectType):
    class Meta:
        model = PlayerShootingStatsModel
        interfaces = (Node,)

class PlayerAdvShootingStats(MongoengineObjectType):
    class Meta:
        model = PlayerAdvShootingStatsModel
        interfaces = (Node,)

def extract_name_filter(**kwargs):
    name_filter = kwargs.pop('name', None)

    return name_filter, kwargs

def fuzzy_name_matching(documents, name_filter):
    # matched_names will be a tuple results from fuzzy matching (matched_string, score, index)
    matched_names = process.extract(unidecode(name_filter.lower()), [unidecode(result.name.lower()) for result in documents], score_cutoff=75, limit=None)
    
    return matched_names

class Query(graphene.ObjectType):
    node = Node.Field()
    all_totals = MongoengineConnectionField(PlayerTotalsStats)
    def resolve_all_totals(self, info, **kwargs):
        name_filter, kwargs = extract_name_filter(**kwargs)
        totals_query = PlayerTotalsStatsModel.objects.filter(**kwargs)
        if name_filter:
            matched_names = fuzzy_name_matching(list(totals_query), name_filter)
            return [totals_query[result[2]] for result in matched_names]
        
        return totals_query

    all_per_g = MongoengineConnectionField(PlayerPerGStats)
    def resolve_all_per_g(self, info, **kwargs):
        name_filter, kwargs = extract_name_filter(**kwargs)
        per_g_query = PlayerPerGStatsModel.objects.filter(**kwargs)
        if name_filter:
            matched_names = fuzzy_name_matching(list(per_g_query), name_filter)
            return [per_g_query[result[2]] for result in matched_names]
        
        return per_g_query

    all_per_m = MongoengineConnectionField(PlayerPerMStats)
    def resolve_all_per_m(self, info, **kwargs):
        name_filter, kwargs = extract_name_filter(**kwargs)
        per_m_query = PlayerPerMStatsModel.objects.filter(**kwargs)
        if name_filter:
            matched_names = fuzzy_name_matching(list(per_m_query), name_filter)
            return [per_m_query[result[2]] for result in matched_names]
        
        return per_m_query
    
    all_per_p = MongoengineConnectionField(PlayerPerPStats)
    def resolve_all_per_p(self, info, **kwargs):
        name_filter, kwargs = extract_name_filter(**kwargs)
        per_p_query = PlayerPerPStatsModel.objects.filter(**kwargs)
        if name_filter:
            matched_names = fuzzy_name_matching(list(per_p_query), name_filter)
            return [per_p_query[result[2]] for result in matched_names]
        
        return per_p_query
    
    all_adv = MongoengineConnectionField(PlayerAdvStats)
    def resolve_all_adv(self, info, **kwargs):
        name_filter, kwargs = extract_name_filter(**kwargs)
        adv_query = PlayerAdvStatsModel.objects.filter(**kwargs)
        if name_filter:
            matched_names = fuzzy_name_matching(list(adv_query), name_filter)
            return [adv_query[result[2]] for result in matched_names]
        
        return adv_query

    all_pbp = MongoengineConnectionField(PlayerPBPStats)
    def resolve_all_pbp(self, info, **kwargs):
        name_filter, kwargs = extract_name_filter(**kwargs)
        pbp_query = PlayerPbpStatsModel.objects.filter(**kwargs)
        if name_filter:
            matched_names = fuzzy_name_matching(list(pbp_query), name_filter)
            return [pbp_query[result[2]] for result in matched_names]
        
        return pbp_query
    
    all_shooting = MongoengineConnectionField(PlayerShootingStats)
    def resolve_all_shooting(self, info, **kwargs):
        name_filter, kwargs = extract_name_filter(**kwargs)
        shooting_query = PlayerShootingStatsModel.objects.filter(**kwargs)
        if name_filter:
            matched_names = fuzzy_name_matching(list(shooting_query), name_filter)
            return [shooting_query[result[2]] for result in matched_names]
        
        return shooting_query
    
    all_adv_shooting = MongoengineConnectionField(PlayerAdvShootingStats)
    def resolve_all_adv_shooting(self, info, **kwargs):
        name_filter, kwargs = extract_name_filter(**kwargs)
        adv_shooting_query = PlayerAdvShootingStatsModel.objects.filter(**kwargs)
        if name_filter:
            matched_names = fuzzy_name_matching(list(adv_shooting_query), name_filter)
            return [adv_shooting_query[result[2]] for result in matched_names]
        
        return adv_shooting_query

schema = graphene.Schema(query=Query, types=[PlayerTotalsStats, PlayerPerGStats, PlayerPerMStats, PlayerPerPStats, PlayerAdvStats, PlayerPBPStats, PlayerShootingStats, PlayerAdvShootingStats])