import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from rapidfuzz import process
from unidecode import unidecode
from ..models import TotalsStatsModel, PerGStatsModel, PerMStatsModel, PerPStatsModel, AdvStatsModel

class PlayerTotalsStats(MongoengineObjectType):
    class Meta:
        model = TotalsStatsModel
        interfaces = (Node,)

class PlayerPerGStats(MongoengineObjectType):
    class Meta:
        model = PerGStatsModel
        interfaces = (Node,)

class PlayerPerMStats(MongoengineObjectType):
    class Meta:
        model = PerMStatsModel
        interfaces = (Node,)

class PlayerPerPStats(MongoengineObjectType):
    class Meta:
        model = PerPStatsModel
        interfaces = (Node,)

class PlayerAdvStats(MongoengineObjectType):
    class Meta:
        model = AdvStatsModel
        interfaces = (Node,)

def extract_name_filter(**kwargs):
    name_filter = kwargs.pop('name_display', None)

    return name_filter, kwargs
    
def fuzzy_name_matching(documents, name_filter):
    # matched_names will be a tuple results from fuzzy matching (matched_string, score, index)
    matched_names = process.extract(unidecode(name_filter.lower()), [unidecode(result['name_display'].lower()) for result in documents], score_cutoff=75, limit=None)
    
    return matched_names

class Query(graphene.ObjectType):
    node = Node.Field()
    all_totals = MongoengineConnectionField(PlayerTotalsStats)
    def resolve_all_totals(self, _, **kwargs):
        print(kwargs)
        name_filter, kwargs = extract_name_filter(**kwargs)
        totals_query = TotalsStatsModel.objects.filter(**kwargs)
        if name_filter:
            matched_names = fuzzy_name_matching(list(totals_query), name_filter)
            return [totals_query[result[2]] for result in matched_names]
        
        return totals_query

    all_per_g = MongoengineConnectionField(PlayerPerGStats)
    def resolve_all_per_g(self, _, **kwargs):
        name_filter, kwargs = extract_name_filter(**kwargs)
        per_g_query = PlayerPerGStats.objects.filter(**kwargs)
        if name_filter:
            matched_names = fuzzy_name_matching(list(per_g_query), name_filter)
            return [per_g_query[result[2]] for result in matched_names]
        
        return per_g_query

    all_per_m = MongoengineConnectionField(PlayerPerMStats)
    def resolve_all_per_m(self, _, **kwargs):
        name_filter, kwargs = extract_name_filter(**kwargs)
        per_m_query = PlayerPerMStats.objects.filter(**kwargs)
        if name_filter:
            matched_names = fuzzy_name_matching(list(per_m_query), name_filter)
            return [per_m_query[result[2]] for result in matched_names]
        
        return per_m_query
    
    all_per_p = MongoengineConnectionField(PlayerPerPStats)
    def resolve_all_per_p(self, _, **kwargs):
        name_filter, kwargs = extract_name_filter(**kwargs)
        per_p_query = PlayerPerPStats.objects.filter(**kwargs)
        if name_filter:
            matched_names = fuzzy_name_matching(list(per_p_query), name_filter)
            return [per_p_query[result[2]] for result in matched_names]
        
        return per_p_query
    
    all_adv = MongoengineConnectionField(PlayerAdvStats)
    def resolve_all_adv(self, _, **kwargs):
        name_filter, kwargs = extract_name_filter(**kwargs)
        adv_query = PlayerAdvStats.objects.filter(**kwargs)
        if name_filter:
            matched_names = fuzzy_name_matching(list(adv_query), name_filter)
            return [adv_query[result[2]] for result in matched_names]
        
        return adv_query

schema = graphene.Schema(query=Query, types=[PlayerTotalsStats, PlayerPerGStats, PlayerPerMStats, PlayerPerPStats, PlayerAdvStats])