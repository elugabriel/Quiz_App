from app import app, db
from models import Question
import json

# Helper function to create questions
def create_question(topic, q_type, image_path, prompt, answer, options, difficulty):
    return {
        "topic": topic,
        "q_type": q_type,
        "image_path": image_path,
        "prompt": prompt,
        "answer": answer,
        "options": json.dumps(options),
        "difficulty": difficulty
    }

# ============================================================
# MODULE 1: COMPUTER HARDWARE (15 questions)
# ============================================================

computer_hardware = [
    # CPU Questions
    create_question("Computer Hardware", "drag_label", "images/cpu.png",
        "What component is often called the 'brain' of the computer?",
        "CPU",
        ["CPU", "RAM", "GPU", "Motherboard"],
        "easy"),
    
    create_question("Computer Hardware", "drag_label", "",
        "Which component's speed is measured in Gigahertz (GHz)?",
        "CPU",
        ["CPU", "RAM", "HDD", "PSU"],
        "easy"),
    
    create_question("Computer Hardware", "drag_label", "",
        "What does a CPU's clock speed determine?",
        "How fast it processes instructions",
        ["How fast it processes instructions", "How much data it stores", "How much power it uses", "How big it is physically"],
        "medium"),
    
    # RAM Questions
    create_question("Computer Hardware", "drag_label", "images/ram.png",
        "Which component provides temporary storage for currently running programs?",
        "RAM",
        ["RAM", "ROM", "HDD", "SSD"],
        "easy"),
    
    create_question("Computer Hardware", "drag_label", "",
        "What happens to data in RAM when you turn off the computer?",
        "It is lost",
        ["It is lost", "It is saved to HDD", "It remains in RAM", "It moves to CPU"],
        "easy"),
    
    create_question("Computer Hardware", "drag_label", "",
        "If your computer is slow when running many programs, what should you upgrade?",
        "RAM",
        ["RAM", "CPU", "Power Supply", "Monitor"],
        "easy"),
    
    # Storage (HDD/SSD)
    create_question("Computer Hardware", "drag_label", "images/hdd.png",
        "Which storage device uses spinning magnetic platters to read/write data?",
        "HDD",
        ["HDD", "SSD", "RAM", "USB Drive"],
        "easy"),
    
    create_question("Computer Hardware", "drag_label", "images/ssd.png",
        "Which storage device has no moving parts and is faster than traditional drives?",
        "SSD",
        ["SSD", "HDD", "DVD Drive", "Floppy Disk"],
        "easy"),
    
    create_question("Computer Hardware", "drag_label", "",
        "What is the main advantage of an SSD over an HDD?",
        "Faster read/write speeds",
        ["Faster read/write speeds", "Higher storage capacity", "Cheaper price", "Longer lifespan"],
        "medium"),
    
    # GPU Questions
    create_question("Computer Hardware", "drag_label", "images/gpu.png",
        "Which component is responsible for rendering images and videos on your screen?",
        "GPU",
        ["GPU", "CPU", "RAM", "Motherboard"],
        "easy"),
    
    create_question("Computer Hardware", "drag_label", "",
        "For gaming and video editing, which component is most important?",
        "GPU",
        ["GPU", "CPU", "RAM", "Power Supply"],
        "easy"),
    
    # Motherboard
    create_question("Computer Hardware", "drag_label", "images/motherboard.png",
        "What connects all computer components together?",
        "Motherboard",
        ["Motherboard", "CPU", "RAM", "PSU"],
        "easy"),
    
    # Power Supply
    create_question("Computer Hardware", "drag_label", "images/psu.png",
        "Which component converts AC power from the wall to DC power for components?",
        "Power Supply Unit (PSU)",
        ["Power Supply Unit (PSU)", "CPU", "Motherboard", "Battery"],
        "medium"),
    
    # Peripherals
    create_question("Computer Hardware", "drag_label", "images/keyboard.png",
        "Which input device is used for typing text?",
        "Keyboard",
        ["Keyboard", "Mouse", "Scanner", "Microphone"],
        "easy"),
    
    create_question("Computer Hardware", "drag_label", "images/monitor.png",
        "Which output device displays visual information?",
        "Monitor",
        ["Monitor", "Printer", "Speaker", "Projector"],
        "easy"),
]

# ============================================================
# MODULE 2: COMPUTER PORTS & CONNECTIONS (10 questions)
# ============================================================

