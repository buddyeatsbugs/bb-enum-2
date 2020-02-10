#!/usr/bin/python

import os, sys, pipes, json, tldextract


input1 = sys.argv[1]
subdomain = pipes.quote(input1)
extracted = tldextract.extract(subdomain)
domain = "{}.{}".format(extracted.domain, extracted.suffix)

urls = "/tmp/urls.txt"

def deserialize_waybackurls():
	with open('/tmp/waybackurls.json') as f:
		array = json.load(f)

	for i in array:
		print i[0]
		with open('/tmp/waybackurls.txt', 'a') as file:
			file.write(i[0] + ' \n ')

def loopThruURLs():
	with open('/tmp/urls.txt') as urls:
		for url in urls:
			os.system(pre_commands)
			os.system(way_back_machine_commands)

'''
def wfuzz():
	output_format_commands = "cat aron.txt | grep URL | cut -d ' ' -f 4 > wfuzz_urls_get.txt | tr 'fuzz' 'FUZZ' ; "
	os.system(output_format_commands)

	with open('/tmp/wfuzz_urls_get.txt) as urls:
		for url in urls:
			wfuzz_commands = "wfuzz -t 1 -z file,/opt/intruder-payloads/FuzzLists/quick_fuzz.txt {}".format(url)
			os.system(wfuzz_commands) 

	#wfuzz_commands_not_working = "wfuzz -z file,/tmp/wfuzz_urls_get2.txt -z file,/opt/intruder-payloads/FuzzLists/quick_fuzz.txt https://postmates.com"
'''	
	
		


pre_commands = "echo Remember.. Remember.. Burp Suite Pro; mkdir -p /bug_bounty/sites/{0}/{1}/eyewitness ;  sleep 5; ".format(domain,subdomain)
way_back_machine_commands="python /opt/waybackurls/waybackurls.py %s ; python /opt/waybackurls/waybackrobots.py %s;  " % (subdomain,subdomain)
brute_force_commands = "/usr/bin/gobuster -fw  -u %s -t 75 -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt -o /tmp/gobuster.txt ; " % (subdomain)
output_format_commands = "  cat /tmp/waybackurls.txt >> /tmp/urls.txt ; sort /tmp/urls.txt | uniq > /tmp/final.txt"
check_if_alive_commands = 'while read subdomain; do if host "$subdomain" > /dev/null; then echo "$subdomain" >> /tmp/live.txt ;  else echo "$subdomain" >> /tmp/dead.txt ; fi ; done < /tmp/final.txt ;'
check_if_resolves_commands = "host & dig"
eye_witness_commands = "/usr/local/bin/eyewitness -f /tmp/final.txt --all-protocols -d /bug_bounty/sites/%s/%s/eyewitness --no-prompt " % (domain,subdomain)

subjack_commands="/opt/go/bin/subjack -a -v -w /tmp/final.txt -t 75 -timeout 25 -ssl -c /opt/go/src/github.com/haccer/subjack/fingerprints.json -o /tmp/subjack.txt " 
curl_commands = " while read url; do curl -k -L --max-redirs 2  --silent --output /dev/null -x http://127.0.0.1:8080 https://$url ; done < /tmp/final.txt"
wafw00f_commands = "/usr/local/bin/wafw00f https://%s -a -v > /tmp/wafw00f.txt" % (subdomain)
linkfinder_commands = "python /opt/linkfinder/linkfinder.py -i https://%s -o /tmp/linkfinder.html -d " % (subdomain)
sandcastle_commands = "python /opt/sandcastle/sandcastle.py -f /tmp/final.txt -o /tmp/sandcastle.txt  " 
s3scanner_commands = "python /opt/s3scanner/s3scanner.py https://%s -o /tmp/s3scanner.txt" % (subdomain)

manual_commands = "/opt/xsscrapy/xsscrapy.py -u http://%s -r 60 ; " % (subdomain)
wfuzz_commands = "wfuzz -c -z file,/opt/intruder-payloads/FuzzLists/quick-fuzz.txt http://s"
truffle_hog_commands = "truffleHog --regex --entropy=False https://github.com/dxa4481/truffleHog.git"


