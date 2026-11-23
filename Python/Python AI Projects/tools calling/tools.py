from fastapi import FastAPI

app = FastAPI()
@app.get("/weather/{city}")

def get_weather(city: str):

    if city.lower() == "bangalore":
        return {
            "city": city,
            "temperature": 28,
            "condition": "sunny",
            "good_weather": True
        }
    elif city.lower() == "mumbai":
         return {
        "city": city,
        "temperature": 21,
        "condition": "Heavy Rain",
        "good_weather": False
    }
    elif city.lower()=="chennai":
        return{
             "city": city,
                    "temperature": 36,
                    "condition": "HOT",
                    "good_weather": False
        }
    else:
          return{
                     "city": city,
                      "temperature": 0,
                            "condition": "NA",
                            "good_weather": False
                }




def book_flight(destination: str):
    return {
        "status": "confirmed",
        "destination": destination,
        "message": f"Flight booked to {destination}"
    }