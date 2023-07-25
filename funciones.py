def es_bisiesto(a):
    if a % 4 == 0:
        if a % 100 == 0:
            if a % 400 == 0:
                return "Es Bisiesto"
            else:
                return "No es Bisiesto"
        else:
            return "Es Bisiesto"
    else:
        return "No es Bisiesto"
    
print(es_bisiesto(2000))
print(es_bisiesto(2005))
print(es_bisiesto(2024))


