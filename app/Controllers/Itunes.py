import requests

async def getFields(artist, title):

 artist = artist.replace(" ", "+")
 title = title.replace(" ", "+")

 base_url = "https://itunes.apple.com/search?media=music&term=" + title + "+" + artist
 dict = {}  # an empty dictionary to hold all the metadata fields
 successfulFieldCalls = 2
 response = requests.get(base_url)

 try:
    res = response.json()
    data = res['results'][0]

   

    album = data['collectionName']
    if album:
        dict['album'] = album
        successfulFieldCalls += 1

    release_date = data['releaseDate']
    if release_date:
        dict['year'] = release_date[0:4]
        successfulFieldCalls += 1

    track = data['trackCensoredName']
    
    if track:
        dict['track'] = track
        successfulFieldCalls += 1
   
    song= data['trackCensoredName']
    if(song):
       dict['song_title']=song

    album_artist = data['artistName']
    if album_artist:
        dict['albumArtist'] = album_artist
        successfulFieldCalls += 1

    genre = data['primaryGenreName']
    if genre:
        dict['genre'] = genre
        successfulFieldCalls += 1

    disc_number = data['discNumber']
    if disc_number:
        dict['disc_number'] = disc_number
        successfulFieldCalls += 1

    
 except:
        print("Error Occured: Data nulled")
        artist = song_title = album = year = track = genre = comments = albumArtist = composer = disc_number = None
        successfulFieldCalls = 0

    # If you still want to print 'data', do it here within the else block
 dict['successfulCalls'] = successfulFieldCalls
 return dict