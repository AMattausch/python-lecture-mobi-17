import matplotlib.pyplot as plt
import pandas as pd

def pandasPlotMethHistogram(cpg_file_path, plot_path):
    # Load methylation data as dataframe, make sure to set the separator as '\t' (default is a comma)
    # Set header = None so the first line wont be used as a header 
    df = pd.read_csv(cpg_file_path, sep='\t', header=None)
    # Since we have no header, access the second column by number
    meth_list = df[2]
    plt.hist(meth_list, bins=50) # Create the plot
    plt.xlabel("methylation value")
    plt.ylabel("frequency")
    plt.title("CpG methylation frequency")
    plt.savefig(plot_path)
    
def pandasPlotMeanMethBoxPlot(cpg_file_path):
    df = pd.read_csv(cpg_file_path, sep='\t', header=None)
    mean_meth_list = df[4]
    plt.boxplot(mean_meth_list)
    plt.ylabel("methylation value")
    plt.title("Promotor mean Methylation")        

