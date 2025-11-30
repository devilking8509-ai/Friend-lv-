import asyncio
from xC4 import Emote_k
import random

# --- SETTINGS (Apni Squad ki UIDs yahan rakhein) ---
VIP_ADMINS = [
    # --- PURANE ADMINS (Ye nahi hatenge) ---
    "11553486931",
    "2572691913",
    "2522821351",
    "9316257817",
    "6477391965",
    
    # --- NAYE 50 SLOTS (Yahan paste karein) ---
    "13984459203",
    "3310162666",
    "UID_3_YAHAN_DALO",
    "UID_4_YAHAN_DALO",
    "UID_5_YAHAN_DALO",
    "UID_6_YAHAN_DALO",
    "UID_7_YAHAN_DALO",
    "UID_8_YAHAN_DALO",
    "UID_9_YAHAN_DALO",
    "UID_10_YAHAN_DALO",
    "UID_11_YAHAN_DALO",
    "UID_12_YAHAN_DALO",
    "UID_13_YAHAN_DALO",
    "UID_14_YAHAN_DALO",
    "UID_15_YAHAN_DALO",
    "UID_16_YAHAN_DALO",
    "UID_17_YAHAN_DALO",
    "UID_18_YAHAN_DALO",
    "UID_19_YAHAN_DALO",
    "UID_20_YAHAN_DALO",
    "UID_21_YAHAN_DALO",
    "UID_22_YAHAN_DALO",
    "UID_23_YAHAN_DALO",
    "UID_24_YAHAN_DALO",
    "UID_25_YAHAN_DALO",
    "UID_26_YAHAN_DALO",
    "UID_27_YAHAN_DALO",
    "UID_28_YAHAN_DALO",
    "UID_29_YAHAN_DALO",
    "UID_30_YAHAN_DALO",
    "UID_31_YAHAN_DALO",
    "UID_32_YAHAN_DALO",
    "UID_33_YAHAN_DALO",
    "UID_34_YAHAN_DALO",
    "UID_35_YAHAN_DALO",
    "UID_36_YAHAN_DALO",
    "UID_37_YAHAN_DALO",
    "UID_38_YAHAN_DALO",
    "UID_39_YAHAN_DALO",
    "UID_40_YAHAN_DALO",
    "UID_41_YAHAN_DALO",
    "UID_42_YAHAN_DALO",
    "UID_43_YAHAN_DALO",
    "UID_44_YAHAN_DALO",
    "UID_45_YAHAN_DALO",
    "UID_46_YAHAN_DALO",
    "UID_47_YAHAN_DALO",
    "UID_48_YAHAN_DALO",
    "UID_49_YAHAN_DALO",
    "UID_50_YAHAN_DALO"
]

DELAY = 5.15  # Speed control

# --- STATE VARIABLES ---
is_running = False
current_task = None

# --- PACKET SENDER ---
async def SEndPacKeT(whisper_writer, online_writer, TypE, PacKeT):
    try:
        if TypE == 'OnLine' and online_writer:
            online_writer.write(PacKeT)
            await online_writer.drain()
        elif TypE == 'ChaT' and whisper_writer:
            whisper_writer.write(PacKeT)
            await whisper_writer.drain()
    except Exception as e:
        print(f"Packet Error: {e}")

# ==========================================
#        EMOTE LISTS (VIDEO ORDER)
# ==========================================

# 1. EVO GUNS & MAX EMOTES (Video ke Start wale)
EVO_IDS = [
    909000075, # Cobra Rising (MP40)
    909000063, # AK Max
    909035007, # Shotgun Max (Green M1014)
    909000068, # Scar Max
    909000085, # XM8 Max
    909038012, # G18 Max
    909035012, # AN94 Max
    909033002, # MP5 Max
    909051003, # M60 Max
    909037011, # Fist Max
    909039011, # M10 Max (Red)
    909000090, # Famas Max
    909049010, # P90 Max
    909038010, # Thompson Max
    909033001, # M4A1 Max
    909000098, # UMP Max
    909040010, # New MP40 Max (Blue)
    909045001, # Parafal Max
    909042008, # Woodpecker Max
    909049012, # Open Fire (Flying Guns)
    909042007, # 100 Gloo Sculpture
]

