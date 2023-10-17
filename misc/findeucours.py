from datetime import datetime


fin_du_cours = datetime.strptime(f"{datetime.now().date()} 12:50:00", "%Y-%m-%d %H:%M:%S")
fin = (fin_du_cours - datetime.now()).seconds // 60

print("La fin du cours est dans", fin, "minutes.")