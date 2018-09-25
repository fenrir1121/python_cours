import requests

def get_location_info():
    key = "664ce90e57e41bd19d62a6b3bd7cda72" 
    return requests.get(f"http://api.ipstack.com/190.3.36.160?access_key={key}&format=1").json()

if __name__ == "__main__":
    print(get_location_info())
