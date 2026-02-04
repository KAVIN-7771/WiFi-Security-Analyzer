#!/usr/bin/env python3
"""
Create tutorial videos using PIL and imageio
This generates simple animated videos from text and images
"""

import os
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
    import imageio
    print("✓ Required libraries found")
except ImportError:
    print("Installing required packages...")
    os.system("pip install pillow imageio -q")
    from PIL import Image, ImageDraw, ImageFont
    import imageio

class VideoGenerator:
    def __init__(self, output_dir="static/videos"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.width = 1280
        self.height = 720
        self.fps = 24
        
    def create_text_frame(self, text, bg_color=(102, 126, 234), title="", text_color=(255, 255, 255)):
        """Create a single frame with text"""
        img = Image.new('RGB', (self.width, self.height), bg_color)
        draw = ImageDraw.Draw(img)
        
        # Try to use a system font
        try:
            title_font = ImageFont.truetype("C:\\Windows\\Fonts\\Arial.ttf", 60)
            text_font = ImageFont.truetype("C:\\Windows\\Fonts\\Arial.ttf", 28)
        except:
            # Fallback to default font
            title_font = ImageFont.load_default()
            text_font = ImageFont.load_default()
        
        # Draw title if provided
        if title:
            title_bbox = draw.textbbox((0, 0), title, font=title_font)
            title_width = title_bbox[2] - title_bbox[0]
            title_x = (self.width - title_width) // 2
            draw.text((title_x, 40), title, fill=text_color, font=title_font)
        
        # Draw text content
        lines = text.split('\n')
        y_offset = 150 if title else 80
        for line in lines:
            draw.text((60, y_offset), line, fill=text_color, font=text_font)
            y_offset += 45
        
        return img
    
    def create_video(self, title, content, bg_color, output_file, duration=15):
        """Create a video from text content"""
        print(f"Creating {output_file}...")
        
        # Create frames
        frames = []
        
        # Repeat the content frame multiple times to create video duration
        frame = self.create_text_frame(content, bg_color=bg_color, title=title)
        frames_needed = int(self.fps * duration)
        
        for _ in range(frames_needed):
            frames.append(frame)
        
        # Write video
        output_path = self.output_dir / output_file
        try:
            imageio.mimsave(str(output_path), frames, fps=self.fps)
            print(f"✓ Created: {output_file}")
            return True
        except Exception as e:
            print(f"✗ Error: {e}")
            return False
    
    def generate_all_videos(self):
        """Generate all tutorial videos"""
        print("=" * 60)
        print("WiFi Security Analyzer - Video Generator")
        print("=" * 60)
        print()
        
        videos = {
            "how-to-use.mp4": {
                "title": "HOW TO USE WiFi SECURITY ANALYZER",
                "content": """
1. Open web browser, go to http://localhost:5000
2. Click 'Analyze WiFi' to scan your network
3. View your network security score

THREAT LEVELS:
🟢 GREEN (0-20): SAFE
🟡 YELLOW (20-40): CAUTION
🟠 ORANGE (40-60): RISKY
🔴 RED (60-100): UNSAFE

CHECK DOMAINS:
• Use Domain Checker to verify websites
• Enter URL and get safety analysis
• Understand domain types and threats

VIEW DEMOS:
• See safe network examples (green)
• See unsafe network examples (red)
• Learn from live demonstrations
                """,
                "bg_color": (102, 126, 234)
            },
            "wifi-security.mp4": {
                "title": "WiFi SECURITY BEST PRACTICES",
                "content": """
ENCRYPTION TYPES:
WEP - Old, NOT secure (avoid)
WPA - Better alternative
WPA2 - Strong encryption ✓
WPA3 - Latest, most secure ✓✓

WHY ENCRYPTION MATTERS:
• Protects your personal data
• Prevents password theft
• Stops eavesdropping
• Secures banking info

SECURE YOUR NETWORK:
1. Change default router password
2. Enable WPA3 or WPA2
3. Use strong password (20+ chars)
4. Update router firmware regularly
5. Disable WPS (WiFi Protected Setup)

ROUTER SECURITY:
• Enable firewall protection
• Disable remote management
• Check connected devices regularly
• Hide SSID broadcast (optional)
                """,
                "bg_color": (118, 75, 162)
            },
            "threat-detection.mp4": {
                "title": "WiFi THREAT DETECTION",
                "content": """
EVIL TWIN ATTACKS:
• Attacker creates fake WiFi
• Looks like legitimate network
• Users unknowingly connect
• Attacker captures all data
Prevention: Use VPN, verify settings

RED FLAGS:
⚠️  Unknown network names
⚠️  No encryption (Open)
⚠️  Unusually strong signal
⚠️  Network name misspellings
⚠️  New networks appearing

SSID CLONING:
• Duplicate network names
• Creates user confusion
• Directs traffic to attacker
• Check your router settings

OPEN NETWORKS:
• No password protection
• All data in clear text
• Anyone can intercept
• Only use for public browsing

PROTECT YOURSELF:
✓ Use VPN on public WiFi
✓ Check network before connecting
✓ Use HTTPS websites
✓ Enable firewall
✓ Keep software updated
                """,
                "bg_color": (255, 107, 107)
            },
            "domain-safety.mp4": {
                "title": "CHECK WEBSITE SAFETY",
                "content": """
DOMAIN TYPES:
🏢 Commercial: .com, .co, .biz
🎓 Educational: .edu
🏛️  Government: .gov
🤝 Organization: .org, .ngo
🌐 Technology: .io, .dev, .app
🏦 Banking: .bank
💰 Finance: .finance

RED FLAGS - MALICIOUS:
⚠️  URLs with typos
⚠️  Misspelled domain names
⚠️  Non-HTTPS websites
⚠️  Suspicious email links
⚠️  Too-good-to-be-true offers

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

TRUST THE INDICATORS:
🟢 GREEN = Safe website
🟡 YELLOW = Be cautious
🔴 RED = Avoid this domain
                """,
                "bg_color": (255, 193, 7)
            }
        }
        
        results = {}
        for filename, data in videos.items():
            result = self.create_video(
                data["title"],
                data["content"],
                data["bg_color"],
                filename,
                duration=15
            )
            results[filename] = result
        
        print()
        print("=" * 60)
        print("Video Generation Complete!")
        print("=" * 60)
        
        successful = sum(1 for r in results.values() if r)
        print(f"Successfully created: {successful}/{len(videos)} videos")
        
        if successful == len(videos):
            print(f"\n✓ All videos ready in: {self.output_dir}")
            print("Videos are now available for streaming!")
            return True
        else:
            print("\n⚠️  Some videos failed to generate")
            return False


if __name__ == "__main__":
    generator = VideoGenerator()
    generator.generate_all_videos()
