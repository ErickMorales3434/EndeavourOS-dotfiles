#!/usr/bin/python

from subprocess import run

def pacman():
    apps = ("xclip","kitty", "krita", "rofi", "bspwm", "sxhkd", "polybar", "picom", "feh",
            "xorg-xsetroot", "neovim", "cmus", "lightdm", "lightdm-gtk-greeter", "scrot",
            "lxappearance-gtk3", "virtualbox", "telegram-desktop", "python-pynvim",
            "obs-studio","playerctl", "vlc", "gparted", "volumeicon",
            "zsh", "ranger", "w3m", "transmission-gtk")

    for app in apps:
        ejecucion = run(["sudo","pacman","-S",app,"--noconfirm"],capture_output=True)
        salida = ejecucion.returncode
        # out = (ejecucion.stdout).decode("utf-8")
        if salida == 0:
            print("[X] ... {} se  ha instalado...".format(app))
        else:
            print("[0] ... {} No se ha instalado".format(app))
    
    print("La instalacion se ha completado\n")
         
            
def aur():
    print("\nInstalando programas de aur...\n")
    apps = ("google-chrome","visual-studio-code-bin")
    for app in apps:
        ejecucion = run(["yay","-S",app,"--noconfirm"],capture_output=True)
        salida = ejecucion.returncode        
        if salida == 0:
            print("[X] ... {} se  ha instalado...".format(app))
        else:
            print("[0] ... {} No se ha instalado".format(app))
 

def copyfiles():
    a = (('config/*','~/.config'),('fonts','~/.fonts'),('themes','~/.themes'),
         ('ssh','~/.ssh'),('Wall','~/Wall'),('xinitrc','~/.xinitrc'),
         ('zshrc','~/.zshrc'))
    for b in a:
        ejecucion = run(['cp -ru ~/EndeavourOS-dotfiles/{} {}'.format(b[0],b[1])],shell=True,capture_output=True)
        if ejecucion.returncode == 0:
            print("[X] ... {} copiado a {}".format(b[0],b[1]))
        else:
            print("[0] ... no copiado owo",ejecucion.stderr.decode('utf-8'))
        

def services():
    print("servicios")
    servicios = ('lightdm','sshd','gdm')
    for servicio in servicios:
        ejecucion = run(['sudo','systemctl','enable',servicio],capture_output=True)
        if ejecucion.returncode == 0:
            print("servicio habilitado",servicio)
        else:
            print("Servicio no habilitado",servicio)
            
            
def otros():
    run(['curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'],shell=True)
    run(['sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"'],shell=True)
    run(['EDITOR=code'],shell=True)
    run(['chsh -s $(which zsh)'],shell=True)
    run(['startx'],shell=True)
    
    
    

# #config zsh
# chsh -s $(which zsh)
# #install oh-my-zsh

# # Iniciar bspwm
# startx
    
            
            
        
if __name__ == "__main__":
    # pacman()
    # aur()
    # copyfiles()
    # services()
    otros()

# # $ eval "$(ssh-agent -s)"

# echo "Instalando bspwm"
# sleep 5
# # Instalar programas de pacman 
# sudo pacman -S xclip kitty krita rofi bspwm sxhkd polybar picom feh xorg-xsetroot numlockx neovim cmus lightdm lightdm-gtk-greeter scrot lxappearance-gtk3 virtualbox telegram-desktop python-pynvim obs-studio playerctl vlc gparted volumeicon zsh ranger w3m transmission-gtk

# # Instalar programas de aur
# yay -S google-chrome
# yay -S visual-studio-code-bin 
# sleep 3
# echo "Instalacion completada"
# sleep 3

# sudo systemctl enable lightdm
# sudo systemctl enable sshd

# cp -r config/* ~/.config
# cp -r fonts ~/.fonts
# cp -r themes ~/.themes
# cp -r ssh ~/.ssh

# cp xinitrc ~/.xinitrc
# cp zshrc ~/.zshrc

# cp -r Wall ~/Wall

# # configuracion de visual studio code
# ## extensiones :
#     #Bracket Pair, One Dark Pro, Pylance, Python, Python indent 

# # neovim plug
# curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

# sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# EDITOR=code

# #config zsh
# chsh -s $(which zsh)
# #install oh-my-zsh

# # Iniciar bspwm
# startx
