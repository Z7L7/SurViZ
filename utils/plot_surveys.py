from matplotlib.patches import Circle
import numpy as np
import sys
sys.path.append('../utils/')

from utils.diverse_utils import init_sky, projection_dec, projection_ra #eq2gal, ecl2gal


def rad(x):
    return x*np.pi/180

def plot_Euclid_Deep_Survey(fig, ax):

    edfn_ra = np.array([269.73])
    edfn_dec = np.array([66.01])
    edfn = Circle((ax.projection_ra(edfn_ra), ax.projection_dec(edfn_dec)), np.sqrt(20/(np.pi))*np.pi/180, ls='--', edgecolor='black', facecolor='blue', label='Euclid Deep')
    ax.add_patch(edfn)

    fornax_ra = np.array([52.93583333]) 
    fornax_dec = np.array([-28.08850000])    
    fornax = Circle((ax.projection_ra(fornax_ra), ax.projection_dec(fornax_dec)), rad(np.sqrt(10/(np.pi))), ls='--', edgecolor='black', facecolor='blue')
    ax.add_patch(fornax)

    edfs_ra= np.array([61.241])
    edfs_dec = np.array([-48.42300000])
    edfs = Circle((ax.projection_ra(edfs_ra), ax.projection_dec(edfs_dec)), rad(np.sqrt(10/(np.pi))), ls='--', edgecolor='black', facecolor='blue')

    ax.add_patch(edfs)
    return ax

def shift(key, array):
    return array[-key:] + array[:-key]

def eq2plot(y, shift=85):
    if (360-shift) >= y >= 0:
        x = -(y - shift)
    elif 360 > y > (360-shift):
        x = 360 - y + shift
    # print(x)
    return rad(x)

def gal2plot(y, shift=102):
    if (360-shift) >= y >= 0:
        x = -(y - shift)
    elif 360 > y > (360-shift):
        x = 360 - y + shift
    # print(x)
    return rad(x)

def plot_Euclid_Wide_Survey(fig, ax, ecl_ra, ecl_dec, gal_ra, gal_dec):

    # North Hole
    s, e = 10, 26
    margin = np.linspace(50, 20, e-s)
    # ax.plot(ax.projection_ra(gal_ra[s:e]), ax.projection_dec(gal_dec[s:e])-rad(margin), color='blue')
    ax.fill(ax.projection_ra(gal_ra[s:e]), ax.projection_dec(gal_dec[s:e])-rad(margin), alpha=0.3, color='blue')
    
    # South Hole
    s, e = 55, 75
    margin = np.linspace(45, 25, e-s)
    # ax.plot(ax.projection_ra(gal_ra[s:e]), ax.projection_dec(gal_dec[s:e])+rad(margin), color='blue')
    ax.fill(ax.projection_ra(gal_ra[s:e]), ax.projection_dec(gal_dec[s:e])+rad(margin), alpha=0.3, color='blue')
    
    # South East
    s, e, margin = 10, 84, 9.8
    # ax.plot(ax.projection_ra(ecl_ra[s:e]), ax.projection_dec(ecl_dec[s:e])-rad(margin), color='blue')
    ax.fill_between(ax.projection_ra(ecl_ra[s:e]), ax.projection_dec(ecl_dec[s:e])-rad(10), rad(-90), alpha=0.3, color='blue')
    
    s, e, margin = 32, 61, 28
    # ax.plot(ax.projection_ra(gal_ra[s:e]), ax.projection_dec(gal_dec[s:e])-rad(margin), color='blue')
    
    ax.fill_between(ax.projection_ra(gal_ra[s:e]), ax.projection_dec(gal_dec[s:e])-rad(margin), rad(-90), alpha=0.3, color='blue')

    # North West
    s, e, margin = 100, 190, 12
    # ax.plot(ax.projection_ra(ecl_ra[s:e]), ax.projection_dec(ecl_dec[s:e])+rad(margin), color='blue')
    ax.fill_between(ax.projection_ra(ecl_ra[s:e]), ax.projection_dec(ecl_dec[s:e])+rad(margin), rad(90), alpha=0.3, color='blue')
    
    return ax

def plot_HST_cosmos_Survey(fig, ax):
    cosmos_ra = np.array([150.11916667])
    cosmos_dec= np.array([2.20583333])

    cosmos = Circle((ax.projection_ra(cosmos_ra), ax.projection_dec(cosmos_dec)), rad(np.sqrt(2/(np.pi))), edgecolor='black', facecolor='orange', alpha=0.5, label=r'HST cosmos (2deg$^2$)')
    zoom_cosmos = Circle((ax.projection_ra(cosmos_ra), ax.projection_dec(cosmos_dec)), rad(np.sqrt(2/(np.pi))), edgecolor='black', facecolor='orange', alpha=0.5, label=r'HST cosmos (2deg$^2$)')
    ax.add_patch(cosmos)
    return ax, zoom_cosmos

