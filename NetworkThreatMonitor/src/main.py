import psutil
import os
import requests

API_KEY = 'test'  # AbuseIPDB API key
LOG_FILE = 'connections.log'

def get_active_connections():
    connections = psutil.net_connections(kind='inet')
    active_connections = []
    for conn in connections:
        if conn.status == 'ESTABLISHED' and conn.raddr:
            local_ip, local_port = conn.laddr
            remote_ip, remote_port = conn.raddr
            active_connections.append({
                'local_ip': local_ip,
                'local_port': local_port,
                'remote_ip': remote_ip,
                'remote_port': remote_port
            })
    print(f"Debug: Active connections gathered: {active_connections}")
    return active_connections

def get_past_connections(log_file):
    past_connections = []
    if os.path.exists(log_file):
        with open(log_file, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 4:
                    past_connections.append({
                        'local_ip': parts[0],
                        'local_port': parts[1],
                        'remote_ip': parts[2],
                        'remote_port': parts[3]
                    })
    print(f"Debug: Past connections gathered: {past_connections}")
    return past_connections

def save_log(connections, log_file):
    with open(log_file, 'a') as file:
        for conn in connections:
            file.write(f"{conn['local_ip']} {conn['local_port']} {conn['remote_ip']} {conn['remote_port']}\n")
    print(f"Debug: Active connections saved to log.")

def check_threat_intelligence(ip):
    url = f"https://api.abuseipdb.com/api/v2/check"
    headers = {
        'Accept': 'application/json',
        'Key': API_KEY
    }
    params = {
        'ipAddress': ip,
        'maxAgeInDays': '90'
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

if __name__ == "__main__":
    # Check for active connections
    active_connections = get_active_connections()
    
    # Check for past connections from log
    past_connections = get_past_connections(LOG_FILE)

    # Create a set of unique connections
    unique_connections = {f"{conn['remote_ip']}:{conn['remote_port']}" for conn in active_connections + past_connections}

    # Save active connections to log
    save_log(active_connections, LOG_FILE)

    # Check threat intelligence for each unique connection
    for conn in unique_connections:
        ip, port = conn.split(':')
        threat_info = check_threat_intelligence(ip)
        print(f"IP: {ip}, Threat Info: {threat_info}")

    print(f"Unique connections: {unique_connections}")