computer_ports = [
    create_question("Computer Ports", "drag_label", "images/usb_port.png",
        "Which rectangular port is used to connect flash drives, keyboards, and mice?",
        "USB Port",
        ["USB Port", "HDMI Port", "Ethernet Port", "Audio Jack"],
        "easy"),
    
    create_question("Computer Ports", "drag_label", "images/hdmi_port.png",
        "Which port transmits high-definition video and audio to TVs and monitors?",
        "HDMI Port",
        ["HDMI Port", "USB Port", "VGA Port", "DisplayPort"],
        "easy"),
    
    create_question("Computer Ports", "drag_label", "images/ethernet_port.png",
        "Which port connects your computer to a wired internet network?",
        "Ethernet Port",
        ["Ethernet Port", "USB Port", "Phone Jack", "Modem Port"],
        "easy"),
    
    create_question("Computer Ports", "drag_label", "images/audio_jack.png",
        "Which 3.5mm port is used for connecting headphones or speakers?",
        "Audio Jack",
        ["Audio Jack", "USB Port", "HDMI Port", "Microphone Port"],
        "easy"),
    
    create_question("Computer Ports", "drag_label", "images/vga_port.png",
        "Which older blue port with 15 pins is used for connecting monitors?",
        "VGA Port",
        ["VGA Port", "HDMI Port", "USB Port", "DVI Port"],
        "medium"),
    
    create_question("Computer Ports", "drag_label", "images/usb_c_port.png",
        "Which newer oval-shaped reversible USB connector is becoming standard on laptops?",
        "USB-C Port",
        ["USB-C Port", "USB-A Port", "Lightning Port", "Micro USB"],
        "medium"),
    
    create_question("Computer Ports", "drag_label", "",
        "What does USB stand for?",
        "Universal Serial Bus",
        ["Universal Serial Bus", "Universal System Bus", "United Serial Bus", "Universal Software Bus"],
        "easy"),
    
    create_question("Computer Ports", "drag_label", "",
        "Which port is specifically designed for connecting a microphone?",
        "Microphone Jack (Pink)",
        ["Microphone Jack (Pink)", "Audio Jack (Green)", "USB Port", "HDMI Port"],
        "medium"),
    
    create_question("Computer Ports", "drag_label", "",
        "What is the maximum number of devices that can be connected to a single USB port using a hub?",
        "127 devices",
        ["127 devices", "10 devices", "50 devices", "Unlimited"],
        "hard"),
    
    create_question("Computer Ports", "drag_label", "",
        "Which port is color-coded GREEN on a standard computer?",
        "Audio Output/Speakers",
        ["Audio Output/Speakers", "Microphone Input", "USB Port", "Ethernet Port"],
        "medium"),
]

# ============================================================
# MODULE 3: SOFTWARE & OPERATING SYSTEMS (10 questions)
# ============================================================

software_questions = [
    create_question("Software", "drag_label", "images/windows_logo.png",
        "Which operating system is developed by Microsoft?",
        "Windows",
        ["Windows", "macOS", "Linux", "Android"],
        "easy"),
    
    create_question("Software", "drag_label", "images/macos_logo.png",
        "Which operating system is developed by Apple for Mac computers?",
        "macOS",
        ["macOS", "Windows", "Linux", "Chrome OS"],
        "easy"),
    
    create_question("Software", "drag_label", "images/linux_logo.png",
        "Which free, open-source operating system is popular for servers?",
        "Linux",
        ["Linux", "Windows", "macOS", "Unix"],
        "medium"),
    
    create_question("Software", "drag_label", "images/word_icon.png",
        "Which Microsoft Office application is used for word processing?",
        "Microsoft Word",
        ["Microsoft Word", "Microsoft Excel", "PowerPoint", "Outlook"],
        "easy"),
    
    create_question("Software", "drag_label", "images/excel_icon.png",
        "Which Microsoft Office application is used for spreadsheets?",
        "Microsoft Excel",
        ["Microsoft Excel", "Microsoft Word", "PowerPoint", "Access"],
        "easy"),
    
    create_question("Software", "drag_label", "images/powerpoint_icon.png",
        "Which Microsoft Office application is used for presentations?",
        "PowerPoint",
        ["PowerPoint", "Microsoft Word", "Microsoft Excel", "Publisher"],
        "easy"),
    
    create_question("Software", "drag_label", "images/chrome_icon.png",
        "Which web browser is developed by Google?",
        "Chrome",
        ["Chrome", "Firefox", "Safari", "Edge"],
        "easy"),
    
    create_question("Software", "drag_label", "",
        "What is an operating system?",
        "Software that manages computer hardware and software",
        ["Software that manages computer hardware", "A type of processor", "A storage device", "A programming language"],
        "easy"),
    
    create_question("Software", "drag_label", "",
        "Which of these is NOT an operating system?",
        "Microsoft Word",
        ["Microsoft Word", "Windows 11", "Ubuntu", "Android"],
        "easy"),
    
    create_question("Software", "drag_label", "",
        "What is the function of an antivirus program?",
        "Protect against malware and viruses",
        ["Protect against malware", "Speed up the computer", "Manage files", "Browse the internet"],
        "easy"),
]

