from fastapi import FastAPI
from action import file_to_svg
from database.database import connect_to_database
import api.routes as routes

app = FastAPI()

connect_to_database()
file_to_svg()

app.include_router(routes.router)

@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API des vols !"}

# # traitement de données :
# airports = op.all_airports()
# count_total_airports = op.count_total_airports()
# count_planes = op.count_planes()
# count_airports_no_summer_time = op.count_airports_no_summer_time()
# most_used_departure_airport = op.most_used_departure_airport()

# top_10_destinations = op.top_10_destinations()
# bottom_10_destinations = op.bottom_10_destinations()
# top_10_planes = op.top_10_planes()
# bottom_10_planes = op.bottom_10_planes()
# destinations_per_airline = op.destinations_per_airline()

# destinations_per_airline = op.destinations_per_airline()
# destinations_per_airline_per_origin = op.destinations_per_airline_per_origin()

# print(top_10_destinations)
# print(bottom_10_destinations)
# print(top_10_planes)
