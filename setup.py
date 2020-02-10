#!/usr/bin/python

import os

cmd = '''
sudo mkdir -p /opt/bb-enum ; cd /opt/bb-enum ; git clone https://github.com/FortyNorthSecurity/EyeWitness.git eyewitness ; git clone https://github.com/s0md3v/Arjun.git arjun ; git clone https://github.com/GerbenJavado/LinkFinder.git linkfinder ; git clone https://github.com/0xSearches/sandcastle.git ; git clone https://github.com/evilpacket/DVCS-Pillage gitpillage ; git clone https://github.com/s0md3v/Photon photon ; git clone https://github.com/si9int/cc.py ; git clone https://github.com/codingo/VHostScan.git vhostscan ; git clone https://github.com/jordanpotti/CloudScraper.git cloudscraper ; pip install truffleHog ; mkdir -p /opt/bb-enum/waybackurls ; cd /opt/bb-enum/waybackurls ; curl https://gist.githubusercontent.com/mhmdiaa/adf6bff70142e5091792841d4b372050/raw/56366e6f58f98a1788dfec31c68f77b04513519d/waybackurls.py > /opt/bb-enum/waybackurls/waybackurls.py ; curl https://gist.githubusercontent.com/mhmdiaa/2742c5e147d49a804b408bfed3d32d07/raw/5dd007667a5b5400521761df931098220c387551/waybackrobots.py > /opt/bb-enum/waybackurls/waybackrobots.py ;  chmod 755 /opt/bb-enum/waybackurls/waybackrobots.py; chmod 755 /opt/bb-enum/waybackurls/waybackurls.py ; cd /opt/bb-enum ; apt-get install golang -y  ; go get github.com/haccer/subjack ; go get https://github.com/subfinder/subfinder ; pip install wafw00f ;  
'''

cmd2 = '''
sudo /opt/bb-enum/eyewitness/setup/setup.sh ; python /opt/bb-enum/linkfinder/setup.py ; pip install -r /opt/bb-enum/gitpillage/pip-requirements.txt ; pip install -r /opt/bb-enum/photon/requirements.txt ; python3 /opt/bb-enum/vhostscan/setup.py install ; pip install -r /opt/bb-enum/cloudscraper/requirements.txt
'''

os.system(cmd)
os.system(cmd2)
