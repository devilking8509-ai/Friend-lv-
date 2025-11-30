import asyncio
from xC4 import Emote_k
import random

# --- SETTINGS (Yahan Apni 5 UIDs Dalo) ---
VIP_ADMINS = [
    "11553486931",  # Admin 1 (Main Boss)
    "2572691913",  # Admin 2
    "2522821351",  # Admin 3
    "9316257817",  # Admin 4
    "13947421096"   # Admin 5
]

DELAY = 4.15  # Speed (Jitna kam number, utna tez spam)

# --- STATE VARIABLES ---
is_running = False
current_task = None

# --- LOCAL HELPER FUNCTION ---
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

# --- 1. EVOLUTION WEAPON EMOTES ---
EVO_IDS = [
    909000063, 909000081, 909000075, 909000085, 909000134,
    909000098, 909035007, 909051012, 909000141, 909034008,
    909051015, 909041002, 909039004, 909042008, 909051014,
    909039012, 909040010, 909035010, 909041005, 909051003, 
    909034001, 909000090, 909000068, 909038012, 909035012,
    909033002, 909037011, 909049010, 909038010, 909033001,
    909045001, 909042008, 909049012, 909042007, 909040010
]

# --- 2. THE MASTER LIST (ALL EMOTES) ---
ALL_IDS = [
    909046007, 909046008, 909046009, 909046010, 909046011, 909046012, 
    909046013, 909046014, 909046015, 909046016, 909046017, 909047001, 
    909047002, 909047003, 909047004, 909047005, 909047006, 909047007, 
    909047008, 909047009, 909047012, 909042005, 909042006, 909042009, 
    909042011, 909042012, 909042013, 909042016, 909042017, 909042018, 
    909043001, 909043002, 909043003, 909043004, 909043005, 909043006,
    909043007, 909043008, 909043009, 909043010, 909043013, 909044001, 
    909044002, 909044003, 909044004, 909044005, 909044006, 909044007, 
    909044015, 909044016, 909045002, 909045003, 909045004, 909045005, 
    909045010, 909045011, 909045012, 909045015, 909045016, 909045017, 
    909046001, 909046002, 909046003, 909046004, 909046005, 909046006,
    909036004, 909036005, 909036006, 909036008, 909036009, 909036010, 
    909036011, 909036012, 909036014, 909037001, 909037002, 909037003, 
    909037004, 909037005, 909037006, 909034013, 909034014, 909035001, 
    909035005, 909035006, 909035008, 909035009, 909035010, 909035011, 
    909035013, 909035014, 909035015, 909036001, 909036002, 909036003,
    909041005, 909041006, 909041007, 909041008, 909041009, 909041010, 
    909041011, 909041012, 909041013, 909041014, 909041015, 909042001, 
    909042002, 909042003, 909042004, 909039001, 909039002, 909039003, 
    909039004, 909039005, 909039006, 909039007, 909039008, 909039009, 
    909039010, 909039011, 909039012, 909039013, 909039014, 909040001,
    909037007, 909037008, 909037009, 909037010, 909037012, 909038001, 
    909038002, 909038003, 909038004, 909038005, 909038006, 909038008, 
    909038009, 909038011, 909038013, 909040002, 909040003, 909040004, 
    909040005, 909040006, 909040008, 909040009, 909040011, 909040012, 
    909040013, 909040014, 909041001, 909041002, 909041003, 909041004,
    909000041, 909000045, 909000046, 909000052, 909000055, 909000056, 
    909000057, 909000058, 909000060, 909000061, 909000062, 909000064, 
    909000065, 909000066, 909000067, 909000135, 909000136, 909000137, 
    909000138, 909000139, 909000140, 909000141, 909000142, 909000143, 
    909000144, 909000145, 909033004, 909033005, 909033006, 909033007,
    909000002, 909000003, 909000010, 909000014, 909000032, 909000034, 
    909000036, 909000038, 909000039, 909000091, 909000093, 909000094, 
    909000095, 909000096, 909000121, 909000122, 909000123, 909000124, 
    909000125, 909000128, 909000129, 909000130, 909000133, 909000134,
    909000069, 909000070, 909000071, 909000072, 909000073, 909000074, 
    909000076, 909000077, 909000078, 909000079, 909000080, 909000086, 
    909000087, 909000088, 909000089, 909033008, 909033009, 909033010, 
    909034001, 909034002, 909034003, 909034004, 909034005, 909034006, 
    909034007, 909034008, 909034009, 909034010, 909034011, 909034012
]

# --- MIXED RANDOM SELECTION ---
FULL_MIX = list(set(EVO_IDS + ALL_IDS))

async def start_loop(mode, uid, key, iv, region, whisper_writer, online_writer):
    global is_running
    is_running = True
    
    # Target list selection
    if mode == 'evo':
        target_list = EVO_IDS
    elif mode == 'all':
        target_list = ALL_IDS
    elif mode == 'mix':
        target_list = FULL_MIX
        random.shuffle(target_list)
    else:
        target_list = ALL_IDS

    print(f"VIP Loop Started: {mode} with {len(target_list)} emotes")
    
    while is_running:
        for emote_id in target_list:
            if not is_running: break
            try:
                # Region logic automatic handled by xC4
                H = await Emote_k(int(uid), int(emote_id), key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                
                # Gap between emotes
                await asyncio.sleep(DELAY)
            except Exception as e:
                print(f"VIP Error: {e}")
                await asyncio.sleep(0.5)
        
        # Loop khatam hone ke baad agar mix mode hai to shuffle karo
        if mode == 'mix':
            random.shuffle(target_list)

async def handle_vip_command(msg, uid, key, iv, region, whisper_writer, online_writer):
    global is_running, current_task
    
    # --- 1. SECURITY CHECK (5 UIDs Support) ---
    # Check karega ki msg bhejne wale ki UID list me hai ya nahi
    if str(uid) not in VIP_ADMINS:
        return "❌ Access Denied! Sirf VIP Admins use kar sakte hain."

    # 2. Stop Command
    if msg == '/stop':
        if is_running:
            is_running = False
            if current_task: current_task.cancel()
            return "🛑 Stopped! Emote spam band kar diya."
        return "⚠️ Already stopped."

    # 3. Start Commands
    mode = None
    count = 0
    
    if msg == '/evo': 
        mode = 'evo'
        count = len(EVO_IDS)
    elif msg == '/all': 
        mode = 'all'
        count = len(ALL_IDS)
    elif msg == '/mix': 
        mode = 'mix'
        count = len(FULL_MIX)
    
    if mode:
        # Purana task roko
        if is_running:
            is_running = False
            if current_task: current_task.cancel()
            await asyncio.sleep(0.5)

        # Naya task shuru
        current_task = asyncio.create_task(
            start_loop(mode, uid, key, iv, region, whisper_writer, online_writer)
        )
        return f"✅ Started {mode.upper()} Mode!\nTotal Emotes: {count}\nSpeed: {DELAY}s"
    
    return None
