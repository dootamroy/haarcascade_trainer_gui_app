# CREATED BY DOOTAM ROY @haarcascade_trainer 
 # EMAIL: dootamroy22@gmail.com

from subprocess import Popen, PIPE


cmd = "opencv_traincascade -data C:/Users/Dell/Desktop/acr/data -vec C:/Users/Dell/Desktop/acr/positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 14 -w 20 -h 20"


with Popen(cmd.split(), stdout=PIPE, bufsize=1, universal_newlines=True) as p:
    for line in p.stdout:
        print(line, end='')