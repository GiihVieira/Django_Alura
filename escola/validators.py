import re
from validate_docbr import CPF

def cpf_invalido(num_cpf):
    cpf = CPF()
    cpf_valido = cpf.validate(num_cpf)
    return not cpf_valido

def nome_invalido(nome):
    return not nome.isalpha()

def celular_invalido(celular):
    # Modelo de celular 99 99999-9999
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}' # [0-9] define o intervalo do números, {2} define quantas vezes esses números se repetem.
    result = re.findall(modelo, celular) # método re (REGEX) do python possibilita operações com expressões regulares
    return not result
