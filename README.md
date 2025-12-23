# lmsify
Reformats a CSV file exported from https://exportify.net/ into a m3u playlist file for use as a LMS (Lyrion Music Server) playlist file.


Run this via python:

python lmsify.py [input_file.csv] [output_file.m3u]

For example, let's say I have exported my Spotify playlist named "Songs I Like" via Exportify.  I'd run:

python lmsify.py Songs_I_Like.csv Songs_I_Like.m3u

I then can take the resulting m3u file and copy it into my LMS "Playlists" folder.  Once the LMS scanner picks it up, I can now play that playlist via Spotify.

If you have a folder full of playlists (assuming this is a Mac or Linux), you can use this bash script to convert them all:

for f in *.csv; do
  python3 lmsify.py "$f" "${f%.csv}.m3u"
done

