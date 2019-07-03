import matplotlib.pyplot as plt

def show():
    plt.show()

def bar(x):
    """ Generates a bar graph with the frequencies of letter """
    pos = list(range(len(x[0])))
    width = 0.15
    fig, ax = plt.subplots(figsize=(20,10))
    
    for i in range(len(x)):
        plt.bar([p + i * width for p in pos], x[i], width, alpha=0.5)
        
    ax.set_xticks([p + len(x) * width / 3 for p in pos])
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    labels = [letter for letter in alphabet]
    ax.set_xticklabels(labels)
    
    plt.ylabel('Frequency')
    plt.title('Frequency of letters')
    plt.grid()
    fig.savefig("bargraph_figure.pdf", bbox_inches='tight')


def hist(x):
    """ Generates the histogram """
    label = ["book {}".format(i + 1) for i in range(len(x))]
    plt.hist(x, label=label, alpha=0.5)
    plt.legend()
    plt.title("Frequency histogram among books")
    plt.xlabel("Letter Frequency")
    plt.ylabel("Number of letters with frequency")
    plt.savefig("histogram_figure.pdf")
