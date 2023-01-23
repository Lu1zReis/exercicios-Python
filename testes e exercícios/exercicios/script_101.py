def voto(anoNasc):
    import datetime
    ano = datetime.date.today().year - anoNasc
    if ano < 16:
        return f"Com {ano} anos: voto NEGADO"
    elif ano > 65:
        return f"Com {ano} anos: voto OPCIONAL"
    else:
        if ano >= 16 and ano < 18:
            return f"Com {ano} anos: voto OPCIONAL"
        elif ano >= 18:
            return f"Com {ano} anos: voto OBRIGATÓRIO"

ano = int(input('Digite sua data de nascimento: '))
print(voto(ano))
