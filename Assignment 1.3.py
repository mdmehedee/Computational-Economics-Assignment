#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment 1
Submitted By: Md Mehedee Zaman Khan
Matrikel-Nr.: 665630
Email: mehedee.zaman95@gmail.com

"""
""" Import modules """
import numpy as np
import matplotlib.pyplot as plt


""" Function definitions """
    
    
def plot_four_slices(L_value_1, L_value_2, L_value_3, L_value_4):
    """ plots four slices of the function"""
    """ Create coordinates data """
    K_values = np.arange(0, 1000, 1)
    F_values_1 = 400 * (K_values**(1/4)) * (L_value_1**(1/3))
    F_values_2 = 400 * (K_values**(1/4)) * (L_value_2**(1/3))
    F_values_3 = 400 * (K_values**(1/4)) * (L_value_3**(1/3))
    F_values_4 = 400 * (K_values**(1/4)) * (L_value_4**(1/3))
    
    """ Create four subplots """
    fig, ax = plt.subplots(nrows=2, ncols=2, squeeze=False)
    
    """Slice 1 subplots"""
    ax[0,0].plot(K_values, F_values_1, label="L = " + str(L_value_1))
    ax[0,0].set_xlabel("K")
    ax[0,0].set_ylabel("F")
    ax[0,0].set_title("Slice 1 for L = " + str(L_value_1))
    ax[0,0].set_ylim([0,1000000])
    ax[0,0].legend()
    
    """Slice 2 subplots"""
    ax[0,1].plot(K_values, F_values_2, label="L = " + str(L_value_2))
    ax[0,1].set_xlabel("K")
    ax[0,1].set_ylabel("F")
    ax[0,1].set_title("Slice 2 for L = " + str(L_value_2))
    ax[0,1].set_ylim([0,1000000])
    ax[0,1].legend()
    
    """Slice 3 subplots"""
    ax[1,0].plot(K_values, F_values_3, label="L = " + str(L_value_3))
    ax[1,0].set_xlabel("K")
    ax[1,0].set_ylabel("F")
    ax[1,0].set_title("Slice 3 for L = " + str(L_value_3))
    ax[1,0].set_ylim([0,1000000])
    ax[1,0].legend()
    
    """Slice 4 subplots"""
    ax[1,1].plot(K_values, F_values_4, label="L = " + str(L_value_4))
    ax[1,1].set_xlabel("K")
    ax[1,1].set_ylabel("F")
    ax[1,1].set_title("Slice 4 for L = " + str(L_value_4))
    ax[1,1].set_ylim([0,1000000])
    ax[1,1].legend()
    
    """Optimize usage of space in the figure"""
    plt.tight_layout()

    """ Save figure as pdf """
    plt.savefig("function_2d_plots.pdf")

    """ Show figure """
    plt.show()
    

""" Main entry point """
if __name__ == '__main__':
    L_value_1 = 0
    L_value_2 = 10000
    L_value_3 = 1000000
    L_value_4 = 100000000
    plot_four_slices(L_value_1, L_value_2, L_value_3, L_value_4)


