from scapy.all import *
from sys import argv
import os
import subprocess

#no pcap file provided
if (len(argv) <= 1):
    print ("Proper usage is 'python pcap_scraper.py [$PCAP_File]'")
    raise SystemExit

HOME = argv[1] + "_files/"
packets = rdpcap(argv[1])
#sessions is like wireshark follow tcp stream
a = packets.sessions()
os.makedirs(HOME)
#put all the raw info together and title it with the src and dest
for session,data in a.items():
    for byte in data:
        if(byte.haslayer(Raw) and len(byte[Raw].load) > 0):
            f = open(HOME+str(session) + ".stream", "ab+")
            f.write(byte[Raw].load)
            f.close()

#run foremost and delete empty folders
for stream in os.listdir(HOME):
    out = HOME + stream + "_out/"
    subprocess.run(['foremost', '-Q', '-t','all','-o',out,'-i',HOME + stream])
    #remove original streams file
    subprocess.run(['rm', HOME + stream])

    #make sure folder has more than just audit.txt
    if len(os.listdir(out)) > 1:
        i=0
        for file_type in os.listdir(out):
            if(os.path.isdir(out + file_type)):
                for outfile in os.listdir(out+file_type):
                    subprocess.run(['mv', out + file_type +"/"+  outfile, HOME + stream + "_" + str(i) + "." + file_type])
                    i += 1
    #remove intermediate results
    subprocess.run(['rm', '-r', out])
