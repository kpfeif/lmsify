# lmsify
Reformats a CSV file exported from https://exportify.net/ into a m3u playlist file for use as a LMS (Lyrion Music Server) playlist file.


Run this via python:

python lmsify.py [input_file.csv] [output_file.m3u]

For example, let's say I have exported my Spotify playlist named "Songs I Like" via Exportify.  I'd run:

python lmsify.py Songs_I_Like.csv Songs_I_Like.m3u

I then can take the resulting m3u file and copy it into my LMS "Playlists" folder.  Once the LMS scanner picks it up, I can now play that playlist via Spotify.
