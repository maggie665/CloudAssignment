
from django.urls import path

from InventorySystem import views
from InventorySystem.views import index


urlpatterns = [
    #path("", index, name="home"),
    path("", views.index),

    ]