from django.urls import path, re_path
from .views import index, categories, archive

urlpatterns = [
    path('', index, name='home'),
    path("cats/<slug:cat>/", categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]