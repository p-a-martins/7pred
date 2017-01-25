######################################################################################################################
### GET PROTEIN SEQUENCE
######################################################################################################################
def getSequence(protein_id):
    inputfile = open('data/blast/uniprot-human.fasta','r')
    indata = inputfile.read().splitlines()
    inputfile.close()
    sequence = False
    outputfile = open('data/blast/sequence.txt','wb')
    
    for i in range(len(indata)):
        x = '>sp|'+ protein_id + '|'
        y = '>tr|'+ protein_id + '|'
        if indata[i].startswith(x) or indata[i].startswith(y):
            line = indata[i]
            outputfile.write(line)
            y=i+1
            for i in range(len(indata)):
                if indata[y].startswith('>sp|') or indata[y].startswith('>tr|'):
                    break
                else:
                    line = '\n' + indata[y]
                    outputfile.write(line)
                    y+=1
                    sequence = True
                    
    return sequence
