# PcapFileCarver
This tool makes use of foremost to carve files out of saved web traffic.

# Usage

Run `python pcap_scraper.py [LOG_FILE]` where `LOG_FILE` is your traffic file.

# How it works

This python tool makes use of `scapy` python library to manipulate the packets. Though the documentation for scapy is not very developed, there exists multiple functions that I found to be very useful. Specifically `sessions()` is similar to `tcpstream ` from wireshark and pulls together all traffic between two sources. That tool was invaluable for concatenating all of the data together for proper scraping with `foremost`.

# Example

An example logfile has been included to test the program. `example.log` can be run through the program and should produce an output that is the same as `examples_output` for comparison. 

# Process

I went through several different iterations of this program before deciding to go with scapy. Initially I had written a session complier but it ran significantly slower and used more memory than `sessions()`. Beyond that, the output has significantly been cleaned up from the default `foremost` output. Initially, the output was divided by session and file type recovered. Since then, the output has been flattened and renamed with the source and destination IPs for the conversation. 
