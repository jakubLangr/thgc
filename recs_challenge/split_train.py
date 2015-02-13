#!/usr/bin/python

def splitfile(infilepath, chunksize):
    fname, ext = infilepath.rsplit('.',1)

    i = 0
    written = False
    with open(infilepath) as infile:
        while True:
            outfilepath = "{}{}.{}".format(fname, i, ext)
            with open(outfilepath, 'w') as outfile:
                for line in (infile.readline() for _ in range(chunksize)):
                    outfile.write(line)
                written = bool(line)
            if not written:
                break
            i += 1
 
fname="/home/lorenz/Documents/HutChallenge/recs_challenge/given/train.csv"

with open(fname) as f:
    Nlines= sum(1 for _ in f)

NlinesTrain=int(round(Nlines*0.7))

NlinesTest=Nlines-NlinesTrain

print NlinesTrain
print NlinesTest

splitfile(fname,NlinesTrain)