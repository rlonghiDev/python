# DESAFIO-RELAMPAGO: INCREMENTE O CODIGO ABAIXO PARA AVALIAR MAIS UM CRITERIO DE DESEMPATE, CASO O NUMERO
# DE VITORIAS TAMBEM SEJA IGUAL , ELE DEVERÁ AVALIAR O SALDO DE GOLS

time1 = "Paissandu"
time2 = "Juventus"

pontuacao_time1 = 100
pontuacao_time2 = 100

vitorias_time1 = 50
vitorias_time2 = 50

saldo_gols_time1 = 57
saldo_gols_time2 = 56

# 1- vou checar se as pontuacoes sao diferentes:
if(pontuacao_time1 != pontuacao_time2):
    if(pontuacao_time1 > pontuacao_time2):
        print(f"{time1} é o campeão")
        exit(0)
    else:
        print(f"{time2} é o campeão")
        exit(0)

if(vitorias_time1 != vitorias_time2):
    if(vitorias_time1 > vitorias_time2):
        print(f"{time1} é o campeão por numero de vitorias")
        exit(0)
    else:
        print(f"{time2} é o campeão por numero de vitorias")
        exit(0)
else:
    if(saldo_gols_time1 > saldo_gols_time1):
        print(f"{time1} é o campeão por saldo de gols")
        
    else:
        print(f"{time2} é o campeão por saldo de gols")