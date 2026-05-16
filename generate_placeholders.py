#!/usr/bin/env python3
"""
generate_placeholders.py
Run this once to create simple placeholder PNG images for each hardware
component, software icon, and process diagram needed for the quiz.

Usage:
    python generate_placeholders.py
"""

import os
from PIL import Image, ImageDraw, ImageFont

IMAGES_DIR = os.path.join(os.path.dirname(__file__), "static", "images")
os.makedirs(IMAGES_DIR, exist_ok=True)

# Try to load a nicer font, fall back to default
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 16)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 12)
except:
    font = ImageFont.load_default()
    font_small = ImageFont.load_default()

# ============================================================
# COMPUTER HARDWARE COMPONENTS (with image file names)
# ============================================================
COMPONENTS = {
    # Basic hardware
    "cpu":         ("CPU\nCentral Processing Unit",  "#1B3A6B"),
    "ram":         ("RAM\nMemory Module",             "#1A7A4A"),
    "motherboard": ("Motherboard\nMain Circuit Board","#6B3A1B"),
    "gpu":         ("GPU\nGraphics Card",             "#4A1B6B"),
    "hdd":         ("HDD\nHard Disk Drive",           "#6B6B1B"),
    "ssd":         ("SSD\nSolid State Drive",         "#1B6B6B"),
    "psu":         ("PSU\nPower Supply Unit",         "#6B1B3A"),
    "monitor":     ("Monitor\nOutput Device",         "#2E4A8A"),
    "keyboard":    ("Keyboard\nInput Device",         "#3A6B1B"),
    "mouse":       ("Mouse\nPointing Device",         "#5C5C5C"),
    "printer":     ("Printer\nOutput Device",         "#8A6B3A"),
    "speakers":    ("Speakers\nAudio Output",         "#4A6B8A"),
    "webcam":      ("Webcam\nVideo Input",            "#2A5A5A"),
    "scanner":     ("Scanner\nInput Device",          "#6A6A2A"),
    "usb_drive":   ("USB Drive\nFlash Storage",       "#3A6B8A"),
    "headphones":  ("Headphones\nPersonal Audio",     "#4A4A4A"),
    "router":      ("Router\nNetworking Device",      "#8A4A2E"),
    "laptop":      ("Laptop\nPortable Computer",     "#2A5A8A"),
    "tablet":      ("Tablet\nTouch Screen Device",    "#4A8A2A"),
    "smartphone":  ("Smartphone\nMobile Phone",       "#2A6B6B"),
    "microphone":  ("Microphone\nAudio Input",        "#6B4A2A"),
    "projector":   ("Projector\nDisplay Output",      "#4A4A6B"),
    
    # Storage devices
    "external_hdd": ("External HDD\nPortable Drive",  "#8A6B4A"),
    "sd_card":      ("SD Card\nMemory Card",          "#5A5A8A"),
    "bluetooth_speaker": ("Bluetooth Speaker\nWireless Audio", "#3A7A5A"),
    "smartwatch":   ("Smartwatch\nWearable Device",   "#6B3A6B"),
    "vr_headset":   ("VR Headset\nVirtual Reality",   "#2A4A6A"),
    
    # Additional hardware
    "cooling_fan":  ("Cooling Fan\nHeat Management",  "#5A6B7A"),
    "cd_dvd_drive": ("DVD Drive\nOptical Storage",    "#7A6B5A"),
    "network_card": ("Network Card\nConnectivity",    "#4A6B7A"),
    "sound_card":   ("Sound Card\nAudio Processing",  "#7A4A6B"),
    "battery":      ("Laptop Battery\nPower Source",  "#6B6B3A"),
    
    # Ports & Connectors
    "usb_port":     ("USB Port\nUniversal Connector", "#3A6B8A"),
    "hdmi_port":    ("HDMI Port\nVideo/Audio Output", "#6B3A4A"),
    "ethernet_port":("Ethernet Port\nWired Network",  "#4A6B3A"),
    "audio_jack":   ("Audio Jack\nHeadphone Port",    "#5A5A5A"),
    "power_port":   ("Power Port\nCharger Connector", "#8A3A2A"),
    
    # Software Icons
    "chrome_icon":      ("Chrome\nWeb Browser",          "#4A8A2A"),
    "word_icon":        ("Microsoft Word\nWord Processor","#2A5A8A"),
    "excel_icon":       ("Microsoft Excel\nSpreadsheet", "#1B6B3A"),
    "powerpoint_icon":  ("PowerPoint\nPresentations",    "#8A3A1B"),
    "recycle_bin":      ("Recycle Bin\nDeleted Files",   "#6B6B6B"),
    "folder_icon":      ("Folder\nFile Organization",    "#4A7A9A"),
    
    # Process Images (for drag-sort questions)
    "boot_sequence":        ("Computer Boot\nStartup Process",      "#2A5A8A"),
    "shutdown_sequence":    ("Shut Down\nPower Off Process",        "#8A3A2A"),
    "send_email":           ("Send Email\nEmail Process",           "#3A7A5A"),
    "web_search":           ("Web Search\nFind Information",        "#5A4A8A"),
    "save_file":            ("Save File\nDocument Storage",         "#4A8A6A"),
    "print_document":       ("Print Document\nPaper Output",        "#8A6A3A"),
    "copy_file":            ("Copy File\nFile Duplication",         "#6A4A8A"),
    "connect_peripherals":  ("Connect Devices\nSetup Process",      "#3A6B8A"),
    "connect_wifi":         ("Connect WiFi\nWireless Setup",        "#4A8A3A"),
    "install_software":     ("Install Software\nProgram Setup",     "#8A3A6A"),
    "eject_usb":            ("Eject USB\nSafely Remove",            "#5A6B4A"),
    "screenshot":           ("Take Screenshot\nCapture Screen",     "#6B4A5A"),
    "strong_password":      ("Strong Password\nPassword Security",  "#3A6B6B"),
    "data_sizes":           ("Data Sizes\nStorage Units",           "#4A6B8A"),
    "file_sizes":           ("File Sizes\nDocument Sizes",          "#6B8A4A"),
    "computer_speed":       ("Computer Speed\nPerformance",         "#8A6B4A"),
    "backup":               ("Backup Files\nData Protection",       "#6B4A6A"),
    "browser_tabs":         ("Browser Tabs\nWeb Browsing",          "#4A8A6A"),
    "bookmark":             ("Bookmark\nSave Webpage",              "#3A7A8A"),
    "clear_history":        ("Clear History\nPrivacy Settings",     "#8A4A4A"),
    "zoom_meeting":         ("Zoom Meeting\nVideo Conference",      "#4A6B8A"),
    "email_attach":         ("Email Attachment\nSend Files",        "#6B8A3A"),
    "upgrade_ram":          ("Upgrade RAM\nMemory Installation",    "#6B3A8A"),
}

