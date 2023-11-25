import requests
from pprint import pprint 
async def getFields(artist, title):
    base_url =await  "https://api.genius.com/search?q="+title+"+"+artist
    headers = {
        "Authorization": "Bearer AXAstvuuSIYEwyM_Ja6OdMeFkZHNGzgtMm6AQL57zz3VPFBDPTwvkZY0E0cCnmXO"
    }
    successfields=2
    response= requests.get(base_url,headers=headers)
    dict = {}
    # Check if the request was successful (status code 200)
    try:
        # Parse and return the JSON response
         
         
         res=response.json()
         trial=res['response']['hits'][0]['result']
         if(trial['full_title']):
             dict['song_title']=trial['full_title']
             successfields+=1
         if(trial['artist_names']):
             dict['album-artist']=trial['artist_names']
             successfields+=1
         if(trial["release_date_components"]['year']):
             dict['year']=trial["release_date_components"]['year']
             successfields+=1
         if( res['response']['hits'][0]['type']):
             dict['genre']=res['response']['hits'][0]['type']
             successfields+=1
    
       

       
    except:
        # Print an error message if the request was not successful
        print("Error Occured: Data nulled")
        artist = song_title = album = year = track = genre = comments = albumArtist = composer = disc_number = None
        successfulFieldCalls = 0
        
    dict['successfulCalls'] =  successfields
    print(dict)
    return dict
# Example usage:


# Print the result
#print(result)
