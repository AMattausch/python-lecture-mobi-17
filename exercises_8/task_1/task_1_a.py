# Task 1a: implement plotting module
import sys
import cpgplotting as cgp
import matplotlib.pyplot as plt

cpg_file_path_1 = sys.argv[1]
cpg_file_path_2 = sys.argv[2]
cpg_plot_path = sys.argv[3]

plt.subplot(1, 2, 1)
cgp.plotMeanMethBoxPlot(cpg_file_path_1)

plt.subplot(1, 2, 2)
cgp.plotMeanMethBoxPlot(cpg_file_path_2)

plt.savefig(cpg_plot_path)