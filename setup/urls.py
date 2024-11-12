from django.contrib import admin
from django.urls import path, include
from escola.views import EstudanteViewSet, CursoViewSet
from rest_framework import routers

# Define a inicialização da routa, https://www.django-rest-framework.org/api-guide/routers/
router = routers.DefaultRouter() 

# Registra uma nova rota identificada pelo 'estudante', usa como paramentro de visualização o viewset definido anteriormente e nomeia como Estudantes
router.register('estudante', EstudanteViewSet, basename='Estudantes') 
router.register('curso', CursoViewSet, basename='Cursos')

# Define as urls para acesso das rotas, o '' vázio determina o acesso primario, ou seja, a home da aplicação
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
