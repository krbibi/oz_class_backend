from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path("", views.Users.as_view()), # api/v1/users
    path("myinfo", views.MyInfo.as_view()), # api/v1/users

    #Authentication
    path("getToken",obtain_auth_token), # DRF token
    path("login", views.Login.as_view()),    #Django Session login
    path("logout", views.Logout.as_view()),    #Django Session login
    #JWT Authentication
    path("login/jwt",views.JWTLogin.as_view()), 
    path("login/jwt/info",views.UserDetailView.as_view()), 

    #Simple JWT Authentication 
    path("login/simpleJWT", TokenObtainPairView.as_view()),
    path("login/simpleJWT/refresh", TokenRefreshView.as_view()),
    path("login/simpleJWT/verify", TokenVerifyView.as_view()),
]

# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwOTYxNjc0NSwiaWF0IjoxNzA4NDA3MTQ1LCJqdGkiOiJlZjEwZjM4MGYyNWE0NGEwYjcwOTcwYjZlOTBhYzE3YiIsInVzZXJfaWQiOjR9.LrnE3fTitPpRRHgFAazoxEAcsofPXVyaeUT1_NRp1xg",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA4NDEwNzQ1LCJpYXQiOjE3MDg0MDcxNDUsImp0aSI6IjViMmJjZWVkYTRhMTQwMTdhZjAzYTk2OGJlOGU0YjU5IiwidXNlcl9pZCI6NH0._Xgu9bm3QnY_E2cX-BI_0UgBfK-WDHrufkHmcscBidQ"
# }