# ============================================================
# MODULE 4: PHONE REPAIR - SCREEN & DISPLAY (8 questions)
# ============================================================

phone_repair_screen = [
    create_question("Phone Repair - Screen", "drag_sort", "",
        "Arrange steps to replace a cracked phone screen (first to last)",
        "Power off phone,Remove SIM tray,Heat screen edges,Remove broken screen,Clean frame,Apply adhesive,Connect new screen,Test display,Seal phone",
        ["Remove broken screen", "Power off phone", "Seal phone", "Heat screen edges", "Test display", "Connect new screen", "Remove SIM tray", "Clean frame", "Apply adhesive"],
        "hard"),
    
    create_question("Phone Repair - Screen", "drag_label", "",
        "What tool is used to heat the screen edges to loosen adhesive?",
        "Heat gun or heat pad",
        ["Heat gun or heat pad", "Screwdriver", "Hammer", "Pliers"],
        "easy"),
    
    create_question("Phone Repair - Screen", "drag_label", "",
        "What type of screen do most modern smartphones use?",
        "OLED or AMOLED",
        ["OLED or AMOLED", "LCD only", "CRT", "Plasma"],
        "medium"),
    
    create_question("Phone Repair - Screen", "drag_label", "",
        "What causes screen burn-in on OLED displays?",
        "Static images displayed too long",
        ["Static images displayed too long", "Water damage", "Dropping the phone", "Using wrong charger"],
        "medium"),
    
    create_question("Phone Repair - Screen", "drag_label", "",
        "What is a digitizer in a phone screen?",
        "The touch-sensitive layer",
        ["The touch-sensitive layer", "The display panel", "The glass protector", "The backlight"],
        "hard"),
    
    create_question("Phone Repair - Screen", "drag_sort", "",
        "Steps to diagnose a black screen issue",
        "Force restart phone,Check battery,Connect to charger,Test in dark room,Connect to computer,Check for physical damage,Replace screen",
        ["Force restart phone", "Check battery", "Connect to charger", "Test in dark room", "Connect to computer", "Check for physical damage", "Replace screen"],
        "medium"),
    
    create_question("Phone Repair - Screen", "drag_label", "",
        "What does a phone with dead pixels look like?",
        "Small dots that don't change color",
        ["Small dots that don't change color", "Lines across screen", "Completely black screen", "Flickering display"],
        "easy"),
    
    create_question("Phone Repair - Screen", "drag_label", "",
        "What is the most common cause of screen flickering?",
        "Loose display cable connection",
        ["Loose display cable connection", "Dead battery", "Software virus", "Water damage"],
        "medium"),
]

# ============================================================
# MODULE 5: PHONE REPAIR - BATTERY & CHARGING (8 questions)
# ============================================================

