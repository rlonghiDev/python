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
    elif month == 12:
        month_days = 31


    return(month_days)

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fracassado")
