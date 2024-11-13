from django.db import models

class Estudante(models.Model):
    nome = models.CharField(max_length = 100)
    email = models.EmailField(blank = False)
    cpf = models.CharField(max_length = 11)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length = 14)

    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )
    codigo = models.CharField(max_length = 10) # max_legth define o tamanho maximo do campo
    descricao = models.CharField(max_length = 100, blank = False) # blank define que o campo não pode ficar em branco
    nivel = models.CharField(max_length = 1, choices = NIVEL, blank=False, null=False, default = 'B') # null define que não pode ser nulo o campo e o choices gere uma escolha entre as opções presentes na tupla definida com NIVEL

    def __str__(self):
        return self.codigo
    
class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    )
    estudante = models.ForeignKey(Estudante, on_delete = models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE)
    periodo = models.CharField(max_length = 1, choices = PERIODO, blank=False, null=False, default = 'M')
