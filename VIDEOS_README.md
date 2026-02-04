# WiFi Security Analyzer - Video Tutorials

## Overview
The WiFi Security Analyzer now includes 4 comprehensive video tutorials that teach users about WiFi security, threat detection, domain safety, and how to use the application.

## Videos Generated

### 1. **How to Use WiFi Security Analyzer**
- **File**: `how-to-use.mp4`
- **Duration**: 15 seconds (repeating slides)
- **Topics**:
  - Opening the application
  - Understanding threat levels (Green/Yellow/Orange/Red)
  - Using the Domain Checker
  - Viewing demo networks

### 2. **WiFi Security Best Practices**
- **File**: `wifi-security.mp4`
- **Duration**: 15 seconds (repeating slides)
- **Topics**:
  - Encryption types (WEP, WPA, WPA2, WPA3)
  - Why encryption matters
  - Home network security setup
  - Router security best practices

### 3. **What Threats Look Like**
- **File**: `threat-detection.mp4`
- **Duration**: 15 seconds (repeating slides)
- **Topics**:
  - Evil Twin attacks
  - SSID cloning and spoofing
  - Open networks vulnerabilities
  - How to recognize threat patterns

### 4. **Check Website Safety**
- **File**: `domain-safety.mp4`
- **Duration**: 15 seconds (repeating slides)
- **Topics**:
  - Domain types (Commercial, Educational, Government, etc.)
  - Red flags for malicious domains
  - Phishing prevention tips
  - Safe browsing practices

## How to Access Videos

1. Open the WiFi Security Analyzer in your browser
2. Go to the **"Video Tutorials"** section
3. Click on any video card to open the player
4. Videos will play with full HTML5 video controls:
   - Play/Pause
   - Volume control
   - Full-screen mode
   - Playback speed (browser dependent)

## Video Generation

All videos were generated using Python with:
- **PIL (Python Imaging Library)**: For creating text-based frames
- **imageio**: For assembling frames into MP4 video files

### Regenerate Videos

To regenerate the videos, run:
```bash
python make_videos.py
```

## Video File Locations

Videos are stored in:
```
static/videos/
├── how-to-use.mp4
├── wifi-security.mp4
├── threat-detection.mp4
└── domain-safety.mp4
```

## Customizing Videos

To customize the video content, edit `make_videos.py`:

1. Modify the text content in the `videos` dictionary
2. Change the `bg_color` values (RGB tuples) for different background colors
3. Adjust `duration` parameter for video length
4. Run `python make_videos.py` to regenerate

### Color Reference
- **How to Use**: Purple (102, 126, 234)
- **WiFi Security**: Dark Purple (118, 75, 162)
- **Threat Detection**: Red (255, 107, 107)
- **Domain Safety**: Yellow (255, 193, 7)

## Upgrading to HD Videos

To replace placeholder text-based videos with higher quality content:

1. **Option 1 - Use FFmpeg**:
   - Install FFmpeg from https://ffmpeg.org/download.html
   - Create videos with ffmpeg commands
   - Place MP4 files in `static/videos/`

2. **Option 2 - Use Professional Videos**:
   - Create or download tutorial videos
   - Ensure 1280x720 (HD) or higher resolution
   - Use MP4 format with H.264 codec
   - Place in `static/videos/` with matching filenames

3. **Option 3 - Use YouTube Videos**:
   - To revert to YouTube embedding, edit `playVideo()` function in `templates/portal.html`
   - Replace the video tag with iframe embeds

## Video Specifications

- **Resolution**: 1280x720 (HD)
- **Frame Rate**: 24 fps
- **Codec**: H.264 (MP4)
- **Audio**: AAC (optional)
- **Container**: MP4

## Browser Support

Videos work on all modern browsers:
- ✓ Chrome/Chromium
- ✓ Firefox
- ✓ Safari
- ✓ Edge
- ✓ Opera

## Troubleshooting

**Videos not playing?**
1. Check that `static/videos/` directory exists
2. Verify video files are not corrupted: `ls -la static/videos/`
3. Check browser console for errors (F12)
4. Clear browser cache and reload

**Videos loading slowly?**
1. Check internet connection speed
2. Reduce video quality or duration if needed
3. Consider caching headers in Flask app

**Need different video format?**
1. Install ffmpeg: `choco install ffmpeg` (Windows) or `brew install ffmpeg` (Mac)
2. Convert videos: `ffmpeg -i input.mp4 -c:v libx264 -preset medium output.mp4`

## Technical Details

### How Videos Are Served

```python
# Flask automatically serves files from static folder
GET /static/videos/how-to-use.mp4 → static/videos/how-to-use.mp4
```

### HTML5 Video Player

```html
<video width="100%" height="100%" controls>
    <source src="/static/videos/how-to-use.mp4" type="video/mp4">
</video>
```

### JavaScript Video Handling

```javascript
function playVideo(videoType) {
    // Opens modal with HTML5 video player
    // Loads appropriate video file based on type
    // Users can control playback with standard controls
}
```

## Future Enhancements

- [ ] Add subtitle/caption files (.vtt)
- [ ] Generate higher quality videos with voiceover
- [ ] Add interactive quiz after each video
- [ ] Create animated diagrams for threat visualization
- [ ] Support for multiple languages with dubbed audio
- [ ] YouTube/Vimeo integration for cloud hosting
- [ ] Progress tracking for video completion

## Support

For issues with videos or to request new tutorials, please refer to:
- Main README.md
- GitHub Issues
- Support email

---

**Generated**: February 4, 2026
**Status**: Ready for Production
**Quality**: Educational/Tutorial Grade
