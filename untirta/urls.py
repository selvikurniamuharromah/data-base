from operator import index
from django.contrib import admin
from django.urls import path
from fkip.views import index
from faperta.views import index
from feb.views import index
from fh.views import index
from fisip.views import index
from fk.views import index
from ft.views import index
from pascasarjana.views import index
from profil.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fkip/', index),
    path('faperta/', index),
    path('feb/', index),
    path('fh/', index),
    path('fisip/', index),
    path('fk/', index),
    path('ft/', index),
    path('pascasarjana/', index),
    path('profil/', index),
]
