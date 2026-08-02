# SOC Threat Intelligence Dashboard v3.0 (Production Ready)

## Overview
A high-performance, secure Cyber Threat Intelligence (CTI) dashboard designed for SOC analysts. Built with Python and Tkinter, it integrates live API data with encrypted configuration and secure database practices.

## Security Features
- **Encrypted Config**: API keys are encrypted using Fernet (AES-128) before storage.
- **SQLi Protection**: All database interactions use parameterized queries.
- **Input Validation**: Strict regex-based validation for all user-provided IOCs.
- **Secure Architecture**: Modular design with separated concerns (API, UI, DB, Logic).

## Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the setup script to configure your API keys securely:
   ```bash
   python setup.py
   ```
3. Launch the dashboard:
   ```bash
   python main.py
   ```

## Modules
- **Dashboard**: Real-time overview of global threat distribution.
- **IOC Lookup**: Live investigation of IPs, Domains, and Hashes.
- **Analytics**: Deep-dive into threat trends and severity metrics.
- **Network Graph**: Relationship mapping between entities.
- **Scan History**: Securely stored historical data for auditing.

## Author
Manus AI
