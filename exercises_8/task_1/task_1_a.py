# Task 1a: implement plotting module
import sys
import cpgplotting as cgp # Import the custom module, set an alias

cpg_file_path = sys.argv[1]
cpg_plot_path = sys.argv[2]

cgp.plotMethHistogram(cpg_file_path, cpg_plot_path) # Call the modules histrogram method