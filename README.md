Wireshark Network Traffic Analysis Lab

A hands-on cybersecurity and network analysis project using Kali Linux, Wireshark, Python, and Nmap.

Project Overview

This project documents eight practical exercises completed in a controlled local lab environment. It demonstrates how to capture, filter, inspect, and interpret network traffic while developing foundational cybersecurity skills.

Objectives

- Capture and analyze network packets.
- Identify TCP three-way handshakes.
- Inspect HTTP requests, responses, and streams.
- Analyze DNS queries and responses.
- Review network traffic statistics.
- Export HTTP objects and verify file integrity using SHA-256.
- Recognize TCP port-scanning activity.

Tools and Technologies

- Kali Linux
- Wireshark
- Python 3
- HTTP and DNS
- curl
- Nmap
- SHA-256
- GitHub

Practical Exercises

Exercise| Topic
1| Initial packet capture
2| Wireshark display filters
3| TCP three-way handshake
4| HTTP stream analysis
5| DNS traffic analysis
6| Network traffic statistics
7| HTTP object export and SHA-256 verification
8| Nmap TCP port scanning

Repository Contents

- "report.md" — Detailed practical report.
- "screenshots/" — Visual evidence from the exercises.
- "lab_server.py" — Local HTTP test server.
- "original_logo.png" — Original test image.
- "exported_logo.png" — Image exported from HTTP traffic.
- ".pcapng" files — Saved packet captures from the lab exercises.

Key Findings

- TCP connections use SYN, SYN-ACK, and ACK to establish communication.
- Unencrypted HTTP traffic can expose transmitted information.
- DNS packets reveal domain lookup activity.
- Wireshark statistics help summarize network conversations.
- Matching SHA-256 hashes indicate identical file contents.
- Nmap identified port 8081 as open and the other scanned ports as closed on the local test machine.

Security and Authorization

All traffic generation and scanning were conducted within my own local lab environment. The HTTP login credentials were fictional training credentials. No third-party systems were targeted.

Project Status

Completed: Eight practical exercises documented with screenshots and supporting files.

Author

Benjamin Dean Ojokpe

Cybersecurity Learner | Network Analysis | Wireshark

Detailed Documentation

See "the complete practical report" (report.md) for exercise descriptions, findings, and screenshot evidence.
