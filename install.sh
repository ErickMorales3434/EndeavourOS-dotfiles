echo "Instalando bspwm"
sleep 5
# Instalar programas de pacman 
sudo pacman -S htop tilix rofi bspwm sxhkd polybar feh xorg-xsetroot numlockx neovim cmus lightdm lightdm-gtk-greeter scrot lxappearance-gtk3
# sudo pacman -S virtualbox telegram-desktop nautilus

# Instalar programas de aur
# yay -S google-chrome
# yay -S visual-studio-code-bin 
sleep 5
echo "Instalacion completada"
sleep 5

sudo systemctl enable lightdm

cp -r config/* ~/.config

cp -r fonts ~/.fonts
cp -r themes ~/.themes
cp xinitrc ~/.xinitrc
cp -r Wall ~/Wall


# neovim plug
curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

# Iniciar bspwm
startx