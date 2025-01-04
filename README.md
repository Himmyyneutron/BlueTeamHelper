# Blue Team Helper 🚀
A Python project to assist with generating and analyzing Windows security logs. This tool is designed for blue teams, SOC analysts, and cybersecurity enthusiasts to practice log analysis and improve threat detection skills.

## Features 🌟
- **Log Generation**: Create realistic Windows security logs with random events like logins, file accesses, and suspicious activities.
- **Log Parsing**: Analyze logs for:
  - Failed login attempts.
  - Connections from flagged IPs (with geolocation).
  - Events occurring during unusual hours (midnight–6 AM).
- **User-Friendly Interface**: Menu-driven design with ASCII art and clear outputs.
- **CSV Export**: Save analysis results (e.g., failed logins) to CSV files for further review.

## Usage 📖
### 1. Clone the Repository
```bash
git clone https://github.com/<YourUsername>/BlueTeamHelper.git
cd BlueTeamHelper
