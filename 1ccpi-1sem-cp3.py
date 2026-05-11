temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]

i = 1
maior_rc = 0                # maior_rc = Maior Registro Crítico
sala_maior_risco = 0        # Sala com Maior Risco

for item in temperaturas:
    rc = 0                  # rc = Registro Crítico

    for temp in item:
        if temp >= 33:
            rc += 1

        temp_media_total = sum(item) / 4

    print(f"Sala: {i}\nTemperatura Média: {temp_media_total}\nRegistros Críticos: {rc}\n")

    if rc > maior_rc:
        maior_rc = rc
        sala_maior_risco = i

    i += 1

print(f"\nA sala com maior risco: Sala {sala_maior_risco}.")