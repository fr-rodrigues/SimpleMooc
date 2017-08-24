from django.conf.urls import url
from django.contrib.auth import views as views_auth
from simplemooc.accounts import views as views_accounts


urlpatterns = [
    url(r'^$', views_accounts.dashboard, name='dashboard'),
    url(r'^entrar/$', views_auth.login,
        {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^sair/$', views_auth.logout,
        {'next_page': 'core:home'}, name='logout'),
    url(r'^cadastre-se/$', views_accounts.register, name='register'),
    url(r'^editar/$', views_accounts.edit, name='edit'),
    url(r'^nova-senha/$', views_accounts.password_reset,
        name='password_reset'),
    url(r'^Confirmar-nova-senha/(?P<key>\w+)/$',
        views_accounts.password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^editar-senha/$', views_accounts.edit_password,
        name='edit_password'),
]
