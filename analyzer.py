import re

log_file = "sample_logs/auth.log"
failed_attempts = {}

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
            if ip_match:
                ip = ip_match.group(1)
                failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

print("=== Failed Login Attempts ===")

for ip, count in failed_attempts.items():
    if count >= 3:
        print(f"[ALERT] Possible brute-force from {ip} ({count} attempts)")