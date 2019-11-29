Follow category playlist
========================
The following script retrieves a Spotify playlist in one of the preset
categories and follows it as the current user.

It assumes that your credentials are saved in the environment.

.. code:: python

    from spotipy import util, Spotify
    from spotipy.scope import scopes

    cred = util.credentials_from_environment()
    scope = scopes.playlist_modify_private
    token = util.prompt_for_user_token(*cred, scope=scope)

    spotify = Spotify(token)
    category = spotify.categories(limit=1).items[0]
    playlist = spotify.category_playlists(category.id, limit=1).items[0]

    print(f'Following "{playlist.name}"" from category "{category.name}"...')
    spotify.playlist_follow(playlist.id, public=False)