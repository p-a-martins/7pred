import os
import sys
from testing_set import *

### Output

print '****************************************************************************'
print '*** 7pred - Protein Subcellular Localization Prediction (Human Proteins) ***'
print '****************************************************************************'
print 'Input Type:'
print "- UniProtKB Accession Number(s) (multiple accession numbers should be "
print "  separated with commas): Enter 1"
print "- File (one UniProtKB Accession Number per line): Enter 2"
print '****************************************************************************'

x = False
while x is False:
    input_type = raw_input("Enter Input Type (1 or 2): ")
    if input_type == '1':
        filename = raw_input("Enter UniProtKB Accession Number(s) (e.g., P20618,P15531,P07384): ")
        proteins_ids = filename.split(',')
        x = True
        
    y = False    
    if input_type == '2':
        while y is False:
            filename = raw_input("Enter file name (e.g., ProteinsIDs.txt): ")
            try:
                infile = open(filename,'r')
                proteins_ids = infile.read().splitlines()
                infile.close()
                y = True
                x = True
            except:
                print "File not found. Try again!"

print '****************************************************************************'

testing_set(proteins_ids,1)
testing_set(proteins_ids,2)


###
print 'Predictions:'
#t-b2_cc-j48.model
print '1. Predictor T-B2/CC-J48:'
os.system('java -cp "./data/meka/*" meka.classifiers.multilabel.CC -l data/models/t-b2_cc-j48.model -t data/datasets/T-B2.arff -T data/datasets/P-B2.arff -predictions data/predictions/t-b2_cc-j48.arff -no-eval')
print 'Predictions saved to: t-b2_cc-j48.txt (.txt format)\n'

#t-b2_cc-smo.model
print '2. Predictor T-B2/CC-SMO:'
os.system('java -cp "./data/meka/*" meka.classifiers.multilabel.CC -l data/models/t-b2_cc-smo.model -t data/datasets/T-B2.arff -T data/datasets/P-B2.arff -predictions data/predictions/t-b2_cc-smo.arff -no-eval')
print 'Predictions saved to: t-b2_cc-smo.txt (.txt format)\n'

#t-b2_lc-smo.model
print '3. Predictor T-B2/LC-SMO:'
os.system('java -cp "./data/meka/*" meka.classifiers.multilabel.LC -l data/models/t-b2_lc-smo.model -t data/datasets/T-B2.arff -T data/datasets/P-B2.arff -predictions data/predictions/t-b2_lc-smo.arff -no-eval')
print 'Predictions saved to: t-b2_lc-smo.txt (.txt format)\n'

#t-c2_cc-j48.model
print '4. Predictor T-C2/CC-J48:'
os.system('java -cp "./data/meka/*" meka.classifiers.multilabel.CC -l data/models/t-c2_cc-j48.model -t data/datasets/T-C2.arff -T data/datasets/P-C2.arff -predictions data/predictions/t-c2_cc-j48.arff -no-eval')
print 'Predictions saved to: t-c2_cc-j48.txt (.txt format)\n'

#t-c2_cc-smo.model
print '5. Predictor T-C2/CC-SMO:'
os.system('java -cp "./data/meka/*" meka.classifiers.multilabel.CC -l data/models/t-c2_cc-smo.model -t data/datasets/T-C2.arff -T data/datasets/P-C2.arff -predictions data/predictions/t-c2_cc-smo.arff -no-eval')
print 'Predictions saved to: t-c2_cc-smo.txt (.txt format)\n'

#t-c2_lc-j48.model
print '6. Predictor T-C2/LC-J48:'
os.system('java -cp "./data/meka/*" meka.classifiers.multilabel.LC -l data/models/t-c2_lc-j48.model -t data/datasets/T-C2.arff -T data/datasets/P-C2.arff -predictions data/predictions/t-c2_lc-j48.arff -no-eval')
print 'Predictions saved to: t-c2_lc-j48.txt (.txt format)\n'

#t-c2_lc-smo.model
print '7. Predictor T-C2/LC-SMO:'
os.system('java -cp "./data/meka/*" meka.classifiers.multilabel.LC -l data/models/t-c2_lc-smo.model -t data/datasets/T-C2.arff -T data/datasets/P-C2.arff -predictions data/predictions/t-c2_lc-smo.arff -no-eval')
print 'Predictions saved to: t-c2_lc-smo.txt (.txt format)\n'

#os.system('cls')


#####

filepath = ['data/predictions/t-b2_cc-j48.arff','data/predictions/t-b2_cc-smo.arff','data/predictions/t-b2_lc-smo.arff','data/predictions/t-c2_cc-j48.arff','data/predictions/t-c2_cc-smo.arff','data/predictions/t-c2_lc-j48.arff','data/predictions/t-c2_lc-smo.arff']
localizations_list = ['centrosome','cytoplasm','cytoskeleton','endoplasmic-reticulum','endosome','extracell', 'Golgi-apparatus','lysosome','microsome', 'mitochondrion','nucleus','peroxisome','plasma-membrane','synapse']

predictions = []

data = False
for files in filepath:
    locs_file = []
    n = 0
    with open(files, 'r') as f:
        while not '@data' in f.next():
            pass
        for line in f:
            locs = line.split(',')[:14]
            x = [localizations_list[i] for i,x in enumerate(locs) if x == '1']
            locs_list = [proteins_ids[n]] + x
            locs_file.append(locs_list)
            n += 1
    predictions.append(locs_file)

with open('t-b2_cc-j48.txt', 'w') as f:
    f.writelines(','.join(str(j) for j in i) + '\n' for i in predictions[0])

with open('t-b2_cc-smo.txt', 'w') as f:
    f.writelines(','.join(str(j) for j in i) + '\n' for i in predictions[1])

with open('t-b2_lc-smo.txt', 'w') as f:
    f.writelines(','.join(str(j) for j in i) + '\n' for i in predictions[2])

with open('t-c2_cc-j48.txt', 'w') as f:
    f.writelines(','.join(str(j) for j in i) + '\n' for i in predictions[3])

with open('t-c2_cc-smo.txt', 'w') as f:
    f.writelines(','.join(str(j) for j in i) + '\n' for i in predictions[4])

with open('t-c2_lc-j48.txt', 'w') as f:
    f.writelines(','.join(str(j) for j in i) + '\n' for i in predictions[5])

with open('t-c2_lc-smo.txt', 'w') as f:
    f.writelines(','.join(str(j) for j in i) + '\n' for i in predictions[6])

input("Press enter to close program")
