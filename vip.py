import asyncio
from xC4 import Emote_k
import random

# ==========================================
#        VIP CONFIGURATION SETTINGS
# ==========================================

# 1. VIP ADMINS (Apni UID yahan dalo)
VIP_ADMINS = [
    "11553486931", 
    "2572691913",   
    "1234567890",   
    "9316257817"    
]

# 2. PUBLIC PASSWORD (Non-Admins ke liye)
PUBLIC_PASSWORD = "QNR"

# 3. SPEED SETTINGS
DELAY = 4.15 

# ==========================================
#        EMOTE LISTS (VIDEO EXTRACTED)
# ==========================================

# LIST 1: EVO & MAX EMOTES (Video Start)
LIST_1 = [
    909000075, 909000063, 909035007, 909000068, 909000085, 
    909038012, 909035012, 909033002, 909051003, 909037011,
    909000081, 909000090, 909041000, 909038010, 909033001,
    909000098, 909040010, 909045001, 909042008, 909041002,
    909042007, 909049010, 909051012, 909000134, 909051014
]

# LIST 2: OLD & RARE (Video Middle)
LIST_2 = [
    909000002, 909000003, 909000010, 909000014, 909000032,
    909000034, 909000036, 909000038, 909000039, 909000041,
    909000045, 909000046, 909000052, 909000017, 909000018,
    909000060, 909000091, 909000093, 909000094, 909000095
]

# LIST 3: DANCE & FUNNY
LIST_3 = [
    909000061, 909000062, 909000064, 909000065, 909000066,
    909000067, 909000069, 909000070, 909000071, 909000089,
    909000096, 909000121, 909000122, 909000123, 909000124,
    909000125, 909046007, 909046008, 909046009, 909046010
]

# LIST 4: ACTION & FIGHTING
LIST_4 = [
    909000072, 909000073, 909000074, 909000076, 909000077,
    909000078, 909000079, 909000080, 909000086, 909000087,
    909000088, 909000091, 909000128, 909000129, 909000130,
    909000133, 909000134, 909044001, 909044002, 909044003
]

# LIST 5: NEW EVENTS & COLLABS
LIST_5 = [
    909000135, 909000136, 909000137, 909000138, 909000139,
    909000140, 909000141, 909000142, 909000143, 909000144,
    909000145, 909033005, 909033006, 909033007, 909033008,
    909033009, 909034001, 909034002, 909034003, 909034004
]

# LIST 6: LATEST ADDITIONS
LIST_6 = [
    909036001, 909036002, 909036003, 909036004, 909036005,
    909036006, 909036008, 909036009, 909036010, 909036011,
    909036012, 909036014, 909037001, 909047001, 909047002,
    909047003, 909047004, 909047005, 909047006, 909047007
]

# LIST 7: EXTRA MIX
LIST_7 = [
    909042005, 909042006, 909042009, 909042011, 909042012,
    909042013, 909042016, 909042017, 909042018, 909043001,
    909043002, 909043003, 909043004, 909043005, 909043006,
    909043007, 909043008, 909043009, 909043010, 909045010
]

# LIST 8: FINAL COLLECTION
LIST_8 = [
    909040001, 909040002, 909040003, 909040004, 909040005,
    909040006, 909040008, 909040009, 909040011, 909040012,
    909040013, 909040014, 909041001, 909041003, 909041004,
    909041005, 909041006, 909041007, 909041008, 909041009
]

# LIST 108: SAB KUCH (ALL LISTS COMBINED)
LIST_108 = LIST_1 + LIST_2 + LIST_3 + LIST_4 + LIST_5 + LIST_6 + LIST_7 + LIST_8

# ==========================================
#           CORE LOGIC & STATE
# ==========================================

is_running = False
current_task = None

async def SEndPacKeT(whisper_writer, online_writer, TypE, PacKeT):
    try:
        if TypE == 'OnLine' and online_writer:
            online_writer.write(PacKeT)
            await online_writer.drain()
        elif TypE == 'ChaT' and whisper_writer:
            whisper_writer.write(PacKeT)
            await whisper_writer.drain()
    except Exception as e:
        print(f"Packet Send Error: {e}")