# 2. NORMAL & RARE EMOTES (Video ke baki emotes sequence mein)
NORMAL_IDS = [
    909000002, # LOL
    909000003, # Provoke
    909000010, # Flowers of Love (Rose)
    909000014, # FFWC Throne
    909000032, # Selfie
    909000034, # Pirate Flag
    909000036, # Top DJ
    909000038, # Power of Money
    909000039, # Eat my dust
    909000041, # Kungfu
    909000045, # I heart you
    909000046, # Tea Time
    909000052, # Doggie
    909000055, # I'm Rich
    909000056, # Make it Rain
    909000057, # Dust Off
    909000058, # Captain Booyah
    909000060, # BOOYAH!
    909000061, # Bhangra
    909000062, # Piece of Cake
    909000064, # I'm Saitama
    909000065, # The Victor
    909000066, # Sii! (CR7)
    909000067, # Obliteration
    909000069, # Top Scorer
    909000070, # Triple Kicks
    909000071, # Cobra Dance
    909000072, # Predator Pulse
    909000073, # Ground Punch
    909000074, # The Biker
    909000076, # One-Finger Pushup
    909000077, # Stage Time
    909000078, # Booyah Balloon
    909000079, # More Practice
    909000080, # FFWS 2021
    909000086, # Mythos Four
    909000087, # Champion Grab
    909000088, # Win and Chill
    909000089, # Hadouken
    909000091, # Big Smash
    909000093, # All In Control
    909000094, # Debugging
    909000095, # Wagor Wave
    909000096, # Crazy Guitar
    909000121, # Dribble King
    909000122, # Name Not Found
    909000123, # Mind It!
    909000124, # Golden Combo
    909000125, # Sick Moves
    909000128, # Ruler's Flag
    909000129, # Money Throw
    909000130, # Endless Bullets
    909000133, # Fire Slam
    909000134, # Heartbroken
    909000135, # Rock Paper Scissors
    909000136, # Shattered Reality
    909000137, # Halo of Music
    909000138, # Burnt BBQ
    909000139, # Switching Steps
    909000140, # Creed Slay
    909000141, # Leap of Fail
    909000142, # Name Not Found 2
    909000143, # Helicopter Shot
    909000144, # Kungfu Tigers
    909000145, # Possessed Warrior
    909033004, # Drop Kick
    909033005, # Sit Down!
    909033006, # BOOYAH Sparks
    909033007, # The FFWS Dance
    909033008, # Easy Peasy
    909033009, # Winner Throw
    909033010, # Weight of Victory
    909034001, # Chronicle of the Sword
    909034002, # The Collapse
    909034003, # Flaming Groove
    909034004, # Energetic
    909034005, # Ridicule
    909034006, # Tease Waggor
    909034007, # Great Conductor
    909034008, # Fake Death
    909034009, # Twerk
    909034010, # BR-Ranked Heroic
    909034011, # BR-Ranked Master
    909034012, # CS-Ranked Heroic
    909034013, # CS-Ranked Master
    909034014, # Yes I Do
    909035001, # Free Money
    909035005, # Victorious Eagle
    909035006, # Flying Saucer
    909035008, # Bobble Dance
    909035009, # Weight Training
    909035010, # Beautiful Love
    909035011, # Groove Moves
    909035013, # Louder Please
    909035014, # Ninja Stand
    909035015, # Creator In Action
    909036001, # Ghost Float
    909036002, # Shiba Surf
    909036003, # Waiter Walk
    909036004, # Graffiti Cameraman
    909036005, # Agile Boxer
    909036006, # Sunbathing
    909036008, # Skateboard Swag
    909036009, # Phantom Tamer
    909036010, # The Signal
    909036011, # Eternal Descent
    909036012, # Swaggy Dance
    909036014, # Admire
    909037001, # Reindeer Float
    909037002, # Bamboo Dance
    909037003, # Dance of Constellation
    909037004, # Trophy Grab
    909037005, # Starry Hands
    909037006, # Yum
    909037007, # Happy Dancing
    909037008, # Juggle
    909037009, # Neon Sign
    909037010, # Beast Tease
    909037012, # Clap Dance
    909038001, # The Influencer
    909038002, # Name Not Found
    909038003, # Techno Blast
    909038004, # Be My Valentine
    909038005, # Angry Walk
    909038006, # Make Some Noise
    909038008, # Croco Hooray
    909038009, # Scorpio Spin
    909038011, # Shall We Dance?
    909038013, # Spin Master
    909039001, # Festival Celebration
    909039002, # Artistic Musical
    909039003, # Forward Backward
    909039004, # Scorpion Friend
    909039005, # Aching Power
    909039006, # Earthly Force
    909039007, # Grenade Magic
    909039008, # Oh Yeah!
    909039009, # Grace On Wheels
    909039010, # Flex
    909039011, # Crimson Doom
    909039012, # Fire Beast Tamer
    909039013, # Crimson Tunes
    909039014, # Swaggy V-Steps
    909040001, # The Chromatic Finish
    909040002, # Smash the Feather
    909040003, # Sonorous Steps
    909040004, # Fishing for Wisdom
    909040005, # Chromatic Pop Dance
    909040006, # Chroma Twist Twist
    909040008, # Birth of Justice
    909040009, # Spider-Sense
    909040011, # Play With Thunderbolt
    909040012, # 6th Anniversary
    909040013, # Wisdom Swing
    909040014, # Helicopter Shot
    909041001, # Thunder Breathing
    909041002, # Water Breathing
    909041003, # Beast Breathing
    909041004, # Flying Ink Sword
    909041005, # Diz My Popblaster (Groza)
    909041006, # Dance Puppet
    909041007, # High Knees
    909041008, # Bony Fumes
    909041009, # Feel the Electricity
    909041010, # Whac-A-Cotton
    909041011, # Honorable Mention
    909041012, # BR-Ranked Grandmaster
    909041013, # CS-Ranked Grandmaster
    909041014, # Monster Clubbing
    909041015, # Basudara Dance
    909042001, # Stir-Fry Frostfire
    909042002, # Money Rain
    909042003, # Frostfire's Calling
    909042004, # Stomping Foot
    909042005, # This Way
    909042006, # Excellent Service
    909042009, # Celebration Schuss
    909042011, # Dawn Voyage
    909042012, # Lamborghini Ride
    909042013, # Hello! Frostfire
    909042016, # Hand Grooves
    909042017, # Free Fire Toiletman
    909042018, # Kemusan
    909043001, # Ribbit Rider
    909043002, # Inner Self Mastery
    909043003, # Emperor's Treasure
    909043004, # Why So Chaos?
    909043005, # Huge Feast
    909043006, # Color Burst
    909043007, # Dragon Swipe
    909043008, # Samba
    909043009, # Speed Summon
    909043010, # What a Match
    909043013, # What a Pair
    909044001, # Byte Mounting
    909044002, # The Unicyclist
    909044003, # Basket Rafting
    909044004, # Happy Lamb
    909044005, # Paradox of Enlighten
    909044006, # Harmonious Paradox
    909044007, # Raise Your Thumb!
    909044015, # The Final Paradox
    909044016, # Honk Up!
    909045002, # Spring Rocker
    909045003, # Giddy Up!
    909045004, # The Goosy Dance
    909045005, # Captain Victor
    909045010, # A Flower Salute
    909045011, # Little Foxy Run
    909045012, # Mr. Waggor's Seesaw
    909045015, # Floating Meditation
    909045016, # Naatu Naatu
    909045017, # Champion's Walk
    909046001, # Aura Boarder
    909046002, # Whos the Booyah
    909046003, # Controlled Combustion
    909046004, # Cheers to Victory!
    909046005, # Shoe Shining
    909046006, # Gunspinning
    909046007, # Crowd Pleaser
    909046008, # No Sweat
    909046009, # Magma Quake
    909046010, # Max Firepower
    909046011, # Can't Touch This
    909046012, # Firestarter
    909046013, # FFWS Flag Flair
    909046014, # Beat Drop
    909046015, # Isagi's Spatial
    909046016, # Nagi's Trapping
    909046017, # Soaring Up
    909047001, # I Want Bow Down
    909047002, # Aurora Iridescence
    909047003, # Couch For Two
    909047004, # Flutter Dash
    909047005, # Slippery Throne
    909047006, # Acceptance Speech
    909047007, # Love Me, Love Me Not
    909047008, # Scissor Savvy
    909047009, # The Thinker
    909047012, # JKT48 No!
    909048001, # To the Rescue
    909048002, # Midnight Peruse
    909048003, # Guitar Groove
    909048004, # Keyboard Player
    909048005, # On Drums
    909048006, # Chac Chac
    909048007, # Pillow Fight
    909048009, # Goofy Camel
    909048010, # Hit a Six!
    909048011, # Flag Summon
    909048014, # Slurp slurp!
    909048015, # Sketching
    909048016, # Half-Time Chilling
    909048017, # Throw-In
    909049001, # Nailong Time!
    909049002, # Hand Raise
    909049003, # Kick It Up
    909049006, # Creation Days
    909049007, # Raining Coins
    909049008, # Clap Clap Hooray
    909049009, # Infinite Loops
    909049011, # Boxing Machine
    909049013, # Comic Barf
    909049016, # Spear Spin
    909049017, # Flag Wave
    909049018, # Disco Dazzle
    909050002, # Reanimation Jutsu
    909050003, # The Final Battle
    909050005, # Fire Style Fireball
    909050006, # Flying Raijin
    909050008, # Hammer Slam
    909050009, # The Rings
    909050010, # Drum Twirl
    909050011, # Bunny Action
    909050012, # Broom Swoosh
    909050013, # Blade from Heart
    909050017, # Bunny Wiggle
    909050018, # Flaming Heart
    909050019, # Rain or Shine
    909050020, # Sholay
    909050021, # Peak Points
    909050027, # Boat Race Aura
    909050028, # Boat Race Rowing
    909051001, # Prismatic Flight
    909051002, # Name Not Found (Dream)
    909051004, # Shower Time
    909051010, # On Motorbike
    909051012, # Celestial Shot (Bow)
    909051013, # Red Petals
]

