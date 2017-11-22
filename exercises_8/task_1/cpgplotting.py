import matplotlib.pyplot as plt

def plotMethHistogram(cpg_file_path, plot_path):
    with open(cpg_file_path) as cpg_file:
        # Get the third column of each line as long as its not a header (starting with '#'), cast it as float
        meth_list = [float(line.rstrip('\n').split('\t')[2]) for line in cpg_file if not line[0] == '#'] 
        plt.hist(meth_list, bins=50) # God I hate pyplot
        plt.xlabel("methylation value") # Set the labels
        plt.ylabel("frequency")
        plt.title("CpG methylation frequency")
        plt.savefig(plot_path) # Save the plot#
    
def plotMeanMethBoxPlot(cpg_file_path):
    with open(cpg_file_path) as cpg_file:
        # Get the third column of each line as long as its not a header (starting with '#'), cast it as float
        mean_meth_list = [float(line.rstrip('\n').split('\t')[4]) for line in cpg_file if not line[0] == '#'] 
        plt.boxplot(mean_meth_list)
        plt.ylabel("methylation value") # Set the labels
        plt.title("Promotor mean Methylation")        

