def media_ponderada(nota1,nota2,nota3):
    pesoA = 2
    pesoB = 3
    pesoC = 5
    pesoTotal = pesoA + pesoB + pesoC
    calc_notas = ((nota1 * pesoA) + (nota2 * pesoB) + (nota3 * pesoC)) / pesoTotal
    return calc_notas
    
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

media = media_ponderada(nota1,nota2,nota3)
    
print(f"MEDIA = {media:.1f}")