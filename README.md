# Python-GC-Content-Calculator

The program read in a text file named "anatolis_dna_sequences.txt", 
that contains DNA sequences of various Anatolis Species -1 per line.

File source: https://www.biointeractive.org/sites/default/files/Anolis-DNA-sequences.txt

Below is an example of the file contents:

>>>Leiocephalus_barahonensis
ATGAGCCCCCTTACAACAACAATTCTACTATCAAGCTTAGCAACCGGCACCATCATTACAGCCACAAGCT
ATCACTGACTATTAGCTTGAATTGGCCTTGAACTAAACACATTAGCTATCATTCCAATTATCTCAAAACA
ACATCACCCCCGAGCGACAGAGGCCGCCACCAAGTACTTCTTAACTCAAGCAGCTGCTTCAGCACTAATC
...

>>>Anolis_alutaceus
TCCATTGATTAATGGCCTGANTCGGATTAGANATCAATACACTATCAATTATTCCAATAATTTCAACATT
ACACCACCCACGATCAACTGAAGCTGCTACAAAATATTTCCTCACCCAAGCAGCTGCTTCANCTTTAATC
CTTTTTTCAAGCACAATTAATGCCTGACAAACAGGATCATGAGACATTACCCAACTATCATCAACCCCCT
...

The program then calculate the GC content for each sequence, and only print out the highest GC content value.

"In molecular biology and genetics, GC-content (or guanine-cytosine content) is the percentage of nitrogenous 
bases in a DNA or RNA molecule that are either guanine (G) or cytosine (C).  
This measure indicates the proportion of G and C bases out of an implied four total bases, 
also including adenine and thymine in DNA and adenine and uracil in RNA." - https://en.wikipedia.org/wiki/GC-content
