# Task 2a: count amino acids per category for whole fasta file
import sys

# Function to get amino acid statistics
def get_aa_stats(fasta):
    # Define aa statistics dict
    aa_stats = {"aliphatic":0,
                "hydrsulf" :0,
                "cyclic"   :0,
                "aromatic" :0,
                "basic"    :0,
                "acidic"   :0,
                "total"    :0}

    # Define aa cetgory dict
    aa_categories = {"aliphatic":"GAVLI",
                     "hydrsulf" :"SCTM",
                     "cyclic"   :"P",
                     "aromatic" :"FYW",
                     "basic"    :"HKR",
                     "acidic"   :"DNEQ"}

    with open(fasta, mode='r') as fasta_file:
        for line in fasta_file:
            if line[0] == '>': # Take care of comment lines
                continue
            else:
                for aa in line.rstrip('\n'):
                    for category, cat_aa in aa_categories.items(): 
                        # For category, check if the AA is in the categorie's associated string
                        if aa.upper() in cat_aa:
                            aa_stats[category] += 1
                            aa_stats["total"]  += 1
    return aa_stats

# Call get_aa_stats function, print results
fasta_path = sys.argv[1]
aa_stats = get_aa_stats(fasta_path)

print(f"Total amount of amino acids: {aa_stats['total']}",
      f"Aliphatic AA: {aa_stats['aliphatic']}",
      f"Hydroxyl/sulfur-containing AA: {aa_stats['hydrsulf']}",
      f"Cyclic AA: {aa_stats['cyclic']}",
      f"Aromatic AA: {aa_stats['aromatic']}",
      f"Basic AA: {aa_stats['basic']}",
      f"Acidic AA: {aa_stats['acidic']}",
      sep='\n')

