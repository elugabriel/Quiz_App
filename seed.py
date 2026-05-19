from app import app, db
from models import Question
import json

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
# MODULE 1: COMPUTER HARDWARE (20 questions with images)
# ============================================================

computer_hardware = [
    # CPU & Processor
    create_question("Computer Hardware", "drag_label", "images/cpu.png",
        "What is the 'brain' of the computer that processes all instructions?",
        "CPU (Central Processing Unit)",
        ["CPU", "RAM", "GPU", "Motherboard"],
        "easy"),
    
    create_question("Computer Hardware", "drag_label", "images/cpu_intel.png",
        "Which company manufactures the Intel Core series processors?",
        "Intel",
        ["Intel", "AMD", "NVIDIA", "Apple"],
        "easy"),
    
    create_question("Computer Hardware", "drag_label", "images/cpu_amd.png",
        "Which company manufactures Ryzen processors?",
        "AMD",
        ["AMD", "Intel", "Qualcomm", "Samsung"],
        "easy"),
    
    # RAM
    create_question("Computer Hardware", "drag_label", "images/ram_ddr4.png",
        "What does RAM stand for?",
        "Random Access Memory",
        ["Random Access Memory", "Read Only Memory", "Rapid Access Module", "Random Allocation Memory"],
        "easy"),
    
    create_question("Computer Hardware", "drag_label", "images/ram_ddr5.png",
        "Which is the latest generation of DDR RAM as of 2024?",
        "DDR5",
        ["DDR5", "DDR4", "DDR3", "DDR6"],
        "medium"),
    
    create_question("Computer Hardware", "drag_label", "images/ram_laptop.png",
        "What type of RAM is commonly used in laptops due to its smaller size?",
        "SODIMM",
        ["SODIMM", "DIMM", "DDR5", "RAM Stick"],
        "medium"),
    
    # Storage - HDD/SSD
    create_question("Computer Hardware", "drag_label", "images/hdd_internal.png",
        "Which storage device uses spinning magnetic platters to read/write data?",
        "Hard Disk Drive (HDD)",
        ["HDD", "SSD", "NVMe", "USB Drive"],
        "easy"),
    
    create_question("Computer Hardware", "drag_label", "images/ssd_sata.png",
        "Which storage device has no moving parts and is faster than traditional drives?",
        "Solid State Drive (SSD)",
        ["SSD", "HDD", "External Drive", "Flash Drive"],
        "easy"),
    
    create_question("Computer Hardware", "drag_label", "images/nvme_ssd.png",
        "Which ultra-fast SSD connects directly to the motherboard via PCIe?",
        "NVMe SSD",
        ["NVMe SSD", "SATA SSD", "M.2 SATA", "External SSD"],
        "medium"),
    
    create_question("Computer Hardware", "drag_label", "images/external_hdd.png",
        "What type of drive is used for portable backup storage?",
        "External Hard Drive",
        ["External Hard Drive", "Internal HDD", "NAS Drive", "Cloud Storage"],
        "easy"),
    
    # GPU/Graphics Cards
    create_question("Computer Hardware", "drag_label", "images/gpu_nvidia.png",
        "Which company manufactures GeForce RTX graphics cards?",
        "NVIDIA",
        ["NVIDIA", "AMD", "Intel", "MSI"],
        "easy"),
    
    create_question("Computer Hardware", "drag_label", "images/gpu_amd.png",
        "Which company manufactures Radeon graphics cards?",
        "AMD",
        ["AMD", "NVIDIA", "Intel", "EVGA"],
        "easy"),
    
    create_question("Computer Hardware", "drag_label", "images/gpu_back.png",
        "What does GPU stand for?",
        "Graphics Processing Unit",
        ["Graphics Processing Unit", "General Processing Unit", "Graphical Program Utility", "Graphics Power Unit"],
        "easy"),
    
    # Motherboard
    create_question("Computer Hardware", "drag_label", "images/motherboard_atx.png",
        "What is the most common motherboard size for desktop computers?",
        "ATX",
        ["ATX", "Micro-ATX", "Mini-ITX", "E-ATX"],
        "medium"),
    
    create_question("Computer Hardware", "drag_label", "images/motherboard_ports.png",
        "What connects all computer components together?",
        "Motherboard",
        ["Motherboard", "CPU", "RAM", "PSU"],
        "easy"),
    
    # Power Supply
    create_question("Computer Hardware", "drag_label", "images/psu_modular.png",
        "What component converts AC power to DC power for computer components?",
        "Power Supply Unit (PSU)",
        ["PSU", "CPU", "Motherboard", "Battery"],
        "easy"),
    
    create_question("Computer Hardware", "drag_label", "images/psu_cables.png",
        "What type of PSU allows you to attach only the cables you need?",
        "Modular PSU",
        ["Modular PSU", "Non-modular PSU", "Semi-modular PSU", "Fixed PSU"],
        "medium"),
    
    # Cooling
    create_question("Computer Hardware", "drag_label", "images/cpu_cooler_air.png",
        "What component prevents the CPU from overheating?",
        "CPU Cooler",
        ["CPU Cooler", "Case Fan", "GPU Fan", "Heat Sink"],
        "easy"),
    
    create_question("Computer Hardware", "drag_label", "images/cpu_cooler_liquid.png",
        "What type of cooling uses liquid to transfer heat away from components?",
        "Liquid Cooling",
        ["Liquid Cooling", "Air Cooling", "Passive Cooling", "Thermal Cooling"],
        "medium"),
    
    create_question("Computer Hardware", "drag_label", "images/case_fan.png",
        "What component helps circulate air inside the computer case?",
        "Case Fan",
        ["Case Fan", "CPU Fan", "GPU Fan", "PSU Fan"],
        "easy"),
    
    # Peripherals
    create_question("Computer Hardware", "drag_label", "images/mechanical_keyboard.png",
        "Which type of keyboard uses individual switches under each key?",
        "Mechanical Keyboard",
        ["Mechanical Keyboard", "Membrane Keyboard", "Wireless Keyboard", "Ergonomic Keyboard"],
        "easy"),
    
    create_question("Computer Hardware", "drag_label", "images/gaming_mouse.png",
        "Which peripheral is used to control the cursor on screen?",
        "Mouse",
        ["Mouse", "Keyboard", "Trackpad", "Joystick"],
        "easy"),
    
    create_question("Computer Hardware", "drag_label", "images/monitor_curved.png",
        "What output device displays visual information from the computer?",
        "Monitor",
        ["Monitor", "Printer", "Projector", "TV"],
        "easy"),
]

