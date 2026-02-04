# WiFi Security Analyzer - Quick Start Guide

## Installation & Running (5 minutes)

### Step 1: Install Dependencies
Open Command Prompt or PowerShell in the project folder and run:
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
python app.py
```

You should see output like:
```
 * Running on http://127.0.0.1:5000
```

### Step 3: Open in Browser
Navigate to: **http://127.0.0.1:5000**

The application will automatically start analyzing your WiFi network!

---

## What You'll See

### 🌐 Current Network Panel
Shows your connected WiFi network details:
- Network name (SSID)
- Signal strength percentage
- Encryption type (WPA2, WPA3, etc.)
- Router IP address
- Estimated distance from router
- Security score (0-100)

### 🚨 Threat Detection
Displays detected threats in your network:
- Encryption weaknesses
- Attack patterns (Evil Twin, SSID cloning)
- Open/guest network warnings

### 🛡️ Security Levels
- **SAFE** (Green) - Excellent, use normally
- **CAUTION** (Yellow) - Minor risks, avoid sensitive data
- **RISKY** (Orange) - Multiple threats, use VPN
- **UNSAFE** (Red) - Critical threats, don't use

### 💡 Recommendations
Personalized security tips based on your network analysis.

### 🔍 Domain Checker
Test if a website domain is safe by checking against malicious domain database.

### 📡 Nearby Networks
Scan and view available WiFi networks in your area.

---

## Features Explained

### 1. Signal Strength & Distance
The app estimates your distance from the router based on signal strength:
- **Very Close** (90%+): 0-5 meters
- **Close** (70-90%): 5-15 meters  
- **Medium** (50-70%): 15-30 meters
- **Far** (30-50%): 30-50 meters
- **Very Far** (<30%): 50m+

### 2. Encryption Detection
The analyzer checks your WiFi encryption:
- ✓ **Secure**: WPA3, WPA2, WPA
- ✗ **Insecure**: WEP, Open networks

### 3. Threat Scoring
Security score is calculated based on:
- Encryption type (40 points max)
- Detected attacks (30 points max)
- Network openness (15 points max)
- Other factors (15 points max)

Scores combine to create your 0-100 threat level.

---

## Common Use Cases

### Checking Home WiFi
✓ Good for ensuring your home network is secure
✓ Should show SAFE (green) with WPA2/WPA3
✓ Signal should be strong (80%+)

### Analyzing Public WiFi
✓ Shows if network is risky (usually RISKY/UNSAFE)
✓ Recommends VPN usage
✓ Warns about open networks

### Network Security Awareness
✓ Educational tool for learning WiFi security
✓ Demonstrates encryption importance
✓ Shows real attack patterns

---

## Troubleshooting

### "Failed to analyze WiFi"
- Make sure you're connected to WiFi (not Ethernet)
- Try clicking "Refresh Analysis" button
- Restart the application

### Domain checker not working
- Enter full domain (example.com, not www.example.com)
- Check internet connection
- Domain must be resolvable

### Permission denied errors (Windows)
- Run Command Prompt as Administrator
- Then run: `python app.py`

### Port 5000 already in use
Edit the last line in `app.py`:
```python
app.run(debug=True, host="127.0.0.1", port=5001)  # Change 5000 to 5001
```

---

## Tips & Best Practices

### For Maximum Security:
1. Use WPA3 or WPA2 encryption at home
2. Use strong, unique passwords (16+ characters)
3. Update router firmware regularly
4. Disable WPS (WiFi Protected Setup)
5. Hide SSID broadcast if not needed

### On Public WiFi:
1. Always use a VPN
2. Disable auto-connect
3. Turn off file sharing
4. Don't enter passwords or payment info
5. Use HTTPS websites only

### Network Monitoring:
- Run analysis regularly (daily or weekly)
- Watch for SSID changes
- Monitor connected device count
- Check for unfamiliar SSIDs in area

---

## Technical Details

### Backend API Endpoints

**GET /api/analyze-wifi**
- Returns complete network analysis
- Includes threats, encryption, recommendations

**POST /api/check-domain**
- Checks domain safety
- Request: `{"domain": "example.com"}`
- Response: `{"safe": true/false, "reason": "..."}`

**GET /api/networks-nearby**
- Lists available WiFi networks
- Returns network details and status

**GET /api/health**
- Server health check
- Returns status and timestamp

### Data Flow
1. Frontend fetches WiFi data via API
2. Backend uses system commands (netsh/nmcli)
3. Python analyzes encryption & threats
4. Results sent back to frontend
5. Frontend displays with color coding

---

## Security Considerations

### What This Tool Can Detect:
- Weak or missing encryption
- Open and guest networks
- Evil Twin attack patterns
- SSID cloning attempts
- Malicious domains

### What It Cannot Detect:
- Active packet sniffing
- Advanced MitM attacks
- SSL/TLS vulnerabilities
- Password strength
- Individual device security

### Limitations:
- Only analyzes connected network
- Pattern-based threat detection
- Limited nearby network range
- No deep packet inspection
- Requires direct access to WiFi

---

## Performance Notes

- Initial analysis: 5-10 seconds
- Subsequent refreshes: 2-3 seconds
- Auto-refresh: Every 30 seconds
- Nearby networks scan: 3-5 seconds

---

## Getting Help

1. Check the full README.md for detailed docs
2. Verify WiFi connection is active
3. Check browser console (F12) for errors
4. Try restarting the application
5. Ensure Python and Flask are installed correctly

---

## Next Steps

1. Run the application and explore all features
2. Check your home WiFi security
3. Test on different networks
4. Use domain checker for websites
5. Monitor network security regularly

Enjoy using WiFi Security Analyzer!
