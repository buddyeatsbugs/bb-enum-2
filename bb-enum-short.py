#!/usr/bin/python

import os

base_path = "/bug_bounty/bb-enum-sh0rt/"
base_domain = raw_input("Enter the domain name: ")

cmd1 = "python {}/Sublist3r/sublist3r.py -t 10 -v -o /tmp/sublister.txt -d {}".format(base_path, base_domain)
cmd2 = "python {}/EyeWitness/EyeWitness.py -f /tmp/sublister.txt --web -d /tmp/readoutfile".format(base_path)
cmd3 = "tr '\n\r' ' ' < /tmp/sublister.txt > /tmp/sparta.txt; cat /tmp/sparta.txt; echo; sparta;"

os.system(cmd1)
os.system(cmd2)
os.system(cmd3)



###Set Up###
'''
git clone https://github.com/aboul3la/Sublist3r.git
sudo pip install -r requirements.txt

python sublist3r.py -t 10 -v -o /tmp/sublister.txt -d kali.org

git clone https://github.com/FortyNorthSecurity/EyeWitness.git
sudo ./setup.sh

python EyeWitness.py -f urls.txt --web -d /tmp/readoutfile
'''
