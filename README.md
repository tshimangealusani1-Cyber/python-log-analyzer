# python-log-analyzer

# 🤖 Python Log Analyzer (Security Automation)

## 📌 Overview

I developed a Python-based log analysis tool to detect suspicious activity in Linux authentication logs.

This project simulates real-world SOC automation by identifying brute-force attacks and analyzing login behavior.

---

## 🎯 Objectives

* Parse authentication logs
* Detect failed login attempts
* Identify brute-force activity
* Track successful logins
* Generate automated security reports

---

## 🛠️ Technologies Used

* Python
* Regular Expressions (re)
* Linux auth.log

---

## 🔍 Features

### 🚨 Brute-Force Detection

* Counts failed login attempts per IP
* Flags IPs with multiple failed attempts

### 🔐 Successful Login Tracking

* Tracks number of successful logins per user

### 📊 Automated Reporting

* Outputs results to terminal
* Saves structured report to `output.txt`

---

## 📂 Project Workflow

1. Read authentication log file
2. Extract relevant data (IP, user)
3. Analyze login patterns
4. Detect suspicious behavior
5. Generate output report

---

## 🧪 Example Output

```
=== FAILED LOGIN ATTEMPTS ===
192.168.64.1 → 5 attempts
[ALERT] Possible brute-force from 192.168.64.1 (5 attempts)

=== SUCCESSFUL LOGINS ===
alusaniadmin → 2 logins

Report saved to output.txt
```

---

## 🚧 Challenges & Solutions

### Issue:

Incorrect file path caused script failure

### Fix:

Updated script to reference correct log file location

---

## 📈 Key Takeaways

* Log parsing using Python
* Automation of security analysis
* Detection of brute-force attacks
* Real-world SOC workflow simulation

---