print("🎨 Generating placeholder images...")
print("=" * 50)

def create_placeholder_image(name, label, colour, width=400, height=300):
    """Create a placeholder image with text"""
    path = os.path.join(IMAGES_DIR, f"{name}.png")
    img = Image.new("RGB", (width, height), colour)
    draw = ImageDraw.Draw(img)
    
    # White rounded rectangle border
    draw.rounded_rectangle([10, 10, width-10, height-10], radius=20, outline="white", width=3)
    
    # Draw a simple icon/diagram in the background
    if "boot" in name or "shutdown" in name:
        # Draw step circles for process diagrams
        for i in range(1, 6):
            x = width // 6 * i
            y = height // 2
            draw.ellipse([x-20, y-20, x+20, y+20], outline="white", width=2)
            draw.text((x-6, y-8), str(i), fill="white", font=font)
            if i < 5:
                draw.line([x+20, y, x+40, y], fill="white", width=2)
    elif "sequence" in name:
        # Draw arrows for sequence diagrams
        draw.line([50, height//2, width-50, height//2], fill="white", width=3)
        draw.polygon([(width-50, height//2-10), (width-30, height//2), (width-50, height//2+10)], fill="white")
    
    # Add main text
    lines = label.split("\n")
    y_offset = height // 3 if len(lines) > 1 else height // 2
    
    # Try to use larger font for main text
    try:
        big_font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 20)
    except:
        big_font = font
    
    for i, line in enumerate(lines):
        if i == 0:
            # Main title
            bbox = draw.textbbox((0, 0), line, font=big_font)
            w = bbox[2] - bbox[0]
            draw.text(((width - w) // 2, y_offset), line, fill="white", font=big_font)
            y_offset += 40
        else:
            # Subtitle
            bbox = draw.textbbox((0, 0), line, font=font_small)
            w = bbox[2] - bbox[0]
            draw.text(((width - w) // 2, y_offset), line, fill="#E0E0E0", font=font_small)
            y_offset += 25
    
    # Add "Drag & Drop" badge
    badge_y = height - 40
    badge_text = "← Drag label here →" if "drag" in name.lower() else "Interactive"
    bbox = draw.textbbox((0, 0), badge_text, font=font_small)
    w = bbox[2] - bbox[0]
    draw.text(((width - w) // 2, badge_y), badge_text, fill="#FFD700", font=font_small)
    
    img.save(path)
    print(f"  ✓ Created {path} ({width}x{height})")

# Generate all images
for name, (label, colour) in COMPONENTS.items():
    # Different sizes for different types
    if name in ["boot_sequence", "shutdown_sequence", "web_search", "send_email"]:
        width, height = 500, 350  # Larger for process diagrams
    elif "_port" in name or "_icon" in name:
        width, height = 200, 150  # Smaller for ports and icons
    else:
        width, height = 400, 300  # Standard size
    
    create_placeholder_image(name, label, colour, width, height)

# Also create generic placeholder for any missing images
create_placeholder_image("placeholder", "Image\nNot Available", "#8895A7", 400, 300)

print("=" * 50)
print(f"\n✅ Generated {len(COMPONENTS)} placeholder images in {IMAGES_DIR}")
print("\n📁 Image files created:")
print("   • Hardware components: 35 files")
print("   • Ports & connectors: 5 files") 
print("   • Software icons: 6 files")
print("   • Process diagrams: 23 files")
print("\n⚠️  IMPORTANT:")
print("   1. These are PLACEHOLDER images for development")
print("   2. Replace with real photos before deploying to production")
print("   3. Keep the same filenames when replacing")
print("\n📝 Image naming convention:")
print("   All images are saved as PNG files with lowercase names")
print("   Use underscores for multi-word names (e.g., usb_drive.png)")