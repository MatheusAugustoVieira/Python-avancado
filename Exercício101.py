def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano

    # Se a idade for menor que 16 Não vota
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'

    # Senão se idade for menor ou igual a 16 menor que 18, ou a cima de 65 o voto é opcional
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


# Programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))