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
    'malware': re.compile(r'malware|virus|trojan|ransomware', re.IGNORECASE),
    'file_tampering': re.compile(r'file tampering|unauthorized file modification', re.IGNORECASE),
    'unauthorized_access': re.compile(r'unauthorized access|login failure|invalid login|access denied', re.IGNORECASE),
    'security_breach': re.compile(r'security breach|data breach|intrusion detected|unauthorized entry', re.IGNORECASE),
    'advanced_malware': re.compile(r'zero-day|advanced persistent threat|rootkit', re.IGNORECASE),
    'phishing': re.compile(r'phishing|spear phishing|fraudulent email', re.IGNORECASE),
    'data_leakage': re.compile(r'data leakage|data exfiltration|information leak', re.IGNORECASE)
}

remedies = {
    'malware': "Remedy: Run a full system antivirus scan, isolate the affected systems, and update your antivirus software.",
    'file_tampering': "Remedy: Restore the affected files from backup, change file permissions, and monitor file integrity.",
    'unauthorized_access': "Remedy: Reset passwords, implement multi-factor authentication, and review access logs.",
    'security_breach': "Remedy: Disconnect affected systems from the network, conduct a thorough investigation, and notify affected parties.",
    'advanced_malware': "Remedy: Employ advanced threat detection tools, perform a deep system scan, and update security protocols.",
    'phishing': "Remedy: Educate users about phishing, implement email filtering solutions, and report the phishing attempt.",
    'data_leakage': "Remedy: Identify the source of the leak, implement data loss prevention solutions, and review data access policies."
}

# Função para obter país a partir do IP
def get_country_from_ip(ip):
    try:
        # Usando uma API pública para geolocalização
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'fail':
            return 'Unknown'
        return data['country']
    except Exception as e:
        print(f"Error fetching country for IP {ip}: {e}")
        return 'Unknown'

# Função para carregar padrões e remédios de um arquivo de configuração, se existir
config_file = 'log_analyzer_config.json'

def load_patterns():
    global patterns, remedies
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            config = json.load(f)
            patterns.update({k: re.compile(v, re.IGNORECASE) for k, v in config.get('patterns', {}).items()})
            remedies.update(config.get('remedies', {}))

# Função para salvar os padrões e remédios em um arquivo de configuração
def save_patterns():
    config = {
        'patterns': {k: v.pattern for k, v in patterns.items()},
        'remedies': {k: v for k, v in remedies.items()}
    }
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=4)

# Função para analisar o arquivo de log
def analyze_log_file(log_file):
    suspicious_activity = defaultdict(int)
    ip_data = defaultdict(list)
    timestamp_data = []
    total_lines = 0
    
    with open(log_file, 'r') as f:
        for line in f:
            total_lines += 1
            try:
                # Pega o timestamp da linha de log
                timestamp_match = re.search(r'\[([^\]]+)\]', line)  # Extrai o timestamp da linha
                if timestamp_match:
                    timestamp_data.append(timestamp_match.group(1))  # Adiciona o timestamp à lista

                # Captura IP de origem (para logs HTTP/SSH)
                ip_match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
                if ip_match:
                    ip = ip_match.group(1)
                    country = get_country_from_ip(ip)
                    ip_data[ip].append(country)

                # Checa as atividades suspeitas
                for activity, pattern in patterns.items():
                    if pattern.search(line):
                        suspicious_activity[activity] += 1
            except Exception as e:
                pass
    return suspicious_activity, total_lines, timestamp_data, ip_data

# Função para salvar o relatório de atividades suspeitas
def save_report(log_file, suspicious_activity, total_lines, ip_data):
    report_file = log_file.replace('.log', '_output.txt')
    with open(report_file, 'w') as f:
        f.write(f'Total lines processed: {total_lines}\n\n')
        
        # Relatório das atividades suspeitas
        if suspicious_activity:
            for activity, count in suspicious_activity.items():
                f.write(f'{activity}: {count}\n')
                f.write(f'{remedies[activity]}\n\n')
        else:
            f.write('No suspicious activity detected.\n')
        
        # Relatório de IPs e países
        f.write("\nIP Address Origins:\n")
        for ip, countries in ip_data.items():
            f.write(f"{ip}: {', '.join(set(countries))}\n")
    return report_file

# Função para gerar e salvar os gráficos das atividades suspeitas e timestamps
def plot_suspicious_activity(log_file, suspicious_activity, timestamp_data):
    # Se não houver atividades suspeitas ou timestamps, retornamos None
    if not suspicious_activity and not timestamp_data:
        return None, None

    # Gráfico de atividades suspeitas (como barras)
    activities = list(suspicious_activity.keys())
    counts = list(suspicious_activity.values())
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(activities, counts, color='red')
    ax.set_xlabel('Activity Type')
    ax.set_ylabel('Count')
    ax.set_title('Suspicious Activity Detected in Logs')

    graph_file = log_file.replace('.log', '_suspicious_activity.png')
    fig.savefig(graph_file)
    plt.close(fig)

    # Gráfico de timestamps (histograma de tentativas de login, por exemplo)
    timestamps = [datetime.strptime(ts, "%d/%b/%Y:%H:%M:%S %z") for ts in timestamp_data]
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(timestamps, bins=50, color='blue', edgecolor='black', alpha=0.7)
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Count')
    ax.set_title('Timestamps of Suspicious Activities')

    timestamp_graph_file = log_file.replace('.log', '_timestamp_activity.png')
    fig.savefig(timestamp_graph_file)
    plt.close(fig)

    return graph_file, timestamp_graph_file

# Função principal para rodar a análise
def run_analysis(log_file):
    suspicious_activity, total_lines, timestamp_data, ip_data = analyze_log_file(log_file)
    report_file = save_report(log_file, suspicious_activity, total_lines, ip_data)
    
    # Gerando os gráficos
    graph_file, timestamp_graph_file = plot_suspicious_activity(log_file, suspicious_activity, timestamp_data)

    result_message = f"Analysis complete!\nReport saved to: {report_file}"
    if graph_file:
        result_message += f"\nGraph saved to: {graph_file}"

    if timestamp_graph_file:
        result_message += f"\nTimestamp Graph saved to: {timestamp_graph_file}"

    # Exibir no terminal
    print(result_message)

    if suspicious_activity:
        alert_message = "Suspicious activity detected!"
        print(f"ALERT: {alert_message}")

# Função principal
if __name__ == '__main__':
    # Carregar padrões de arquivo de configuração
    load_patterns()

    # Solicitar o caminho do arquivo de log ao usuário
    log_file = input("Enter the path of the log file to analyze: ")

    # Executar análise
    if os.path.exists(log_file):
        run_analysis(log_file)
    else:
        print(f"File {log_file} does not exist!")
