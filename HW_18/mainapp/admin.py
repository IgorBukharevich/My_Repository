from django.contrib import admin
from .models import Category
from .models import Actor
from .models import Genre
from .models import Movie
from .models import MovieShots
from .models import RatingStar
from .models import Rating
from .models import Reviews
from .models import TimeShow
from .models import RegistrationVisitors
from .models import HallPlace


admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)
admin.site.register(TimeShow)
admin.site.register(RegistrationVisitors)
admin.site.register(HallPlace)
