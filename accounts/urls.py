from django.urls import path
from .views import sing_up,activate_code,activated

app_name='accounts'


urlpatterns = [
        path('signup/', sing_up, name='signup'),
        path('activated/', activated, name='activated'),
        path('<str:username>/activate', activate_code, name='activate'),

]
