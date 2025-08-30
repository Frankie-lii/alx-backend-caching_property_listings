#!/usr/bin/env python3
from django.core.cache import cache
from django_redis import get_redis_connection
from .models import Property
import logging

logger = logging.getLogger(__name__)

def get_all_properties():
    """
    Fetch all properties from cache if available,
    otherwise query DB and cache the result for 1 hour.
    """
    properties = cache.get('all_properties')

    if properties is None:
        properties = list(Property.objects.all())
        cache.set('all_properties', properties, 3600)
    
    return properties

def get_redis_cache_metrics():
    """
    Fetch Redis cache hit/miss statistics and calculate hit ratio.
    """
    conn = get_redis_connection("default")
    info = conn.info()

    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    total = hits + misses

    hit_ratio = (hits / total) if total > 0 else 0

    metrics = {
        "hits": hits,
        "misses": misses,
        "hit_ratio": round(hit_ratio, 2)
    }

    logger.info(f"Redis Cache Metrics: {metrics}")
    return metrics

