def annot_max(S,G, a, b, ax=None):
    """

    :param S: throughput of 5 access mode
    :param G: Offered Load
    :param a: plot label x_axis
    :param b: plot label y_axis
    :param ax: null
    :return: null
    """
    ymax = max(S)
    xpos = S.index(ymax)
    xmax = G[xpos]
    text= "G={:.3f}, S={:.3f}".format(xmax, ymax)
    if not ax:
        ax=plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60")
    kw = dict(xycoords='data',textcoords="axes fraction",
              arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
    ax.annotate(text, xy=(xmax, ymax), xytext=(a,b), **kw)