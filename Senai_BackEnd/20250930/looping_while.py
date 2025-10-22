venda = [250,330,440,540,350,250,368,40,250,30,30,]

vendedores =['maria','mara','joão','silva','santos','mario','carlos','marly','xuxa','chica','zinha']

meta = 50


i= 0

while len(venda) > i:
    
    if venda[i] > meta:
        print('{} atingiu a meta de vendas: {}'.format(vendedores[i], venda[i]))
    
    i += 1
