#authors: Alessandro Napolitano, Erika Oliveri
"""
    Restituisce la lista degli utenti distinti presenti nei log.

    Parametri:
        logs (list[list]): lista di log; ogni log è una lista,
        dove l'elemento in posizione 1 rappresenta
        il nome dell'utente.

    Ritorno:
        list: lista degli utenti distinti
"""
def user_utils(logs: list[list] ):
    lista_utenti = []
    for lista in logs:
        if lista[1] not in lista_utenti:
            lista_utenti.append(lista[1])
    return lista_utenti

