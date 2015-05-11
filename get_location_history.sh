#!/bin/bash
cd /home/david/Weasley/
wget -x --load-cookies cookies_david.txt -O output_david.txt "https://maps.google.com/locationhistory/b/0/kml?startTime="$(date -d "-2 day" +"%s")"000&endTime="$(date +"%s")"000" 
wget -x --load-cookies cookies_peto.txt -O output_peto.txt "https://maps.google.com/locationhistory/b/0/kml?startTime="$(date -d "-2 day" +"%s")"000&endTime="$(date +"%s")"000" 
python weasley.py
cp weasley.png /var/www/bucket.broukej.cz/weasley.png
chmod 777 /var/www/bucket.broukej.cz/weasley.png
