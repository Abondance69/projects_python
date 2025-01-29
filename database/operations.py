from sqlalchemy import text
from database.database import get_db

def all_airports() :
    query = "SELECT * FROM airports"
    db = next(get_db())
    result = db.execute(text(query)).fetchone()
    return result[0] if result else 0

# Cette fonction récupère le nombre total d'aéroports distincts dans la table "airports".
def count_total_airports():
    query = "SELECT COUNT(DISTINCT faa) FROM airports"
    db = next(get_db())
    result = db.execute(text(query)).fetchone()
    return result[0] if result else 0

# Cette fonction récupère le nombre d'avions distincts dans la table "planes".
def count_planes():
    query = "SELECT COUNT(DISTINCT tailnum) FROM planes"
    db = next(get_db())
    result = db.execute(text(query)).fetchone()
    return result[0] if result else 0

# Cette fonction récupère le nombre d'aéroports où la colonne "dst" est égale à 23 (indiquant qu'ils ne passent pas à l'heure d'été).
def count_airports_no_summer_time():
    query = "SELECT COUNT(*) FROM airports WHERE dst = '23'"
    db = next(get_db())
    result = db.execute(text(query)).fetchone()
    return result[0] if result else 0

# Cette fonction récupère le nombre de fuseaux horaires distincts dans la table "airports" (excluant les valeurs "N" de la colonne "tzone").
def count_timezones():
    query = "SELECT COUNT(DISTINCT tzone) FROM airports WHERE tzone != 'N'"
    db = next(get_db())
    result = db.execute(text(query)).fetchone()
    return result[0] if result else 0

# Cette fonction récupère le nombre de compagnies distinctes dans la table "airlines".
def count_airlines():
    query = "SELECT COUNT(DISTINCT carrier) FROM carrier"
    db = next(get_db())
    result = db.execute(text(query)).fetchone()
    return result[0] if result else 0

# Cette fonction récupère l’aéroport de départ le plus emprunté.
def most_used_departure_airport():
    query = """
        SELECT origin, COUNT(*) as flight_count
        FROM flights
        GROUP BY origin
        ORDER BY flight_count DESC
        LIMIT 1;
    """
    db = next(get_db())
    result = db.execute(text(query)).fetchone()
    return result if result else None

# Cette fonction récupère les 10 destinations les plus prisées avec le pourcentage correspondant.
def top_10_destinations():
    query = """
        SELECT a.name as destination_name, COUNT(f.dest) as flight_count,
               ROUND(COUNT(f.dest) * 100.0 / (SELECT COUNT(*) FROM flights), 2) as percentage
        FROM flights f
        JOIN airports a ON f.dest = a.faa
        GROUP BY a.name
        ORDER BY flight_count DESC
        LIMIT 10;
    """
    db = next(get_db())
    results = db.execute(text(query)).fetchall()
    return results

# Cette fonction récupère les 10 destinations les moins prisées avec leur pourcentage.
def bottom_10_destinations():
    query = """
        SELECT a.name as destination_name, COUNT(f.dest) as flight_count,
               ROUND(COUNT(f.dest) * 100.0 / (SELECT COUNT(*) FROM flights), 2) as percentage
        FROM flights f
        JOIN airports a ON f.dest = a.faa
        GROUP BY a.name
        ORDER BY flight_count ASC
        LIMIT 10;
    """
    db = next(get_db())
    results = db.execute(text(query)).fetchall()
    return results

# Cette fonction récupère les 10 avions ayant effectué le plus de décollages.
def top_10_planes():
    query = """
        SELECT tailnum, COUNT(*) as flight_count
        FROM flights
        WHERE tailnum IS NOT NULL
        GROUP BY tailnum
        ORDER BY flight_count DESC
        LIMIT 10;
    """
    db = next(get_db())
    results = db.execute(text(query)).fetchall()
    return results

