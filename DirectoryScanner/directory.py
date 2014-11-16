import os

WARNING_LENGTH = 300
WAY_TO_LONG = 400
filesToLong = {}
warningFiles = {}

rootDir = os.path.dirname(os.path.abspath(__file__))

print "Searching Directory %s" % rootDir
for dirName, subdirList, fileList in os.walk(rootDir):
    #filters out directories that start with '.'
    #http://stackoverflow.com/questions/13454164/os-walk-without-hidden-folders
    subdirList[:] = [d for d in subdirList if not d[0] == '.']

    for fname in fileList:
        #append file name to directory or python doesn't can't open files without extensions
        filepath = os.path.join(dirName, fname)
        file=open(filepath)

        lines=file.readlines()

        fileLength = len(lines)
        if fileLength > WAY_TO_LONG:
            filesToLong[filepath] = fileLength
        elif fileLength >= WARNING_LENGTH and fileLength <= WAY_TO_LONG:
            warningFiles[filepath] = fileLength

if len(filesToLong) > 0:
    print "You have %s files that are over length of challenge:" % len(filesToLong)
    for filename, length in filesToLong.items():
        print '\tfile %s has length %i' % (filename, length)
else:
    print "Congratulations you met the challenge of 400 line files!"

if len(warningFiles) >0:
    print "\nYou may want to look at these files:"
    for filename, length in warningFiles.items():
        print '\tfile %s has length %i' % (filename, length)

input("Press Enter to continue...")