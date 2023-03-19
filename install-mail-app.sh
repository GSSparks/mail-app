#!/bin/bash

if [ "$1" == "remove" ]; then
  # Remove the mail-app.py script from /usr/bin/
  sudo rm /usr/bin/mail-app

  # Remove the icons folder from $HOME/.icons
  rm -rf "$HOME/.icons/home_FILL1_wght400_GRAD0_opsz48.png"
  rm -rf "$HOME/.icons/map_FILL1_wght400_GRAD0_opsz48.png"
  rm -rf "$HOME/.icons/tugaa.svg"
  rm -rf "$HOME/.icons/tugaa-48px.png"

  # Remove desktop launcher
  rm -rf "$HOME/.local/share/applications/mail-app.desktop"
  
  echo "Mail app uninstalled successfully"
else
  # Download the mail-app.py script from the GitHub repo
  curl -o mail-app.py https://raw.githubusercontent.com/GSSparks/mail-app/main/mail-app.py

  # Copy the script to /usr/bin/
  sudo mv mail-app.py /usr/bin/mail-app

  # Copy the icons folder to $HOME/.icons
  if [ ! -d "$HOME/.icons" ]; then
    mkdir "$HOME/.icons"
  fi
  curl -o $HOME/.icons/tugaa.svg https://raw.githubusercontent.com/GSSparks/mail-app/main/icons/tugaa.svg
  curl -o $HOME/.icons/tugaa-48px.png https://raw.githubusercontent.com/GSSparks/mail-app/main/icons/tugaa-48px.png
  curl -o $HOME/.icons/home_FILL1_wght400_GRAD0_opsz48.png https://raw.githubusercontent.com/GSSparks/mail-app/main/icons/home_FILL1_wght400_GRAD0_opsz48.png
  curl -o $HOME/.icons/map_FILL1_wght400_GRAD0_opsz48.png https://raw.githubusercontent.com/GSSparks/mail-app/main/icons/map_FILL1_wght400_GRAD0_opsz48.png

  # Copy the desktop launcher to $HOME/.local/share/applications
  if [ ! -d "$HOME/.local/share/applications" ]; then
    mkdir "$HOME/.local/share/applications"
  fi
  curl -o $HOME/.local/share/applications/mail-app.desktop https://raw.githubusercontent.com/GSSparks/mail-app/main/launchers/mail-app.desktop
  
  echo "Mail app installed successfully"
fi
