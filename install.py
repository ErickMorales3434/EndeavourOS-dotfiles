#!/usr/bin/python

from subprocess import run

def pacman():
    apps = ("xclip","kitty", "krita", "rofi", "bspwm", "sxhkd", "polybar", "picom", "feh",
            "xorg-xsetroot", "neovim", "cmus", "lightdm", "lightdm-gtk-greeter", "xcrot",
            "lxappearance-gtk3", "virtualbox", "telegram-desktop", "python-pynvim",
            "obs-studio","playerctl", "vlc", "gparted", "volumeicon",
            "zsh", "ranger", "w3m", "transmission-gtk")

    for app in apps:
        ejecucion = run(["sudo","pacman","-S",app,"--noconfirm"],capture_output=True)
        salida = ejecucion.returncode
        # out = (ejecucion.stdout).decode("utf-8")
        if salida == 0:
            print("{} se  ha instalado...".format(app))
        else:
            print(" {} No se ha instalado".format(app))
            
def aur():
    apps = ("google-chrome","visual-studio-code-bin")
    for app in apps:
        ejecucion = run(["yay","-S",app,"--noconfirm"],capture_output=True)
        salida = ejecucion.returncode        
        if salida == 0:
            print("{} se  ha instalado...".format(app))
        else:
            print(" {} No se ha instalado".format(app))
    
if __name__ == "__main__":
    pacman()
    aur()