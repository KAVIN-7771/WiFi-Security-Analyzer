# WiFi Security Analyzer 🔒

A comprehensive web-based application that analyzes WiFi network security, detects potential threats, and provides security recommendations.

## Features

### 🌐 Current Network Analysis
- **Real-time Network Detection**: Automatically detects your current WiFi network
- **Signal Strength Monitoring**: Shows WiFi signal quality as a percentage
- **Authentication Type**: Displays encryption method (WPA3, WPA2, WEP, etc.)
- **Router IP Address**: Shows gateway/router IP address
- **Distance Estimation**: Rough distance estimation based on signal strength (0-5m, 5-15m, 15-30m, 30-50m, 50m+)
- **Security Score**: Visual threat level indicator (0-100)

### 🚨 Threat Detection
- **Encryption Analysis**: Checks for weak or missing encryption
- **Attack Pattern Detection**: Identifies signs of Evil Twin attacks, SSID cloning
- **Malicious Domain Database**: Checks against known malicious domains
- **Security Status**: Displays threats with severity levels
  - SAFE ✓ (Green) - Excellent security
  - CAUTION 🛡️ (Yellow) - Minor risks
  - RISKY ⚡ (Orange) - Significant risks
  - UNSAFE ⚠️ (Red) - Critical risks

### 🔍 Domain Safety Checker
- Check if a domain is safe to visit
- Verifies against malicious domain database
- Checks for threat keywords in domain names
- Validates domain resolution

### 📡 Nearby Networks
- Lists available WiFi networks in your area
- Shows network status and security information
- One-click network selection for connecting

### 💡 Security Recommendations
- Personalized security tips based on your network
- Best practices for WiFi security
- Recommendations for VPN usage on public networks

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Windows, Linux, or macOS system

### Setup Steps

1. **Clone or Download** the project:
   ```bash
   cd C:\Users\kavin\OneDrive\Documents\KAVIN
   ```

2. **Install Required Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   The dependencies are:
   - Flask 3.0.0 - Web framework
   - Flask-CORS 4.0.0 - Cross-origin request handling
   - Werkzeug 3.0.1 - WSGI utility library
   - requests 2.31.0 - HTTP library

3. **Run the Application**:
   ```bash
   python app.py
   ```

4. **Access the Application**:
   - Open your web browser
   - Navigate to: `http://127.0.0.1:5000`
   - The application will automatically start analyzing your WiFi

## Application Structure

