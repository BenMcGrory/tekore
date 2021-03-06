|logo|

|python|

Welcome to the Python Package Index page of Tekore,
a client of the Spotify Web API for Python!
Tekore allows you to interact with the Web API effortlessly.

.. code:: python

    from tekore import Spotify

    spotify = Spotify(token)

    tracks = spotify.current_user_top_tracks(limit=10)
    for track in tracks.items:
        print(track.name)

    finlandia = '3hHWhvw2hjwfngWcFjIzqr'
    spotify.playback_start_tracks([finlandia])

See our online documentation on `Read The Docs`_ for tutorials,
examples, package reference and a detailed description of features.
Visit our repository on `GitHub`_  if you'd like to submit an issue
or ask just about anything related to Tekore.

Installation
============
Tekore can be installed from the Package Index via ``pip``.

.. code:: sh

    $ pip install tekore

Versioning
==========
Tekore provides both stable and beta endpoints of the Web API.
However, beta endpoints may be changed by Spotify without prior notice,
so older versions of the library may have unintended issues.
Because of this, Tekore follows a modified form of
`Semantic Versioning <https://semver.org/>`_.
Incompatible changes in the library are still introduced in major versions,
and new features and endpoints are added in minor versions.
But endpoints removed by Spotify are removed in minor versions and changes
to endpoints are implemented as bugfixes.
See the Web API `documentation <web api_>`_ for further information on beta endpoints.

Changelog
=========
1.0.1
-----
Bugfixes
********
- Accept missing video thumbnail in PlaylistTrack (#132)

1.0.0
-----
- Packaging improvements
- Declare versioning scheme

0.1.0
-----
Initial release of Tekore!


.. |logo| image:: https://raw.githubusercontent.com/felix-hilden/tekore/master/docs/logo_small.png
   :alt: logo

.. |python| image:: https://img.shields.io/pypi/pyversions/tekore
   :alt: python version

.. _github: https://github.com/felix-hilden/tekore
.. _read the docs: https://tekore.readthedocs.io
.. _web api: https://developer.spotify.com/documentation/web-api
