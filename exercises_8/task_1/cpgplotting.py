import matplotlib.pyplot as plt

def plotMethHistogram(cpg_file_path, plot_path):
    with open(cpg_file_path) as cpg_file:
        meth_list = [line.rstrip('\n').split('\t')[2] for line in cpg_file if not line[0] == '#']
        plot = plt.hist(meth_list)
        plot.savefig(plot_path)