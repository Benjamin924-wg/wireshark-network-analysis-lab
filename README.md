Wireshark Network Analysis Lab

Project Overview

This project documents my beginner cybersecurity practical exercises using Wireshark and Kali Linux. I learned how to capture network packets, inspect TCP connections, analyze HTTP and DNS traffic, export files, and recognize TCP port scans on my own computer.

Objectives

- Learn basic packet capture with Wireshark.
- Understand TCP three-way handshakes.
- Analyze HTTP requests and responses.
- Observe why unencrypted HTTP can expose submitted data.
- Examine DNS queries and responses.
- Use Wireshark statistics to analyze traffic.
- Export HTTP objects and compare SHA-256 hashes.
- Recognize port scanning activity using Nmap.

Tools Used

- Kali Linux
- Wireshark
- Python 3
- curl
- Nmap
- GitHub

Practical Exercises

1. First packet capture
2. Display filters
3. TCP three-way handshake
4. HTTP stream and lab-only test credentials
5. DNS traffic analysis
6. Protocol hierarchy, conversations, endpoints, and I/O graphs
7. HTTP object export and SHA-256 integrity verification
8. TCP port scan recognition on localhost

Lab Environment

The test server runs locally at "127.0.0.1:8081". It is designed for authorized practice on my own computer.

Key Learning

- How to filter packets by protocol and port.
- How TCP connections are established and closed.
- How HTTP traffic can expose information without encryption.
- How to identify DNS activity and TCP port scanning patterns.
- How to verify exported files using SHA-256 hashes.

Safety

All scanning and traffic generation in this project are limited to my own local lab environment. The login details used are fake training credentials.

Project Status

Practical exercises completed so far include HTTP object export and hash comparison, and a local Nmap scan. Additional screenshots and results will be added as the lab documentation progresses.
