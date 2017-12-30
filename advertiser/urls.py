from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from advertiser import views
from advertiser.views import RegistrationFormView,AddAdvertisementView,AdvertisersListView,LoginFormView

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'registration/$',RegistrationFormView.as_view(), name='registration'),
    url(r'add-advertisement/$', AddAdvertisementView.as_view()),
    url(r'test/$', AdvertisersListView.as_view()),
    url(r'login/$',LoginFormView.as_view(),name='login')

]
#if settings.DEBUG:
 #   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
