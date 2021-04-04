with open("Week 3/anolis_dna_sequences.txt", "r") as dna_sequence:
    dna_sequence = dna_sequence.readlines()
    print(len(dna_sequence))

gc_contents = []

for line in dna_sequence:
    gc_content = 0
    #if line[0] != ">":
    for nucleotide in line:
        if nucleotide == "G" or nucleotide == "C":
            gc_content += 1
    gc_contents.append(gc_content)
    
print(gc_contents)
print(len(gc_contents))
print(max(gc_contents))