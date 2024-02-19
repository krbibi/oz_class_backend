from django.contrib import admin
from django.urls import path,include

from bookmark import views as bookmark_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookmark/',
         bookmark_views.bookmark_list,
         name='bookmark_list'),

    path("api/v1/feeds/", include("feeds.urls")),
    path("api/v1/users/",include("users.urls")),
    path("api/v1/reviews/", include("reviews.urls")),
]