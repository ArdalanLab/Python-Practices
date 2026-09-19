
#script to give out the position of every "gt" in the sequence
rna = input("Enter your sequence: ")

for i in range(len(rna) - 1):
    if rna[i:i+2] == "AUG":
        print(f"'AUG' found at position {i}")