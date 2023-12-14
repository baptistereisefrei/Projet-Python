import requests

def parseJson(jsonFile):
    if (jsonFile == None):
        return None
    
    moviesArray = []

    for i in jsonFile['results']:
        movieArray = {
            'title': i['title'],
            'overview': i['overview'],
            'release_date': i['release_date'],
        }
        moviesArray.append(movieArray)
    return moviesArray

def requestApi(findUrl):
    headers = {
        "accept": "application/json",
    }

    urlPattern = 'https://api.themoviedb.org/3/movie/'
    apiKey = '?api_key=10cc4880f99db6dbc89c50638b3663cd'

    response = requests.get(urlPattern + findUrl + apiKey, headers=headers)

    return response

def openAccessTokenFile():
    with open("accessToken.txt") as file:
        data = file.read()
        return data

def mainProgram():
    response = requestApi('popular')
    moviesArray = parseJson(response.json())
    return moviesArray

if __name__ == "__main__":
    print (mainProgram())
