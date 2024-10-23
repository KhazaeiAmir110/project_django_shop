"""
URL configuration for djshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

doc_patterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

admin_urls = [
    path('api/admin/catalog/', include(('apps.catalog.urls.admin', 'apps.admin'), namespace='catalog-admin')),
]

front_urls = [
    path('api/front/catalog/', include(('apps.catalog.urls.front', 'apps.admin'), namespace='catalog-front')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += admin_urls + front_urls + doc_patterns

# Admin Site
admin.sites.AdminSite.site_header = "Djshop"
admin.sites.AdminSite.site_title = "Djshop"
admin.sites.AdminSite.index_title = "Djshop"
