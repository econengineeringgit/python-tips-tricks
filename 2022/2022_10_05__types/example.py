import logging
import os


import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


def get_color_map(moduleSettings, logger):
    try:
        first_end, second_end, s, l = [int(item) for item in moduleSettings['husl_palette']]
    except TypeError:
        first_end, second_end, s, l = ['289', '260', '66', '36']
        logger.info('Default colors are used for BarrierIntrusion colormap.')
    if moduleSettings['abs_value']:
        cmap = sns.diverging_palette(first_end, second_end, s=s, l=l, as_cmap=True)
    else:
        cmap = sns.light_palette([second_end, s, l], as_cmap=True, input='husl')
    return cmap

def plot_cmap(cmap, filename):
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    fig, ax = plt.subplots(1,1)
    ax.imshow(gradient, aspect='auto', cmap=cmap)
    ax.set_axis_off()
    fig.savefig(filename)

if __name__ == '__main__':
    
    logger = logging.getLogger('main')
    os.makedirs('out', exist_ok=True)
    
    moduleSettings = {'husl_palette': ['289', '260', '66', '36'], 'abs_value':True}
    cmap = get_color_map(moduleSettings, logger)
    plot_cmap(cmap, 'out/cmap_abs.png')
    
    moduleSettings = {'husl_palette': ['289', '260', '66', '36'], 'abs_value':False}
    cmap = get_color_map(moduleSettings, logger)
    plot_cmap(cmap, 'out/cmap.png')

    moduleSettings = {'husl_palette': ['200', '100', '66', '36'], 'abs_value':False}
    cmap = get_color_map(moduleSettings, logger)
    plot_cmap(cmap, 'out/cmap_other.png')