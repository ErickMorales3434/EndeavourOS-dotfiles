# $ eval "$(ssh-agent -s)"

echo "Instalando bspwm"
sleep 5
# Instalar programas de pacman 
sudo pacman -S xclip kitty krita rofi bspwm sxhkd polybar picom feh xorg-xsetroot numlockx neovim cmus lightdm lightdm-gtk-greeter scrot lxappearance-gtk3 virtualbox telegram-desktop python-pynvim obs-studio playerctl vlc gparted volumeicon zsh ranger w3m transmission-gtk

# Instalar programas de aur
yay -S google-chrome
yay -S visual-studio-code-bin 
sleep 3
echo "Instalacion completada"
sleep 3

sudo systemctl enable lightdm
sudo systemctl enable sshd

cp -r config/* ~/.config
cp -r fonts ~/.fonts
cp -r themes ~/.themes
cp -r ssh ~/.ssh

cp xinitrc ~/.xinitrc
cp zshrc ~/.zshrc

cp -r Wall ~/Wall

# configuracion de visual studio code
## extensiones :
    #Bracket Pair, One Dark Pro, Pylance, Python, Python indent 

# neovim plug
curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

EDITOR=code

#config zsh
chsh -s $(which zsh)
#install oh-my-zsh

# Iniciar bspwm
startx


