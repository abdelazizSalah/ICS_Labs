# MITM Attack (Mallory)

| Name       | Date       | Description                |
|------------|------------|----------------------------|
| Abdelaziz Nematallah  | 01-12-2024 | This file contains the steps of how to apply the man in the middle attack |

* The main idea is to connect on the network, and sniff all the packets sent from alice to bob.
* to do this we need to apply "MAC Poisoning" or "ARP Poioning"
* ARP is Address Resolution Protocol
* which is a technology that allows devices to identify themselves on a network
* this is by associating its MAC address with an IP address on a network
* so each device will keep in its cache a log of the MAC addresses associated with other devices
* So in ARP Poisoning we lie to Alice by sending our Mac as Bob's Mac
* and lie to Bob by sending our Mac as Alice's Mac
* to do so we need to implement an ARP following this structure: 
   * hardware type 2bytes -> 0001 eth1
   * protocol type 2bytes -> 0800 ipv4
   * MAC add length 1 byte -> 0006 mac is 6 bytes
   * Protocol address length -> 0004 ipv4 is 4 bytes
   * operation 2bytes -> ARP Reply
   * sender MAC -> MAC of the Attacker
   * sender IP -> the spoofed IP (like if we want to lie to Alice put Bob's IP)
   * Target MAC -> Alice MAC
   * Target IP -> Alice IP

> to know how I got the exact solution please open the notebook **lab2_solutions.ipynb**