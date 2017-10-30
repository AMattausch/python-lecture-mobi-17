# Task 2c: count EcoRI / BamHI cutting sites

seq_list = ["GATTACA", # No cutting site
            "AAAAAAAAGAATTCAAAA", # EcoRI cutting site
            "AAGAATTCAAAGAATTCA", # Two EcoRI cutting sites
            "AAAAAAAGGATCCAAAAA", # BamHI cutting site
            "AAGGATCCAAGAATTCAA",
            "AAGAATTCAAGGATCCGGATCCAA"] # 1x EcoRI, 2x BamHI

ecori = "GAATTC"
bamhi = "GGATCC"

for seq in seq_list:
    print("Current sequence:", seq)
    print("Reverse complementary sequence:",
          seq.replace('A', 't')
             .replace('T', 'a')
             .replace('G', 'c')
             .replace('C', 'g')
             .upper()
             [::-1])
    # Count occurences of cutting sites:
    ecori_counts = seq.count(ecori) # str.count(pattern) counts the occurences of pattern in str
    bamhi_counts = seq.count(bamhi)
    print(f"Sequence contains {ecori_counts} EcoRI cutting site(s) and {bamhi_counts} BamHI cuttting site(s).") # By placing an 'f' in front of the string, you can format it in place with variables! (Python 3.6 required)

