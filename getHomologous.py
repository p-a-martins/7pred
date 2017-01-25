import os
######################################################################################################################
### GET HOMOLOGOUS
######################################################################################################################
def getHomologous(protein_id, sequence):
    retval = os.getcwd()
    os.chdir('./data/blast')
    #os.system('makeblastdb -in uniprot-human.fasta -title uniprot -out uniprot -dbtype prot') # database
    os.system('blastp -query sequence.txt -db uniprot -evalue 0.001 -out result.txt -outfmt "10 qseqid sseqid"')
    inputfile = open('result.txt','rb')
    indata = inputfile.read().splitlines()
    inputfile.close()    
    homologous = []
    for i in indata:
        l = i.split('|')
        homologous.append(l[3])
    os.chdir(retval)
    return homologous