def plot_JWST_CEERS_Survey(fig, ax):
    ceers_rad = [96, 59] #eq2gal(14.28, 53)
    ceers = Circle((ceers_rad[0], ceers_rad[1]), rad(np.sqrt((1/6)/(2*np.pi))), edgecolor='black', ls='--', facecolor='red', alpha=0.5, label=r'JWST CEERS (0.02 deg$^2$)')
    zoom_ceers = Circle((ceers_rad[0], ceers_rad[1]), rad(np.sqrt((1/6)/(2*np.pi))), edgecolor='black', facecolor='red', alpha=0.5)
    ax.add_patch(ceers)
    return ax, zoom_ceers

def plot_cosmos_Web_Survey(fig, ax):
    cosmos_ra = np.array([150.11916667])
    cosmos_dec= np.array([2.20583333])

    cosmos = Circle((ax.projection_ra(cosmos_ra), ax.projection_dec(cosmos_dec)), rad(np.sqrt(0.6/(np.pi))), edgecolor='black', facecolor='red', alpha=0.5, label=r'Cosmos-Web (0.6deg$^2$)')
    zoom_cosmos_web = Circle((ax.projection_ra(cosmos_ra), ax.projection_dec(cosmos_dec)), rad(np.sqrt(0.6/(np.pi))), edgecolor='black', facecolor='red', alpha=0.5)
    ax.add_patch(cosmos)
    return ax, zoom_cosmos_web

def plot_Rubin_LSST_Survey(fig, ax):

    ax.fill_between(np.linspace(-180, 180), rad(30), rad(-90), alpha=0.3, color='green', label='Rubin LSST')
    return ax

def plot_HST_CANDELS_Survey(fig, ax, show_name=True):
    # rad_goods-s = 37000 pix = 558'' = 0.3deg
    goods_s_ra = np.array([53])
    goods_s_dec= np.array([-27.8])
    goods_s = Circle((ax.projection_ra(goods_s_ra), ax.projection_dec(goods_s_dec)), rad(np.sqrt(0.3/(np.pi))), edgecolor='black', facecolor='red', alpha=0.5, label=r'HST CANDELS (2.82deg$^2$)')
    ax.add_patch(goods_s)

    # rad_goods-n = same good s
    goods_n_ra = np.array([189])
    goods_n_dec= np.array([62])
    goods_n = Circle((ax.projection_ra(goods_n_ra), ax.projection_dec(goods_n_dec)), rad(np.sqrt(0.3/(np.pi))), edgecolor='black', facecolor='red', alpha=0.5)
    ax.add_patch(goods_n)

    # rad EGS = 22673 = 0.12deg
    EGS_ra = np.array([214.8])
    EGS_dec= np.array([52.8])
    EGS = Circle((ax.projection_ra(EGS_ra), ax.projection_dec(EGS_dec)), rad(np.sqrt(0.12/(np.pi))), edgecolor='black', facecolor='red', alpha=0.5)
    ax.add_patch(EGS)

    # rad UDS = 19829 = 0.16deg
    UDS_ra = np.array([34])
    UDS_dec= np.array([-5.2])
    UDS = Circle((ax.projection_ra(UDS_ra), ax.projection_dec(UDS_dec)), rad(np.sqrt(0.11/(np.pi))), edgecolor='black', facecolor='red', alpha=0.5)
    ax.add_patch(UDS)

    # rad UDS = 19829 = 0.16deg
    cosmos_ra = np.array([150.11916667])
    cosmos_dec= np.array([2.20583333])
    cosmos = Circle((ax.projection_ra(cosmos_ra), ax.projection_dec(cosmos_dec)), rad(np.sqrt(2/(np.pi))), edgecolor='black', facecolor='red', alpha=0.5, label=r'Cosmos-Web (0.6deg$^2$)')
    ax.add_patch(cosmos)

    if show_name:
        ax.text(ax.projection_ra(goods_s_ra), ax.projection_dec(goods_s_dec)+rad(1),'GOODS-S', color='red')
        ax.text(ax.projection_ra(goods_n_ra), ax.projection_dec(goods_n_dec)+rad(1),'GOODS-N', color='red')
        ax.text(ax.projection_ra(UDS_ra), ax.projection_dec(UDS_dec)+rad(1),'UDS', color='red')
        ax.text(ax.projection_ra(EGS_ra), ax.projection_dec(EGS_dec)+rad(1),'EGS', color='red')
        ax.text(ax.projection_ra(cosmos_ra), ax.projection_dec(cosmos_dec)+rad(1.5),'COSMOS', color='red')

    return ax
