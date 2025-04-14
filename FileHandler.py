from pathlib import Path
import os
import shutil

class FileHandler:
    minMovieSize = 1024*1024*1024 # 1 GB
    movieExtention = ".mp4"
    sourceDir: Path
    destinationDir: Path
    sourceFiles = {}
    totalMovies = 0

    def __init__(self, sourceDir: str, destinationDir: str):
        self.sourceDir = Path(sourceDir)
        self.destinationDir = Path(destinationDir)

        if not self.sourceDir.exists():
            print("Source path is invalid: " + self.sourceDir)
            raise SystemExit(1)
        
        if not self.destinationDir.exists():
            print("Destination path is invalid: " + self.destinationDir)
            raise SystemExit(1)

    def scanSourceForMovies(self):
        print("Scanning source files")
        for dirPath, dirNames, fileNames in os.walk(self.sourceDir):
            for file in fileNames:
                if os.path.getsize(os.path.join(dirPath, file)) > self.minMovieSize:
                    if dirPath in self.sourceFiles:
                        self.sourceFiles[dirPath].append(file)
                    else:
                        self.totalMovies += 1
                        self.sourceFiles[dirPath] = [file]
        print(self.sourceFiles + " files found")

    def copyMoviesToDestination(self, deleteOrigionalFiles = False):
        print("Copying files to destination")
        print("%s/%s" % (0, self.totalMovies), flush=True)
        for index, movie in enumerate(self.sourceFiles):
            movieName = movie.split("\\")[-1]

            outputFolderPath = os.path.join(self.destinationDir, movieName)
            if not os.path.exists(outputFolderPath):
                os.mkdir(outputFolderPath)

            sourceMovieFiles = self.sourceFiles[movie]
            for index, sourceFile in enumerate(sourceMovieFiles):
                outputFile = movieName + self.movieExtention
                if len(sourceMovieFiles) > 1:
                    outputFile = movieName + " - Part" + str(index) + self.movieExtention
                
                sourceFilePath = os.path.join(self.sourceDir, movieName, sourceFile)
                outputFilePath = os.path.join(outputFolderPath, outputFile)
            
                shutil.copyfile(sourceFilePath, outputFilePath)
                if deleteOrigionalFiles:
                    print("Deleting source file: " + sourceFilePath)
                    os.remove(sourceFilePath)

            print("%s/%s" % (index + 1, self.totalMovies), flush=True)

                