```
KAVIN/
├── app.py                 # Flask backend with WiFi security analyzer
├── portal.html            # Frontend UI with real-time analysis
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## How It Works

### Backend (app.py)

#### WiFiSecurityAnalyzer Class
The core analysis engine that performs:

1. **Network Detection**:
   - Windows: Uses `netsh wlan show interfaces` command
   - Linux: Uses `nmcli device wifi show` command

2. **Security Assessment**:
   - Checks encryption method (WPA3/WPA2 = secure, WEP/Open = insecure)
   - Analyzes SSID for attack patterns
   - Calculates threat score (0-100)

3. **Threat Analysis**:
   - Detects Evil Twin networks (free/public/guest networks)
   - Identifies SSID cloning patterns
   - Checks for suspicious network names

#### API Endpoints

- **GET `/api/analyze-wifi`**
  - Performs complete WiFi security analysis
  - Returns network info, threat level, recommendations
  ```json
  {
    "network_info": {
      "ssid": "Network Name",
      "signal": 85,
      "auth": "WPA2-Personal",
      "gateway": "192.168.1.1",
      "estimated_distance": "Close (5-15m)"
    },
    "threat_level": "SAFE ✓",
    "threat_score": 15,
    "threats": [],
    "encryption": {
      "is_encrypted": true,
      "status": "Uses WPA2-Personal encryption (Good)"
    },
    "recommendations": [...]
  }
  ```

- **POST `/api/check-domain`**
  - Checks if a domain is safe
  - Request body: `{"domain": "example.com"}`
  ```json
  {
    "safe": true,
    "reason": "Domain resolves successfully"
  }
  ```

- **GET `/api/networks-nearby`**
  - Lists nearby WiFi networks
  - Returns list of available networks with security status

- **GET `/api/health`**
  - Health check endpoint
  - Returns server status and timestamp

### Frontend (portal.html)

Modern responsive web interface with:

- **Real-time Analysis**: Updates WiFi security status automatically
- **Visual Indicators**: Color-coded threat levels (green/yellow/orange/red)
- **Interactive Elements**: Domain checker, network scanner, refresh buttons
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Auto-refresh**: Analyzes network every 30 seconds

## Threat Database

### Known Malicious Domains
The system includes a database of known malicious domains:
- attacker.com
- phishing-site.net
- malware-distribution.org
- trojan-host.com
- ransomware-server.net
- botnet-command.org

### Threat Keywords
Detects suspicious domain names containing:
- trojan, malware, phishing, ransomware, botnet
- exploit, backdoor, spyware, adware, scareware

## WiFi Security Levels

### SAFE ✓ (Green - Score 0-20)
- Uses WPA3 or WPA2 encryption
- No attack patterns detected
- Professional network configuration
- **Recommendation**: Safe to use for normal activities

### CAUTION 🛡️ (Yellow - Score 20-40)
- Minor encryption concerns
- Some suspicious patterns detected
- **Recommendation**: Avoid sensitive data on this network

### RISKY ⚡ (Orange - Score 40-60)
- Weak encryption or multiple threats
- Several attack patterns detected
- **Recommendation**: Use VPN if possible, avoid sensitive data

### UNSAFE ⚠️ (Red - Score 60-100)
- No encryption or critical vulnerabilities
- Clear signs of potential attacks
- **Recommendation**: Do not use this network

## Security Features

### Encryption Check
- **Secure**: WPA3, WPA2, WPA
- **Insecure**: WEP, Open networks

### Attack Pattern Detection
- Evil Twin networks (open/guest networks)
- SSID cloning patterns (_ext, _guest suffixes)
- Suspiciously short SSID names
- Public network detection

### Signal Strength Analysis
- **Very Close (0-5m)**: 90%+ signal - Likely legitimate
- **Close (5-15m)**: 70-90% signal
- **Medium (15-30m)**: 50-70% signal
- **Far (30-50m)**: 30-50% signal
- **Very Far (50m+)**: <30% signal

## Security Best Practices

1. **On Public Networks**:
   - ✓ Always use a VPN
   - ✓ Disable auto-connect features
   - ✗ Don't enter passwords or credit card info

2. **At Home**:
   - ✓ Use WPA3 or WPA2 encryption
   - ✓ Use strong, unique passwords
   - ✓ Update router firmware regularly

3. **General Tips**:
   - ✓ Keep software updated
   - ✓ Use a firewall
   - ✓ Avoid public file sharing
   - ✓ Monitor connected devices

## System Requirements

### Windows
- Windows 7 or higher
- Administrator privileges (for WiFi scanning)
- netsh command-line utility (built-in)

### Linux
- Ubuntu, Debian, Fedora, or other distributions
- nmcli tool (`sudo apt install network-manager`)

### macOS
- macOS 10.12 or higher
- May require modification to WiFi detection code

## Troubleshooting

### "Unable to analyze WiFi"
- **Cause**: WiFi not detected or network unavailable
- **Solution**: Connect to a WiFi network and refresh the page

### "Domain cannot be resolved"
- **Cause**: Domain name is invalid or DNS resolution failed
- **Solution**: Check domain spelling and ensure internet connection

### Backend not responding
- **Cause**: Flask server not running
- **Solution**: Run `python app.py` in terminal

### Permission denied on network analysis
- **Cause**: Insufficient permissions for WiFi commands
- **Solution**: Run terminal as administrator (Windows) or use sudo (Linux)

### Port already in use
- **Cause**: Port 5000 is already being used
- **Solution**: Modify `app.py` line to use different port:
  ```python
  app.run(debug=True, host="127.0.0.1", port=5001)
  ```

## Advanced Configuration

### Change Analysis Refresh Rate
In `portal.html`, find the auto-refresh interval:
```javascript
setInterval(analyzeWiFi, 30000);  // 30 seconds
```
Change `30000` to your desired milliseconds.

### Add Custom Malicious Domains
In `app.py`, add to `MALICIOUS_DOMAINS` list:
```python
MALICIOUS_DOMAINS = [
    'attacker.com',
    'your-domain.com',  # Add here
    ...
]
```

### Adjust Threat Scoring
Modify threat calculation in `WiFiSecurityAnalyzer.analyze_network()`:
```python
if is_encrypted is False:
    threat_score += 40  # Change this value
```

## API Response Examples

### Analyze WiFi Response
```json
{
  "network_info": {
    "ssid": "MyHomeWiFi",
    "signal": 88,
    "auth": "WPA2-Personal",
    "gateway": "192.168.1.1",
    "estimated_distance": "Close (5-15m)"
  },
  "threat_level": "SAFE ✓",
  "threat_score": 10,
  "color": "green",
  "threats": [],
  "encryption": {
    "is_encrypted": true,
    "status": "Uses WPA2-Personal encryption (Good)"
  },
  "recommendations": [
    "Network appears secure. Continue standard security practices.",
    "Avoid sharing sensitive data on any public network."
  ]
}
```

### Domain Check Response (Safe)
```json
{
  "safe": true,
  "reason": "Domain resolves successfully"
}
```

### Domain Check Response (Unsafe)
```json
{
  "safe": false,
  "reason": "Contains threat keyword: malware"
}
```

## Performance Notes

- Initial analysis may take 5-10 seconds on first load
- Subsequent refreshes are faster (2-3 seconds)
- Network scanning is non-blocking
- Auto-refresh happens every 30 seconds in background

## Limitations

1. **WiFi Detection**: Only works on connected networks
2. **Nearby Networks**: Limited in range (~100m depending on router)
3. **Encryption Check**: Only verifies type, not password strength
4. **Attack Detection**: Pattern-based, not comprehensive
5. **Domain Check**: Limited to malicious domain database

## Future Enhancements

- [ ] Real-time packet capture and analysis
- [ ] IP reputation checking
- [ ] SSL certificate validation
- [ ] Network speed testing
- [ ] Device scanning on connected network
- [ ] DNS spoofing detection
- [ ] Man-in-the-Middle attack detection
- [ ] Mobile app version
- [ ] Machine learning threat detection

## License

This project is provided as-is for educational and security awareness purposes.

## Support

For issues or questions:
1. Check the Troubleshooting section
2. Verify all dependencies are installed
3. Ensure WiFi connection is active
4. Check browser console for errors (F12)

## Disclaimer

This tool is designed for educational purposes and network security awareness. Always:
- Get proper authorization before analyzing networks
- Use responsibly and ethically
- Follow local laws and regulations
- Respect network privacy and security
