from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from advertiser import views
from advertiser.views import RegistrationFormView,DashboardView,AddAdvertisementView,AdvertisersListView,LoginFormView, ContactView,FormsView,ChartsView,HomeView

app_name = 'advertiser'

urlpatterns = [
    url(r'dashboard/$', DashboardView.as_view(), name='dashboard'),
    url(r'registration/$',RegistrationFormView.as_view(), name='registration'),
    url(r'add-advertisement/$', AddAdvertisementView.as_view()),
    url(r'test/$', AdvertisersListView.as_view()),
    url(r'login/$',LoginFormView.as_view(),name='login'),
    url(r'forms/$', FormsView.as_view(), name='forms'),
url(r'charts/$', ChartsView.as_view(), name='charts'),
url(r'contact/$', ContactView.as_view(), name='contact'),
url(r'^$', HomeView.as_view(), name='home'),


]
#if settings.DEBUG:
 #   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