# Cette fonction récupère les 10 avions ayant effectué le moins de décollages.
def bottom_10_planes():
    query = """
        SELECT tailnum, COUNT(*) as flight_count
        FROM flights
        WHERE tailnum IS NOT NULL
        GROUP BY tailnum
        ORDER BY flight_count ASC
        LIMIT 10;
    """
    db = next(get_db())
    results = db.execute(text(query)).fetchall()
    return results

# Cette fonction récupère le nombre de destinations desservies par chaque compagnie.
def destinations_per_airline():
    query = """
        SELECT al.name as airline_name, COUNT(DISTINCT f.dest) as destination_count
        FROM flights f
        JOIN airlines al ON f.carrier = al.carrier
        GROUP BY al.name
        ORDER BY destination_count DESC;
    """
    db = next(get_db())
    results = db.execute(text(query)).fetchall()
    return results

# Cette fonction récupère le nombre de destinations desservies par chaque compagnie selon l'aéroport d'origine.
def destinations_per_airline_per_origin():
    query = """
        SELECT al.name as airline_name, f.origin, COUNT(DISTINCT f.dest) as destination_count
        FROM flights f
        JOIN airlines al ON f.carrier = al.carrier
        GROUP BY al.name, f.origin
        ORDER BY al.name, destination_count DESC;
    """
    db = next(get_db())
    results = db.execute(text(query)).fetchall()
    return results


























# 4 différence


















# # Cette fonction récupère le nombre d'aéroports de départ distincts dans la table "flights".
# def count_departure_airports():
#     query = "SELECT COUNT(DISTINCT id) FROM flights"
#     db = next(get_db())
#     result = db.execute(text(query)).fetchone()
#     return result[0] if result else 0

# # Cette fonction récupère le nombre de vols annulés dans la table "flights" où la colonne "cancelled" est égale à 1.
# def count_cancelled_flights():
#     query = "SELECT COUNT(*) FROM flights WHERE cancelled = 1"
#     db = next(get_db())
#     result = db.execute(text(query)).fetchone()
#     return result[0] if result else 0

# # Cette fonction récupère le nombre d'aéroports de destination distincts dans la table "flights".
# def count_destination_airports():
#     query = "SELECT COUNT(DISTINCT id) FROM flights"
#     db = next(get_db())
#     result = db.execute(text(query)).fetchone()
#     return result[0] if result else 0







# def check_duplicates(table_name, column_name):
#     query = f"""
#         SELECT {column_name}, COUNT(*)
#         FROM {table_name}
#         GROUP BY {column_name}
#         HAVING COUNT(*) > 1;
#     """
#     db = next(get_db())
#     result = db.execute(text(query)).fetchall()

#     if result:
#         return [row for row in result]
#     else:
#         return f"Aucun doublon trouvé dans la colonne {column_name} de la table {table_name}."

# def check_foreign_key_inconsistencies():
#     query = """
#         SELECT f.flight_id, f.airport_id
#         FROM flights f
#         LEFT JOIN airports a ON f.airport_id = a.airport_id
#         WHERE a.airport_id IS NULL;
#     """
#     db = next(get_db())
#     result = db.execute(text(query)).fetchall()

#     if result:
#         return [f"Vol ID {row[0]} avec un airport_id {row[1]} inexistant." for row in result]
#     else:
#         return "Aucune incohérence de clé étrangère trouvée dans la table des vols."

# def delete_duplicates(table_name, column_name):
#     query = f"""
#         WITH duplicates AS (
#             SELECT MIN(ctid) as ctid, {column_name}
#             FROM {table_name}
#             GROUP BY {column_name}
#             HAVING COUNT(*) > 1
#         )
#         DELETE FROM {table_name}
#         WHERE ctid NOT IN (SELECT ctid FROM duplicates);
#     """
#     db = next(get_db())
#     db.execute(text(query))
#     db.commit()
#     return f"Doublons supprimés dans la colonne {column_name} de la table {table_name}."
