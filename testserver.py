from classi.send_receve_sock import *
import socket
import json

HOST = "127.0.0.1"  # IP del server
PORT = 65432  # Porta di comunicazione

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Attendo connessione")
    conn, addr = s.accept()
    sr = SRS(conn)
    
    # Verifica messaggio di controllo dal client
    if sr.ricevi() == "CI SEI?":
        sr.invia("SI")  # Conferma al client
        
        # Ricevi il contenuto JSON come una singola stringa
        contenuto_json_stringa = sr.ricevi()
        
        if contenuto_json_stringa:
            # Conversione della stringa ricevuta in un oggetto JSON
            try:
                contenuto_json = json.loads(contenuto_json_stringa)
                with open("FileSalvataggio.json", "w") as file:
                    # Salvataggio del contenuto JSON in un nuovo file
                    json.dump(contenuto_json, file, indent=4)
                sr.invia("OK")  # Conferma ricezione file JSON completo
            except json.JSONDecodeError:
                print("Errore nella decodifica del JSON")
                sr.invia("ERRORE")
        else:
            print("Nessun contenuto JSON ricevuto.")
    else:
        print("Messaggio di controllo non riconosciuto.")

