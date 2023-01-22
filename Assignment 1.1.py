#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment 1
Submitted By: Md Mehedee Zaman Khan
Matrikel-Nr.: 665630
Email: mehedee.zaman95@gmail.com
"""

""" Import modules"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

""" Function definitions"""
def main():
    """
    Function for creating the 3d plot
    """
    
    """ Define base coordinates"""
    K_2D = np.arange(0, 100, 1)
    L_2D = np.arange(0, 100, 1)
    K_3D, L_3D = np.meshgrid(K_2D, L_2D)
    
    """ Define parameters"""
   
    
    """ Compute function"""
    F_1 = 400 * (K_3D**(1/4)) * (L_3D**(1/3))
    F_2 = K_3D**(-0.5) * L_3D**(0.5)
    
    
    """ Plot function 1"""
    """ Prepare figure"""
    fig_1 = plt.figure()
    """ Prepare 3d Axis"""
    ax_1 = Axes3D(fig_1)
    ax_1 = fig_1.gca(projection='3d')
    """ Plot the 3d function, using colormap 'turbo'"""
    ax_1.plot_surface(K_3D, L_3D, F_1, cmap='turbo')
    """Label the axes and the figure"""
    ax_1.set_xlabel("Capital(K)")
    ax_1.set_ylabel("Labor (L)")
    ax_1.set_zlabel("F")
    ax_1.set_title("Y(K, L) = 400 * 4√K * 3√L")
    """ use method ax.view_init for changing the angle of the plot """
    ax_1.view_init(azim = 120)
    
    
    """Plot function 2"""
    """Prepare figure"""
    fig_2 = plt.figure()
    """ Prepare 3d Axis"""
    ax_2 = Axes3D(fig_2)
    ax_2 = fig_2.gca(projection='3d')
    """ Plot the 3d function, using colormap 'turbo'"""
    ax_2.plot_surface(K_3D, L_3D, F_2, cmap='turbo')
    """Label the axes and the figure"""
    ax_2.set_xlabel("Capital(K)")
    ax_2.set_ylabel("Labor (L)")
    ax_2.set_zlabel("F")
    ax_2.set_title("Y(K, L) = K**(−0.5) * L**0.5")
    """ use method ax.view_init for changing the angle of the plot """
    ax_2.view_init(azim = 110)
    
    
    """ Optimize usage of space in the figure"""
    plt.tight_layout()
    
    """ Save figure as pdf"""
    plt.savefig("functions_3d_plots.pdf")
    
    """ Show figure"""
    plt.show()

""" Main entry point"""
if __name__ == '__main__':
    main()