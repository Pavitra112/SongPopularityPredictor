from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from accounts import views
from SongPopularityPredictor import settings

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_login, name='user_login'),
    path('accounts/', include('accounts.urls')),
    path('predict/', include('predict_popularity.urls')),
]


urlpatterns += staticfiles_urlpatterns()
