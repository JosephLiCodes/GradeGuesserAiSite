from django import urls
from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings
urlpatterns = [
    
    path("test",views.test, name = "test"),
    path("<int:id>", views.index, name = "index"),
     #looks for int, and passes it into index
    #path("<int:id>", views.intTest, name = "id"),
    path("",views.home, name = "home"),
    path("create/", views.create, name = "create"),
    path("predict/", views.predict, name = "predict"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
