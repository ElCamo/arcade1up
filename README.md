# Arcade 1Up scripts

A couple of Python scripts to use the Power &amp; Volume buttons of the Arcade 1Up with a Raspberry Pi 3B+ assuming you have done similar mods to ETA Prime like so... https://www.youtube.com/watch?v=09DQCOr6zQM

#### Note: Older generation Raspberry Pi boards with the same GPIO layout should also work.

## Firstly, wire up you Raspberry Pi 3B+ with the following pin layout:

I used 150mm Plug to Socket Jumper Leads to reach from the existing connectors to the Rasberry Pi munted on the side of the Arcade 1Up.

### Power switch
Connect the black wire to Pin 5 (GPIO3) & the red wire to Pin 6 (Ground) of the GPIO header

### Volume switch
Connect the brown wire to Pin 7 (GPIO4), red wire to Pin 9 (Ground) & the black wire to Pin 11 (GPIO17) of the GPIO header.

#### Note: I use the audio out from the Pi directly to my amp (mini phono to 2x RCA)

## Install

I created a directory called arcade1up under my home folder.
These instructions will do the same.
Hit F4 to exit out of RetroPie / Emulation Station to the terminal.

Type:

git clone https://github.com/dmanlfc/arcade1up.git

#### Note: If you don't have git, you can download by typing sudo apt install git

Once complete you will have a directory under your home directory (/home/pi) call arcade1up

Next we edit your rc.local file like so...type:

sudo nano /etc/rc.local

In nano scroll down to after fi line but before exit 0 & add the lines as so...

(sudo python /home/pi/arcade1up/shutdown.py) &
(sudo python /home/pi/arcade1up/volume.py) &

Save the file (CTRL x, y, enter)

We also need to install the GPIO & Python packages for this to work.
Type:

sudo apt install python-rpi.gpio python3-rpi.gpio

Reboot & profit! (sudo reboot)

### Special notes

The power switch will only power down the Raspberry Pi & not the monitor or speakers. You still need to physically power off at the wall. I haven't done anything with an IoT relay yet.
If you power off at the wall please ensure before you start the Pi to toggle the switch back to on & then start the Pi otherwise within 10 seconds the Pi will power off again (the script see's the switch in the off position).
