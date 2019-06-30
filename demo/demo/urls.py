from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    # Incluindo as URLs do app website
    path('website/', include('website.urls', namespace='website')),
    # Incluindo URLs para login com Facebook
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name='login.html')),
    # Interface administrativa
    path('admin/', admin.site.urls),
]
