#!/usr/bin/env bash

rofi_command="rofi -theme $HOME/.config/rofi/screenshot_theme/screenshot.rasi"

# Error msg
msg() {
	rofi -theme "$HOME/.config/rofi/screenshot_theme/configs/message.rasi" -e "Please install 'scrot' first."
}

# Options
screen=""
area=""
window=""

# Variable passed to rofi
options="$screen\n$area\n$window"

chosen="$(echo -e "$options" | $rofi_command -p 'App : scrot' -dmenu -selected-row 1)"
case $chosen in
    $screen)
		if [[ -f /usr/bin/scrot ]]; then
			sleep 1; scrot -q 100 -d 1 $HOME/Imágenes/Screenshot-$(date "+%d-%m-%Y-%H:%M:%S").png
		else
			msg
		fi
        ;;
    $area)
		if [[ -f /usr/bin/scrot ]]; then
    		sleep 1;scrot -q 100 -s $HOME/Imágenes/Screenshot-$(date "+%d-%m-%Y-%H:%M:%S").png
			
		else
			msg
		fi
        ;;
    $window)
		if [[ -f /usr/bin/scrot ]]; then
			sleep 1;scrot -q 100 -u $HOME/Imágenes/Screenshot-$(date "+%d-%m-%Y-%H:%M:%S").png 
		else
			msg
		fi
        ;;
esac

