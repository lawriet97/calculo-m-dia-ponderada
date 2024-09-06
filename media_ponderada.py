def media_ponderada(nota_a, nota_b):
    peso1 = 3.5
    peso2 = 7.5
    total_pesos = peso1 + peso2
    calc_media1 = ((nota_a * peso1) + (nota_b * peso2)) / total_pesos
    
    return calc_media1
    
nota_a = float(input())
nota_b = float(input())

media = media_ponderada(nota_a, nota_b)

print(f"MEDIA = {media:.5f}")