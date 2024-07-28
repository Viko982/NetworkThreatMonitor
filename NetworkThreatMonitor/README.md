# NetworkThreatMonitor

## Overview

NetworkThreatMonitor is a Python application that gathers active and past network connection information, and checks it against a threat intelligence platform (AbuseIPDB).

## Features

- Gather active network connections.
- Retrieve past network connections from logs.
- Check network connections against AbuseIPDB.
- OS agnostic (Windows, MacOS, Linux).

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/NetworkThreatMonitor.git
    cd NetworkThreatMonitor
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Update `API_KEY` in `src/main.py` with your AbuseIPDB API key.

## Usage

Run the application:
```bash
python src/main.py
