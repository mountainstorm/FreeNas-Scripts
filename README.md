auto-shutdown.py
================

This is a simple python script which, when scheduled as a launch job, checks 
if it can ping a list of client ip addresses; if it can't ping any of them for
an hour it calls shutdown.


Requirements
------------

FreeNAS 9.1; for init job support (and HP Microserver WoL support)


Installation
------------

1. Copy the auto-shutdown.py script onto one of your file shares
2. Log into the FreeNas web interface
3. Goto Shell
4. If you have a USB (embedded) install of FreeNas; remount the filesystem rw
	1. mount -uw /
	2. mv /mnt/StorageArray/Media/auto-shutdown.py /bin/
	3. chmod +x /bin/auto-shutdown.py
	4. sync
	5. mount -ur /
	6. reboot
5. Goto System > Add Init/Shutdown Script
	Type: Command
	Command: /bin/auto-shutdown.py
	Type: Post Init


Notes
-----

If your using windows clients; you will need to enable ping replies.  There are
many good guides to doing this only, I used this one: 
http://www.howtogeek.com/77132/how-to-enable-ping-echo-replies-in-windows-8/

In short you need to open up the "Windows Firewall and Advanced Settings" MMC
application > Select "Inbound Rules" > "File and Printer Sharing (Echo Request - ICMPv4-In)". 
Right click and enable rule.

simple!


wake_on_lan.py
--------------

This is the companion script, which is used to send a wake on lan packet to 
FreeNas (when my desktop wakes up) to ensure the shares are avaliable.

You will need to update the mac address in the format: aa:bb:cc:dd:ee:ff, the
easiest way to get the mac address of your FreeNas is to  

1. Log into the FreeNas web interface
2. Goto Shell
3. ifconfig


Keywords
--------
FreeNas, MacOSX, Windows, Ping, Shutdown, Wake on lan, HP Microserver, N54L
