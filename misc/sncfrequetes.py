import requests
from datetime import datetime


def req(index):
    # Obtenir la date et l'heure actuelles
    date_actuelle = datetime.now()

    # Formater la date actuelle en chaîne dans le format souhaité
    date_str = date_actuelle.strftime("%Y%m%dT%H%M%S")

    res = requests.get(f"https://api.sncf.com/v1/coverage/sncf/stop_areas/stop_area:SNCF:87393009/departures?datetime={date_str}", headers={"Authorization": "237d701a-5818-4da3-91d2-3d1e018d5fe5"})


    inf = {

    }
    truc_gen = res.json()["departures"][index]

    try :
        inf["id"] = truc_gen["display_informations"]["headsign"]
        
        inf["ligne"]  = truc_gen["route"]["name"]
        if "Bus" in inf["ligne"]:
            inf["ligne"] = "Bus"
        elif "Paris" in inf["ligne"]:
            inf["ligne"] = "TER"

        j = truc_gen["links"][1]["id"]
        req = requests.get(f"https://api.sncf.com/v1/coverage/sncf/vehicle_journeys/{j}/?", headers={"Authorization": "237d701a-5818-4da3-91d2-3d1e018d5fe5"})


        arrets = []
        g = ""

        for arret in req.json()["vehicle_journeys"][0]["stop_times"]:
            if g == "Versailles Chantiers":
                arrets.append(arret["stop_point"]["name"])
            else :
                g = arret["stop_point"]["name"]
        
        inf["arrêts"] = arrets

        date_str = truc_gen["stop_date_time"]["departure_date_time"]
        format_str = "%Y%m%dT%H%M%S"

        # Créez l'objet de date
        date_obj = datetime.strptime(date_str, format_str)

        # Affichez l'heure et les minutes
        inf["arrivee"] = date_obj
        inf["terminus"] = inf["arrêts"][-1]

        return inf
    except :
        print("Erreur")
        return "E"