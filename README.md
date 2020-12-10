# Random Scripts
Test repository for some sample scripts I have written and use in penetration testing labs, such as HackTheBox, Dante, Proving Grounds, WebGoat, and DVWA. The Network Attack scripts are all written in python and are intended for use in legal ethical hacking and security research. Do NOT attempt to use any of these tools against any machine that you do not own or have written, legally-binding permission to do so. With that said, spin up a virtual network and have fun with these scripts! 

Note: Not all of them are finished, so if you see something that needs fixing, feel free to let me know! I am open to helpful feedback. 

## Python Scripts
- ceasar (substitution) cipher written in python. It works with any shift value, such as 13 for ROT13.
Example usage:
```[python]
python3 ceasar.py -m "attack at dawn" -s 3
python3 ceasar.py -m "ciphertext" -s 3 -d true
```
- ARP spoofer works with a wireless connection on a local network, exiting with CTRL+C will restore the arp tables of the victim.
Example usage:
```[python]
python3 arp_spoof.py -t 192.168.0.x -g 192.168.0.1 -l 192.168.0.x
```
- The HTTP traffic sniffer will capture all HTTP traffic from a target on the LAN that you are currently running the ARP spoofing script against.
Example usage:
```[python]
python3 sniffer.py -i "wlan0"
```
- The DNS spoofer has given me quite a bit of trouble, as I have not gotten it to fully work yet. Please let me know if I have any glaring errors!
- The file interceptor script is also still in development.
## Bash Scripts
- revshell.sh is a helpful script I use to auto-format reverse shell one-liners with my attacking ip and port and output them to the terminal. This tool is especially handy for command injection vulnerabilities. These one-liners were taken from:
[PayloadsAllTheThings reverse shell cheatsheet](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md)
- for usage instructions, use:
```[bash]
./revshell.sh --help
```
Example usage:
```[bash]
./revshell.sh bash_tcp 1.3.3.7 1337 
./revshell.sh powershell 10.10.10.10 9001 #Shout out to IppSec
./revshell.sh all 10.10.10.10 9002
```
