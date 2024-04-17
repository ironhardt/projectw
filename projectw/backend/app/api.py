from fastapi import FastAPI
import json

app = FastAPI()


# Load routes from a JSON file
def load_routes():
    with open("C:/Users/green/Desktop/projects/projectw/sites.json", "r") as f:
        data = json.load(f)
    return data


def load_sites(route):
    with open("C:/Users/green/Desktop/projects/projectw/testData.json") as f:
        data = json.load(f)
        print(data[route])
    return data[route]


# Dynamically add routes to the FastAPI app
def create_dynamic_routes():
    routes = load_routes()
    for route in routes:
        app.add_api_route(
            route["path"], load_sites(route["name"])["item"], methods=["GET"]
        )


create_dynamic_routes()