# ============================================================
# MODULE 2: COMPUTER PORTS & CABLES (10 questions with images)
# ============================================================

computer_ports = [
    create_question("Computer Ports", "drag_label", "images/usb_type_a.png",
        "Which rectangular USB connector is most common on computers?",
        "USB Type-A",
        ["USB Type-A", "USB Type-C", "USB Type-B", "Micro USB"],
        "easy"),
    
    create_question("Computer Ports", "drag_label", "images/usb_type_c.png",
        "Which reversible USB connector is becoming standard on modern devices?",
        "USB Type-C",
        ["USB Type-C", "USB Type-A", "Lightning", "Micro USB"],
        "easy"),
    
    create_question("Computer Ports", "drag_label", "images/hdmi_port.png",
        "Which port transmits high-definition video and audio to monitors/TVs?",
        "HDMI Port",
        ["HDMI Port", "DisplayPort", "VGA Port", "DVI Port"],
        "easy"),
    
    create_question("Computer Ports", "drag_label", "images/displayport.png",
        "Which port is commonly used for high refresh rate gaming monitors?",
        "DisplayPort",
        ["DisplayPort", "HDMI", "VGA", "DVI"],
        "medium"),
    
    create_question("Computer Ports", "drag_label", "images/ethernet_port.png",
        "Which port connects your computer to a wired network?",
        "Ethernet Port (RJ45)",
        ["Ethernet Port", "USB Port", "Phone Jack", "HDMI Port"],
        "easy"),
    
    create_question("Computer Ports", "drag_label", "images/audio_jacks.png",
        "Which color-coded port is used for speakers/headphones (usually green)?",
        "Audio Output",
        ["Audio Output", "Microphone Input", "Line In", "SPDIF"],
        "easy"),
    
    create_question("Computer Ports", "drag_label", "images/vga_port.png",
        "Which older blue 15-pin port was used for monitors?",
        "VGA Port",
        ["VGA Port", "DVI Port", "HDMI Port", "DisplayPort"],
        "easy"),
    
    create_question("Computer Ports", "drag_label", "images/dvi_port.png",
        "Which digital video port has a distinctive cross-shaped pin layout?",
        "DVI Port",
        ["DVI Port", "VGA Port", "HDMI Port", "DisplayPort"],
        "medium"),
    
    create_question("Computer Ports", "drag_label", "images/thunderbolt.png",
        "Which high-speed port combines PCIe and DisplayPort into one connector?",
        "Thunderbolt",
        ["Thunderbolt", "USB-C", "HDMI", "DisplayPort"],
        "hard"),
    
    create_question("Computer Ports", "drag_label", "images/sd_card_reader.png",
        "What port is used to read memory cards from cameras?",
        "SD Card Reader",
        ["SD Card Reader", "USB Port", "Card Slot", "Memory Reader"],
        "easy"),
]

