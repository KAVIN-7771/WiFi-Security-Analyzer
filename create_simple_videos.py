#!/usr/bin/env python3
"""
Simple AI Video Creator - Creates basic tutorial videos using ffmpeg
"""

import os
import subprocess
from pathlib import Path
import json

class SimpleVideoCreator:
    """Create simple tutorial videos using ffmpeg"""
    
    def __init__(self, output_dir="static/videos"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def create_video_with_text(self, title, text_content, color, output_file):
        """Create a video with scrolling text using ffmpeg"""
        duration = 15  # seconds
        width = 1280
        height = 720
        
        # Create a text file for the content
        text_file = self.output_dir / f"{output_file.stem}_text.txt"
        with open(text_file, 'w', encoding='utf-8') as f:
            f.write(text_content)
        
        # FFmpeg command to create video
        cmd = [
            'ffmpeg', '-y',
            '-f', 'lavfi',
            '-i', f'color={color}:s={width}x{height}:d={duration}',
            '-vf', f'drawtext=textfile={text_file}:fontfile=/Windows/Fonts/arial.ttf:fontsize=40:fontcolor=white:x=50:y=50',
            '-pix_fmt', 'yuv420p',
            str(output_file)
        ]
        
        try:
            subprocess.run(cmd, capture_output=True, check=True)
            print(f"✓ Created: {output_file}")
            return True
        except Exception as e:
            print(f"✗ Error creating {output_file}: {e}")
            return False
    
    def create_how_to_use_video(self):
        """Create 'How to Use' tutorial"""
        print("Creating 'How to Use' tutorial video...")
        
        text = """
HOW TO USE WiFi SECURITY ANALYZER

1. Open your web browser
2. Go to http://localhost:5000
3. Click 'Analyze WiFi' button
4. View your network security score

UNDERSTAND THE RESULTS:
• Green (0-20): SAFE network
• Yellow (20-40): CAUTION needed
• Orange (40-60): RISKY network
• Red (60-100): UNSAFE network

CHECK DOMAINS:
• Use the Domain Checker
• Enter any website URL
• Get safety analysis
• Learn about domain types

NEXT STEPS:
• Review recommendations
• Secure your network
• Change weak passwords
• Update encryption to WPA3
"""
        
        output_file = self.output_dir / "how-to-use.mp4"
        return self.create_video_with_text("How to Use", text, "667eea", output_file)
    
    def create_wifi_security_video(self):
        """Create 'WiFi Security' tutorial"""
        print("Creating 'WiFi Security' tutorial video...")
        
        text = """
WiFi SECURITY BEST PRACTICES

ENCRYPTION TYPES:
WEP - OLD, NOT SECURE (avoid)
WPA - Better alternative
WPA2 - Strong, widely used ✓
WPA3 - Latest, most secure ✓✓

WHY ENCRYPTION MATTERS:
• Protects your personal data
• Prevents password theft
• Stops eavesdropping
• Secures banking info

SECURE YOUR HOME NETWORK:
1. Change default router password
2. Enable WPA3 or WPA2
3. Use strong WiFi password (20+ chars)
4. Update router firmware regularly
5. Disable WPS (WiFi Protected Setup)

ROUTER SECURITY:
• Enable firewall protection
• Disable remote management
• Check connected devices regularly
• Hide SSID broadcast (optional)
"""
        
        output_file = self.output_dir / "wifi-security.mp4"
        return self.create_video_with_text("WiFi Security", text, "764ba2", output_file)
    
    def create_threat_detection_video(self):
        """Create 'Threat Detection' tutorial"""
        print("Creating 'Threat Detection' tutorial video...")
        
        text = """
WIFI THREAT DETECTION

EVIL TWIN ATTACKS:
• Attacker creates fake WiFi
• Looks like legitimate network
• Users unknowingly connect
• Attacker captures all data
• Prevention: Use VPN, verify settings

RED FLAGS:
⚠️ Unknown network names
⚠️ No encryption (Open network)
⚠️ Unusually strong signal
⚠️ Network name misspellings
⚠️ New networks appearing

SSID CLONING:
• Duplicate network names
• Creates user confusion
• Directs traffic to attacker
• Check your router settings

OPEN NETWORKS:
• No password protection
• All data in clear text
• Anyone can intercept data
• Only use for public browsing

PROTECT YOURSELF:
✓ Use VPN on public WiFi
✓ Check network before connecting
✓ Use HTTPS websites
✓ Enable firewall
✓ Keep software updated
"""
        
        output_file = self.output_dir / "threat-detection.mp4"
        return self.create_video_with_text("Threat Detection", text, "ff6b6b", output_file)
    
    def create_domain_safety_video(self):
        """Create 'Domain Safety' tutorial"""
        print("Creating 'Domain Safety' tutorial video...")
        
        text = """
CHECK WEBSITE SAFETY

DOMAIN TYPES:
🏢 Commercial: .com, .co, .biz
🎓 Educational: .edu
🏛️ Government: .gov
🤝 Organization: .org, .ngo
🌐 Technology: .io, .dev, .app
🏦 Banking: .bank
💰 Finance: .finance

RED FLAGS:
⚠️ URLs with typos
⚠️ Misspelled domain names
⚠️ Non-HTTPS websites
⚠️ Suspicious email links
⚠️ Too-good-to-be-true offers

PHISHING PREVENTION:
1. Check sender email address
2. Look for HTTPS lock icon
3. Verify official website link
4. Don't click email links
5. Type URL directly in browser

SAFE BROWSING:
✓ Use HTTPS websites
✓ Verify domain name carefully
✓ Check certificate validity
✓ Use domain checker tool
✓ Enable browser protection
✓ Keep browser updated

TRUST THE TOOL:
🟢 GREEN = Safe website
🟡 YELLOW = Be cautious
🔴 RED = Avoid this domain
"""
        
        output_file = self.output_dir / "domain-safety.mp4"
        return self.create_video_with_text("Domain Safety", text, "ffc107", output_file)
    
    def create_all_videos(self):
        """Create all tutorial videos"""
        print("=" * 60)
        print("WiFi Security Analyzer - Video Creator")
        print("=" * 60)
        print()
        
        # Check if ffmpeg is available
        try:
            subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
        except:
            print("❌ FFmpeg not found!")
            print("Please install FFmpeg from: https://ffmpeg.org/download.html")
            print("Or install via: choco install ffmpeg")
            return False
        
        results = {
            "how-to-use": self.create_how_to_use_video(),
            "wifi-security": self.create_wifi_security_video(),
            "threat-detection": self.create_threat_detection_video(),
            "domain-safety": self.create_domain_safety_video(),
        }
        
        print()
        print("=" * 60)
        print("Video Creation Complete!")
        print("=" * 60)
        
        successful = sum(1 for r in results.values() if r)
        print(f"\nSuccessfully created: {successful}/4 videos")
        
        if successful > 0:
            print(f"\nVideos saved to: {self.output_dir}")
            return True
        else:
            print("\nNo videos created - check FFmpeg installation")
            return False


if __name__ == "__main__":
    creator = SimpleVideoCreator()
    creator.create_all_videos()
