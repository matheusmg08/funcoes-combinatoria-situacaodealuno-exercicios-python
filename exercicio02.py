"""
2- Faça um função que informe o status do aluno a partir da sua média de acordo com a tabela a seguir:
- Nota acima de 6 --> Aprovado
- Nota entre 4 e 6 --> Verificação Suplementar
- Nota abaixo de 4 --> Reprovado
Heitor, Cicero e Pratico 
3.2.1 / (1.2.1) = 3
"""
def status_aluno(media):
    if media > 6:
        return "Aprovado"
    elif media >= 4 and media <= 6:
        return "Verificação Suplementar"
    else:
        return "Reprovado"
    
alunos = {"Heitor": 7.8, "Cicero": 4.5, "Pratico": 2.2}
for aluno, media in alunos.items():
    print(f"O aluno {aluno} está com o status: {status_aluno(media)}, com a média: {media}.")
    






