from django.conf.urls import url

from advertiser.views import RegistrationFormView, DashboardView, AdvertisementFormView, AdvertisersListView, \
    LoginFormView, ContactView, HomeView, Student, ChartsView, ResetFormView,advertisement,delete,ChangepasswordFormView,UpdateFormView
from django.contrib.auth import views as auth_views


app_name = 'advertiser'

urlpatterns = [
    url(r'dashboard/$', DashboardView.as_view(), name='dashboard'),
    url(r'registration/$',RegistrationFormView.as_view(), name='registration'),
    # url(r'add-advertisement/$', AdvertisementFormView.as_view()),
    url(r'test/$', AdvertisersListView.as_view()),
    url(r'login/$',LoginFormView.as_view(),name='login'),
    url(r'forms/$', AdvertisementFormView.as_view(), name='forms'),
    # url(r'charts/$', ChartsView.as_view(), name='charts'),
    url(r'charts/$', ChartsView.as_view(), name='charts'),
    url(r'contact/$', ContactView.as_view(), name='contact'),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'email/$', ResetFormView.as_view(), name='email'),
    url(r'Advertisements/$', advertisement, name='Advertisements'),
    url(r'Advertisements/(?P<part_id>[0-9]+)/$', delete, name='delete'),
    url(r'Changepassword/$', ChangepasswordFormView.as_view(), name='Changepassword'),
    url(r'update/(?P<part_id>[0-9]+)/$', UpdateFormView.as_view(), name='update'),

]
#if settings.DEBUG:
 #   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
