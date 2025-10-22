def is_year_leap(year):
    test_four = year % 4
    test_hundred = year % 100
    test_4Hundred = year % 400
    
    if test_hundred == 0 and test_4Hundred == 0:
        return True
    
    elif test_hundred != 0 and test_four == 0:
        return True
    
    else:    
        return False

def days_in_month(year, month):
    
    leap_year = is_year_leap(year)
    month_days = 0

    if month == 1:
        month_days = 31
    
    elif month == 2:
        if leap_year == True:
            month_days = 29
        else:
            month_days = 28

    elif month == 3:
        month_days = 31
    
    elif month == 4:
        month_days = 30
    
    elif month == 5:
        month_days = 31
    
    elif month == 6:
        month_days = 30

    elif month == 7:
        month_days = 31

    elif month == 8:
        month_days = 31

    elif month == 9:
        month_days = 30

    elif month == 10:
        month_days = 31

    elif month == 11:
        month_days = 30

    else:
        month_days = 31
        
    return(month_days)

def day_of_year(year, month, day):
    #Calcula os dias corridos dentro do ano em que a data foi indicada.
    
    # contabiliza quantos dias "avulsos" no mês de estudo contados à partir do dia 01
    resto_de_dias = day
    
    #Contabiliza dias de meses completos
    # mes = month - 1 #Quandidade de looping a realizar para chegar no total de meses cheios
    mes_inicio = 1 #Começa "pegando" dias de janeiro
    dias_meses_cheios = 0
    
    while month > mes_inicio:
        dias_meses_cheios += days_in_month(year,mes_inicio)
        mes_inicio += 1
    
    total_de_dias = dias_meses_cheios + resto_de_dias

    return total_de_dias



print(day_of_year(2000, 12, 31))