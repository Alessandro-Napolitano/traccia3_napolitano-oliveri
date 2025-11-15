#authors: Alessandro Napolitano, Erika Oliveri
"""
    Estrae la lista degli eventi distinti presenti nei log.

    Parametri:
        logs (list[list]): lista di log; ogni log è una lista,
        dove l'elemento in posizione 4 rappresenta
        il nome dell'evento.

    Ritorno:
        list: lista degli eventi distinti, nell'ordine con cui compaiono
        per la prima volta nella lista di log.
"""
def events_utils(logs : list[list]):
    events_list = []
    for l in logs:
        if l[4] not in events_list:
            events_list.append(l[4])
    return events_list

"""
    Calcola il numero di occorrenze di ciascun evento presente nei log.

    Parametri:
        logs (list[list]): lista di log; ogni log è una lista, 
        dove l'elemento in posizione 4 rappresenta
        il nome dell'evento.

    Ritorno:
        dict: dizionario che associa a ogni evento (chiave) il numero di
        volte in cui esso compare nei log (valore intero).
"""
def events_utils_and_count(logs : list[list]):
    diz_events = {}

    for l in logs:
        evento = l[4]
        diz_events[evento] = diz_events.get(evento, 0) + 1

    return diz_events