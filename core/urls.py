from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from contas.views import CustomLoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('consultar.urls')),
    path('', include('arquivos.urls')),
    
    path('contas/', include('contas.urls')),

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
