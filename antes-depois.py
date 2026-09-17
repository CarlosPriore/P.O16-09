aluno1_nome = "Fulano"
aluno1_idade = 20
aluno1_notas = [5, 7, 9]


aluno2_nome = "Ciclano"
aluno2_idade = 22
aluno2_notas = [6, 8, 10]

def calcular_media(notas:list[float]) -> float:
    return sum(notas) / len(notas) if notas else 0.0

aluno1_media = calcular_media(aluno1_notas)
aluno2_media = calcular_media(aluno2_notas)