photon_commands = "python /opt/photon/photon.py --keys --wayback -v -o /tmp/photon.txt -u %s" % (subdomain)
arjun_get_commands = "python3 /opt/arjun-scan/arjun.py -f /opt/arjun-scan/db/params.txt -u https://%s --get -t 22 > /tmp/arjun_get.txt" % (subdomain)
arjun_post_commands = "/usr/bin/python3 /opt/arjun-scan/arjun.py -f /opt/arjun-scan/db/params.txt -u https://%s --post -t 22 > /tmp/arjun_post.txt" % (subdomain)
cc_commands = "/usr/bin/python3 /opt/cc/cc.py -y 2018 https://%s -o /tmp/cc.txt" % (subdomain)
aron_get_commands = "go run /opt/aron/aron.go -wordlist /opt/aron/dict.txt -url https://%s -get  > /tmp/aron_get.txt" % (subdomain)
aron_post_commands = "go run /opt/aron/aron.go -wordlist /opt/aron/dict.txt -url https://%s -post > /tmp/aron_post.txt" % (subdomain)
cloud_scraper_commands = "python /opt/CloudScraper.py -v -p 10 -d 5 -u %s > /tmp/cloudscraper.txt" % (url)
git_pillage_commands = "/opt/gitpillage/gitpillage.sh https://%s > /tmp/gitpillage.txt" % (subdomain)
vhost_commands = "nmap --script http-vhosts -p 80,8080,443 %s > /tmp/vhosts.txt" % (subdomain)
dirb_commands = "dirb https://%s -v > /tmp/dirb.txt" % (subdomain)
nikto_commands = "nikto -h https://%s -o /tmp/nikto.txt" % (subdomain)
sparta_commands = ""

post_commands1 = "cp /tmp/final.txt /bug_bounty/sites/%s/%s ; cp /tmp/live.txt /bug_bounty/sites/%s/%s ; cp /tmp/dead.txt /bug_bounty/sites/%s/%s ; cp /tmp/waybackurls.txt /bug_bounty/sites/%s/%s/ ; cp /tmp/waybackrobots.txt /bug_bounty/sites/%s/%s/ ; " % (domain,subdomain,domain,subdomain,domain,subdomain,domain,subdomain,domain,subdomain) 
post_commands2 = "cp /tmp/subjack.txt /bug_bounty/sites/%s/%s/subjack.txt ; cp /tmp/wafw00f.txt /bug_bounty/sites/%s/%s/wafw00f.txt ; cp /tmp/linkfinder.html /bug_bounty/sites/%s/%s/linkfinder.html ; cp /tmp/sandcastle.txt /bug_bounty/sites/%s/%s/sandcastle.txt ; cp /tmp/s3scanner.txt /bug_bounty/sites/%s/%s/s3scanner.txt ;" % (domain,subdomain,domain,subdomain,domain,subdomain,domain,subdomain,domain,subdomain)
post_commands3 = "cp /tmp/photon.txt /bug_bounty/sites/%s/%s/ ; cp /tmp/arjun_get.txt /bug_bounty/sites/%s/%s/ ; cp /tmp/arjun_post.txt /bug_bounty/sites/%s/%s/ " % (domain,subdomain,domain,subdomain,domain,subdomain)
post_commands4 = "cp /tmp/cc.txt /bug_bounty/sites/%s/%s/ ; cp /tmp/aron_get.txt /bug_bounty/sites/%s/%s/ ; cp /tmp/aron_post.txt /bug_bounty/sites/%s/%s/ ;" % (domain,subdomain,domain,subdomain,domain,subdomain)
post_commands5 = "cp /tmp/gitpillage.txt /bug_bounty/sites/%s/%s/ ; cp /tmp/parameter.txt /bug_bounty/sites/%s/%s/ ; cp /tmp/dirb.txt /bug_bounty/sites/%s/%s/ ; cp /tmp/nikto.txt /bug_bounty/sites/%s/%s/ ; cp /tmp/vhosts.txt /bug_bounty/sites/%s/%s/ ;" % (domain,subdomain,domain,subdomain,domain,subdomain,domain,subdomain,domain,subdomain)
post_commands6 = "cp /tmp/cloudscraper.txt /bug_bounty/sites/%s/%s ; " % (domain, subdomain)

if __name__ == '__main__':


	fd = os.open("/tmp", os.O_RDONLY) 
	os.fchdir(fd) #Change working dir to /tmp

	os.system(pre_commands)
	
	os.system(brute_force_commands)
	os.system(way_back_machine_commands)
	deserialize_waybackurls()
	os.system(output_format_commands)
	#os.system(alt_dns_commands)
	#os.system(check_if_alive_commands)
	#os.system(check_if_resolves_commands)
	os.system(eye_witness_commands)
	os.system(curl_commands)
	

	os.system(photon_commands)
	os.system(arjun_get_commands)
	os.system(arjun_post_commands)
	os.system(cc_commands)
	os.system(git_pillage_commands)
	os.system(cloud_scraper_commands)
	#os.system(aron_get_commands) #  alternative to arjun-scan #not working
	#os.system(aron_post_commands) # alternative to arjun-scan #not working
	os.system(vhost_commands)
	os.system(dirb_commands)
	os.system(sparta_commands)

	os.system(wafw00f_commands)
	os.system(linkfinder_commands)
	os.system(sandcastle_commands)
	os.system(s3scanner_commands)
	os.system(subjack_commands)
	os.system(post_commands1)
	os.system(post_commands2)
	os.system(post_commands3)
	os.system(post_commands4)
	os.system(post_commands5)
	os.system(post_commands6)
