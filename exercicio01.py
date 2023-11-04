"""
1- O professor deseja dividir uma turma com N alunos em dois grupos: um com M alunos e outro com (N-M) alunos. Faça o programa que lê o valor de N e M e informa o número de combinações possíveis 
-Número de combinações é igual a N!/(M! * (N-M)!)
-Use funções para evitar repetição de código
"""
import math
def combinacao(n,m):
    fatorialn = math.factorial(n)
    fatorialm = math.factorial(m)
    sub = (n-m)
    fatorialsub = math.factorial(sub)
    n_combinacoes = fatorialn/(fatorialm * (fatorialsub))
    return n_combinacoes

n = int(input("Digite a quantidade de alunos da turma: "))
m = int(input("Digite a quantidade de alunos do primeiro grupo: "))
combinacoes = combinacao(n,m)
print (f"O número de combinações possíveis é: {combinacoes}")



      