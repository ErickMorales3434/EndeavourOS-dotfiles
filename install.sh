# $ eval "$(ssh-agent -s)"

echo "Instalando bspwm"
sleep 5
# Instalar programas de pacman 
sudo pacman -S kitty rofi bspwm sxhkd polybar picom feh xorg-xsetroot numlockx neovim cmus lightdm lightdm-gtk-greeter scrot lxappearance-gtk3 virtualbox telegram-desktop python-pynvim obs-studio playerctl vlc gparted volumeicon zsh ranger w3m

# Instalar programas de aur
yay -S google-chrome
yay -S visual-studio-code-bin 
sleep 5
echo "Instalacion completada"
sleep 5

sudo systemctl enable lightdm

cp -r config/* ~/.config
cp -r fonts ~/.fonts
cp -r themes ~/.themes
cp -r ssh ~/.ssh

cp xinitrc ~/.xinitrc
cp -r Wall ~/Wall



# neovim plug
curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

EDITOR=code

#config zsh
chsh -s $(which zsh)
#install oh-my-zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Iniciar bspwm
startx