# 3. MASTER LIST (SEQUENTIAL FOR /ALL COMMAND)
# Logic: Pehle Evo list khatam hogi, phir Normal list start hogi
ALL_IDS = EVO_IDS + NORMAL_IDS

# --- MAIN LOOP FUNCTION ---
async def start_loop(mode, key, iv, region, whisper_writer, online_writer):
    global is_running
    is_running = True
    
    # Mode Selection
    if mode == 'evo':
        target_list = EVO_IDS
    elif mode == 'all':
        # ALL means: Evo First -> Then Normal (Ordered)
        target_list = ALL_IDS
    elif mode == 'mix':
        # Mix means: All IDs shuffled randomly
        target_list = list(ALL_IDS)
        random.shuffle(target_list)
    else:
        target_list = ALL_IDS

    print(f"VIP Loop Started: {mode} with {len(target_list)} emotes")
    print(f"Targeting SQUAD: {VIP_ADMINS}") 
    
    while is_running:
        for emote_id in target_list:
            if not is_running: break
            try:
                # --- SQUAD SPAM LOGIC ---
                packets = []
                for admin_uid in VIP_ADMINS:
                    # Har admin ke liye packet banao
                    # Agar UID placeholder hai to skip karo, error se bachne ke liye
                    if "YAHAN_DALO" in str(admin_uid): 
                        continue
                        
                    pkt = await Emote_k(int(admin_uid), int(emote_id), key, iv, region)
                    packets.append(pkt)

                # Sabko packet bhejo
                for p in packets:
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', p)
                
                # Gap between emotes
                await asyncio.sleep(DELAY)
                
            except Exception as e:
                print(f"VIP Error: {e}")
                await asyncio.sleep(0.5)
        
        # Agar Mix mode hai to list dobara shuffle karo
        if mode == 'mix':
            random.shuffle(target_list)

# --- COMMAND HANDLER ---
async def handle_vip_command(msg, uid, key, iv, region, whisper_writer, online_writer):
    global is_running, current_task
    
    # 1. SECURITY CHECK (UID verification)
    # Check if uid is in list (String match)
    if str(uid) not in VIP_ADMINS:
        return "❌ Access Denied! Sirf VIP Admins use kar sakte hain."

    # 2. Stop Command
    if msg == '/stop all':
        if is_running:
            is_running = False
            if current_task: current_task.cancel()
            return "🛑 Stopped! Squad Emote Spam band kar diya."
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
        count = len(ALL_IDS)
    
    if mode:
        # Purana task roko
        if is_running:
            is_running = False
            if current_task: current_task.cancel()
            await asyncio.sleep(0.5)

        # Naya task shuru
        current_task = asyncio.create_task(
            start_loop(mode, key, iv, region, whisper_writer, online_writer)
        )
        # Message Return
        mode_text = "EVO ONLY" if mode == 'evo' else "FULL SEQUENCE (Evo->Normal)" if mode == 'all' else "RANDOM MIX"
        return f"✅ Started {mode_text} Mode!\nTotal Emotes: {count}\nTargets: All VIP Admins"
    
    return None
                    
