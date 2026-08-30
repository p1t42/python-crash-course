# User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an 
# album’s artist and title. Once you have that information, call make_album() with the user’s input and 
# print the dictionary that’s created. Be sure to include a quit value in the while loop.


def make_album(artist_name, album_title, songs_count=None):
    """This function stores data in a dictionarie"""
    artist = {"name": artist_name, "album": album_title,}
    
    if songs_count:
        artist["songs"] = songs_count
    
    return artist


while True:
    print(f"\nIf you want to quit press 'q'")
    
    artist_name = input(f"\nWhats your favourte artist's name: ")
    if artist_name == "q":
        break
    
    album_title = input(f"\nWhats his best album's name: ")
    if album_title == "q":
        break

    full_artist = make_album(artist_name, album_title)
    print(f"\nHere is your artist: {full_artist}")