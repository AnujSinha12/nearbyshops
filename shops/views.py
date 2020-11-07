from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Shop


longitude = -80.191_788
latitude = 25.761_681


user_location = Point(longitude, latitude, srid=4326)


class Home(generic.ListView):
    print('__entered shops/views/Home___')
    ##overriding variables
    model = Shop
    context_object_name = "shops"

    ##getting point objects(6) which are near to user's location
    queryset = Shop.objects.annotate(distance=Distance("location", user_location)).order_by("distance")[0:6]

    ##template for url- ''
    template_name = "shops/index.html"

home = Home.as_view()
