#!/usr/bin/env python3
from django.core.cache import cache
from .models import Property

def get_all_properties():
    """
    Fetch all properties from cache if available, 
    otherwise query DB and cache the result for 1 hour.
    """
    properties = cache.get('all_properties')

    if properties is None:
        properties = list(Property.objects.all())  # Convert to list to make cacheable
        cache.set('all_properties', properties, 3600)  # Cache for 1 hour (3600 seconds)
    
    return properties

