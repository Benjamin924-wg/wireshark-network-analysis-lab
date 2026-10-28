Wireshark Network Analysis Lab — Project Report

Student: Benjamin Dean Ojokpe
Project: Wireshark Network Analysis Lab
Environment: Kali Linux running in VMware
Tools: Wireshark, Python, HTTP, DNS, Nmap, SHA-256
Repository: "Wireshark Network Analysis Lab" (https://github.com/Benjamin924-wg/wireshark-network-analysis-lab)

1. Introduction

This project demonstrates beginner-level network traffic analysis using Wireshark on Kali Linux. The practical exercises cover packet capture, TCP connections, HTTP traffic, DNS queries, HTTP object export, traffic statistics, file integrity verification, and Nmap port scanning.

2. Objectives

- Capture and inspect network packets.
- Identify TCP three-way handshakes.
- Examine HTTP requests and responses.
- Understand DNS queries and responses.
- Export an HTTP object and compare file hashes.
- Review traffic statistics and network conversations.
- Observe TCP port-scanning traffic in an authorized local lab.
- Document practical findings using screenshots.

3. Lab Environment

The exercises used Kali Linux in VMware and a local Python HTTP server at "127.0.0.1:8081".

The local server provided a test webpage and an image file for HTTP traffic analysis. Nmap scanning was restricted to the user's own local test environment.

4. Practical Exercises

Exercise 1: Packet Capture

Captured traffic with Wireshark while accessing the local test server. Saved a packet capture for analysis.

Exercise 2: Display Filters

Practised filtering HTTP and TCP packets using filters including:

- "tcp.port == 8081"
- "http"
- "http.request"
- "http.request.method == "GET""
- "http.response.code == 200"

Exercise 3: TCP Three-Way Handshake

Examined TCP connection establishment using SYN and ACK flags. The handshake consists of SYN, SYN-ACK, and ACK packets.

"TCP Handshake" (screenshots/TCP%20Handshake1.jpg)

Exercise 4: HTTP Stream Analysis

Inspected HTTP requests and responses and used Follow HTTP Stream to understand the contents of a test HTTP session. The lab used fictional credentials for educational purposes.

"HTTP Stream" (screenshots/HTTP%20Stream%201.jpg)

Security lesson: Plain HTTP does not encrypt its contents. Real credentials and sensitive information should never be sent over insecure HTTP.

Exercise 5: DNS Analysis

Generated DNS queries for test domains and used Wireshark filters to inspect DNS questions and responses.

"DNS Analysis" (screenshots/DNS%20Analysis.jpg)

Exercise 6: Traffic Statistics

Generated repeated requests to the local server and used Wireshark statistics, including Conversations, Endpoints, and Protocol Hierarchy, to examine the captured traffic.

"Traffic Statistics" (screenshots/Traffic%20Statistics.jpg)

Exercise 7: HTTP Object Export and File Integrity

Exported an image object from HTTP traffic and compared its SHA-256 hash with the original image. The hashes matched, indicating that the two files had identical contents.

"SHA-256 Comparison" (screenshots/SHA-256%20Comparison.jpg)

Exercise 8: Nmap Port Scanning

Scanned ports 8070–8090 on the local test machine using Nmap. The test server was listening on port 8081, while the other scanned ports were reported closed during the exercise.

"Nmap Scan" (screenshots/Nmap%20Scan.jpg)

Safety note: Port scanning was restricted to the local lab machine. Scanning systems without permission is not appropriate.

5. Key Findings

1. Wireshark can capture and filter packets for detailed inspection.
2. TCP flags help explain how connections are established.
3. HTTP streams can expose unencrypted content.
4. DNS packets reveal domain lookup activity.
5. Wireshark statistics help summarize network conversations and traffic.
6. SHA-256 provides a practical way to compare file integrity.
7. Nmap can identify open and closed ports on an authorized test host.

6. Skills Practised

- Basic packet capture and filtering
- TCP handshake analysis
- HTTP request and response inspection
- DNS query analysis
- HTTP object export
- SHA-256 file verification
- Network traffic statistics
- Basic Nmap port scanning
- Technical documentation

7. Limitations

This was a beginner-level lab conducted in a controlled local environment. The results should not be interpreted as a full security audit or proof that a real network is secure.

8. Conclusion

This project provided practical experience using Wireshark and related tools to investigate network traffic. It improved my understanding of TCP, HTTP, DNS, file integrity, traffic statistics, and basic port scanning.

The exercises form part of my ongoing development in networking and cybersecurity.

9. Screenshot Evidence Checklist

- [x] TCP three-way handshake
- [x] HTTP stream analysis
- [x] DNS query and response
- [x] Traffic statistics
- [x] SHA-256 comparison
- [x] Nmap port scan

All six screenshots are stored in the repository's "screenshots" folder.