# ============================================================
# MODULE 3: PHONE REPAIR - SCREEN & DISPLAY (10 questions with images)
# ============================================================

phone_repair_screen = [
    create_question("Phone Repair", "drag_sort", "images/cracked_screen.jpg",
        "Arrange steps to replace a cracked phone screen (first to last)",
        "Power off phone,Remove SIM tray,Heat screen edges,Use suction cup,Insert pry tool,Remove broken screen,Clean frame,Apply adhesive,Connect new screen,Test display,Press to seal",
        ["Remove broken screen", "Power off phone", "Heat screen edges", "Test display", "Connect new screen", "Remove SIM tray", "Clean frame", "Apply adhesive", "Use suction cup", "Insert pry tool", "Press to seal"],
        "hard"),
    
    create_question("Phone Repair", "drag_label", "images/screen_repair_tools.jpg",
        "What tool is used to heat the screen edges to loosen adhesive?",
        "Heat gun or heat pad",
        ["Heat gun or heat pad", "Screwdriver", "Hammer", "Pliers"],
        "easy"),
    
    create_question("Phone Repair", "drag_label", "images/suction_cup.jpg",
        "What tool helps lift the screen after heating?",
        "Suction cup",
        ["Suction cup", "Screwdriver", "Spudger", "Tweezers"],
        "easy"),
    
    create_question("Phone Repair", "drag_label", "images/oled_vs_lcd.jpg",
        "Which screen technology offers deeper blacks and better contrast?",
        "OLED",
        ["OLED", "LCD", "TFT", "IPS"],
        "medium"),
    
    create_question("Phone Repair", "drag_label", "images/screen_burn_in.jpg",
        "What causes screen burn-in on OLED displays?",
        "Static images displayed too long",
        ["Static images displayed too long", "Water damage", "Dropping the phone", "Using wrong charger"],
        "medium"),
    
    create_question("Phone Repair", "drag_label", "images/digitizer.jpg",
        "What is a digitizer in a phone screen?",
        "The touch-sensitive layer",
        ["The touch-sensitive layer", "The display panel", "The glass protector", "The backlight"],
        "hard"),
    
    create_question("Phone Repair", "drag_sort", "images/black_screen.jpg",
        "Steps to diagnose a black screen issue",
        "Force restart phone,Check battery level,Connect to charger,Test in dark room,Connect to computer,Check for physical damage,Professional diagnosis",
        ["Force restart phone", "Check battery level", "Connect to charger", "Test in dark room", "Connect to computer", "Check for physical damage", "Professional diagnosis"],
        "medium"),
    
    create_question("Phone Repair", "drag_label", "images/dead_pixels.jpg",
        "What does a phone with dead pixels look like?",
        "Small dots that don't change color",
        ["Small dots that don't change color", "Lines across screen", "Completely black screen", "Flickering display"],
        "easy"),
    
    create_question("Phone Repair", "drag_label", "images/screen_flicker.jpg",
        "What is the most common cause of screen flickering?",
        "Loose display cable connection",
        ["Loose display cable connection", "Dead battery", "Software virus", "Water damage"],
        "medium"),
    
    create_question("Phone Repair", "drag_label", "images/tempered_glass.jpg",
        "What accessory helps prevent screen cracks from drops?",
        "Tempered glass screen protector",
        ["Tempered glass screen protector", "Phone case", "Pop socket", "Charging cable"],
        "easy"),
]

