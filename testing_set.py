from getGO_Terms import *
######################################################################################################################
### TESTITNG SET
######################################################################################################################
def testing_set(proteins_ids, extraction):

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

    localizations_array = ['?']*14
    go_terms = go_terms2array(proteins_ids, extraction)
    go_terms_list = go_terms[0]
    go_terms_array = go_terms[1]

    if extraction == 1:
        relation = 'testing_t-b2'
        output = open('data/datasets/P-B2.arff','w')  
    if extraction == 2:
        relation = 'testing_t-c2'
        output = open('data/datasets/P-C2.arff','w')

    # OUTPUT       
    header = "@relation '" + relation + ": -C -14'\n\n"
    attribute1 = "@attribute id string\n"
    attribute2 = '@attribute ' + ' numeric\n@attribute '.join(str(x) for x in go_terms_list) + ' numeric\n'
    attribute3 = '@attribute ' + ' {0,1}\n@attribute '.join(str(x) for x in localizations_list) + ' {0,1}\n\n'
    data1 = '@data'
    data2 = {key: go_terms_array[key] + localizations_array for key in go_terms_array}
    
    output.write(header)
    #output.write(attribute1)
    output.write(attribute2)
    output.write(attribute3)
    output.write(data1)

    for i in proteins_ids:
        if i in data2.keys():
            line = '\n' + ','.join(str(x) for x in data2[i])
            #line = '\n' + i + ',' + ','.join(str(x) for x in data2[i])
            output.write(line)
        else:
            proteins_ids.remove(i)
    output.close()
 
    return 'Done!'
