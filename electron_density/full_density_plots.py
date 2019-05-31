#! /usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

def density_import():
    global df
    df = pd.DataFrame()
    #print(df)


    ed=open('ed_full.txt','r')
    ed_full=ed.read()
    ed.close()



    shell=ed_full.split('#')

    line = shell[-1].split('\n')
    radius_list = []
    dens_list = []
    for l in line[1:-1]:
        entry = l.split()
        num=entry[0]
        radius_list.append(float(entry[1]))
        dens_list.append(float(entry[2]))
    radius_series=pd.Series(radius_list)
    dens_series=pd.Series(dens_list)
    df = pd.concat([df,radius_series.rename('radius')], ignore_index=False, axis=1)
    df = pd.concat([df,dens_series.rename('total_density')], ignore_index=False, axis=1)

    for sh in shell[1:-1]:
        line = sh.split('\n')
        orbital = line[0].split()
        radius_list = []
        dens_list = []
        x=orbital[1] + ' ' + orbital[2]
        for l in line[1:-1]:
            entry = l.split()
            num=entry[0]
            #print(type(float(entry[1])))
            #radius_list.append(entry[1])
            dens_list.append(float(entry[2]))
        #radius_series=pd.Series(radius_list)
        dens_series=pd.Series(dens_list)
        df = pd.concat([df,dens_series.rename(x)], ignore_index=False, axis=1)

    #print(df)
    #plt.figure()
    #df.plot(x='radius', y='total_density')
    #plt.show()

def nr_import():
    global dfnr
    dfnr = pd.DataFrame()
    #print(df)


    ed=open('ed_nr.out','r')
    ed_nr=ed.read()
    ed.close()



    shell=ed_nr.split('#')

    line = shell[-1].split('\n')
    radius_list = []
    dens_list = []
    for l in line[1:-1]:
        entry = l.split()
        num=entry[0]
        radius_list.append(float(entry[1]))
        dens_list.append(float(entry[2]))
    radius_series=pd.Series(radius_list)
    dens_series=pd.Series(dens_list)
    dfnr = pd.concat([dfnr,radius_series.rename('radius')], ignore_index=False, axis=1)
    dfnr = pd.concat([dfnr,dens_series.rename('total_density')], ignore_index=False, axis=1)

    for sh in shell[1:-1]:
        line = sh.split('\n')
        orbital = line[0].split()
        radius_list = []
        dens_list = []
        x=orbital[1] + ' ' + orbital[2]
        for l in line[1:-1]:
            entry = l.split()
            num=entry[0]
            #print(type(float(entry[1])))
            #radius_list.append(entry[1])
            dens_list.append(float(entry[2]))
        #radius_series=pd.Series(radius_list)
        dens_series=pd.Series(dens_list)
        dfnr = pd.concat([dfnr,dens_series.rename(x)], ignore_index=False, axis=1)

    #print(df)
    #plt.figure()
    #df.plot(x='radius', y='total_density')
    #plt.show()

def All_shell_density_plot():

    csfont = {'fontname':'Comic Sans MS'}
    hfont = {'fontname':'Helvetica'}
    CMUfont = {'fontname': 'cmr10','size':'x-large'}
    CMUmath = {'fontname': 'cmmi10','size':'large'}

    # x=df.radius/(0.000268)
    # y= 4*(np.pi)*df.total_density


    for column in df[2:]:
        x=df['radius']/(0.000268)
        y= 4*(np.pi)*df[column]
        line, = plt.plot(x,y,  label=column)



    plt.xscale('log')
    plt.axis([0.001, 100000, -10, 2000])
    plt.tick_params(labelsize='large')

    plt.ylabel(r'$4 \pi \rho(r) r^2$ (a.u.)', **CMUfont)
    plt.xlabel(r'$r/a_B$', **CMUfont)
    plt.legend(loc='upper left' , fontsize='x-large')


    plt.show()
    #plt.savefig('electron_density.eps', format='eps', dpi=1000)



def full_density_plot():

    csfont = {'fontname':'Comic Sans MS'}
    hfont = {'fontname':'Helvetica'}
    CMUfont = {'fontname': 'cmr10','size':'x-large'}
    CMUmath = {'fontname': 'cmmi10','size':'large'}

    xr=df.radius/(0.000268)
    yr= 4*(np.pi)*df.total_density
    liner, = plt.plot(xr,yr,  label='relativitic')

    xnr=dfnr.radius/(0.000268)
    ynr= 4*(np.pi)*dfnr.total_density
    linenr, = plt.plot(xnr,ynr,  label='non-relativitic')

    plt.xscale('log')
    plt.axis([0.001, 100000, -10, 2000])
    plt.tick_params(labelsize='large')

    plt.ylabel(r'$4 \pi \rho(r) r^2$ (a.u.)', **CMUfont)
    plt.xlabel(r'$r/a_B$', **CMUfont)
    plt.legend(loc='upper left' , fontsize='x-large')


    plt.show()
    #plt.savefig('electron_density.eps', format='eps', dpi=1000)




def main():
    density_import()
    nr_import()
    full_density_plot()


if __name__ == "__main__":
    main()
