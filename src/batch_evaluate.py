
import os
import sys

if __name__ == "__main__":
    print "Evaluating activity:", sys.argv[1]
    print "CSV file:", sys.argv[2]
    outfile = sys.argv[1] + '.csv'
    print "Output filename:", outfile

    with open(sys.argv[2]) as f:
        content = f.readlines()

    for c in content:
        cp = c.rstrip('\n').split()
        if len(cp) == 1:
            print "Error in user: ", cp
            continue   
        ra = cp[0]
        user = cp[1]

    	print "Evaluating ", cp[0], " (username: ", cp[1], ")"
        commandline = "sh ./clone_and_eval.sh " + sys.argv[1] + " " +\
                     user + " " + ra + " >> " + outfile
	print commandline
        os.system(commandline)

