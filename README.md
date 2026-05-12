# 🛡️ Dark Web Leak Intelligence Aggregator

A cybersecurity intelligence platform designed to crawl publicly accessible dark web sources, detect sensitive data leaks, and provide forensic-grade threat intelligence through an interactive dashboard.

Built using Python, Flask, Selenium, Tor, and SQLite, the system automates leak detection workflows commonly used in cyber threat intelligence (CTI), OSINT, and digital forensics environments.

---

# 🚀 Features

## 🔍 Automated Dark Web Crawling
- Crawls `.onion` websites using Tor + Selenium
- Supports JavaScript-rendered pages
- Captures screenshots and extracted text content
- Works with SOCKS5 proxy routing for anonymity

## 🧠 Leak Detection Engine
Detects:
- Aadhaar number patterns
- PAN card leaks
- Email/password credential dumps
- Citizen database mentions
- Banking records & IFSC codes
- Sensitive PII exposure

Uses:
- Regular expressions
- Keyword heuristics
- Fuzzy pattern analysis

## 📊 Intelligence Dashboard
Interactive Flask dashboard with:
- Leak search functionality
- Screenshot previews
- Timestamped evidence tracking
- CSV export support
- Local forensic database querying

## 🗄️ Forensic Storage System
Stores:
- Leak URLs
- Leak types
- Extracted text samples
- Screenshot evidence
- Detection timestamps

Powered by SQLite for lightweight offline deployment.

---

# 🏗️ System Architecture

```text
Onion Site Feed
       ↓
Tor + Selenium Crawler
       ↓
Text & Screenshot Extraction
       ↓
Leak Detection Engine
       ↓
SQLite Intelligence Database
       ↓
Flask Dashboard
       ↓
CSV / Forensic Evidence Export
```

---

# ⚙️ Tech Stack

## Backend
- Python
- Flask
- SQLite3

## Crawling & Automation
- Selenium
- Tor Network
- SOCKS5 Proxy
- Headless Browser Automation

## Detection & Analysis
- Regex Pattern Matching
- NLP / Fuzzy Keyword Detection

## Storage & Reporting
- SQLite Database
- CSV Export Pipeline

---

# 📂 Project Structure

```text
darkweb-leak-aggregator/
│
├── dashboard/
│   └── app.py
│
├── database/
│   └── db.py
│
├── scrapers/
│   └── tor_browser_selenium.py
│
├── utils/
│   └── leak_detector.py
│
├── onion_sites.txt
├── requirements.txt
└── README.md
```

---

# 🧪 How It Works

1. Provide a list of `.onion` targets in:
   ```text
   onion_sites.txt
   ```

2. The crawler connects through Tor and loads pages anonymously.

3. Extracted content is analyzed using detection rules.

4. Matching leaks are stored in SQLite along with screenshots.

5. Results become searchable through the Flask dashboard.

---

# 💻 Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/darkweb-leak-aggregator.git
cd darkweb-leak-aggregator
```

## Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Start Dashboard

```bash
python dashboard/app.py
```

Dashboard:
```text
http://localhost:5000
```

---

# 📸 Capabilities

- Automated threat intelligence gathering
- Dark web monitoring
- Cybercrime evidence collection
- Credential leak discovery
- OSINT research workflows
- Offline forensic analysis

---

# 🔒 Security & Ethics Notice

This project was built strictly for:
- educational purposes,
- cybersecurity research,
- threat intelligence analysis,
- and defensive security workflows.

The project is not intended for unauthorized access, illegal activity, or malicious use.

Users are responsible for complying with all applicable laws and ethical cybersecurity practices.

---

# 📈 Future Improvements

- Multi-threaded crawling engine
- Elasticsearch integration
- Threat actor fingerprinting
- Real-time alert system
- Distributed scanning support
- Advanced NLP classification
- Docker deployment
- REST API integration

---

# 🧠 Computer Science Concepts Demonstrated

- Web scraping & browser automation
- Network proxy routing
- Tor architecture integration
- Cyber threat intelligence pipelines
- Database design
- Backend engineering
- Pattern matching algorithms
- NLP-based classification
- OSINT tooling
- Forensic evidence collection

---

# 👨‍💻 Author

**Nilesh Sharma**  
Computer Science Student | Cybersecurity Enthusiast | Systems & Infrastructure Engineering

---

# ⭐ Disclaimer

This repository is intended solely for educational and defensive cybersecurity research purposes. The author does not encourage or support illegal activities, unauthorized access, or malicious operations of any kind.
