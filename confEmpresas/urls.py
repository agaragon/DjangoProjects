from django.contrib import admin
from django.urls import path
from calcularConf.views import homeView,verificarCadastrosView,atualizarCadastrosView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',homeView,name='home'),
    path('verificarCadastros/',verificarCadastrosView,name='verificarCadastros'),
    path('atualizarCadastros/',atualizarCadastrosView,name='atualizarCadastros'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)