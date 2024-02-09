from classi.send_receve_sock import SRS
import socket
import json

HOST = "127.0.0.1"  # IP del server
PORT = 65432  # Porta di comunicazione

def invia_file_json(srs, percorso_file):
    # Lettura e invio dell'intero file JSON come un unico pezzo
    with open(percorso_file, "r") as file:
        contenuto_json = json.load(file)
    
    # Serializzazione del contenuto JSON in una stringa
    contenuto_stringa = json.dumps(contenuto_json)
    
    # Invio del contenuto JSON serializzato al server
    srs.invia(contenuto_stringa)
    
    # Attendi la conferma del server
    if srs.ricevi() == "OK":
        print("File JSON inviato con successo.")
    else:
        print("Errore nell'invio del file JSON.")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    sr = SRS(s)
    
    # Invio messaggio di controllo al server
    sr.invia("CI SEI?")
    
    # Attesa risposta dal server
    if sr.ricevi() == "SI":
        invia_file_json(sr, "FileDaMandare.json")
    else:
        print("Il server non è disponibile.")
