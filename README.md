# PlexMovieImporter
Copies and renames completed movies from source folders into plex

Source files should be seperated by movie into folders with the name and year "<Movie_Name> (<year>)", which will produce outputs of "/<Movie_Name> (<year>)/<Movie_Name> (<year>).mp4" or "/<Movie_Name> (<year>)/<Movie_Name> (<year>) - Part<X>.mp4" (for folders with multiple files greater than 1GB in size), for any files greater than 1 GB in size in the source folders.

Notes: 
  The script has no information on what the movie files are, so any files above 1GB will be treated as movies. With this in mind, multipart movies will be processed in alphabetical order, this means that the parts could be out of order depending on the origional files names. All output files should be reviewed.
  The script will error out if copying a file fails, this is a protection to prevent deleting files that were not copied properly. Manual cleanup may need to occur if this happens.

Examples:
  /Jungle Book (1942)/ that contains files, movie.mp4, behindthescenes.mp4, themakingof.mp4, where only movie.mp4 is greater than 1GB, will have an output of /Jungle Book (1942)/Jungle Book (1942).mp4
  /The Three Musketeers (1921)/ that contains files, movie_pt1.mp4, movie_pt2.mp4, behindthescenes.mp4, themakingof.mp4, where only movie.mp4 is greater than 1GB, will have an output of /The Three Musketeers (1921)/The Three Musketeers (1921) - Part1.mp4,  /The Three Musketeers (1921)/The Three Musketeers (1921) - Part2.mp4
