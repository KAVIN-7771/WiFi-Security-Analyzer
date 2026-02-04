# WiFi Security Analyzer - Start Here

Welcome to the **WiFi Security Analyzer**! This complete application checks if your WiFi network is safe, detects threats, estimates distance to your router, checks domain safety, and provides security recommendations.

---

## ⚡ Quick Start (2 minutes)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
python app.py
```

### Step 3: Open in Browser
Navigate to: **http://127.0.0.1:5000**

That's it! The app automatically analyzes your WiFi network.

---

## 📁 File Guide

### Core Files
- **`app.py`** - Backend server with WiFi analyzer (Flask)
- **`templates/portal.html`** - Frontend web interface
- **`requirements.txt`** - Python dependencies

### Quick Start Files
- **`run.bat`** - Windows launcher (double-click to run)
- **`QUICKSTART.md`** - 5-minute setup guide
- **`SETUP.md`** - This file (installation overview)

### Documentation
- **`README.md`** - Complete documentation with all details
- **`PROJECT_SUMMARY.md`** - Technical project overview
- **`portal.html`** - Backup HTML file

---

## 🎯 What This App Does

### Network Analysis
- ✓ Detects your current WiFi network
- ✓ Shows signal strength percentage
- ✓ Identifies encryption type (WPA2, WPA3, etc.)
- ✓ Gets router IP address
- ✓ Estimates distance based on signal strength
- ✓ Calculates security threat score (0-100)

### Threat Detection
- ✓ Checks for weak encryption
- ✓ Identifies Evil Twin attacks
- ✓ Detects SSID cloning
- ✓ Finds open/guest networks
- ✓ Shows detected threats with severity

### Security Levels
- 🟢 **SAFE** - Excellent security (Score 0-20)
- 🟡 **CAUTION** - Minor risks (Score 20-40)
- 🟠 **RISKY** - Significant risks (Score 40-60)
- 🔴 **UNSAFE** - Critical risks (Score 60-100)

### Additional Features
- 🔍 Domain safety checker (test if websites are safe)
- 📡 Nearby networks scanner (discover WiFi in your area)
- 💡 Security recommendations (personalized advice)
- 🔄 Auto-refresh every 30 seconds

---

## 🚀 Getting Started

### For Windows Users:
**Option 1: Double-click the launcher**
```
Double-click: run.bat
```

**Option 2: Run manually**
```
1. Open Command Prompt
2. Navigate to: c:\Users\kavin\OneDrive\Documents\KAVIN
3. Type: python app.py
4. Open browser to: http://127.0.0.1:5000
```

### For Mac/Linux Users:
```
1. Open Terminal
2. Navigate to project folder
3. Run: python3 app.py
4. Open browser to: http://127.0.0.1:5000
```

---

## 📖 Documentation Guide

Choose what you need:

### I want to start RIGHT NOW
→ Read: **QUICKSTART.md** (5 minutes)

### I want to understand everything
→ Read: **README.md** (comprehensive guide)

### I want technical details
→ Read: **PROJECT_SUMMARY.md** (architecture & algorithms)

### I need help installing
→ Read: This file + QUICKSTART.md

---

## 🎨 Features Overview

### 🌐 Current Network Panel
Shows your connected WiFi with:
- Network name and signal strength
- Encryption type and status
- Router IP address
- Distance estimate
- Security score with visual bar
- Threat level indicator (color-coded)

### 🚨 Threats Detection
Lists all detected security issues:
- Encryption problems
- Attack patterns
- Network vulnerabilities
- Security warnings

### 💡 Recommendations
Personalized security advice:
- Encryption upgrade suggestions
- VPN recommendations
- Best practices for your network
- Protection tips

### 🔍 Domain Safety Checker
Check if websites are safe:
- Enter any domain name
- Get instant safety report
- See detailed reason
- Avoid malicious sites

### 📡 Nearby Networks
Discover WiFi networks nearby:
- Lists all available networks
- Shows network status
- Compare security
- Select to connect

---

## ✅ System Requirements

- **Python**: 3.8 or higher
- **OS**: Windows, Mac, or Linux
- **Browser**: Any modern browser (Chrome, Firefox, Edge, Safari)
- **Internet**: Connection required (for WiFi analysis)
- **Admin Access**: Needed for WiFi scanning (Windows)

---

## 🔐 Security Best Practices

### Home Network
- Use WPA3 or WPA2 encryption
- Strong password (16+ characters)
- Update router firmware
- Monitor connected devices

### Public WiFi
- Always use VPN
- Don't enter passwords or payment info
- Use HTTPS only
- Disable auto-connect

---

## ⚠️ Troubleshooting

### "Failed to analyze WiFi"
→ Make sure you're connected to WiFi (not Ethernet)
→ Click "Refresh Analysis" button
→ Restart application

### Permission denied (Windows)
→ Run Command Prompt as Administrator
→ Then run: `python app.py`

### Port 5000 already in use
→ Edit app.py, change port from 5000 to 5001
→ Access at: http://127.0.0.1:5001

### Python not found
→ Install Python from python.org
→ Make sure to check "Add Python to PATH"
→ Restart Command Prompt/Terminal

---

## 🎓 Example Use Cases

### Check Home WiFi Security
1. Connect to home WiFi
2. Open application
3. Should show SAFE (green) if using WPA2/WPA3
4. Review signal strength and recommendations

### Assess Public WiFi
1. Connect to public WiFi
2. Open application
3. Will likely show RISKY/UNSAFE (orange/red)
4. Follow VPN recommendation
5. Avoid sensitive activities

### Test Domain Safety
1. Use Domain Checker section
2. Enter suspicious website
3. Get instant safety report
4. Know before you visit

---

## 📊 Performance

- Initial Analysis: 5-10 seconds
- Refreshes: 2-3 seconds
- Domain Check: 1-2 seconds
- Auto-Refresh: Every 30 seconds

---

## 🆘 Getting Help

1. **Quick questions?** → Check QUICKSTART.md
2. **Setup issues?** → Read Troubleshooting above
3. **Need details?** → See README.md
4. **Technical info?** → View PROJECT_SUMMARY.md
5. **Still stuck?** → Check browser console (F12)

---

## 🎉 Ready to Start?

### Three Simple Steps:

```bash
# Step 1: Install packages
pip install -r requirements.txt

