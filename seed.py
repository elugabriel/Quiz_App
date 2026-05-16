from app import app, db
from models import Question

questions = [

    # ════════════════════════════════════════════════════
    # DRAG-LABEL — Computer Hardware (images without names)
    # ════════════════════════════════════════════════════
    {"topic":"Computer Hardware","q_type":"drag_label","image_path":"images/cpu.png",
     "prompt":"Identify the correct label for the image below","answer":"CPU",
     "options":["CPU","RAM","GPU","PSU"],"difficulty":"easy"},

    {"topic":"Computer Hardware","q_type":"drag_label","image_path":"images/ram.png",
     "prompt":"Identify the correct label for the image below","answer":"RAM",
     "options":["ROM","RAM","HDD","SSD"],"difficulty":"easy"},

    {"topic":"Computer Hardware","q_type":"drag_label","image_path":"images/motherboard.png",
     "prompt":"Identify the correct label for the image below","answer":"Motherboard",
     "options":["CPU","GPU","Motherboard","PSU"],"difficulty":"medium"},

    {"topic":"Computer Hardware","q_type":"drag_label","image_path":"images/gpu.png",
     "prompt":"Identify the correct label for the image below","answer":"GPU",
     "options":["CPU","GPU","RAM","SSD"],"difficulty":"easy"},

    {"topic":"Computer Hardware","q_type":"drag_label","image_path":"images/hdd.png",
     "prompt":"Identify the correct label for the image below","answer":"HDD",
     "options":["SSD","HDD","RAM","ROM"],"difficulty":"easy"},

    {"topic":"Computer Hardware","q_type":"drag_label","image_path":"images/ssd.png",
     "prompt":"Identify the correct label for the image below","answer":"SSD",
     "options":["HDD","SSD","USB","DVD"],"difficulty":"medium"},

    {"topic":"Computer Hardware","q_type":"drag_label","image_path":"images/psu.png",
     "prompt":"Identify the correct label for the image below","answer":"PSU",
     "options":["PSU","CPU","UPS","GPU"],"difficulty":"medium"},

    {"topic":"Computer Hardware","q_type":"drag_label","image_path":"images/monitor.png",
     "prompt":"Identify the correct label for the image below","answer":"Monitor",
     "options":["Printer","Monitor","Projector","Speaker"],"difficulty":"easy"},

    {"topic":"Computer Hardware","q_type":"drag_label","image_path":"images/keyboard.png",
     "prompt":"Identify the correct label for the image below","answer":"Keyboard",
     "options":["Mouse","Keyboard","Scanner","Joystick"],"difficulty":"easy"},

    {"topic":"Computer Hardware","q_type":"drag_label","image_path":"images/mouse.png",
     "prompt":"Identify the correct label for the image below","answer":"Mouse",
     "options":["Keyboard","Mouse","Trackball","Touchpad"],"difficulty":"easy"},

    {"topic":"Computer Hardware","q_type":"drag_label","image_path":"images/printer.png",
     "prompt":"Identify the correct label for the image below","answer":"Printer",
     "options":["Scanner","Printer","Plotter","Fax"],"difficulty":"easy"},

    {"topic":"Computer Hardware","q_type":"drag_label","image_path":"images/speakers.png",
     "prompt":"Identify the correct label for the image below","answer":"Speakers",
     "options":["Headphones","Speakers","Microphone","Earbuds"],"difficulty":"easy"},

    {"topic":"Computer Hardware","q_type":"drag_label","image_path":"images/webcam.png",
     "prompt":"Identify the correct label for the image below","answer":"Webcam",
     "options":["Webcam","Microphone","Phone","Scanner"],"difficulty":"easy"},

    {"topic":"Computer Hardware","q_type":"drag_label","image_path":"images/scanner.png",
     "prompt":"Identify the correct label for the image below","answer":"Scanner",
     "options":["Printer","Scanner","Copier","Fax"],"difficulty":"medium"},

    {"topic":"Computer Hardware","q_type":"drag_label","image_path":"images/usb_drive.png",
     "prompt":"Identify the correct label for the image below","answer":"USB Drive",
     "options":["USB Drive","SD Card","Hard Drive","CD"],"difficulty":"easy"},

    {"topic":"Computer Hardware","q_type":"drag_label","image_path":"images/headphones.png",
     "prompt":"Identify the correct label for the image below","answer":"Headphones",
     "options":["Headphones","Speakers","Microphone","Earbuds"],"difficulty":"easy"},

    {"topic":"Computer Hardware","q_type":"drag_label","image_path":"images/router.png",
     "prompt":"Identify the correct label for the image below","answer":"Router",
     "options":["Router","Switch","Modem","Hub"],"difficulty":"medium"},

    {"topic":"Computer Hardware","q_type":"drag_label","image_path":"images/laptop.png",
     "prompt":"Identify the correct label for the image below","answer":"Laptop",
     "options":["Laptop","Desktop","Tablet","Notebook"],"difficulty":"easy"},

    {"topic":"Computer Hardware","q_type":"drag_label","image_path":"images/tablet.png",
     "prompt":"Identify the correct label for the image below","answer":"Tablet",
     "options":["Tablet","Smartphone","Laptop","iPad"],"difficulty":"easy"},

    {"topic":"Computer Hardware","q_type":"drag_label","image_path":"images/smartphone.png",
     "prompt":"Identify the correct label for the image below","answer":"Smartphone",
     "options":["Smartphone","table phone","PC","Speakers"],"difficulty":"easy"},

    {"topic":"Computer Hardware","q_type":"drag_label","image_path":"images/microphone.png",
     "prompt":"Identify the correct label for the image below","answer":"Microphone",
     "options":["Microphone","Speakers","Headphones","Webcam"],"difficulty":"easy"},

    {"topic":"Computer Hardware","q_type":"drag_label","image_path":"images/projector.png",
     "prompt":"Identify the correct label for the image below","answer":"Projector",
     "options":["Projector","Monitor","TV","Screen"],"difficulty":"medium"},

    # ════════════════════════════════════════════════════
    # DRAG-LABEL — Computer Ports (images without names)
    # ════════════════════════════════════════════════════
    {"topic":"Computer Ports","q_type":"drag_label","image_path":"images/usb_port.png",
     "prompt":"Identify the correct label for the image below","answer":"USB Port",
     "options":["USB Port","HDMI Port","Ethernet Port","Audio Jack"],"difficulty":"easy"},

    {"topic":"Computer Ports","q_type":"drag_label","image_path":"images/hdmi_port.png",
     "prompt":"Identify the correct label for the image below","answer":"HDMI Port",
     "options":["HDMI Port","USB Port","VGA Port","DisplayPort"],"difficulty":"medium"},

    {"topic":"Computer Ports","q_type":"drag_label","image_path":"images/ethernet_port.png",
     "prompt":"Identify the correct label for the image below","answer":"Ethernet Port",
     "options":["Ethernet Port","USB Port","Phone Jack","Modem Port"],"difficulty":"medium"},

    {"topic":"Computer Ports","q_type":"drag_label","image_path":"images/audio_jack.png",
     "prompt":"Identify the correct label for the image below","answer":"Audio Jack",
     "options":["Audio Jack","USB Port","HDMI Port","Power Port"],"difficulty":"easy"},

    {"topic":"Computer Ports","q_type":"drag_label","image_path":"images/power_port.png",
     "prompt":"Identify the correct label for the image below","answer":"Power Port",
     "options":["Power Port","USB Port","Charging Port","AC Port"],"difficulty":"easy"},

    # ════════════════════════════════════════════════════
    # DRAG-LABEL — Software Icons (images without names)
    # ════════════════════════════════════════════════════
    {"topic":"Software","q_type":"drag_label","image_path":"images/chrome_icon.png",
     "prompt":"Identify the correct label for the image below","answer":"Chrome",
     "options":["Chrome","Firefox","Safari","Edge"],"difficulty":"easy"},

    {"topic":"Software","q_type":"drag_label","image_path":"images/word_icon.png",
     "prompt":"Identify the correct label for the image below","answer":"Microsoft Word",
     "options":["Microsoft Word","Google Docs","Pages","WordPad"],"difficulty":"easy"},

    {"topic":"Software","q_type":"drag_label","image_path":"images/excel_icon.png",
     "prompt":"Identify the correct label for the image below","answer":"Microsoft Excel",
     "options":["Microsoft Excel","Google Sheets","Numbers","Calc"],"difficulty":"easy"},

    {"topic":"Software","q_type":"drag_label","image_path":"images/powerpoint_icon.png",
     "prompt":"Identify the correct label for the image below","answer":"PowerPoint",
     "options":["PowerPoint","Google Slides","Keynote","Prezi"],"difficulty":"easy"},

    {"topic":"Software","q_type":"drag_label","image_path":"images/recycle_bin.png",
     "prompt":"Identify the correct label for the image below","answer":"Recycle Bin",
     "options":["Recycle Bin","Trash","Deleted Items","Bin"],"difficulty":"easy"},

    {"topic":"Software","q_type":"drag_label","image_path":"images/folder_icon.png",
     "prompt":"Identify the correct label for the image below","answer":"Folder",
     "options":["Folder","Directory","File","Cabinet"],"difficulty":"easy"},

    # ════════════════════════════════════════════════════
    # DRAG-SORT — Phone Repair Activities
    # ════════════════════════════════════════════════════

    {"topic":"Phone Repair","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to replace a cracked phone screen (top = first)",
     "answer":"Power off phone,Remove SIM tray,Heat screen edges,Remove broken screen,Connect new screen,Test display,Seal phone",
     "options":["Remove broken screen","Power off phone","Seal phone","Heat screen edges","Test display","Connect new screen","Remove SIM tray"],
     "difficulty":"hard"},

    {"topic":"Phone Repair","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to replace a phone battery (top = first)",
     "answer":"Power off phone,Open back cover,Disconnect old battery,Remove old battery,Insert new battery,Connect new battery,Close back cover,Power on",
     "options":["Insert new battery","Power off phone","Power on","Open back cover","Connect new battery","Disconnect old battery","Close back cover","Remove old battery"],
     "difficulty":"hard"},

    {"topic":"Phone Repair","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to troubleshoot a phone that won't charge (top = first)",
     "answer":"Check charging cable,Try different cable,Clean charging port,Try different charger,Restart phone,Check battery health,Replace charging port",
     "options":["Try different charger","Restart phone","Check charging cable","Replace charging port","Try different cable","Check battery health","Clean charging port"],
     "difficulty":"medium"},

    {"topic":"Phone Repair","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to replace a phone charging port (top = first)",
     "answer":"Power off phone,Open phone case,Locate charging port,Unsolder old port,Solder new port,Test charging,Close case",
     "options":["Solder new port","Open phone case","Test charging","Power off phone","Close case","Locate charging port","Unsolder old port"],
     "difficulty":"hard"},

    {"topic":"Phone Repair","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to handle a water-damaged phone (top = first)",
     "answer":"Power off immediately,Remove SIM and SD card,Dry exterior,Place in silica gel,Wait 48 hours,Power on,Test functions",
     "options":["Power on","Place in silica gel","Dry exterior","Remove SIM and SD card","Test functions","Power off immediately","Wait 48 hours"],
     "difficulty":"medium"},

    {"topic":"Phone Repair","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to factory reset a phone (top = first)",
     "answer":"Backup data,Open Settings,Go to General Management,Select Reset,Select Factory Reset,Confirm reset,Wait for restart",
     "options":["Select Factory Reset","Open Settings","Wait for restart","Backup data","Confirm reset","Go to General Management","Select Reset"],
     "difficulty":"medium"},

    {"topic":"Phone Repair","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to replace a broken phone camera lens (top = first)",
     "answer":"Power off phone,Heat lens area,Remove broken lens,Clean lens housing,Attach new lens,Test camera,Power on",
     "options":["Test camera","Remove broken lens","Power off phone","Power on","Attach new lens","Clean lens housing","Heat lens area"],
     "difficulty":"hard"},

    {"topic":"Phone Repair","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to fix an unresponsive touchscreen (top = first)",
     "answer":"Restart phone,Clean screen,Remove screen protector,Check for software update,Calibrate touchscreen,Open back cover,Reseat screen connector",
     "options":["Remove screen protector","Restart phone","Reseat screen connector","Open back cover","Calibrate touchscreen","Check for software update","Clean screen"],
     "difficulty":"medium"},

    {"topic":"Phone Repair","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to replace a phone speaker (top = first)",
     "answer":"Power off phone,Open back cover,Locate speaker,Disconnect speaker,Remove speaker,Install new speaker,Connect new speaker,Close back cover,Test audio",
     "options":["Remove speaker","Open back cover","Test audio","Locate speaker","Power off phone","Install new speaker","Disconnect speaker","Connect new speaker","Close back cover"],
     "difficulty":"hard"},

    {"topic":"Phone Repair","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to troubleshoot an overheating phone (top = first)",
     "answer":"Power off phone,Remove case,Close background apps,Check for malware,Update software,Check battery condition,Replace battery if faulty",
     "options":["Check battery condition","Power off phone","Update software","Replace battery if faulty","Remove case","Check for malware","Close background apps"],
     "difficulty":"medium"},

    {"topic":"Phone Repair","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to recover data from a broken phone (top = first)",
     "answer":"Connect phone to PC,Enable USB debugging,Open recovery software,Scan phone storage,Select files to recover,Export files to PC",
     "options":["Scan phone storage","Connect phone to PC","Export files to PC","Enable USB debugging","Select files to recover","Open recovery software"],
     "difficulty":"hard"},

    {"topic":"Phone Repair","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to replace a faulty power button (top = first)",
     "answer":"Power off phone,Open phone casing,Locate power button flex cable,Disconnect flex cable,Remove button assembly,Install new button,Reconnect flex cable,Close casing,Test button",
     "options":["Install new button","Open phone casing","Test button","Power off phone","Close casing","Disconnect flex cable","Reconnect flex cable","Remove button assembly","Locate power button flex cable"],
     "difficulty":"hard"},

    {"topic":"Phone Repair","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to update phone software to fix bugs (top = first)",
     "answer":"Charge phone above 50%,Connect to WiFi,Open Settings,Go to Software Update,Download update,Install update,Wait for restart",
     "options":["Install update","Charge phone above 50%","Wait for restart","Go to Software Update","Connect to WiFi","Download update","Open Settings"],
     "difficulty":"easy"},

    {"topic":"Phone Repair","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to safely clean a blocked charging port (top = first)",
     "answer":"Power off phone,Get a toothpick or brush,Gently remove debris,Use compressed air,Inspect port,Power on,Test charging",
     "options":["Inspect port","Power off phone","Test charging","Get a toothpick or brush","Power on","Use compressed air","Gently remove debris"],
     "difficulty":"easy"},

    {"topic":"Phone Repair","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to fix a phone stuck in a bootloop (top = first)",
     "answer":"Remove battery if possible,Wait 30 seconds,Reinsert battery,Boot into recovery mode,Wipe cache partition,Reboot phone,Factory reset if needed",
     "options":["Factory reset if needed","Remove battery if possible","Reboot phone","Reinsert battery","Boot into recovery mode","Wait 30 seconds","Wipe cache partition"],
     "difficulty":"hard"},

    {"topic":"Phone Repair","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to replace a phone back cover (top = first)",
     "answer":"Power off phone,Heat back cover,Insert prying tool at edge,Slide tool around edges,Lift off back cover,Attach new back cover,Press edges to seal",
     "options":["Insert prying tool at edge","Power off phone","Press edges to seal","Lift off back cover","Attach new back cover","Heat back cover","Slide tool around edges"],
     "difficulty":"medium"},

    {"topic":"Phone Repair","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to test a phone after completing repairs (top = first)",
     "answer":"Power on phone,Test touchscreen,Test speaker and microphone,Test cameras,Test charging,Test WiFi and Bluetooth,Make a test call",
     "options":["Test WiFi and Bluetooth","Power on phone","Make a test call","Test cameras","Test touchscreen","Test charging","Test speaker and microphone"],
     "difficulty":"medium"},

    {"topic":"Phone Repair","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to fix a phone with no sound (top = first)",
     "answer":"Check volume settings,Disable silent mode,Test with headphones,Restart phone,Clear cache,Check speaker for damage,Replace speaker",
     "options":["Replace speaker","Check volume settings","Restart phone","Test with headphones","Check speaker for damage","Clear cache","Disable silent mode"],
     "difficulty":"medium"},

    {"topic":"Phone Repair","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to safely disassemble a smartphone (top = first)",
     "answer":"Power off phone,Remove SIM tray,Heat edges to loosen adhesive,Pry open back cover,Unscrew internal screws,Disconnect battery,Remove components carefully",
     "options":["Unscrew internal screws","Remove SIM tray","Disconnect battery","Heat edges to loosen adhesive","Power off phone","Remove components carefully","Pry open back cover"],
     "difficulty":"hard"},

    {"topic":"Phone Repair","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to fix a phone with broken WiFi (top = first)",
     "answer":"Toggle WiFi off and on,Restart phone,Forget and reconnect to network,Reset network settings,Check for software update,Open phone,Inspect WiFi antenna",
     "options":["Inspect WiFi antenna","Toggle WiFi off and on","Check for software update","Restart phone","Open phone","Reset network settings","Forget and reconnect to network"],
     "difficulty":"medium"},

    {"topic":"Phone Repair","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to replace a damaged SIM card tray (top = first)",
     "answer":"Power off phone,Insert SIM ejector pin,Remove old tray,Insert SIM into new tray,Slide new tray into slot,Power on phone,Verify network connection",
     "options":["Insert SIM into new tray","Power off phone","Verify network connection","Slide new tray into slot","Remove old tray","Insert SIM ejector pin","Power on phone"],
     "difficulty":"easy"},

    {"topic":"Phone Repair","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to fix GPS not working on a phone (top = first)",
     "answer":"Enable Location Services,Toggle GPS off and on,Check app permissions,Calibrate GPS,Clear GPS cache,Update software,Check GPS antenna connection",
     "options":["Update software","Enable Location Services","Check GPS antenna connection","Clear GPS cache","Toggle GPS off and on","Check app permissions","Calibrate GPS"],
     "difficulty":"medium"},

    # ════════════════════════════════════════════════════
    # TRUE/FALSE — Hardware Functions (22 questions)
    # ════════════════════════════════════════════════════

    # --- CPU ---
    {"topic":"Hardware Functions","q_type":"true_false","image_path":"",
     "prompt":"The CPU (Central Processing Unit) is the main chip that processes instructions and runs programs on a computer.",
     "answer":"True","options":["True","False"],"difficulty":"easy"},

    {"topic":"Hardware Functions","q_type":"true_false","image_path":"",
     "prompt":"The CPU is responsible for storing large amounts of files and documents permanently.",
     "answer":"False","options":["True","False"],"difficulty":"easy"},

    {"topic":"Hardware Functions","q_type":"true_false","image_path":"",
     "prompt":"A faster CPU generally means a computer can process tasks more quickly.",
     "answer":"True","options":["True","False"],"difficulty":"easy"},

    # --- RAM ---
    {"topic":"Hardware Functions","q_type":"true_false","image_path":"",
     "prompt":"RAM (Random Access Memory) temporarily stores data that the CPU is actively using.",
     "answer":"True","options":["True","False"],"difficulty":"easy"},

    {"topic":"Hardware Functions","q_type":"true_false","image_path":"",
     "prompt":"Data stored in RAM is permanently saved even after the computer is turned off.",
     "answer":"False","options":["True","False"],"difficulty":"easy"},

    {"topic":"Hardware Functions","q_type":"true_false","image_path":"",
     "prompt":"Adding more RAM to a computer can help it run more programs at the same time without slowing down.",
     "answer":"True","options":["True","False"],"difficulty":"easy"},

    # --- Motherboard ---
    {"topic":"Hardware Functions","q_type":"true_false","image_path":"",
     "prompt":"The motherboard is the main circuit board that connects all components of a computer together.",
     "answer":"True","options":["True","False"],"difficulty":"easy"},

    {"topic":"Hardware Functions","q_type":"true_false","image_path":"",
     "prompt":"The motherboard can function normally without a CPU installed.",
     "answer":"False","options":["True","False"],"difficulty":"medium"},

    # --- GPU ---
    {"topic":"Hardware Functions","q_type":"true_false","image_path":"",
     "prompt":"The GPU (Graphics Processing Unit) is responsible for rendering images, videos, and animations on screen.",
     "answer":"True","options":["True","False"],"difficulty":"easy"},

    {"topic":"Hardware Functions","q_type":"true_false","image_path":"",
     "prompt":"A dedicated GPU is more important than RAM when running word processing applications.",
     "answer":"False","options":["True","False"],"difficulty":"medium"},

    # --- HDD vs SSD ---
    {"topic":"Hardware Functions","q_type":"true_false","image_path":"",
     "prompt":"A Hard Disk Drive (HDD) uses spinning magnetic disks to store data permanently.",
     "answer":"True","options":["True","False"],"difficulty":"easy"},

    {"topic":"Hardware Functions","q_type":"true_false","image_path":"",
     "prompt":"An SSD (Solid State Drive) is generally faster than a traditional HDD because it has no moving parts.",
     "answer":"True","options":["True","False"],"difficulty":"easy"},

    {"topic":"Hardware Functions","q_type":"true_false","image_path":"",
     "prompt":"An HDD and an SSD serve completely different purposes and cannot both be used to store files.",
     "answer":"False","options":["True","False"],"difficulty":"medium"},

    # --- PSU ---
    {"topic":"Hardware Functions","q_type":"true_false","image_path":"",
     "prompt":"The Power Supply Unit (PSU) converts electricity from the wall outlet into the correct voltages needed by computer components.",
     "answer":"True","options":["True","False"],"difficulty":"easy"},

    {"topic":"Hardware Functions","q_type":"true_false","image_path":"",
     "prompt":"A faulty PSU can damage other components inside a computer.",
     "answer":"True","options":["True","False"],"difficulty":"medium"},

    # --- Monitor ---
    {"topic":"Hardware Functions","q_type":"true_false","image_path":"",
     "prompt":"A monitor is an output device that displays visual information from the computer.",
     "answer":"True","options":["True","False"],"difficulty":"easy"},

    {"topic":"Hardware Functions","q_type":"true_false","image_path":"",
     "prompt":"A monitor can send data back to the CPU for processing, making it both an input and output device.",
     "answer":"False","options":["True","False"],"difficulty":"medium"},

    # --- Keyboard & Mouse ---
    {"topic":"Hardware Functions","q_type":"true_false","image_path":"",
     "prompt":"Both the keyboard and mouse are input devices used to send instructions to the computer.",
     "answer":"True","options":["True","False"],"difficulty":"easy"},

    # --- Router ---
    {"topic":"Hardware Functions","q_type":"true_false","image_path":"",
     "prompt":"A router directs internet traffic between devices on a network and connects them to the internet.",
     "answer":"True","options":["True","False"],"difficulty":"easy"},

    {"topic":"Hardware Functions","q_type":"true_false","image_path":"",
     "prompt":"A router and a modem are exactly the same device with the same function.",
     "answer":"False","options":["True","False"],"difficulty":"medium"},

    # --- Printer & Scanner ---
    {"topic":"Hardware Functions","q_type":"true_false","image_path":"",
     "prompt":"A printer is an output device that produces a physical copy of digital documents.",
     "answer":"True","options":["True","False"],"difficulty":"easy"},

    {"topic":"Hardware Functions","q_type":"true_false","image_path":"",
     "prompt":"A scanner converts physical documents or images into digital files the computer can use.",
     "answer":"True","options":["True","False"],"difficulty":"easy"},

    # ════════════════════════════════════════════════════
    # TRUE/FALSE — GSM / Phone Repair Knowledge (22 questions)
    # ════════════════════════════════════════════════════

    # --- GSM Basics ---
    {"topic":"GSM Repair","q_type":"true_false","image_path":"",
     "prompt":"GSM stands for Global System for Mobile Communications and is used for transmitting voice and data on mobile networks.",
     "answer":"True","options":["True","False"],"difficulty":"easy"},

    {"topic":"GSM Repair","q_type":"true_false","image_path":"",
     "prompt":"A SIM card stores a subscriber's identity and allows a phone to connect to a mobile network.",
     "answer":"True","options":["True","False"],"difficulty":"easy"},

    {"topic":"GSM Repair","q_type":"true_false","image_path":"",
     "prompt":"Removing the SIM card from a phone while it is powered on can damage the SIM card or phone network settings.",
     "answer":"True","options":["True","False"],"difficulty":"medium"},

    {"topic":"GSM Repair","q_type":"true_false","image_path":"",
     "prompt":"A phone showing 'No Service' always means the SIM card is permanently damaged and must be replaced.",
     "answer":"False","options":["True","False"],"difficulty":"easy"},

    # --- Phone Battery ---
    {"topic":"GSM Repair","q_type":"true_false","image_path":"",
     "prompt":"A swollen phone battery is dangerous and the phone should be powered off and serviced immediately.",
     "answer":"True","options":["True","False"],"difficulty":"easy"},

    {"topic":"GSM Repair","q_type":"true_false","image_path":"",
     "prompt":"It is safe to continue using a phone with a swollen battery as long as it still charges.",
     "answer":"False","options":["True","False"],"difficulty":"easy"},

    {"topic":"GSM Repair","q_type":"true_false","image_path":"",
     "prompt":"Phone batteries lose capacity over time and may need to be replaced after 1–3 years of heavy use.",
     "answer":"True","options":["True","False"],"difficulty":"easy"},

    # --- Charging & Ports ---
    {"topic":"GSM Repair","q_type":"true_false","image_path":"",
     "prompt":"Dust and debris inside the charging port is a common cause of a phone not charging properly.",
     "answer":"True","options":["True","False"],"difficulty":"easy"},

    {"topic":"GSM Repair","q_type":"true_false","image_path":"",
     "prompt":"Using a sharp metal object to clean a phone's charging port is the safest and recommended method.",
     "answer":"False","options":["True","False"],"difficulty":"easy"},

    {"topic":"GSM Repair","q_type":"true_false","image_path":"",
     "prompt":"A damaged charging port can be replaced without replacing the entire phone.",
     "answer":"True","options":["True","False"],"difficulty":"medium"},

    # --- Screen & Display ---
    {"topic":"GSM Repair","q_type":"true_false","image_path":"",
     "prompt":"A phone screen that shows lines or dead pixels may have a damaged LCD or AMOLED display panel.",
     "answer":"True","options":["True","False"],"difficulty":"medium"},

    {"topic":"GSM Repair","q_type":"true_false","image_path":"",
     "prompt":"Replacing a cracked phone screen always requires special tools and cannot be done by hand alone.",
     "answer":"True","options":["True","False"],"difficulty":"medium"},

    {"topic":"GSM Repair","q_type":"true_false","image_path":"",
     "prompt":"A cracked screen protector always means the phone screen underneath is also cracked.",
     "answer":"False","options":["True","False"],"difficulty":"easy"},

    # --- Water Damage ---
    {"topic":"GSM Repair","q_type":"true_false","image_path":"",
     "prompt":"The first thing to do when a phone falls in water is to immediately press the power button to check if it still works.",
     "answer":"False","options":["True","False"],"difficulty":"easy"},

    {"topic":"GSM Repair","q_type":"true_false","image_path":"",
     "prompt":"Placing a water-damaged phone in a bag of silica gel or uncooked rice can help absorb moisture.",
     "answer":"True","options":["True","False"],"difficulty":"easy"},

    {"topic":"GSM Repair","q_type":"true_false","image_path":"",
     "prompt":"Water damage indicators (small stickers inside the phone) turn red or pink when exposed to moisture.",
     "answer":"True","options":["True","False"],"difficulty":"medium"},

    # --- Software & Firmware ---
    {"topic":"GSM Repair","q_type":"true_false","image_path":"",
     "prompt":"Flashing a phone's firmware can fix software problems that cause a phone to freeze or not start up.",
     "answer":"True","options":["True","False"],"difficulty":"medium"},

    {"topic":"GSM Repair","q_type":"true_false","image_path":"",
     "prompt":"A factory reset removes all apps and personal data from a phone and restores it to its original settings.",
     "answer":"True","options":["True","False"],"difficulty":"easy"},

    {"topic":"GSM Repair","q_type":"true_false","image_path":"",
     "prompt":"You should always back up your data before performing a factory reset.",
     "answer":"True","options":["True","False"],"difficulty":"easy"},

    # --- Components & Tools ---
    {"topic":"GSM Repair","q_type":"true_false","image_path":"",
     "prompt":"A heat gun or heated pad is commonly used in phone repair to soften adhesive holding the screen or back cover.",
     "answer":"True","options":["True","False"],"difficulty":"medium"},

    {"topic":"GSM Repair","q_type":"true_false","image_path":"",
     "prompt":"ESD (Electrostatic Discharge) can damage sensitive phone components, so technicians should use anti-static tools.",
     "answer":"True","options":["True","False"],"difficulty":"medium"},

    {"topic":"GSM Repair","q_type":"true_false","image_path":"",
     "prompt":"Any screwdriver can be safely used to open a smartphone, regardless of the screw type.",
     "answer":"False","options":["True","False"],"difficulty":"easy"},

    # --- Network & Signal ---
    {"topic":"GSM Repair","q_type":"true_false","image_path":"",
     "prompt":"A broken or bent internal antenna can cause poor call quality or loss of network signal on a phone.",
     "answer":"True","options":["True","False"],"difficulty":"medium"},

    {"topic":"GSM Repair","q_type":"true_false","image_path":"",
     "prompt":"Inserting a SIM card from one network operator always works in any phone without any configuration.",
     "answer":"False","options":["True","False"],"difficulty":"medium"},
]

