import os, csv

with open("100MostStreamedSongs.csv") as file:
  ## DictReader because the file has a header row (2D dictionary key)
  topSongs = csv.DictReader(file)
  ## for every row
  for row in topSongs:
    # check if the following folders exist in the 
    dir = os.listdir()
    artist = row["Artist(s)"].title()
    print(artist)
    if artist not in dir:
      os.mkdir(artist)
    song = row["Song"]
    rank = row["Rank"]
    path = os.path.join(f"{artist}/", f"{rank}-{song}.txt")
    f = open(path, "w")
    f.close()