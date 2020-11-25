import requests
import json

api_key = '210aea2be2408f7c583e89e2adf8098a'

# Base url used for the requests
api_url = 'https://api.musixmatch.com/ws/1.1/'


def music_matcher(dict_info):
    """
    Looks for a song whether by track and artist name or by a part
    of lyrics.

    Args:
        dict_info (dict): a dict object with the information needed, like
        artist name, track name, lyrics string and a bool if the search is
        done by lyrics or by track name.
    """

    if dict_info['by_lyrics']:
        if dict_info['artist'] != None:
            call = api_url + 'track.search?' + '&q_lyrics=' + \
                dict_info['lyrics'] + '&q_artist=' + \
                dict_info['artist'] + '&s_track_release_date=asc'
        else:
            call = api_url + 'track.search?' + \
                '&q_lyrics=' + dict_info['lyrics'] + \
                '&s_track_release_date=asc'
    else:
        if dict_info['artist'] != None:
            call = api_url + 'track.search?' + '&q_track=' + \
                dict_info['track'] + '&q_artist=' + \
                dict_info['artist'] + '&s_track_release_date=asc'
        else:
            call = api_url + 'track.search?' + '&q_track=' + \
                dict_info['track'] + '&s_track_release_date=asc'

    # Song matcher
    request = requests.get(call + f'&apikey={api_key}').json()
    track = request['message']['body']['track_list'][0]['track']

    # Lyrics print
    call = api_url + 'track.lyrics.get?' + \
        '&track_id=' + str(track['track_id']) + f'&apikey={api_key}'
    request = requests.get(call).json()

    print('Canción: {}'.format(track['track_name']))
    print('Artista: {}\n'.format(track['artist_name']))
    print(request['message']['body']['lyrics']['lyrics_body'])


def top_artists(dict_info):
    """
    It generates the top of a number of artists (default 10) of a given country

    Args:
        dict_info (dict): a dict object with the number of artists,
        and country.
    """
    call = api_url + 'chart.artists.get?' + '&country=' + \
        dict_info['country'] + '&page=1&page_size=' + dict_info['top']

    # Searching for top artist
    request = requests.get(call + f'&apikey={api_key}').json()
    for artist in request['message']['body']['artist_list']:
        artist_name = artist['artist']['artist_name']
        artist_country = artist['artist']['artist_country']
        print(f'{artist_name}\t({artist_country})')


def top_tracks(dict_info):
    """
    It generates the top of a number of tracks (default 10) of a given country

    Args:
        dict_info (dict): a dict object with the number of tracks,
        and country.
    """
    call = api_url + 'chart.tracks.get?' + '&country=' + \
        dict_info['country'] + '&page=1&page_size=' + dict_info['top']

    # Searching for top artist
    request = requests.get(call + f'&apikey={api_key}').json()
    index = 1
    for track in request['message']['body']['track_list']:
        track_name = track['track']['track_name']
        track_album = track['track']['album_name']
        track_artist = track['track']['artist_name']
        track_genre = track['track']['primary_genres']['music_genre_list']
        if track_genre:
            track_genre = track['track']['primary_genres']['music_genre_list'][0]['music_genre']['music_genre_name']
        else:
            track_genre = 'Unknown'
        print(f'{index}. {track_name} \t Album: {track_album} \t Artist: {track_artist} \t Genre: {track_genre}')
        index += 1


def recommendations_genre(dict_info):
    """
    It generates a list of recommended tracks (default 10) of a given genre

    Args:
        dict_info (dict): a dict object with the number of tracks,
        genre id and country.
    """

    # At first it needs to look for the genre id in the database
    call = api_url + 'music.genres.get?'
    request = requests.get(call + f'&apikey={api_key}').json()
    genre_id = None
    for genre in request['message']['body']['music_genre_list']:
        if dict_info['genre'] in genre['music_genre'].values():
            genre_id = genre['music_genre']['music_genre_id']

    # This part uses the genre_id gotten before
    call = api_url + 'track.search?' + '&f_music_genre_id=' + \
        str(genre_id) + '&s_track_rating=desc'

    # Searching for the top tracks by a given genre
    request = requests.get(call + f'&apikey={api_key}').json()
    index = 1
    for track in request['message']['body']['track_list']:
        track_name = track['track']['track_name']
        track_album = track['track']['album_name']
        track_artist = track['track']['artist_name']
        track_genre = track['track']['primary_genres']['music_genre_list']
        if track_genre:
            track_genre = track['track']['primary_genres']['music_genre_list'][0]['music_genre']['music_genre_name']
        else:
            track_genre = 'Unknown'
        print(f'{index}. {track_name} \t Album: {track_album} \t Artist: {track_artist} \t Genre: {track_genre}')
        index += 1


if __name__ == "__main__":
    music_matcher(
        {
            'by_lyrics': False,
            'track': 'Señorita',
            'artist': 'Shawn Mendes'
        }
    )
    print('--------------------------------------------')
    top_artists(
        {
            'top': '10',
            'country': 'cl'
        }
    )
    print('--------------------------------------------')
    top_tracks(
        {
            'top': '10',
            'country': 'cl'
        }
    )
    print('--------------------------------------------')
    recommendations_genre(
        {
            'top': '10',
            'genre': 'Rock'
        }
    )
