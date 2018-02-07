from utils import *
from ipywidgets import interact

def load_and_prepare_cmd(filename,verbose=False): # (g, gr) = load_and_prepare_cmd('fieldA.csv')
    """ 
    Loads in data. Returns pandas Series of g-r and r respectively.
    """
    FIELD = pd.read_csv("fieldA.csv")
    g = FIELD["g"] # probs slower than inital idea
    gr = g - FIELD["r"]
    mask = (g>14) & (g<24) & (gr>-0.5) & (gr<2.5)
    if verbose:
        print("Length of g and gr are {0:d} and {1:d} respectively".format(len(g),len(gr)))
    return gr.where(mask), g.where(mask)
    
def interactive_hess(gr,g):
    """
    Returns interactive HESS plot.
    """
    def plot(size=100):
        fig,ax = plt.subplots()
        fig.set_size_inches(8,6)
        ax.hexbin(gr, g, gridsize=size, bins='log', cmap='inferno', label="Relative stellar density")
        ax.set_title("HESS DIAGRAM, gridsize={0:d}".format(size), fontsize = 15)
        ax.set_xlabel(r"$g-r$",fontsize = 25)
        ax.set_ylabel(r"$g$",fontsize = 25)
        ax.legend(loc='upper left')
        ax.set_ylim(ax.get_ylim()[::-1])
        plt.show()
    interact(plot, size=(50,300,1),continuous_update=False);