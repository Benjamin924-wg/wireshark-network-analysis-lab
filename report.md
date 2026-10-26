Wireshark Network Analysis Lab — Project Report

Student: Benjamin Dean Ojokpe
Project: Wireshark Network Analysis Lab
Environment: Kali Linux running in VMware
Repository: https://github.com/Benjamin924-wg/wireshark-network-analysis-lab

1. Introduction

This project demonstrates beginner-level network traffic analysis using Wireshark on Kali Linux. The practical exercises focused on examining network packets, understanding TCP connections, inspecting HTTP and DNS traffic, exporting HTTP objects, and recognizing TCP port scans.

2. Objectives

- Capture and inspect network traffic using Wireshark.
- Apply display filters to identify specific packets.
- Understand the TCP three-way handshake.
- Examine HTTP requests and responses.
- Observe DNS queries and responses.
- Export an HTTP object and compare its SHA-256 hash.
- Identify open and closed TCP ports in a local scan.

3. Tools and Environment

- Kali Linux running in VMware
- Wireshark
- Python 3 local HTTP server
- curl
- Nmap
- GitHub for project documentation

The HTTP lab server used the local address "127.0.0.1:8081". Testing was performed on my own lab environment.

4. Practical Exercises and Findings

Exercise 1: Packet Capture

Captured network traffic using Wireshark and saved packet captures for inspection.

Evidence to add: Screenshot showing the packet list and capture interface.

Exercise 2: Display Filters

Practised filtering HTTP traffic using expressions including:

- "tcp.port == 8081"
- "http"
- "http.request"
- "http.request.method == "GET""
- "http.response.code == 200"

These filters helped isolate relevant requests and responses.

Exercise 3: TCP Three-Way Handshake

Used TCP flag filters to examine connection establishment:

- "tcp.flags.syn == 1"
- "tcp.flags.syn == 1 && tcp.flags.ack == 0"

The TCP handshake consists of SYN, SYN-ACK, and ACK packets.

Evidence to add: Screenshot showing the three handshake packets, labelled in order.

Exercise 4: HTTP Traffic Inspection

Inspected HTTP traffic from the local training server and practised following an HTTP stream.

The login exercise used fictional credentials for educational purposes. Plain HTTP does not encrypt transmitted content, so credentials sent over it may be exposed to anyone able to capture the traffic.

Evidence to add: A screenshot of the lab-only HTTP stream. Do not use real passwords or personal credentials.

Exercise 5: DNS Analysis

Generated DNS queries using "nslookup" and examined DNS packets with Wireshark filters such as "dns" and "dns.flags.response == 1".

This exercise introduced the relationship between DNS queries and their responses.

Evidence to add: Screenshot of a DNS query and its response.

Exercise 6: Traffic Statistics

Generated repeated requests to the local HTTP server and examined Wireshark statistics, including Conversations, Endpoints, Protocol Hierarchy, and I/O Graphs.

The exercise demonstrated how packet statistics can help summarize network activity.

Evidence to add: Screenshot of the Conversations table and, if available, the I/O Graph.

Exercise 7: HTTP Object Export and Integrity Verification

Downloaded the lab's "logo.png" object and exported the corresponding HTTP object from Wireshark.

Compared the SHA-256 hashes of "original_logo.png" and "exported_logo.png". The hashes matched, confirming that the two files had identical contents.

Evidence to add: Screenshot showing both filenames and their matching SHA-256 hashes.

Exercise 8: Local TCP Port Scan

Used Nmap to scan TCP ports 8070–8090 on "127.0.0.1".

The scan identified TCP port 8081 as open and the other scanned ports as closed at the time of testing.

This result was consistent with the local HTTP server listening on port 8081. The scan was restricted to my own lab machine.

Evidence to add: Screenshot of the Nmap results and Wireshark packets showing SYN traffic from the scan.

5. Security Lessons

The exercises demonstrated that:

- Packet captures can reveal details about network communication.
- Display filters make traffic analysis more efficient.
- Plain HTTP does not provide transport encryption.
- DNS traffic can be inspected to understand name resolution.
- SHA-256 hashes can be used to compare file contents.
- TCP scans can help identify which ports are accepting connections.

6. Challenges and Learning Outcomes

Working through the lab improved my familiarity with Wireshark filters, packet capture files, HTTP traffic, TCP flags, DNS, file export, and basic Nmap scanning.

The project also helped me practise documenting technical work and maintaining a cybersecurity portfolio on GitHub.

7. Conclusion

This project provided practical introductory experience in network traffic analysis using Wireshark and Kali Linux. It established a foundation for further learning in network security, packet inspection, and defensive cybersecurity.

8. Evidence Checklist

- [ ] TCP three-way handshake screenshot
- [ ] HTTP stream screenshot using fictional lab credentials
- [ ] DNS query and response screenshot
- [ ] Network statistics screenshot
- [ ] Matching SHA-256 hash screenshot
- [ ] Nmap scan and SYN traffic screenshot
