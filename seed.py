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
     "options":["Webcam","Microphone","Camera","Scanner"],"difficulty":"easy"},

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
     "options":["Smartphone","Cell phone","Tablet","Mobile"],"difficulty":"easy"},

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
    # DRAG-SORT — NO IMAGES (just text-based ordering)
    # ════════════════════════════════════════════════════
    {"topic":"Computer Basics","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to start a computer in the correct order (top = first)",
     "answer":"Plug in power,Press power button,Wait for startup,Enter password",
     "options":["Enter password","Wait for startup","Press power button","Plug in power"],"difficulty":"easy"},

    {"topic":"Computer Basics","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to shut down a computer correctly (top = first)",
     "answer":"Click Start,Click Power icon,Select Shut down,Wait for shutdown",
     "options":["Select Shut down","Click Power icon","Wait for shutdown","Click Start"],"difficulty":"easy"},

    {"topic":"Email","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to send an email (top = first)",
     "answer":"Open email,Click Compose,Type address,Write message,Click Send",
     "options":["Click Send","Write message","Click Compose","Type address","Open email"],"difficulty":"easy"},

    {"topic":"Internet","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to search the internet (top = first)",
     "answer":"Open browser,Type search words,Press Enter,Click on result",
     "options":["Click on result","Open browser","Press Enter","Type search words"],"difficulty":"easy"},

    {"topic":"File Management","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to save a file (top = first)",
     "answer":"Click File,Click Save As,Choose location,Type name,Click Save",
     "options":["Click Save As","Click Save","Choose location","Type name","Click File"],"difficulty":"easy"},

    {"topic":"File Management","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to print a document (top = first)",
     "answer":"Open document,Click File,Click Print,Choose printer,Click Print",
     "options":["Click Print","Choose printer","Open document","Click File","Click Print"],"difficulty":"easy"},

    {"topic":"File Management","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to copy a file (top = first)",
     "answer":"Select file,Right-click,Choose Copy,Go to destination,Right-click,Paste",
     "options":["Paste","Choose Copy","Go to destination","Select file","Right-click","Right-click"],"difficulty":"easy"},

    {"topic":"Computer Setup","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to set up a new computer (top = first)",
     "answer":"Unbox computer,Connect monitor,Connect keyboard,Connect mouse,Plug in power,Press power",
     "options":["Press power","Connect mouse","Unbox computer","Connect monitor","Connect keyboard","Plug in power"],"difficulty":"easy"},

    {"topic":"WiFi Setup","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to connect to WiFi (top = first)",
     "answer":"Click WiFi icon,Select network,Type password,Click Connect",
     "options":["Click WiFi icon","Type password","Select network","Click Connect"],"difficulty":"easy"},

    {"topic":"Software Installation","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to install a program (top = first)",
     "answer":"Download installer,Open installer,Click Next,Agree to terms,Choose location,Click Install",
     "options":["Click Install","Choose location","Open installer","Agree to terms","Download installer","Click Next"],"difficulty":"medium"},

    {"topic":"USB Drive","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to safely remove a USB drive (top = first)",
     "answer":"Click USB icon,Select Eject,Wait for message,Pull out USB",
     "options":["Select Eject","Click USB icon","Pull out USB","Wait for message"],"difficulty":"easy"},

    {"topic":"Taking Screenshot","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to take a screenshot (top = first)",
     "answer":"Press PrtScn key,Open Paint,Paste image,Crop if needed,Save file",
     "options":["Open Paint","Paste image","Press PrtScn key","Crop if needed","Save file"],"difficulty":"medium"},

    {"topic":"Password Creation","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange these passwords from WEAKEST to STRONGEST (top = weakest)",
     "answer":"123456,password,Football,Summer2024,Tr0ub4dour&2024",
     "options":["Football","Summer2024","123456","password","Tr0ub4dour&2024"],"difficulty":"easy"},

    {"topic":"Data Sizes","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange these data sizes from SMALLEST to LARGEST (top = smallest)",
     "answer":"Bit,Byte,KB,MB,GB,TB",
     "options":["MB","KB","TB","Byte","GB","Bit"],"difficulty":"easy"},

    {"topic":"File Sizes","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange these files from SMALLEST to LARGEST (top = smallest)",
     "answer":"Text file,Word doc,Music song,Video clip,Full movie",
     "options":["Video clip","Music song","Full movie","Word doc","Text file"],"difficulty":"easy"},

    {"topic":"Computer Speed","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange these tasks from FASTEST to SLOWEST for a computer (top = fastest)",
     "answer":"Type letter,Open photo,Play music,Play video,Start game",
     "options":["Play game","Type letter","Open photo","Play music","Play video"],"difficulty":"medium"},

    {"topic":"Backup Steps","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to backup files (top = first)",
     "answer":"Plug USB,Open files,Select files,Drag to USB,Wait for copy,Eject USB",
     "options":["Drag to USB","Select files","Open files","Eject USB","Wait for copy","Plug USB"],"difficulty":"medium"},

    {"topic":"Browser Tabs","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to open a new browser tab (top = first)",
     "answer":"Open browser,Click + icon,Type website,Press Enter",
     "options":["Press Enter","Click + icon","Type website","Open browser"],"difficulty":"easy"},

    {"topic":"Bookmark Webpage","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to bookmark a webpage (top = first)",
     "answer":"Go to website,Click star icon,Choose folder,Click Done",
     "options":["Click star icon","Go to website","Choose folder","Click Done"],"difficulty":"easy"},

    {"topic":"Clear History","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to clear browsing history (top = first)",
     "answer":"Click menu,Go to History,Click Clear data,Choose time range,Click Clear",
     "options":["Click Clear data","Clear","Choose time range","Click menu","Go to History"],"difficulty":"medium"},

    {"topic":"Zoom Meeting","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to join a Zoom meeting (top = first)",
     "answer":"Open Zoom,Click Join,Enter Meeting ID,Enter password,Click Join",
     "options":["Enter password","Open Zoom","Join","Enter Meeting ID","Click Join"],"difficulty":"easy"},

    {"topic":"Email Attachment","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to attach a file to an email (top = first)",
     "answer":"Compose email,Click Attach,Find file,Select file,Click Open",
     "options":["Attach","Select file","Compose email","Click Open","Find file"],"difficulty":"easy"},

    {"topic":"Hardware Upgrade","q_type":"drag_sort","image_path":"",
     "prompt":"Drag and arrange the steps to install new RAM (top = first)",
     "answer":"Shut down computer,Open case,Find RAM slots,Insert RAM,Close case,Power on",
     "options":["Find RAM slots","Insert RAM","Open case","Power on","Shut down computer","Close case"],"difficulty":"hard"},
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
needed = 50 - current_label_count  # Aim for 50 drag-label, 50 drag-sort

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
print(f"Drag-label (images): {sum(1 for q in questions if q['q_type'] == 'drag_label')}")
print(f"Drag-sort (text only): {sum(1 for q in questions if q['q_type'] == 'drag_sort')}")

with app.app_context():
    db.create_all()
    Question.query.delete()
    for q in questions:
        db.session.add(Question(**q))
    db.session.commit()
    print(f"✅ Successfully seeded {len(questions)} questions!")