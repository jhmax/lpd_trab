## LOG FILES script inspired by techniques from Rishikesh Khot.
## reference: https://github.com/Rishikesh-khot/Log_analyzer/blob/main/log_analyzer.py

import re
import requests
import matplotlib.pyplot as plt
import os
from collections import defaultdict
from datetime import datetime
import json

# Padrões de atividades suspeitas
patterns = {
    'unauthorized_access': re.compile(r'Failed password|Invalid user', re.IGNORECASE)
}

remedies = {
    'unauthorized_access': "Remedy: Check login attempts, enforce strong passwords, and implement multi-factor authentication."
}

def get_country_from_ip(ip):
    return 'Unknown'

# Função para analisar o arquivo de log
def analyze_log_file(log_file):
    suspicious_activity = defaultdict(int)
    ip_data = defaultdict(list)
    timestamp_data = []
    total_lines = 0
    
    with open(log_file, 'r') as f:
        for line in f:
            total_lines += 1
            timestamp_match = re.search(r'([A-Za-z]+\s+\d+\s+\d+:\d+:\d+)', line)
            if timestamp_match:
                timestamp_data.append(timestamp_match.group(1))
            ip_match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
            if ip_match:
                ip = ip_match.group(1)
                ip_data[ip].append(get_country_from_ip(ip))
            for activity, pattern in patterns.items():
                if pattern.search(line):
                    suspicious_activity[activity] += 1
    return suspicious_activity, total_lines, timestamp_data, ip_data

# Função para salvar o relatório
def save_report(log_file, suspicious_activity, total_lines, ip_data):
    report_file = log_file.replace('.log', '_output.txt')
    with open(report_file, 'w') as f:
        f.write(f'Total lines processed: {total_lines}\n\n')
        if suspicious_activity:
            for activity, count in suspicious_activity.items():
                f.write(f'{activity}: {count}\n{remedies[activity]}\n\n')
        else:
            f.write('No suspicious activity detected.\n')
        f.write("\nIP Address Origins:\n")
        for ip, countries in ip_data.items():
            f.write(f"{ip}: {', '.join(set(countries))}\n")
    return report_file

# Função para gerar gráficos
def plot_suspicious_activity(log_file, suspicious_activity, timestamp_data):
    if not suspicious_activity and not timestamp_data:
        return None, None
    activities = list(suspicious_activity.keys())
    counts = list(suspicious_activity.values())
    if activities:
        plt.figure(figsize=(10, 5))
        plt.bar(activities, counts, color='red')
        plt.xlabel('Activity Type')
        plt.ylabel('Count')
        plt.title('Suspicious Activity Detected in Logs')
        plt.savefig(log_file.replace('.log', '_suspicious_activity.png'))
        plt.close()
    if timestamp_data:
        timestamps = [datetime.strptime(ts, "%b %d %H:%M:%S") for ts in timestamp_data]
        plt.figure(figsize=(10, 5))
        plt.hist(timestamps, bins=10, color='blue', edgecolor='black', alpha=0.7)
        plt.xlabel('Timestamp')
        plt.ylabel('Count')
        plt.title('Timestamps of Suspicious Activities')
        plt.savefig(log_file.replace('.log', '_timestamp_activity.png'))
        plt.close()

# Função principal
def run_analysis(log_file):
    suspicious_activity, total_lines, timestamp_data, ip_data = analyze_log_file(log_file)
    save_report(log_file, suspicious_activity, total_lines, ip_data)
    plot_suspicious_activity(log_file, suspicious_activity, timestamp_data)
    print("Analysis complete! Check generated report and graphs.")

if __name__ == '__main__':
    log_file = input("Enter the path of the log file to analyze: ")
    if os.path.exists(log_file):
        run_analysis(log_file)
    else:
        print(f"File {log_file} does not exist!")
