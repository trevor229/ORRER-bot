#!/bin/sh

if [ -e /tmp/botLOCK ]
then
	echo "[$(date)]Check complete, bot is running." >> /home/alex/botChecker.txt
else
	touch /tmp/botLOCK
	sudo python3.5 /home/alex/alexclean.py
	rm /tmp/botLOCK
fi
