from typing import Type, TYPE_CHECKING

from django.contrib.gis.db.models.functions import AsGeoJSON, Centroid
from django.db.models import QuerySet

if TYPE_CHECKING:
    from geo.models import AdminRegion


def all_geogs_in_extent(geog_type: Type['AdminRegion']) -> QuerySet['AdminRegion']:
    return geog_type.objects \
        .annotate(centroid=Centroid('geom')) \
        .filter(in_extent=True)
