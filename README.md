# ![TUGA App icon](/icons/tugaa-48px.png?raw=true "TUGA App icon") The Unofficial Google Apps ... App
uh ... TUGA App ... and like a toga this is a simple wrapper using python and the PyQt5 libraries that will display your Gmail, Google calendar, and maps. This project came about to make using Google apps easier for me from my desktop for work. More apps may be added if I come to use them frequently in the future. 

## Benefits of using this over a general purpose web browser:

* Dedicated use.
  * Keeps you logged in even on restarts until you log out. 
  * Automatically Loads on start.
* Isolated from other browsing.
  * You can run two instances with two different Gmail accounts.
  * Links open in system's default web browser.

## Screenshots:
![Home tab](/media/mail-app-screenshot1.png?raw=true "Home tab view")
![Maps tab](/media/mail-app-screenshot2.png?raw=true "Maps tab view")

## How to Install:
To install download and run `install-mail-app.sh`. This will install all of the needed files from this repo to your system. To uninstall simply run `install-mail-script.sh remove`. 

If you like to live dangerously then you can install with one command:

`curl https://raw.githubusercontent.com/GSSparks/mail-app/main/install-mail-app.sh | bash`

To uninstall:

`curl https://raw.githubusercontent.com/GSSparks/mail-app/main/install-mail-app.sh | bash -s remove`