phone_repair_battery = [
    create_question("Phone Repair - Battery", "drag_sort", "",
        "Steps to safely replace a phone battery",
        "Power off phone,Remove back cover,Disconnect old battery,Remove adhesive,Remove old battery,Install new battery,Connect new battery,Apply new adhesive,Close phone,Test charging",
        ["Install new battery", "Power off phone", "Test charging", "Open back cover", "Connect new battery", "Disconnect old battery", "Close back cover", "Remove old battery", "Apply new adhesive", "Remove adhesive"],
        "hard"),
    
    create_question("Phone Repair - Battery", "drag_label", "",
        "What should you do if you notice a swollen battery?",
        "Stop using and replace immediately",
        ["Stop using and replace immediately", "Continue using normally", "Puncture to release gas", "Put in freezer"],
        "easy"),
    
    create_question("Phone Repair - Battery", "drag_label", "",
        "How long do lithium-ion phone batteries typically last?",
        "2-3 years or 300-500 charge cycles",
        ["2-3 years or 300-500 cycles", "6 months", "5-7 years", "10+ years"],
        "easy"),
    
    create_question("Phone Repair - Battery", "drag_label", "",
        "What is the safest way to clean a charging port?",
        "Compressed air or non-conductive tool",
        ["Compressed air or toothpick", "Metal paperclip", "Blow hard into it", "Rinse with water"],
        "easy"),
    
    create_question("Phone Repair - Battery", "drag_label", "",
        "What does fast charging technology require?",
        "Compatible charger and phone hardware",
        ["Compatible charger and phone", "Any USB cable", "Wireless charging pad", "Special software"],
        "medium"),
    
    create_question("Phone Repair - Battery", "drag_label", "",
        "Why does phone battery drain faster in cold weather?",
        "Chemical reactions slow down",
        ["Chemical reactions slow down", "Screen gets brighter", "Processor works harder", "Network signal weakens"],
        "medium"),
    
    create_question("Phone Repair - Battery", "drag_sort", "",
        "Troubleshooting steps for phone not charging",
        "Check charging cable,Inspect charging port,Try different charger,Restart phone,Check battery health,Clean charging port,Replace charging port",
        ["Check charging cable", "Try different charger", "Clean charging port", "Restart phone", "Check battery health", "Replace charging port", "Inspect charging port"],
        "medium"),
    
    create_question("Phone Repair - Battery", "drag_label", "",
        "What is wireless charging?",
        "Charging using electromagnetic induction",
        ["Charging using electromagnetic induction", "Charging without electricity", "Solar-powered charging", "Charging through USB cable"],
        "easy"),
]

# ============================================================
# MODULE 6: PHONE REPAIR - WATER DAMAGE & REPAIR (8 questions)
# ============================================================

phone_repair_water = [
    create_question("Phone Repair - Water Damage", "drag_sort", "",
        "Steps to handle a water-damaged phone",
        "Remove from water immediately,Power off phone,Remove SIM and SD card,Dry exterior,Place in silica gel,Wait 48 hours,Do not charge,Test functions,Take to professional",
        ["Power on to test", "Place in silica gel", "Dry exterior", "Remove SIM and SD card", "Test functions", "Power off immediately", "Wait 48 hours", "Remove from water", "Do not charge"],
        "hard"),
    
    create_question("Phone Repair - Water Damage", "drag_label", "",
        "What should you NEVER do with a wet phone?",
        "Turn it on or charge it",
        ["Turn it on or charge it", "Remove the case", "Dry it with towel", "Remove SIM card"],
        "easy"),
    
    create_question("Phone Repair - Water Damage", "drag_label", "",
        "What household item can help absorb moisture from a wet phone?",
        "Uncooked rice or silica gel",
        ["Uncooked rice or silica gel", "Salt", "Sugar", "Baking soda"],
        "easy"),
    
    create_question("Phone Repair - Water Damage", "drag_label", "",
        "What do Liquid Damage Indicators (LDIs) look like when activated?",
        "They turn red or pink",
        ["They turn red or pink", "They turn blue", "They turn white", "They disappear"],
        "medium"),
    
    create_question("Phone Repair - Water Damage", "drag_label", "",
        "Are phones with IP68 rating completely waterproof?",
        "No, they are water-resistant, not waterproof",
        ["No, they are water-resistant", "Yes, completely waterproof", "Only for fresh water", "Only for 1 minute"],
        "medium"),
    
    create_question("Phone Repair - Water Damage", "drag_label", "",
        "What does IP68 rating mean?",
        "Protected against dust and immersion in water",
        ["Protected against dust and immersion", "Waterproof only", "Shockproof only", "No protection"],
        "hard"),
    
    create_question("Phone Repair - Water Damage", "drag_label", "",
        "What is the first thing to do when a phone falls in water?",
        "Power it off immediately",
        ["Power it off immediately", "Try to turn it on", "Plug it in to charge", "Shake it vigorously"],
        "easy"),
    
    create_question("Phone Repair - Water Damage", "drag_label", "",
        "What tool is used to open water-damaged phones?",
        "Precision screwdrivers and spudgers",
        ["Precision screwdrivers and spudgers", "Regular screwdriver", "Knife", "Hammer"],
        "easy"),
]

# ============================================================
# MODULE 7: GSM & NETWORK KNOWLEDGE (6 questions)
# ============================================================