# ============================================================
# MODULE 4: PHONE REPAIR - BATTERY & CHARGING (10 questions with images)
# ============================================================

phone_repair_battery = [
    create_question("Phone Repair", "drag_sort", "images/battery_replacement.jpg",
        "Steps to safely replace a phone battery",
        "Power off phone,Open phone,Disconnect old battery,Remove pull tabs/Remove adhesive,Lift out old battery,Place new battery,Connect new battery,Apply new adhesive,Close phone,Test charging",
        ["Install new battery", "Power off phone", "Test charging", "Open phone", "Connect new battery", "Disconnect old battery", "Close phone", "Remove old battery", "Remove pull tabs", "Apply new adhesive"],
        "hard"),
    
    create_question("Phone Repair", "drag_label", "images/swollen_battery.jpg",
        "What should you do if you notice a swollen battery?",
        "Stop using and replace immediately",
        ["Stop using and replace immediately", "Continue using normally", "Puncture to release gas", "Put in freezer"],
        "easy"),
    
    create_question("Phone Repair", "drag_label", "images/li_ion_battery.jpg",
        "How long do lithium-ion phone batteries typically last?",
        "2-3 years or 300-500 charge cycles",
        ["2-3 years or 300-500 cycles", "6 months", "5-7 years", "10+ years"],
        "easy"),
    
    create_question("Phone Repair", "drag_label", "images/charging_port.jpg",
        "What is the safest way to clean a charging port?",
        "Compressed air or non-conductive tool",
        ["Compressed air or toothpick", "Metal paperclip", "Blow hard into it", "Rinse with water"],
        "easy"),
    
    create_question("Phone Repair", "drag_label", "images/fast_charger.jpg",
        "What does fast charging technology require?",
        "Compatible charger and phone hardware",
        ["Compatible charger and phone", "Any USB cable", "Wireless charging pad", "Special software"],
        "medium"),
    
    create_question("Phone Repair", "drag_label", "images/wireless_charging.jpg",
        "What is wireless charging?",
        "Charging using electromagnetic induction",
        ["Charging using electromagnetic induction", "Charging without electricity", "Solar-powered charging", "Charging through USB cable"],
        "easy"),
    
    create_question("Phone Repair", "drag_sort", "images/phone_not_charging.jpg",
        "Troubleshooting steps for phone not charging",
        "Check charging cable,Inspect charging port,Try different charger,Restart phone,Check battery health,Clean charging port,Replace charging port",
        ["Check charging cable", "Try different charger", "Clean charging port", "Restart phone", "Check battery health", "Replace charging port", "Inspect charging port"],
        "medium"),
    
    create_question("Phone Repair", "drag_label", "images/battery_drain.jpg",
        "What can cause rapid battery drain?",
        "Background apps and high screen brightness",
        ["Background apps and high brightness", "Dark mode", "Low signal strength", "All of the above"],
        "easy"),
    
    create_question("Phone Repair", "drag_label", "images/pull_tabs.jpg",
        "What are the adhesive strips called that hold iPhone batteries?",
        "Pull tabs",
        ["Pull tabs", "Sticky strips", "Battery tape", "Adhesive pads"],
        "medium"),
    
    create_question("Phone Repair", "drag_label", "images/battery_health.jpg",
        "Where can you check battery health on iPhones?",
        "Settings > Battery > Battery Health",
        ["Settings > Battery > Battery Health", "Settings > General > About", "Settings > Display", "Settings > Privacy"],
        "easy"),
]

# ============================================================
# MODULE 5: PHONE REPAIR - WATER DAMAGE (8 questions with images)
# ============================================================

