from fastapi import APIRouter
import database.operations as op

router = APIRouter()

@router.get("/datas", tags=["Airports"])
def get_all_data():
    return {
        "airports": op.all_airports(),
        "total_airports": op.count_total_airports(),
        "total_planes": op.count_planes(),
        "airports_no_summer_time": op.count_airports_no_summer_time(),
        "most_used_departure_airport": op.most_used_departure_airport(),
        "top_10_destinations": op.top_10_destinations(),
        "bottom_10_destinations": op.bottom_10_destinations(),
        "top_10_planes": op.top_10_planes(),
        "bottom_10_planes": op.bottom_10_planes(),
        "destinations_per_airline": op.destinations_per_airline(),
        "destinations_per_airline_per_origin": op.destinations_per_airline_per_origin()
    }

# Route pour récupérer la liste complète des aéroports
@router.get("/airports", tags=["Airports"])
def get_all_airports():
    return {"airports": op.all_airports()}

# Route pour récupérer le nombre total d’aéroports
@router.get("/airports/count", tags=["Airports"])
def get_total_airports():
    return {"total_airports": op.count_total_airports()}

# Route pour récupérer le nombre d’avions
@router.get("/planes/count", tags=["Planes"])
def get_total_planes():
    return {"total_planes": op.count_planes()}

# Route pour récupérer le nombre d’aéroports ne passant pas à l'heure d'été
@router.get("/airports/no_summer_time", tags=["Airports"])
def get_airports_no_summer_time():
    return {"airports_no_summer_time": op.count_airports_no_summer_time()}

# Route pour récupérer l’aéroport de départ le plus utilisé
@router.get("/airports/most_used_departure", tags=["Airports"])
def get_most_used_departure_airport():
    return {"most_used_departure_airport": op.most_used_departure_airport()}

# Route pour les 10 destinations les plus populaires
@router.get("/destinations/top10", tags=["Destinations"])
def get_top_10_destinations():
    return {"top_10_destinations": op.top_10_destinations()}

# Route pour les 10 destinations les moins populaires
@router.get("/destinations/bottom10", tags=["Destinations"])
def get_bottom_10_destinations():
    return {"bottom_10_destinations": op.bottom_10_destinations()}

# Route pour les 10 avions qui ont le plus décollé
@router.get("/planes/top10", tags=["Planes"])
def get_top_10_planes():
    return {"top_10_planes": op.top_10_planes()}

# Route pour les 10 avions qui ont le moins décollé
@router.get("/planes/bottom10", tags=["Planes"])
def get_bottom_10_planes():
    return {"bottom_10_planes": op.bottom_10_planes()}

# Route pour obtenir le nombre de destinations par compagnie
@router.get("/airlines/destinations", tags=["Airlines"])
def get_destinations_per_airline():
    return {"destinations_per_airline": op.destinations_per_airline()}

# Route pour obtenir le nombre de destinations par compagnie et aéroport d’origine
@router.get("/airlines/destinations_by_origin", tags=["Airlines"])
def get_destinations_per_airline_per_origin():
    return {"destinations_per_airline_per_origin": op.destinations_per_airline_per_origin()}
