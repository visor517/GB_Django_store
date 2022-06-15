from django.contrib import admin
from django.urls import path, include
from storeapp import urls

import storeapp


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('storeapp.urls'))
]