gsm_knowledge = [
    create_question("GSM Knowledge", "drag_label", "",
        "What does GSM stand for?",
        "Global System for Mobile Communications",
        ["Global System for Mobile Communications", "General Service for Mobile", "Global Signal Management", "General Subscriber Module"],
        "easy"),
    
    create_question("GSM Knowledge", "drag_label", "",
        "What information is stored on a SIM card?",
        "Subscriber identity and network authentication",
        ["Subscriber identity and network data", "All photos and videos", "The operating system", "Contact list only"],
        "easy"),
    
    create_question("GSM Knowledge", "drag_label", "",
        "What does IMEI stand for?",
        "International Mobile Equipment Identity",
        ["International Mobile Equipment Identity", "Internal Mobile Exchange ID", "International Mobile Email ID", "Internal Memory Equipment ID"],
        "medium"),
    
    create_question("GSM Knowledge", "drag_label", "",
        "How can you find your phone's IMEI number?",
        "Dial *#06# on keypad",
        ["Dial *#06#", "Check Settings > About", "Look under battery", "All of the above"],
        "easy"),
    
    create_question("GSM Knowledge", "drag_label", "",
        "What is a carrier lock?",
        "Phone only works with one network provider",
        ["Phone only works with one provider", "Phone is stolen", "Battery is locked", "Screen is locked"],
        "easy"),
    
    create_question("GSM Knowledge", "drag_label", "",
        "What frequency band does 4G LTE typically use?",
        "700MHz to 2600MHz",
        ["700MHz to 2600MHz", "900MHz only", "1800MHz only", "5GHz only"],
        "hard"),
]

# ============================================================
# MODULE 8: TOOLS & SAFETY (5 questions)
# ============================================================

tools_safety = [
    create_question("Tools & Safety", "drag_label", "",
        "What tool is best for opening a phone without damaging it?",
        "Plastic pry tool or spudger",
        ["Plastic pry tool or spudger", "Metal screwdriver", "Knife", "Scissors"],
        "easy"),
    
    create_question("Tools & Safety", "drag_label", "",
        "What is ESD and why is it important?",
        "Electrostatic Discharge - can damage components",
        ["Electrostatic Discharge - damages components", "Electronic System - tests phones", "External Storage - backs up data", "Emergency Shutdown - turns off phone"],
        "medium"),
    
    create_question("Tools & Safety", "drag_label", "",
        "What should you use to prevent ESD damage?",
        "Anti-static wrist strap and mat",
        ["Anti-static wrist strap and mat", "Rubber gloves", "Metal tools", "Paper towel"],
        "easy"),
    
    create_question("Tools & Safety", "drag_label", "",
        "What size screws are commonly found in iPhones?",
        "Pentalobe screws",
        ["Pentalobe screws", "Phillips screws", "Flat head screws", "Hex screws"],
        "hard"),
    
    create_question("Tools & Safety", "drag_label", "",
        "What is a spudger used for?",
        "Prying and disconnecting cables",
        ["Prying and disconnecting cables", "Tightening screws", "Cleaning screens", "Testing batteries"],
        "easy"),
]

# ============================================================
# COMBINE ALL MODULES
# ============================================================

all_questions = (
    computer_hardware +      # 15 questions
    computer_ports +         # 10 questions
    software_questions +     # 10 questions
    phone_repair_screen +    # 8 questions
    phone_repair_battery +   # 8 questions
    phone_repair_water +     # 8 questions
    gsm_knowledge +          # 6 questions
    tools_safety             # 5 questions
)

print("=" * 60)
print("QUESTION BANK SUMMARY")
print("=" * 60)
print(f"Total questions: {len(all_questions)}")
print()
print("By Module:")
print(f"  📁 Computer Hardware:      {len(computer_hardware)} questions")
print(f"  🔌 Computer Ports:          {len(computer_ports)} questions")
print(f"  💻 Software & OS:           {len(software_questions)} questions")
print(f"  📱 Phone Repair - Screen:   {len(phone_repair_screen)} questions")
print(f"  🔋 Phone Repair - Battery:  {len(phone_repair_battery)} questions")
print(f"  💧 Phone Repair - Water:    {len(phone_repair_water)} questions")
print(f"  📡 GSM Knowledge:           {len(gsm_knowledge)} questions")
print(f"  🔧 Tools & Safety:          {len(tools_safety)} questions")
print()
print("By Type:")
drag_label = sum(1 for q in all_questions if q['q_type'] == 'drag_label')
drag_sort = sum(1 for q in all_questions if q['q_type'] == 'drag_sort')
print(f"  🏷️  Drag & Label:  {drag_label}")
print(f"  🔄 Drag & Sort:    {drag_sort}")
print("=" * 60)

# Seed the database
with app.app_context():
    db.create_all()
    Question.query.delete()
    for q in all_questions:
        db.session.add(Question(**q))
    db.session.commit()
    print(f"\n✅ Successfully seeded {len(all_questions)} questions to database!")