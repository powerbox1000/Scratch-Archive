Scratch GPIO 3 is basically a version of Scratch 1.4 purely designed for the Raspberry Pi. It is pretty much an .sh file and some extra .py files for
different handlers. But, believe it or not, this will work on any Linux machine, including a ChromeBook! First, download Scratch 1.4 for Linux by typing
`sudo apt-get install scratch`. Then, download the Scratch GPIO 3 Installer.sh file. Next, to install it, type: `sudo bash "Scratch GPIO 3 Installer.sh" yourlinuxusername`, replacing
`yourlinuxusername` with your actual Linux username. This should have installed the neccessary files and created a directory called `scratchgpio`. Locate
there and run `./scratchgpio3.sh`. You're done! And, if you happened to be installing this on an actual Raspberry Pi, then you'll get the intended GPIO pin
functionality! That's all I have to say about Scratch GPIO 3.
