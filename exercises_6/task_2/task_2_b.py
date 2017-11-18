# Task 2b: count amino acids per category for each protein in given fasta file
import sys

# Function to get amino acid statistics
def get_aa_stats_per_protein(fasta):
    
    aa_stats_per_protein = []

    # Define aa cetgory dict
    aa_categories = {"aliphatic":"GAVLI",
                     "hydrsulf" :"SCTM",
                     "cyclic"   :"P",
                     "aromatic" :"FYW",
                     "basic"    :"HKR",
                     "acidic"   :"DNEQ"}
    
    # Define aa statistics dict
    aa_stats = {cat:0 for cat in aa_categories.keys()}
    prot_name = None

    with open(fasta, mode='r') as fasta_file:
        for line in fasta_file:
            if line[0] == '>': 
                # If the loop hits a comment line (and therefore a new protein sequence),
                # append the stats to aa_stats_per_protein and reset aa_stats                
                if prot_name: # Only do this
                    aa_stats_per_protein.append([prot_name, aa_stats])
                aa_stats = {cat:0 for cat in aa_categories.keys()}  
                prot_name = line.lstrip('>').rstrip('\n')
            else:
                for aa in line.rstrip('\n'):
                    for category, cat_aa in aa_categories.items(): 
                        # For category, check if the AA is in the categorie's associated string
                        if aa.upper() in cat_aa:
                            aa_stats[category] += 1
        else: # Save final protein sequence
            aa_stats_per_protein.append([prot_name, aa_stats])
           
    return aa_stats_per_protein

# Call get_aa_stats function, print results
fasta_path = sys.argv[1]
aa_stats_per_protein = get_aa_stats_per_protein(fasta_path)

for prot_name, aa_stats in aa_stats_per_protein:
    print(f"\nAA stats for {prot_name}:",
          f"Total amount of amino acids: {sum(aa_stats.values())}",
          f"Aliphatic AA: {aa_stats['aliphatic']}",
          f"Hydroxyl/sulfur-containing AA: {aa_stats['hydrsulf']}",
          f"Cyclic AA: {aa_stats['cyclic']}",
          f"Aromatic AA: {aa_stats['aromatic']}",
          f"Basic AA: {aa_stats['basic']}",
          f"Acidic AA: {aa_stats['acidic']}",
          sep = '\n')