async def start_loop(target_list, target_uid, key, iv, region, whisper_writer, online_writer):
    global is_running
    is_running = True
    
    print(f"VIP Loop Started on Target: {target_uid} with {len(target_list)} emotes")
    
    while is_running:
        for emote_id in target_list:
            if not is_running: break
            try:
                H = await Emote_k(int(target_uid), int(emote_id), key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                await asyncio.sleep(DELAY)
            except Exception as e:
                print(f"VIP Spam Error: {e}")
                await asyncio.sleep(1)
        
        # Loop khatam hone ke baad wapas shuru karo (agar 108 hai to shuffle kar do)
        if len(target_list) > 100:
            random.shuffle(target_list)

# ==========================================
#        COMMAND HANDLER (1-8 and 108 Logic)
# ==========================================

async def handle_vip_command(msg, sender_uid, key, iv, region, whisper_writer, online_writer):
    global is_running, current_task
    
    parts = msg.split()
    command = parts[0].lower()
    
    # --- STOP COMMAND ---
    if command == '/stop':
        if is_running:
            is_running = False
            if current_task: current_task.cancel()
            return "🛑 VIP Stopped! Sab kuch rok diya."
        return "⚠️ Bot pehle se hi rukka hua hai."

    # --- ONLY /ALL COMMAND HANDLED HERE ---
    if command != '/all':
        return None

    # --- PASSWORD CHECK ---
    is_admin = str(sender_uid) in VIP_ADMINS
    has_password = False
    if parts[-1] == PUBLIC_PASSWORD:
        has_password = True
    
    if not is_admin and not has_password:
        return f"🔒 Access Denied! Password lagao.\nFormat: /all [1-8/108] [TargetUID] {PUBLIC_PASSWORD}"

    # --- ARGUMENT PARSING (The "1 se 8" and "108" Logic) ---
    
    # Default Values
    list_num = 108      # Default to Full Power if not specified
    target_uid = sender_uid # Default to Sender
    
    # Arguments nikalna (Password ko ignore karke agar hai to)
    args = parts[1:-1] if has_password else parts[1:]
    
    if len(args) == 0:
        # Case: "/all" -> Default 108 list on Sender
        pass
        
    elif len(args) == 1:
        # Case: "/all 1" OR "/all 123456"
        val = args[0]
        if len(val) <= 2: # Ye List Number hai (1-8)
            list_num = int(val)
        elif val == "108": # Ye Special Code hai
            list_num = 108
        else: # Ye Target UID hai
            target_uid = val
            
    elif len(args) >= 2:
        # Case: "/all 1 123456" (List + UID)
        val1 = args[0]
        val2 = args[1]
        
        if len(val1) <= 3: # First arg is List number (1, 8, 108)
            list_num = int(val1)
            target_uid = val2
        else: # First arg is UID, Second is maybe List? (Rare case)
            target_uid = val1
            if len(val2) <= 3: list_num = int(val2)

    # --- SELECT LIST BASED ON NUMBER ---
    selected_list = []
    mode_name = ""
    
    if list_num == 1: selected_list = LIST_1; mode_name = "EVO LIST (1)"
    elif list_num == 2: selected_list = LIST_2; mode_name = "RARE LIST (2)"
    elif list_num == 3: selected_list = LIST_3; mode_name = "FUNNY LIST (3)"
    elif list_num == 4: selected_list = LIST_4; mode_name = "ACTION LIST (4)"
    elif list_num == 5: selected_list = LIST_5; mode_name = "EVENTS LIST (5)"
    elif list_num == 6: selected_list = LIST_6; mode_name = "LATEST LIST (6)"
    elif list_num == 7: selected_list = LIST_7; mode_name = "EXTRA LIST (7)"
    elif list_num == 8: selected_list = LIST_8; mode_name = "FINAL LIST (8)"
    elif list_num == 108: selected_list = LIST_108; mode_name = "🔥 FULL POWER (108) 🔥"
    else: 
        selected_list = LIST_108; mode_name = "DEFAULT (108)"

    # --- START EXECUTION ---
    if selected_list:
        if is_running:
            is_running = False
            if current_task: current_task.cancel()
            await asyncio.sleep(0.5)

        current_task = asyncio.create_task(
            start_loop(selected_list, target_uid, key, iv, region, whisper_writer, online_writer)
        )
        
        return f"""
✅ COMMAND ACCEPTED!
📜 List: {mode_name}
🎯 Target: {target_uid}
🔢 Total Emotes: {len(selected_list)}
🚀 Speed: {DELAY}s
"""
    
    return "❌ Error: List load nahi hui."
