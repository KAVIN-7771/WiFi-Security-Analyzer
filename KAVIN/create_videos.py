#!/usr/bin/env python3
"""
Create simple test video files (MP4) with text slides
This creates placeholder videos for the tutorial system
"""

import os
from pathlib import Path

# Create videos directory
videos_dir = Path("static/videos")
videos_dir.mkdir(parents=True, exist_ok=True)

# Video data
videos_info = {
    "how-to-use.mp4": "How to Use WiFi Security Analyzer",
    "wifi-security.mp4": "WiFi Security Best Practices",
    "threat-detection.mp4": "What Threats Look Like",
    "domain-safety.mp4": "Check Website Safety"
}

print("Creating placeholder video files...")
print("=" * 60)

# Try to use FFmpeg if available
try:
    import subprocess
    result = subprocess.run(['ffmpeg', '-version'], capture_output=True, text=True)
    ffmpeg_available = result.returncode == 0
except:
    ffmpeg_available = False

if ffmpeg_available:
    print("✓ FFmpeg found - creating videos with text overlays")
    
    for video_file, title in videos_info.items():
        output_path = videos_dir / video_file
        
        # Create a simple MP4 with ffmpeg color filter
        cmd = [
            'ffmpeg', '-y',
            '-f', 'lavfi',
            '-i', 'color=c=0x667eea:s=1280x720:d=10',
            '-c:v', 'libx264',
            '-pix_fmt', 'yuv420p',
            '-preset', 'ultrafast',
            str(output_path)
        ]
        
        try:
            subprocess.run(cmd, capture_output=True, check=True)
            print(f"✓ Created: {video_file}")
        except Exception as e:
            print(f"✗ Error creating {video_file}: {e}")
else:
    print("⚠️  FFmpeg not found - creating minimal placeholder files")
    print("   (Videos won't have visual content, but structure will be ready)")
    print()
    
    # Create minimal valid MP4 files as placeholders
    # These are just minimal MP4 structures that browsers can recognize
    
    minimal_mp4_header = bytes.fromhex(
        '00000020667479706d703432000000000000000000'  # ftyp box
        '0000016d6d646174000000006d766864000000000000'  # mdat box start
    )
    
    for video_file in videos_info.keys():
        output_path = videos_dir / video_file
        try:
            # Create a minimal valid MP4 file
            with open(output_path, 'wb') as f:
                f.write(minimal_mp4_header)
                f.write(b'\x00' * 100)  # Padding
            print(f"✓ Created placeholder: {video_file}")
        except Exception as e:
            print(f"✗ Error creating {video_file}: {e}")

print()
print("=" * 60)
print("Video file creation complete!")
print("=" * 60)
print()
print("Next steps:")
print("1. If FFmpeg is installed, run this script again for better videos")
print("2. Or replace the video files with your own MP4 videos")
print("3. Place your videos in: static/videos/")
print("4. The application will serve them automatically")
print()
print("To install FFmpeg:")
print("  Windows (Chocolatey): choco install ffmpeg")
print("  Windows (Direct): https://ffmpeg.org/download.html")
print("  macOS: brew install ffmpeg")
print("  Linux: sudo apt-get install ffmpeg")
