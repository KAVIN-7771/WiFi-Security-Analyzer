#!/usr/bin/env python3
"""
AI Video Generator for WiFi Security Analyzer Tutorials
Generates tutorial videos using text-to-speech and slide animations
"""

import os
import sys
from pathlib import Path
from datetime import datetime
import json

try:
    from moviepy.editor import (
        ColorClip, TextClip, CompositeVideoClip, 
        concatenate_videoclips, AudioFileClip
    )
    from pydub import AudioSegment
    from pydub.generators import Sine
except ImportError:
    print("Installing required packages...")
    os.system("pip install moviepy pydub pillow")
    from moviepy.editor import (
        ColorClip, TextClip, CompositeVideoClip, 
        concatenate_videoclips, AudioFileClip
    )
    from pydub import AudioSegment

try:
    import pyttsx3
    tts_available = True
except ImportError:
    print("Note: pyttsx3 not available, will use alternative TTS")
    tts_available = False


class AIVideoGenerator:
    """Generate tutorial videos with text-to-speech and animations"""
    
    def __init__(self, output_dir="static/videos"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.fps = 24
        self.width = 1280
        self.height = 720
        
    def text_to_speech(self, text, output_file):
        """Convert text to speech using pyttsx3"""
        if not tts_available:
            print(f"Skipping TTS for: {text[:50]}...")
            return None
            
        try:
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            engine.setProperty('volume', 0.9)
            engine.save_to_file(text, output_file)
            engine.runAndWait()
            return output_file
        except Exception as e:
            print(f"TTS Error: {e}")
            return None
    
    def create_title_slide(self, title, duration=3):
        """Create an animated title slide"""
        clip = ColorClip(size=(self.width, self.height), color=(102, 126, 234))
        
        txt_clip = TextClip(
            title,
            fontsize=60,
            color='white',
            font='Arial',
            method='caption',
            size=(self.width - 100, None),
            align='center'
        )
        txt_clip = txt_clip.set_duration(duration)
        txt_clip = txt_clip.set_position('center')
        
        video = CompositeVideoClip([clip, txt_clip])
        return video.set_duration(duration)
    
    def create_content_slide(self, title, content_list, duration=5):
        """Create a slide with title and bullet points"""
        clip = ColorClip(size=(self.width, self.height), color=(255, 255, 255))
        
        # Title
        title_clip = TextClip(
            title,
            fontsize=50,
            color=(51, 51, 51),
            font='Arial',
            bold=True
        )
        title_clip = title_clip.set_position((60, 60))
        title_clip = title_clip.set_duration(duration)
        
        # Content
        content_text = "\n".join(f"• {item}" for item in content_list)
        content_clip = TextClip(
            content_text,
            fontsize=32,
            color=(102, 102, 102),
            font='Arial',
            method='caption',
            size=(self.width - 200, None)
        )
        content_clip = content_clip.set_position((100, 250))
        content_clip = content_clip.set_duration(duration)
        
        video = CompositeVideoClip([clip, title_clip, content_clip])
        return video.set_duration(duration)
    
    def create_highlight_slide(self, title, highlight_text, color, duration=4):
        """Create a highlighted information slide"""
        clip = ColorClip(size=(self.width, self.height), color=(240, 240, 240))
        
        # Title
        title_clip = TextClip(
            title,
            fontsize=50,
            color=(51, 51, 51),
            font='Arial',
            bold=True
        )
        title_clip = title_clip.set_position((60, 60))
        title_clip = title_clip.set_duration(duration)
        
        # Highlight box
        highlight_bg = ColorClip(
            size=(self.width - 200, 300),
            color=color
        ).set_duration(duration).set_position((100, 250))
        
        # Highlight text
        highlight_clip = TextClip(
            highlight_text,
            fontsize=36,
            color='white',
            font='Arial',
            method='caption',
            size=(self.width - 240, 280),
            align='center'
        )
        highlight_clip = highlight_clip.set_position((120, 270))
        highlight_clip = highlight_clip.set_duration(duration)
        
        video = CompositeVideoClip([clip, highlight_bg, title_clip, highlight_clip])
        return video.set_duration(duration)
    
    def generate_how_to_use_video(self):
        """Generate 'How to Use' tutorial video"""
        print("Generating 'How to Use WiFi Security Analyzer' video...")
        
        slides = [
            self.create_title_slide("How to Use WiFi Security Analyzer", 3),
            self.create_content_slide(
                "Getting Started",
                [
                    "Open the WiFi Security Analyzer in your web browser",
                    "Navigate to http://localhost:5000",
                    "The application automatically detects your WiFi network",
                    "View the security analysis results"
                ],
                5
            ),
            self.create_content_slide(
                "Main Features",
                [
                    "Network Analysis: Real-time WiFi security check",
                    "Domain Checker: Verify if websites are safe",
                    "Threat Detection: Identify security threats",
                    "Demo Mode: See safe vs unsafe networks",
                    "Video Tutorials: Learn WiFi security"
                ],
                5
            ),
            self.create_highlight_slide(
                "Understanding Threat Levels",
                "🟢 SAFE (0-20)\n🟡 CAUTION (20-40)\n🟠 RISKY (40-60)\n🔴 UNSAFE (60-100)",
                (100, 150, 255),
                5
            ),
            self.create_content_slide(
                "Next Steps",
                [
                    "Click 'Analyze WiFi' to check your network",
                    "Use Domain Checker to verify websites",
                    "Review security recommendations",
                    "Take action to improve your security"
                ],
                4
            ),
            self.create_title_slide("Start Protecting Your WiFi Today!", 3)
        ]
        
        try:
            final_video = concatenate_videoclips(slides)
            output_path = self.output_dir / "how-to-use.mp4"
            final_video.write_videofile(
                str(output_path),
                fps=self.fps,
                codec='libx264',
                audio_codec='aac',
                verbose=False,
                logger=None
            )
            print(f"✓ Created: {output_path}")
            return output_path
        except Exception as e:
            print(f"✗ Error: {e}")
            return None
    
    def generate_wifi_security_video(self):
        """Generate 'WiFi Security Best Practices' video"""
        print("Generating 'WiFi Security Best Practices' video...")
        
        slides = [
            self.create_title_slide("WiFi Security Best Practices", 3),
            self.create_content_slide(
                "Encryption Types",
                [
                    "WEP: Outdated, not secure (avoid)",
                    "WPA: Better, but WPA2/WPA3 preferred",
                    "WPA2: Strong encryption, widely used",
                    "WPA3: Latest, most secure standard"
                ],
                5
            ),
            self.create_highlight_slide(
                "Why Encryption Matters",
                "Encryption protects your data from:\n• Hackers and eavesdroppers\n• Data theft\n• Password capture\n• Personal information exposure",
                (76, 175, 80),
                5
            ),
            self.create_content_slide(
                "Home Network Security Setup",
                [
                    "Change default router password",
                    "Update router firmware regularly",
                    "Enable WPA3 or WPA2 encryption",
                    "Use a strong WiFi password (20+ characters)",
                    "Disable WPS (WiFi Protected Setup)"
                ],
                5
            ),
            self.create_content_slide(
                "Router Security Best Practices",
                [
                    "Disable remote management",
                    "Enable firewall protection",
                    "Hide SSID broadcast (optional)",
                    "Use MAC filtering for trusted devices",
                    "Regularly check connected devices"
                ],
                5
            ),
            self.create_title_slide("Secure Your WiFi Now!", 3)
        ]
        
        try:
            final_video = concatenate_videoclips(slides)
            output_path = self.output_dir / "wifi-security.mp4"
            final_video.write_videofile(
                str(output_path),
                fps=self.fps,
                codec='libx264',
                audio_codec='aac',
                verbose=False,
                logger=None
            )
            print(f"✓ Created: {output_path}")
            return output_path
        except Exception as e:
            print(f"✗ Error: {e}")
            return None
    
    def generate_threat_detection_video(self):
        """Generate 'What Threats Look Like' video"""
        print("Generating 'What Threats Look Like' video...")
        
        slides = [
            self.create_title_slide("What Threats Look Like", 3),
            self.create_content_slide(
                "Evil Twin Attacks",
                [
                    "Attacker creates fake WiFi with legitimate name",
                    "Users unknowingly connect to malicious network",
                    "Attacker captures all data transmitted",
                    "Prevention: Check router settings, use VPN"
                ],
                5
            ),
            self.create_highlight_slide(
                "Evil Twin Attack",
                "Fake WiFi that looks legitimate\nSteal passwords and personal data\nUse VPN to stay safe",
                (255, 87, 34),
                4
            ),
            self.create_content_slide(
                "SSID Cloning & Spoofing",
                [
                    "Attacker duplicates network name (SSID)",
                    "Creates confusion among users",
                    "Users connect to wrong network",
                    "Data can be intercepted by attacker"
                ],
                5
            ),
            self.create_content_slide(
                "Open Networks & Guest Networks",
                [
                    "No password protection",
                    "All data transmitted in clear text",
                    "Anyone can connect and see traffic",
                    "Only use for non-sensitive activities"
                ],
                5
            ),
            self.create_highlight_slide(
                "Recognize Threats",
                "🚩 No encryption (Open)\n🚩 Unknown network names\n🚩 Unusually strong signals\n🚩 Network name misspellings",
                (244, 67, 54),
                4
            ),
            self.create_title_slide("Stay Alert, Stay Secure!", 3)
        ]
        
        try:
            final_video = concatenate_videoclips(slides)
            output_path = self.output_dir / "threat-detection.mp4"
            final_video.write_videofile(
                str(output_path),
                fps=self.fps,
                codec='libx264',
                audio_codec='aac',
                verbose=False,
                logger=None
            )
            print(f"✓ Created: {output_path}")
            return output_path
        except Exception as e:
            print(f"✗ Error: {e}")
            return None
    
    def generate_domain_safety_video(self):
        """Generate 'Check Website Safety' video"""
        print("Generating 'Check Website Safety' video...")
        
        slides = [
            self.create_title_slide("Check Website Safety", 3),
            self.create_content_slide(
                "Domain Types",
                [
                    "🏢 Commercial (.com, .co, .biz)",
                    "🎓 Educational (.edu)",
                    "🏛️ Government (.gov)",
                    "🤝 Organization (.org, .ngo)",
                    "🌐 Technology (.io, .dev, .app)"
                ],
                5
            ),
            self.create_highlight_slide(
                "Red Flags - Malicious Domains",
                "⚠️ URLs with typos of popular sites\n⚠️ Domains with unusual extensions\n⚠️ Non-HTTPS websites for sensitive data\n⚠️ Known phishing site lists",
                (255, 152, 0),
                5
            ),
            self.create_content_slide(
                "How to Check Domain Safety",
                [
                    "Use the Domain Checker in the application",
                    "Enter website URL to analyze",
                    "Check if domain is known malicious",
                    "Verify encryption and certificate validity",
                    "Read safety explanation provided"
                ],
                5
            ),
            self.create_content_slide(
                "Phishing Attack Prevention",
                [
                    "Never click links in unsolicited emails",
                    "Verify sender email address carefully",
                    "Check for HTTPS and lock icon",
                    "Look for suspicious grammar/spelling",
                    "When in doubt, go directly to website"
                ],
                5
            ),
            self.create_highlight_slide(
                "Trust the Indicators",
                "🟢 GREEN = Safe to visit\n🟡 YELLOW = Be cautious\n🔴 RED = Avoid this domain",
                (76, 175, 80),
                4
            ),
            self.create_title_slide("Browse Safely Online!", 3)
        ]
        
        try:
            final_video = concatenate_videoclips(slides)
            output_path = self.output_dir / "domain-safety.mp4"
            final_video.write_videofile(
                str(output_path),
                fps=self.fps,
                codec='libx264',
                audio_codec='aac',
                verbose=False,
                logger=None
            )
            print(f"✓ Created: {output_path}")
            return output_path
        except Exception as e:
            print(f"✗ Error: {e}")
            return None
    
    def generate_all_videos(self):
        """Generate all tutorial videos"""
        print("=" * 60)
        print("WiFi Security Analyzer - AI Video Generator")
        print("=" * 60)
        print()
        
        results = {
            "how-to-use": self.generate_how_to_use_video(),
            "wifi-security": self.generate_wifi_security_video(),
            "threat-detection": self.generate_threat_detection_video(),
            "domain-safety": self.generate_domain_safety_video(),
        }
        
        print()
        print("=" * 60)
        print("Video Generation Complete!")
        print("=" * 60)
        
        # Save metadata
        metadata = {
            "generated_at": datetime.now().isoformat(),
            "videos": {
                name: {
                    "path": str(path),
                    "status": "completed" if path else "failed"
                }
                for name, path in results.items()
            }
        }
        
        metadata_file = self.output_dir / "metadata.json"
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"Metadata saved to: {metadata_file}")
        print()
        
        # Summary
        successful = sum(1 for p in results.values() if p)
        print(f"Successfully generated: {successful}/4 videos")
        for name, path in results.items():
            status = "✓" if path else "✗"
            print(f"  {status} {name}")


if __name__ == "__main__":
    generator = AIVideoGenerator()
    generator.generate_all_videos()
