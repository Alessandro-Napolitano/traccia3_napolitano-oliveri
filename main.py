import argparse as ap
import json as js
from utils_functions import json_utils as ju, events_utils as eu, users_utils as ut


#authors: Alessandro Napolitano, Erika Oliveri
def main():
    # Parser degli argomenti
    parser = ap.ArgumentParser(description='Processa un file di log JSON.')
    parser.add_argument('-f', '--file', required=True, help='Inserisci il percorso del file JSON da processare.')

    # Estrazione dei parametri
    args = parser.parse_args()
    file_path = args.file

    """
    Viene letto il file JSON e inoltre vengono anche catturate e gestite
    le eccezioni quali :
    1. FileNotFoundException se il file non viene trovato.
    2. JSONDecodeError se il file non contiene un JSON valido.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as fin:
            logs = js.load(fin)
    except FileNotFoundError:
        print(f"Errore: il file '{file_path}' non esiste.")
        return
    except js.JSONDecodeError:
        print("Errore: il file non contiene un JSON valido.")
        return

    # Chiamata della funzione che estrae gli utenti diversi dal file di log
    user_list = ut.user_utils(logs)

    # Chiamata della funzione che estrae gli eventi diversi dal file di log
    event_list = eu.events_utils(logs)

    # Creazione del dizionario che contiene solo le liste degli utenti e degli eventi senza occorrenze
    users_events = {
        "users" : user_list,
        "events" : event_list
    }

    # Chiamata della funzione che calcola il numero di occorrenze di ciascun evento presente nei log.
    event_count = eu.events_utils_and_count(logs)

    # Chiama la funzione che crea il file di uscita degli utenti e degli eventi senza occorrenze
    ju.save_json(users_events, "/Users/alessandronapolitano/Downloads/esercitazione/test_data/risUserEvents.json")
    ju.save_json(event_count, "/Users/alessandronapolitano/Downloads/esercitazione/test_data/risEventCount.json")

# Viene eseguito il main
if __name__ == "__main__":
    main()