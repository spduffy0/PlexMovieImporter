from FileHandler import FileHandler
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("destination")
    parser.add_argument("-d", "--delete", action="store_true", help="Delete source files that were moved when set")

    args = parser.parse_args()

    fh = FileHandler(args.source, args.destination)
    fh.scanSourceForMovies()
    fh.copyMoviesToDestination(deleteOrigionalFiles=args.delete)