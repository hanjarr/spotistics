
#!/usr/bin/env python3
"""
Usage:
  ./recently_saved.py <username> [options]

Display the most recently saved tracks

Options:
    --number-of-tracks=<n> Number of saved tracks displayed [default: 20]
"""
import docopt
import spotipy
import spotipy.util as util

SCOPE = 'user-library-read'

def main():
    arguments = docopt.docopt(__doc__)
    username = arguments['<username>']
    number_of_tracks = arguments['--number-of-tracks']
    token = util.prompt_for_user_token(username, SCOPE)

    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_saved_tracks(limit=number_of_tracks)
        for item in results['items']:
            track = item['track']
            print(f"{track['name']} - {track['artists'][0]['name']}")
    else:
        print(f"Can't get token for {username}")

if __name__ == '__main__':
    main()
