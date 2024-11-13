from django.contrib import admin
from django.urls import path, include
from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculaEstudante, ListarMatriculaCurso
from rest_framework import routers

# Define a inicialização da routa, https://www.django-rest-framework.org/api-guide/routers/
router = routers.DefaultRouter() 

# Registra uma nova rota identificada pelo 'estudante', usa como paramentro de visualização o viewset definido anteriormente e nomeia como Estudantes
router.register('estudantes', EstudanteViewSet, basename='Estudantes') 
router.register('curso', CursoViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matrículas')

# Define as urls para acesso das rotas, o '' vázio determina o acesso primario, ou seja, a home da aplicação.
# as_view() determina que aquele acesso é somente de leitura
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas/', ListaMatriculaEstudante.as_view()),
    path('cursos/<int:pk>/matriculas/', ListarMatriculaCurso.as_view()),
]
