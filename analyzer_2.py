import re

log_file = "sample_logs/auth.log"

failed_attempts = {}
successful_logins = {}
alerts = []

with open(log_file, "r") as file:
    for line in file:

        # FAILED LOGINS
        if "Failed password" in line:
            ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
            user_match = re.search(r"for (\w+)", line)

            if ip_match:
                ip = ip_match.group(1)
                failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

            if user_match:
                user = user_match.group(1)
                successful_logins[user] = successful_logins.get(user, 0)

        # SUCCESSFUL LOGINS
        if "Accepted password" in line:
            user_match = re.search(r"for (\w+)", line)

            if user_match:
                user = user_match.group(1)
                successful_logins[user] = successful_logins.get(user, 0) + 1

# PRINT RESULTS
print("\n=== FAILED LOGIN ATTEMPTS ===")
for ip, count in failed_attempts.items():
    print(f"{ip} → {count} attempts")
    if count >= 3:
        alert = f"[ALERT] Possible brute-force from {ip} ({count} attempts)"
        alerts.append(alert)
        print(alert)

print("\n=== SUCCESSFUL LOGINS ===")
for user, count in successful_logins.items():
    print(f"{user} → {count} logins")

# SAVE TO FILE
with open("output.txt", "w") as out:
    out.write("=== SECURITY REPORT ===\n\n")

    out.write("FAILED LOGIN ATTEMPTS:\n")
    for ip, count in failed_attempts.items():
        out.write(f"{ip} → {count}\n")

    out.write("\nALERTS:\n")
    for alert in alerts:
        out.write(alert + "\n")

    out.write("\nSUCCESSFUL LOGINS:\n")
    for user, count in successful_logins.items():
        out.write(f"{user} → {count}\n")

print("\nReport saved to output.txt")