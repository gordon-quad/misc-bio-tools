#!/usr/bin/python2.7

from glob import glob
from Bio import SeqIO
from Bio.Blast.NCBIWWW import qblast
from os.path import splitext, basename

with open('archaea_gis.txt') as f:
    gis = map(lambda x: x.strip(), f.readlines())
    query = " ".join(gis)

for fn in glob('oriC/*.fasta'):
    try:
        print "getting BLAST for %s" % (fn)
        rec = SeqIO.read(fn, 'fasta')
        accid = splitext(basename(fn))[0]
        handle = qblast('blastn', 'chromosome', rec.seq, entrez_query=query)
        with open('blast/' + accid + '.xml', 'w') as alf:
            alf.write(handle.read())
    except Exception as e:
        print "failed %s: %s" % (fn, str(e))

