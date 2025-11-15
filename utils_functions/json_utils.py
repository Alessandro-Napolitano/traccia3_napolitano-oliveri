import json as js

def save_json(dict : dict, file_name : str):
    """
    Funzione:
        Salva una lista in formato JSON.

    Parametri:
        data (dict): dati da salvare.
    """
    try:
        with open(file_name, "a", encoding="utf-8") as fout:
            # Serializza il dizionario 'data' in formato JSON e lo scrive sul file.
            # con indent=4 si rende il file più leggibile,
            # infine con ensure_ascii=False i caratteri rimangono in unicode (es. lettere accentate).
            js.dump(dict, fout, indent=4,ensure_ascii=False)
    except Exception as e:
        print("Errore nel salvataggio JSON:", e)
