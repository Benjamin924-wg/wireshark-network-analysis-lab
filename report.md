Wireshark Network Analysis Lab — Project Report

Student: Benjamin Dean Ojokpe
Project: Wireshark Network Analysis Lab
Environment: Kali Linux running in VMware
Tools: Wireshark, Python, HTTP, DNS, Nmap, SHA-256
Repository: "View project on GitHub" (https://github.com/Benjamin924-wg/wireshark-network-analysis-lab)

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
- Document practical findings with screenshots.

3. Lab Environment

The lab used Kali Linux running in VMware, Wireshark, Python, and a local HTTP test server at "127.0.0.1:8081".

The server provided a test webpage and an image for HTTP traffic analysis. Port scanning was restricted to the local test machine.

4. Exercise 1 — Packet Capture

Captured network traffic in Wireshark while accessing the local test server. Saved a packet capture for later inspection.

5. Exercise 2 — Display Filters

Practised using Wireshark display filters to isolate relevant packets:

- "tcp.port == 8081"
- "http"
- "http.request"
- "http.request.method == "GET""
- "http.response.code == 200"

These filters helped identify traffic associated with the local web server.

6. Exercise 3 — TCP Three-Way Handshake

Examined TCP connection establishment using SYN and ACK flags. A typical TCP handshake consists of SYN, SYN-ACK, and ACK packets.

Screenshot evidence:

![TCP Three-Way Handshake](screenshots/TCP%20Handshake1.jpg)

7. Exercise 4 — HTTP Stream Analysis

Inspected HTTP requests and responses and used Follow HTTP Stream to examine a test session. The lab used fictional credentials for educational purposes.

Screenshot evidence:

![HTTP Stream Analysis](screenshots/HTTP%20Stream%201.jpg)

Security lesson: Plain HTTP does not encrypt its contents. Real credentials and sensitive information should not be sent over insecure HTTP.

8. Exercise 5 — DNS Analysis

Generated DNS queries for test domains and used Wireshark filters to inspect DNS questions and responses.

Screenshot evidence:

![DNS Analysis](screenshots/DNS%20Analysis.jpg)

9. Exercise 6 — Traffic Statistics

Generated repeated requests to the local test server and reviewed Wireshark statistics, including Conversations, Endpoints, and Protocol Hierarchy.

Screenshot evidence:

![Traffic Statistics](screenshots/Traffic%20Statistics.jpg)

10. Exercise 7 — HTTP Object Export and File Integrity

Exported an image object from HTTP traffic and compared its SHA-256 hash with the original image. The hashes matched, indicating that both files had identical contents.

Screenshot evidence:

![SHA-256 Comparison](screenshots/SHA-256%20Comparison.jpg)

11. Exercise 8 — Nmap Port Scanning

Scanned ports 8070–8090 on the local test machine using Nmap. During the exercise, the test server was listening on port 8081, while the other scanned ports were reported closed.

Screenshot evidence:

![Nmap Port Scan](screenshots/Nmap%20Scan.jpg)

Safety note: The scan was limited to the local lab machine. Only scan systems when you have permission.

12. Key Findings

1. Wireshark can capture and filter network packets.
2. TCP flags help explain how connections are established.
3. HTTP streams can expose unencrypted content.
4. DNS packets reveal domain lookup activity.
5. Traffic statistics help summarize network conversations.
6. SHA-256 can be used to compare file integrity.
7. Nmap can identify open and closed ports on an authorized test host.

13. Skills Practised

- Packet capture and display filtering
- TCP handshake analysis
- HTTP request and response inspection
- DNS query analysis
- HTTP object export
- SHA-256 file verification
- Network traffic statistics
- Basic Nmap port scanning
- Technical documentation

14. Limitations

This was a beginner-level exercise conducted in a controlled local environment. It was not a full security audit and does not establish that a real network is secure.

15. Conclusion

This project provided practical experience using Wireshark and related tools to investigate network traffic. It strengthened my understanding of TCP, HTTP, DNS, file integrity, traffic statistics, and basic port scanning.

These exercises form part of my ongoing learning in networking and cybersecurity.

16. Screenshot Evidence Checklist

- [x] TCP three-way handshake
- [x] HTTP stream analysis
- [x] DNS query and response
- [x] Traffic statistics
- [x] SHA-256 file integrity comparison
- [x] Nmap port scan

All six screenshots are stored in the repository's "screenshots" folder and linked in the relevant exercise sections above.
