#!/usr/bin/env python3
"""
Usage:
  ./top_tracks.py <username> [options]

Options:
    --number-of-tracks=<n> Number of top tracks displayed [default: 20]
"""
import docopt
import spotipy
import spotipy.util as util

SCOPE = 'user-top-read'

def main():
    arguments = docopt.docopt(__doc__)
    username = arguments['<username>']
    number_of_tracks = arguments['--number-of-tracks']
    token = util.prompt_for_user_token(username, SCOPE)

    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_top_tracks(limit=number_of_tracks)
        for item in results['items']:
            print(f"{', '.join(a['name'] for a in item['artists'])} - {item['name']}")
    else:
        print(f"Can't get token for {username}")

if __name__ == '__main__':
    main()