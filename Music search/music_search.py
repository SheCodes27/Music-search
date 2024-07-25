import requests

def search_music(track_name):
    # URL for the iTunes Search API
    url = "https://itunes.apple.com/search"
    
    # Parameters for the API request
    params = {
        'term': track_name,
        'limit': 1  # Limit the results to 1
    }
    
    # Make the request to the API
    response = requests.get(url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Check if any results were returned
        if data['resultCount'] > 0:
            # Get the first result
            result = data['results'][0]
            track_name = result['trackName']
            artist_name = result['artistName']
            genre = result['primaryGenreName']
            
            print(f"Track: {track_name}")
            print(f"Artist: {artist_name}")
            print(f"Genre: {genre}")
        else:
            print("No results found.")
    else:
        print("Failed to retrieve data.")

if __name__ == "__main__":
    track_name = input("Enter the name of the music track: ")
    search_music(track_name)
