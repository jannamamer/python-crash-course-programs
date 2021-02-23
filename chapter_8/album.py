def make_album(artist_name, album_title, no_of_songs=None):
    album = {
        'artist': artist_name,
        'title': album_title
    }

    if no_of_songs:
        album['no_of_songs'] = no_of_songs

    return album


while True:
    print("\nPlease enter album details:")
    print("(enter 'q' anytime to quit)")

    artist_name = input("Artist name: ")
    if artist_name == 'q':
        break

    album_title = input("Album title: ")
    if album_title == 'q':
        break

    album = make_album(artist_name, album_title)
    print(album)
