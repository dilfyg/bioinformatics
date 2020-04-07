# import packages
from Bio.Seq import Seq
import os
from Bio.Alphabet import generic_dna

# set wd on laptop
#os.chdir('C:/Users/barke/Documents/2020/Github-Repositories/Bioinformatics')
# set wd on pc
os.chdir('C:/Users/barke/Documents/2020/Coding and Stats/Github-Repositories/Bioinformatics')

# load the sequence
from Bio import SeqIO
for record in SeqIO.parse("genome.fasta", "fasta"):
    genome_id  = record.id
    genome_seq = record.seq

### id gives the id of the genome, whilst seq is the fill sequence

# translate the sequence
genome_translated_seq = genome_seq.translate()

# load in the spike protein translated sequence from the .fasta file in the directory
for record in SeqIO.parse("spike.fasta", "fasta"):
    spike_id  = record.id
    spike_translated_seq = record.seq

# blast
from Bio.Blast.Applications import NcbiblastxCommandline

blastx_cline = NcbiblastxCommandline(query="spike.fasta", db="nr", evalue=0.001, outfmt=5, out="spike.xml")
blastx_cline = NcbiblastxCommandline(cmd='C:/Program Files/NCBI/blast-2.10.0+/bin/blastx.exe', out='spike.xml', outfmt=5, query='spike.fasta', db='nr', evalue=0.001)
print(blastx_cline)
stdout, stderr = blastx_cline()