phone_repair_water = [
    create_question("Phone Repair", "drag_sort", "images/water_damage.jpg",
        "Steps to handle a water-damaged phone",
        "Remove from water immediately,Power off phone,Remove SIM and SD card,Dry exterior,Place in silica gel,Wait 48 hours,Do not charge,Test functions",
        ["Power on to test", "Place in silica gel", "Dry exterior", "Remove SIM and SD card", "Test functions", "Power off immediately", "Wait 48 hours", "Remove from water", "Do not charge"],
        "hard"),
    
    create_question("Phone Repair", "drag_label", "images/wet_phone.jpg",
        "What should you NEVER do with a wet phone?",
        "Turn it on or charge it",
        ["Turn it on or charge it", "Remove the case", "Dry it with towel", "Remove SIM card"],
        "easy"),
    
    create_question("Phone Repair", "drag_label", "images/silica_gel.jpg",
        "What household item can help absorb moisture from a wet phone?",
        "Uncooked rice or silica gel",
        ["Uncooked rice or silica gel", "Salt", "Sugar", "Baking soda"],
        "easy"),
    
    create_question("Phone Repair", "drag_label", "images/liquid_damage_indicator.jpg",
        "What do Liquid Damage Indicators (LDIs) look like when activated?",
        "They turn red or pink",
        ["They turn red or pink", "They turn blue", "They turn white", "They disappear"],
        "medium"),
    
    create_question("Phone Repair", "drag_label", "images/ip68_rating.jpg",
        "Are phones with IP68 rating completely waterproof?",
        "No, they are water-resistant, not waterproof",
        ["No, they are water-resistant", "Yes, completely waterproof", "Only for fresh water", "Only for 1 minute"],
        "medium"),
    
    create_question("Phone Repair", "drag_label", "images/water_damage_repair.jpg",
        "What is the first thing to do when a phone falls in water?",
        "Power it off immediately",
        ["Power it off immediately", "Try to turn it on", "Plug it in to charge", "Shake it vigorously"],
        "easy"),
    
    create_question("Phone Repair", "drag_label", "images/corrosion.jpg",
        "What damage can water cause to phone components?",
        "Corrosion and short circuits",
        ["Corrosion and short circuits", "Screen cracks", "Battery swelling", "Software issues"],
        "medium"),
    
    create_question("Phone Repair", "drag_label", "images/isopropyl_alcohol.jpg",
        "What solution is used to clean corrosion from circuit boards?",
        "Isopropyl alcohol (90%+)",
        ["Isopropyl alcohol", "Water", "Vinegar", "Soap solution"],
        "hard"),
]

# ============================================================
# MODULE 6: PHONE REPAIR - TOOLS & REPAIR (9 questions with images)
# ============================================================

phone_repair_tools = [
    create_question("Phone Repair", "drag_label", "images/repair_tool_kit.png",
        "What tool set is essential for phone repair?",
        "Precision screwdriver set",
        ["Precision screwdriver set", "Regular screwdriver", "Hammer", "Wrench"],
        "easy"),
    
    create_question("Phone Repair", "drag_label", "images/spudger.png",
        "What tool is best for opening a phone without damaging it?",
        "Plastic spudger or pry tool",
        ["Plastic spudger or pry tool", "Metal screwdriver", "Knife", "Scissors"],
        "easy"),
    
    create_question("Phone Repair", "drag_label", "images/esd_strap.png",
        "What is ESD and why is it important?",
        "Electrostatic Discharge - can damage components",
        ["Electrostatic Discharge - damages components", "Electronic System - tests phones", "External Storage - backs up data", "Emergency Shutdown - turns off phone"],
        "medium"),
    
    create_question("Phone Repair", "drag_label", "images/anti_static_mat.png",
        "What should you use to prevent ESD damage?",
        "Anti-static wrist strap and mat",
        ["Anti-static wrist strap and mat", "Rubber gloves", "Metal tools", "Paper towel"],
        "easy"),
    
    create_question("Phone Repair", "drag_label", "images/pentalobe_screwdriver.png",
        "What size screws are commonly found in iPhones?",
        "Pentalobe screws",
        ["Pentalobe screws", "Phillips screws", "Flat head screws", "Hex screws"],
        "hard"),
    
    create_question("Phone Repair", "drag_label", "images/magnifying_lamp.png",
        "What tool helps see small components clearly?",
        "Magnifying lamp or microscope",
        ["Magnifying lamp", "Regular lamp", "Flashlight", "Reading glasses"],
        "easy"),
    
    create_question("Phone Repair", "drag_label", "images/soldering_iron.png",
        "What tool is used to repair broken solder connections?",
        "Soldering iron",
        ["Soldering iron", "Glue gun", "Tape", "Screwdriver"],
        "medium"),
    
    create_question("Phone Repair", "drag_label", "images/tweezers.png",
        "What tool helps handle small screws and components?",
        "Precision tweezers",
        ["Precision tweezers", "Fingers", "Pliers", "Scissors"],
        "easy"),
    
    create_question("Phone Repair", "drag_sort", "images/phone_opening.png",
        "Steps to safely open a phone",
        "Power off phone,Remove SIM tray,Heat edges,Apply suction cup,Insert pry tool,Slide around edges,Lift carefully",
        ["Apply suction cup", "Power off phone", "Heat edges", "Lift carefully", "Insert pry tool", "Slide around edges", "Remove SIM tray"],
        "medium"),
]

