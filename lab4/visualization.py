from matplotlib import pylab
import matplotlib.pyplot as plt
import seaborn as sns


def display_three_graphs(x1, x2, x3, label1, label2, label3):
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(7, 4))

    ax1.plot(range(len(x1)), x1, label=label1, color='red')
    ax1.set_title(label1)
    ax2.plot(range(len(x2)), x2, label=label2, color='blue')
    ax2.set_title(label2)
    ax3.plot(range(len(x3)), x3, label=label3, color='green')
    ax3.set_title(label3 )
    plt.tight_layout()
    plt.show()



def display_hist(array):
    plt.figure(figsize=(6, 4))
    plt.hist(array, bins=30, color='skyblue', edgecolor='black')
    plt.title('Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    plt.show()



def scatter_diagram(array):
    plt.scatter(range(len(array)), array, color='purple', alpha=0.6)
    plt.title('Scatter Diagram')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.grid(True)
    plt.show()



def xyz_array(array):
    fig = pylab.figure()
    ax = fig.add_subplot(projection='3d')
    x = list(range(len(array)))
    ax.bar(x, array, zs=0, zdir='y', color='purple', alpha=0.8)
    ax.set_xlabel('X Time')
    ax.set_ylabel('Y Data')
    ax.set_zlabel('Z quantity')
    pylab.show()