# Step 2: Run the app
python app.py

# Step 3: Open browser
http://127.0.0.1:5000
```

That's it! Enjoy analyzing your WiFi security! 🔒

---

## 📝 What's Inside

### Backend (Python/Flask)
- Network detection engine
- Security analysis algorithms
- Threat detection system
- Domain safety checker
- REST API endpoints

### Frontend (HTML/CSS/JavaScript)
- Real-time analysis display
- Interactive domain checker
- Network scanner interface
- Visual threat indicators
- Auto-refresh functionality

### Documentation
- Complete setup guide
- Quick start guide
- Full reference manual
- Project architecture
- Troubleshooting help

---

## 🌟 Key Features

1. **Real-time Analysis** - Automatic WiFi security checking
2. **Visual Indicators** - Color-coded threat levels
3. **Distance Estimation** - Based on signal strength
4. **Domain Checker** - Verify website safety
5. **Network Scanner** - Discover nearby WiFi
6. **Recommendations** - Personalized security advice
7. **Responsive Design** - Works on all devices
8. **No Installation Required** - Just Python and Flask

---

## 🔄 Auto-Analysis

The application automatically:
- Checks WiFi every 30 seconds
- Updates threat level in real-time
- Refreshes network information
- Monitors security changes
- Keeps recommendations current

---

## 💻 Technical Stack

- **Backend**: Python + Flask
- **Frontend**: HTML5 + CSS3 + JavaScript
- **Framework**: Flask with CORS
- **Communication**: REST API (JSON)
- **Styling**: Modern CSS with gradients

---

## 📚 Full Documentation Index

| File | Purpose | Read Time |
|------|---------|-----------|
| **QUICKSTART.md** | Get started in 5 minutes | 5 min |
| **README.md** | Complete documentation | 15 min |
| **PROJECT_SUMMARY.md** | Technical overview | 10 min |
| **This file** | Quick reference | 3 min |

---

## 🎯 Next Steps

1. ✓ Install dependencies: `pip install -r requirements.txt`
2. ✓ Start the app: `python app.py`  
3. ✓ Open browser: `http://127.0.0.1:5000`
4. ✓ Analyze your WiFi
5. ✓ Check domain safety
6. ✓ Review recommendations
7. ✓ Improve your network security

---

## 📞 Support

For detailed help:
- Check QUICKSTART.md for quick answers
- Read README.md for comprehensive guide
- Review PROJECT_SUMMARY.md for technical details
- Check browser console (F12) for error messages

---

**Version**: 1.0  
**Status**: Complete and Ready to Use ✓  
**Last Updated**: February 4, 2026

---

## 🚀 Ready?

```bash
python app.py
```

Then open: **http://127.0.0.1:5000**

Enjoy analyzing your WiFi security! 🔒
