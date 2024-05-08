from django.urls import path
from .views import HomePage, AboutPage # we import our views in the app dir into the apps urls file,


urlpatterns=[
    path('', HomePage.as_view(), name='home'), # we specify the routing.
    path('about/', AboutPage.as_view(), name='about'), # we specify the routing.
]