# Add additional drag-label questions (without revealing names in filenames)
additional_hardware = [
    ("cooling_fan.png", "Cooling Fan", ["Fan", "Heatsink", "CPU Cooler", "Case Fan"]),
    ("cd_dvd_drive.png", "DVD Drive", ["DVD Drive", "Blu-ray", "CD Drive", "Optical Drive"]),
    ("network_card.png", "Network Card", ["Network Card", "WiFi Card", "Ethernet", "Adapter"]),
    ("sound_card.png", "Sound Card", ["Sound Card", "Audio Card", "Amplifier", "DSP"]),
    ("battery.png", "Laptop Battery", ["Battery", "Power Cell", "Charger", "UPS"]),
    ("sd_card.png", "SD Card", ["SD Card", "Memory Card", "Flash Card", "MicroSD"]),
]

current_label_count = sum(1 for q in questions if q["q_type"] == "drag_label")
needed = 50 - current_label_count  # Aim for 50 drag-label

for img, ans, opts in additional_hardware[:needed]:
    questions.append({
        "topic": "Computer Hardware",
        "q_type": "drag_label",
        "image_path": f"images/{img}",
        "prompt": "Identify the correct label for the image below",
        "answer": ans,
        "options": opts,
        "difficulty": "easy"
    })

print(f"Total questions: {len(questions)}")
print(f"Drag-label (images):  {sum(1 for q in questions if q['q_type'] == 'drag_label')}")
print(f"Drag-sort (ordering): {sum(1 for q in questions if q['q_type'] == 'drag_sort')}")
print(f"True/False:           {sum(1 for q in questions if q['q_type'] == 'true_false')}")

with app.app_context():
    db.create_all()
    Question.query.delete()
    for q in questions:
        db.session.add(Question(**q))
    db.session.commit()
    print(f"✅ Successfully seeded {len(questions)} questions!")
