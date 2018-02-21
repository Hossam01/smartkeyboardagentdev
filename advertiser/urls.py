from django.conf.urls import url

from advertiser.views import RegistrationFormView, DashboardView, AdvertisementFormView, AdvertisersListView, \
    LoginFormView, ContactView, HomeView, Student, ChartsView

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



]
#if settings.DEBUG:
 #   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
