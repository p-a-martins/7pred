from getGO_Terms import *
######################################################################################################################
### HUM-MPLOC 2.0 DATASET
######################################################################################################################
def dataset_hummploc20():
    infile = open('data/datasets/SM_Hum-mPLoc_2.0.txt','r')
    indata = infile.readlines()
    infile.close()
    indata = map(lambda s: s.strip(), indata)

    protein2localizations = {}

    localization = ''
    for line in indata:
        if line.startswith('('):
            loc = line.split(' ')
            loc = loc[2:-1]
            loc = ' '.join(loc)
            localization = loc
            
        if line.startswith('>'):
            protein = line[1:]
            if protein in protein2localizations.keys():
                protein2localizations[protein].append(localization)
            else:
                protein2localizations[protein] = [localization]
       
    return protein2localizations

######################################################################################################################
### LOCALIZATIONS ARRAY - TRAINING SET
######################################################################################################################
def localizations2array(protein2localizations):

    localizations_list = ['centrosome',
                          'cytoplasm',
                          'cytoskeleton',
                          'endoplasmic reticulum',
                          'endosome',
                          'extracell',
                          'Golgi apparatus',
                          'lysosome',
                          'microsome',
                          'mitochondrion',
                          'nucleus',
                          'peroxisome',
                          'plasma membrane',
                          'synapse']

    localizations_array = {}
    for protein_id, localizations in protein2localizations.iteritems():
        array = [0]*len(localizations_list)
        for localization in localizations_list:
            if localization in localizations:
                array[localizations_list.index(localization)] = 1
        localizations_array[protein_id] = array

    return localizations_array


######################################################################################################################
### TRAINING SET
######################################################################################################################
def training_set(extraction):
    protein2localizations = dataset_hummploc20()

    localizations_list = ['centrosome',
                          'cytoplasm',
                          'cytoskeleton',
                          'endoplasmic-reticulum',
                          'endosome',
                          'extracell',
                          'Golgi-apparatus',
                          'lysosome',
                          'microsome',
                          'mitochondrion',
                          'nucleus',
                          'peroxisome',
                          'plasma-membrane',
                          'synapse']

    localizations_array = localizations2array(protein2localizations)
    proteins_ids =  localizations_array.keys()
    go_terms = go_terms2array(proteins_ids, extraction)
    go_terms_list = go_terms[0]
    go_terms_array = go_terms[1]
       
    if extraction == 1:
        relation = 'training_t-b2'
        output = open('data/datasets/T-B2.arff','w')

    if extraction == 2:
        relation = 'training_t-c2'
        output = open('data/datasets/T-C2.arff','w')

    # OUTPUT       
    header = "@relation '" + relation + ": -C -14'\n\n"
    attribute1 = "@attribute id string\n"
    attribute2 = '@attribute ' + ' numeric\n@attribute '.join(str(x) for x in go_terms_list) + ' numeric\n'
    attribute3 = '@attribute ' + ' {0,1}\n@attribute '.join(str(x) for x in localizations_list) + ' {0,1}\n\n'
    data1 = '@data'
    data2 = {key: go_terms_array[key] + localizations_array[key] for key in proteins_ids}
    
    output.write(header)
    #output.write(attribute1)
    output.write(attribute2)
    output.write(attribute3)
    output.write(data1)

    for i in proteins_ids:
        line = '\n' + ','.join(str(x) for x in data2[i])
        #line = '\n' + i + ',' + ','.join(str(x) for x in data2[i])
        output.write(line)
    output.close()
 
    return 'Done!'

training_set(1)
training_set(2)