# ============================================================
# MODULE 7: GSM & MOBILE NETWORKS (5 questions)
# ============================================================

gsm_knowledge = [
    create_question("GSM Knowledge", "drag_label", "images/gsm_network.png",
        "What does GSM stand for?",
        "Global System for Mobile Communications",
        ["Global System for Mobile Communications", "General Service for Mobile", "Global Signal Management", "General Subscriber Module"],
        "easy"),
    
    create_question("GSM Knowledge", "drag_label", "images/sim_card.png",
        "What information is stored on a SIM card?",
        "Subscriber identity and network authentication",
        ["Subscriber identity and network data", "All photos and videos", "The operating system", "Contact list only"],
        "easy"),
    
    create_question("GSM Knowledge", "drag_label", "images/imei_number.png",
        "What does IMEI stand for?",
        "International Mobile Equipment Identity",
        ["International Mobile Equipment Identity", "Internal Mobile Exchange ID", "International Mobile Email ID", "Internal Memory Equipment ID"],
        "medium"),
    
    create_question("GSM Knowledge", "drag_label", "images/network_bands.png",
        "What frequency band does 4G LTE typically use?",
        "700MHz to 2600MHz",
        ["700MHz to 2600MHz", "900MHz only", "1800MHz only", "5GHz only"],
        "hard"),
    
    create_question("GSM Knowledge", "drag_label", "images/carrier_lock.png",
        "What is a carrier lock?",
        "Phone only works with one network provider",
        ["Phone only works with one provider", "Phone is stolen", "Battery is locked", "Screen is locked"],
        "easy"),
]

# ============================================================
# COMBINE ALL MODULES
# ============================================================

all_questions = (
    computer_hardware +      # 22 questions
    computer_ports +         # 10 questions
    phone_repair_screen +    # 10 questions
    phone_repair_battery +   # 10 questions
    phone_repair_water +     # 8 questions
    phone_repair_tools +     # 9 questions
    gsm_knowledge            # 5 questions
)

print("=" * 60)
print("QUESTION BANK SUMMARY")
print("=" * 60)
print(f"Total questions: {len(all_questions)}")
print()
print("By Module:")
print(f"  🖥️  Computer Hardware:        {len(computer_hardware)} questions")
print(f"  🔌 Computer Ports:            {len(computer_ports)} questions")
print(f"  📱 Phone Repair - Screen:     {len(phone_repair_screen)} questions")
print(f"  🔋 Phone Repair - Battery:    {len(phone_repair_battery)} questions")
print(f"  💧 Phone Repair - Water:      {len(phone_repair_water)} questions")
print(f"  🔧 Phone Repair - Tools:      {len(phone_repair_tools)} questions")
print(f"  📡 GSM Knowledge:             {len(gsm_knowledge)} questions")
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