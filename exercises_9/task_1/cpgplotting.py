import matplotlib.pyplot as plt
import pandas as pd

def pandasPlotMethHistogram(cpg_file_path, plot_path):
    df = pd.read_csv(cpg_file_path, sep='\t', header=None)
    meth_list = df[2]
    plt.hist(meth_list, bins=50) # God I hate pyplot
    plt.xlabel("methylation value") # Set the labels
    plt.ylabel("frequency")
    plt.title("CpG methylation frequency")
    plt.savefig(plot_path) # Save the plot#
    
def pandasPlotMeanMethBoxPlot(cpg_file_path):
    df = pd.read_csv(cpg_file_path, sep='\t', header=None)
    mean_meth_list = df[4]
    plt.boxplot(mean_meth_list)
    plt.ylabel("methylation value") # Set the labels
    plt.title("Promotor mean Methylation")        

