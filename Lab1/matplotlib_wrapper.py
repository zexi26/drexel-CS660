import matplotlib.pyplot as plt


def hist(x):
    pos = list(range(len(x[0])))
    width = 0.15
    fig, ax = plt.subplots(figsize=(20, 10))
    
    for i in range(len(x)):
        plt.bar([p + i * width for p in pos], x[i], width, alpha=0.5)
        
    ax.set_xticks([p + len(x) * width / 3 for p in pos])
    ax.set_xticklabels(
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z'])
    
    plt.ylabel('Frequency')
    plt.title('Frequency of letters')
    plt.grid()
    plt.show()
    
