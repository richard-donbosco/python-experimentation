import requests 
import json 



def get_routes():
    res= requests.get("https://api-v3.mbta.com/routes")
    routes= json.loads(res.text)
    print(routes)
    return routes 


if __name__=="__main__":
    get_routes()