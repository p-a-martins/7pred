from getSequence import *
from getHomologous import *
######################################################################################################################
### GET GO TERMS
######################################################################################################################
def getGO_terms(protein_id):
    infile = open('data/go_terms/proteins2go.txt','r')
    indata = infile.read().splitlines()
    infile.close()
    result = []
    for i in indata:
        x = i.split(',')
        if x[0] == protein_id:
            result = x[1:]

    return result

####################################################################################################################
# GO TERMS ARRAY
####################################################################################################################
def go_terms2array(proteins_ids, extraction):
    # Extraction: 1 - GO_terms_mEN; 2 - GO_terms_mLASSO

    # GO TERMS LIST
    if extraction == 1:
        infile = open('data/go_terms/T-B2_go_terms.txt','r')
        indata = infile.readline()
        infile.close()
        go_terms_list = indata.split(' ')
        
    if extraction == 2:
        infile = open('data/go_terms/T-C2_go_terms.txt','r')
        indata = infile.readline()
        infile.close()
        go_terms_list = indata.split(' ')

    protein2go_terms = {}
    
    # GO TERMS EXTRACTION
    for protein_id in proteins_ids:
        result = getGO_terms(protein_id)
        results = list(set(go_terms_list).intersection(result))
        
        # BLAST
        if len(results) == 0:
            sequence = getSequence(protein_id)
            if sequence is True:
                homologous = getHomologous(protein_id, sequence)
                k = 0
                kmax = len(homologous)-1
                while k < kmax:
                    result = getGO_terms(homologous[k])
                    results = list(set(go_terms_list).intersection(result))
                    if len(results) == 0:
                        k += 1
                    else:
                        break
            else:
                pass

        if len(results) == 0:
            pass
        else:  
            protein2go_terms[protein_id] = result

    # VECTOR CONSTRUCTION
    protein2go_terms_array = {}
    for ids, go_terms in protein2go_terms.iteritems():
        array = [0]*len(go_terms_list)
        for go_term in go_terms_list:
            if go_term in go_terms:
                array[go_terms_list.index(go_term)] = go_terms.count(go_term)

        protein2go_terms_array[ids] = array

    return [go_terms_list, protein2go_terms_array]
