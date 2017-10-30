# Task 2a: check for EcoRI / BamHI cutting sites

seq_list = ["GATTACA", # No cutting site
            "AAAAAAAAGAATTCAAAA", # EcoRI cutting site
            "AAAAAAAGGATCCAAAAA", # BamHI cutting site
            "AAGGATCCAAGAATTCAA"] # Cutting sites for both

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
    # Check for EcoRI cutting sites:
    if ecori in seq:
        print("Sequence contains EcoRI cutting site")
    else:
        print("Sequence contains no EcoRI cutting site")

    # Check for EcoRI cutting sites:
    if bamhi in seq:
        print("Sequence contains BamHI cutting site")
    else:
        print("Sequence contains no BamHI cutting site")