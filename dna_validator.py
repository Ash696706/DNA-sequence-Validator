DNA = "ATGCATGGCATGCCAA"
valid = True
for base in DNA:
  if base != "A" and base != "T" and base != "G" and base != "C":
    valid = False
if valid:
  print("Valid DNA sequence")
else:
  print("Invalid DNA sequence")
