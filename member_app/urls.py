from django.urls import path
from .views.list_view import list_media
from .views.log_view import MemberLoginView, MemberLogoutView

urlpatterns = [
    path('medias/', list_media, name='list_media'),
    path('login/', MemberLoginView.as_view(), name='login'),
    path('logout/', MemberLogoutView.as_view(), name='logout')
]
