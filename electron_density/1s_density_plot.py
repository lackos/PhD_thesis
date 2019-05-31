#! /usr/bin/env python3

# Imports and plots relativistic data for Og and Rn spectrum.

import matplotlib.pyplot as plt
import numpy as np
import math

def density_import():
    global radr1s
    global densr1s
    global radr2s
    global densr2s
    global radr2p
    global densr2p
    global radr3s
    global densr3s
    radr1s = (np.loadtxt('1s_ed.txt', usecols=(1), comments='#'))/(0.000268)
    densr1s = 4*(np.pi)*np.loadtxt('1s_ed.txt', usecols=(2), comments='#')
    radr2s = (np.loadtxt('2s_ed.txt', usecols=(1), comments='#'))/(0.000268)
    densr2s = 4*(np.pi)*np.loadtxt('2s_ed.txt', usecols=(2), comments='#')
    radr2p = (np.loadtxt('2p_ed.txt', usecols=(1), comments='#'))/(0.000268)
    densr2p = 4*(np.pi)*np.loadtxt('2p_ed.txt', usecols=(2), comments='#')
    radr3s = (np.loadtxt('3s_ed.txt', usecols=(1), comments='#'))/(0.000268)
    densr3s = 4*(np.pi)*np.loadtxt('3s_ed.txt', usecols=(2), comments='#')

def Whole_plot():

    csfont = {'fontname':'Comic Sans MS'}
    hfont = {'fontname':'Helvetica'}
    CMUfont = {'fontname': 'cmr10','size':'x-large'}
    CMUmath = {'fontname': 'cmmi10','size':'large'}


    one_s_line, =  plt.plot(radr1s, densr1s, 'b-', label='1s')
    two_s_line, = plt.plot(radr2s, densr2s, 'r--', label='2s')
    two_p_line, =  plt.plot(radr2p, densr2p, 'b-', label='2p')
    three_s_line, = plt.plot(radr3s, densr3s, 'r--', label='3s')
    plt.xscale('log')
    plt.axis([0.001, 100000, -10, 4*(np.pi)*270])
    plt.tick_params(labelsize='large')

    plt.ylabel(r'$4 \pi \rho(r) r^2$ (a.u.)', **CMUfont)
    plt.xlabel(r'$r/a_B$', **CMUfont)
    # first peak

    plt.legend(loc='upper left' , fontsize='x-large')


    plt.show()
    #plt.savefig('Ogplot.eps', format='eps', dpi=1000)


def Zoom_plot():

    csfont = {'fontname':'Comic Sans MS'}
    hfont = {'fontname':'Helvetica'}
    CMUfont = {'fontname': 'cmr10', 'size':'x-large'}
    CMUmath = {'fontname': 'cmmi10'}



    plt.xscale('log')
    plt.axis([1000, 20000, -9, 4*(np.pi)*90])
    plt.tick_params(labelsize='large')

    plt.ylabel(r'$4\pi \rho(r) r^2$ (a.u.)', **CMUfont)
    plt.xlabel(r'$r/a_B$', **CMUfont)
    #6th peak
    plt.annotate(r'n=6', xy=(4000, 4*(np.pi)*27.799), xytext=(4400, 4*(np.pi)*27.799),
            arrowprops={'arrowstyle':'-', 'color':'w'}, **CMUfont
            )
    #7th peak
    plt.annotate(r'n=7', xy=(10000, 4*(np.pi)*4.8705), xytext=(10000, 4*(np.pi)*8),
            arrowprops={'arrowstyle':'-', 'color':'w'}, **CMUfont
            )
    plt.legend(loc='upper right', fontsize='x-large')



    plt.savefig('Ogplot_zoom.eps', format='eps', dpi=1000)



def main():
    density_import()
    Whole_plot()


if __name__ == "__main__":
    main()
