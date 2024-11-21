import streamlit as st
import time

# Set page configuration
st.set_page_config(
    page_title="Happy Birthday!",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's default menu and footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles.css")

def celebration_animation():
    # Display the GIF
    st.image("images/confetti-style.gif", width = 1500)
    # Overlay the 'Happy Birthday!' text using negative margin
    st.markdown(
        """
        <div style='text-align: center; margin-top: -550px;'>
            <h1 style='font-size: 96px; color: #ff69b4;'>Happy 20th Birthday, Pookie!</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

def main_content():
    # Display an audio player for the background music
    st.markdown("<h2 style='text-align: center;'>PLAY ME</h2>", unsafe_allow_html=True)
    audio_file = open('audio/background.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes)

    # List of sections with text and optional images/videos
    sections = [
        {
            'text': "Hey Pumpkin Pie,\n\nYAY HAPPY HAPPY BIRTHDAY TO YOUUU, right now, you should be livin' it up in Rome babyyy~ "
                    "I really hope you're having a blast and enjoying your holidays with your friends cause you truly deserve it. "
                    "I love you so much and with all my heart~ I still can't believe we've been together for 2 whole years, it's really "
                    "been an absolutely crazy ride. I've seen you grow more and more independent every day and I'm so proud of what you've "
                    "accomplished over the years~ From ace-ing your studies to being a pro netballer to being an amazingly supportive and loving "
                    "daughter, 'big sister' to your cousins, and loving girlfriend to me. I don't deserve you because you're always "
                    "so naturally sweet to everyone and you're so loving to my family <3 Anyways, I really hope you like this "
                    "token of appreciation I made. It took me a lot of trial and error (and ChatGPT......) to get it up so "
                    "I really hope you like it~ P.S. I tried making it more funny but it was so difficult to get it like how I envisioned... "
                    "Also, some of the pictures will be upside down for some reason... so maybe that can be a future project hehe, "
                    "here's to many more birthdays, events, anniversaries and happiness together~ I've complied a bunch of our mmrs "
                    "and moments of the past year(ish) together here, hope you enjoy it my princess ^_^\n\n",
        },
        {
            'text': '<br><br><br><br>Always bullying me while I sleeping bodoh, then I do you always go "OIII" or "EHHH" or "DELETE!" -,- (ily)',
            'image': 'images/always_sleeping2.jpg',
            'align': 'left'
        },
        {
            'text': '<br><br><br><br>Part 2, round 2, I miss sleeping on your shoulder T_T please can I sleep more ard you <3',
            'video': 'videos/always_sleeping.MOV',
            'align': 'right'
        },
        {
            'text': '<br><br><br>YAY our cookings, dabaoings and dapperings moments~ I MISS IT SO MUCH, the cheap food was so fking gooooood, '
                    'I am sure mrs worldwide finland kia (aka you) can relate Xd',
            'image': 'images/dapper_food.jpg',
            'align': 'left'
        },
        {
            'text': '<br><br><br>Another diaper moment hehe, he got so excited that day on our first time in the first SG pet-friendly mall <3 '
                    'I still cant believe bro pooped on the floor T_T but I miss himmmm~ lets go again when we both back, okkkk!!',
            'image': 'images/dapper_poop_on_floor.jpg',
            'align': 'right'
        },
        {
            'text': '<br><br><br><br><br><br><br><br><br>HELP do you remember THIS!!!! It was so fking funny I swear HAHAHAH why you so goofy T_T but yea your bro ah... '
                    'LMAO I think we gonna be flaming him and how smelly and dirty his shit is for life XD',
            'video': 'videos/smelly_bro_clothes.MOV',
            'align': 'left'
        },
        {
            'text': '<br><br><br><br>This day was so nice ^_^ we walked like 15k steps or sth but I think it was a really nice date hehe, I love nature '
                    'moments~ lets try to do something like this again soon when we get back ya :D',
            'image': 'images/flower_dome.jpg',
            'align': 'right'
        },
        {
            'text': '<br><br><br><br>You look so pretty here my princess, I miss kissing you D: the flowers bring out the shine in your eyes shawty ;)',
            'image': 'images/gbtb.jpg',
            'align': 'left'
        },
        {
            'text': '<br><br><br><br><br><br><br><br>GAHHHH just watching this video again reminds me of how carefree we were on that day~ '
                    'but it really was a "first" test to our parenthood LOL #babysitting Xd but I loved every second of it, it was superrrr fun :>',
            'video': 'videos/zoo_trampoline.MOV',
            'align': 'right'
        },
        {
            'text': '<br><br><br>You and your family treat me so well darling, really like my second family :") thank you for planning out '
                    'such a cute celebration for me, I dont deserve this T_T I love you baby~',
            'image': 'images/my_bday.jpg',
            'align': 'left'
        },
        {
            'text': '<br><br><br>Here again you always going out your way to spend time wimme or else I solo makan owo~ thanks for being '
                    'there for me after tiring grab shifts, my ass always pain then you help me massage hehe, now can I massage '
                    'your ankles :P',
            'image': 'images/simpang_feast_aft_grab.jpg',
            'align': 'right'
        },
        {
            'text': '<br><br><br>LOL Helium moment, I think the balloons are still inflated til now XD thanks for the birthday balloons hehe',
            'video': 'videos/helium.MOV',
            'align': 'left'
        },
        {
            'text': '<br>WOAH pro player alert! You deserve every flower that gets given to you pookie dookie ^_^ Im so happy '
                    'I still got to see you play your matches <3 Hopefully there will be more when you join back the team then '
                    'I can be there holding up pom poms and cheerleading HEHEHEHA',
            'image': 'images/pro_player_happycanstillseeuplay.jpg',
            'align': 'right'
        },
        {
            'text': '<br><br>#foreheadreveal XD do you remember I let you use my grandpas shoes then something like 2 or 3 pairs broke '
                    'T_T so fking funny bruh HAHAHAH this was our first ever run together I think, lets try to do it more and '
                    'gym more when we get home hehe #healthgurulife',
            'image': 'images/run_shoe_broke_3times.jpg',
            'align': 'left'
        },
        {
            'text': '<br><br>Im SOOOO happy we went for this, even though the place was a bit run down, but it was our way of getting '
                    '"snow" during winter time hehe, then soon we gna be in REAL snow place (i know you alr experienced, BUT '
                    'this time we will be tgt :D) I CANT WAIT AHHHHHH',
            'video': 'videos/snow_time.mp4',
            'align': 'right'
        },
        {
            'text': '<br><br><br>Your hair smell good :o) I miss our Christmas timez~ #frequentSuntecGoers I CANT WAIT FOR OUR EUROPE TRIP '
                    'UIASHDIUASHDASHDIUH now lets make out under the mistletoe',
            'image': 'images/xmas~.jpg',
            'align': 'left'
        },
        {
            'text': '<br><br>Yay MBS, I cant rly rmb if we had wings but I miss the wings bruh LOL rly obsessed fr... but yay we managed to '
                    'catch the national day fireworks~ next time as a family with our goldie, ginger cat, and boy and girl, lets vow '
                    'to always try to catch the fireworks on national day okie, its the lil things in life ^_^',
            'image': 'images/national_day.jpg',
            'align': 'right'
        },
        {
            'text': '<br>*sobbing at sparks* but OMG YAY our first ever concert together <3 and I cant believe it was Coldplay, '
                    'truly a bucket list checked off moment :D it was such an amazing time and thanks for agreeing to have '
                    'my friends stand together with us that day~ I sometimes just think back to this day when I listen to Coldplay tbh',
            'video': 'videos/coldplay!.MOV',
            'align': 'left'
        },
        {
            'text': '<br><br>TBH we rly spend a lot of time at this table LOL and I think we gna spend a lot of January here again HAHAHAH I will '
                    'be staying at the 786F Woodlands AirBnb once again XD gahhhh then sleep all day and rotting and NO WE WILL GYM OK!',
            'image': 'images/together_minion_drink.jpeg',
            'align': 'right'
        },
        {
            'text': '<br><br><br>Thank you for introducing me to photobooth moments, it really brightens my day everytime I see your photos that I '
                    'pin up on my shelves :> I dont feel so stressed about my work and everything in life when I see our photos tgt <3',
            'image': 'images/photo_booth_no.999_iloveit.jpg',
            'align': 'left'
        },
        {
            'text': '<br><br><br><br><br><br><br><br>KATA ROCKS BABY~ I still rmb the vibes were absolutely immaculate, food was amazing and the guy playing the guitar '
                    'was so cool and chill too hehe no regrettis wld come back again~ maybe when we loaded we come back and actl stay ya '
                    'HEHEHEHA',
            'video': 'videos/date_night_golf_cart.MOV',
            'align': 'right'
        },
        {
            'text': '<br><br>You were so sweet to bring me here, I cant believe I didnt suspect anything, I rly dk if its like gullible or what '
                    'LMAO, but I had such an amazing time here and we made beautiful crafts~ can we do that romcom scene where we play '
                    'with the pottery together on the spinning stone and our hands touch then we start making out XDXDXDXDXDDXDXDD',
            'image': 'images/pottery.jpg',
            'align': 'left'
        },
        {
            'text': '<br><br><br>When my parents were overseas XD I miss doing maskings with you darling <3 I remember I made you into avatar aang LOL '
                    'but awww I wna do it again right nowwww gahhh I miss you qtpie T_T you look so cute here somemore',
            'image': 'images/masking_while_parentsout.jpg',
            'align': 'right'
        },
        {
            'text': '<br><br><br><br><br><br><br><br>"I take video so nice for youuuu then my one come out like that" SORRY LAH LOL I AINT NO VIDEOGRAPHER, but anyways '
                    'it really was a vibe taking motorbikes around in Phuket hehe~ we had so much fun on this trippy :o)',
            'video': 'videos/first_motorbike(yourvidbtr).MOV',
            'align': 'left'
        },
        {
            'text': '<br><br><br><br><br>Our first ever ATV ride together yay, it was short but sweet, I think quite worth hehe, I lowk regret not '
                    'bringing you to the gun range tho, I think it would have been pretty crazy then you can live out your real '
                    'life valorant flick head shot moment XD But nonetheless, it was a fun experience <3 I miss the tiny cat we '
                    'saw after we finished the ATV huehue',
            'image': 'images/first_atv.jpg',
            'align': 'right'
        },
        {
            'text': '<br><br><br><br><br>Another first together yeehaw, funny ah ah nights I swear, cant believe we threw everything out LOL',
            'image': 'images/good_stuff_shh.jpg',
            'align': 'left'
        },
        {
            'text': '<br>Do you remember the kids wore their court shoes here then keep complaining T_T really is so funny HAHAH '
                    'but a family moment indeed hehe it was so fun to go to the great outdoors together and be one with NATURE '
                    'lets do early morning hikes like this again dodo ^_^ OMG AND the bak kut teh afterwards was so fking gooooood '
                    'god damn its so late here rn and Im craving it......',
            'video': 'videos/macritchie.mp4',
            'align': 'right'
        },
        {
            'text': '<br><br><br><br><br><br>Im sorry for almost drowning you T_T I think I just needed to be confident but jeez the waves were crazy that '
                    'day HAHAHAH thank god we dont need pay with our kidney or sth cus the water got into the jetski or wtv '
                    'but this really was a CRAZY experience, together with the para gliding, omgggg I miss it sm~',
            'image': 'images/jetski_almost_drowned.jpg',
            'align': 'left'
        },
        {
            'text': '<br><br>LOOK AT HOW EXHAUSTED WE LOOK LMFAO literally can fall asleep on the floating platform but the fishies were '
                    'so cute and so fun to swim in the open sea hehe~ Im glad we decided to go down cus god knows we rly wanted '
                    'to just stay on deck and bing chilling LOL 8/10 adventure~',
            'image': 'images/snorkling_exhausted.jpg',
            'align': 'right'
        },
        {
            'text': '<br><br><br><br>Me wanting to bonk your head with this bowling ballz but yay throwback to that day when we bought so much food '
                    'back to the villas, truly a feasting and drinking moment, was a fun time hehe <3',
            'image': 'images/bowling.jpg',
            'align': 'left'
        },
        {
            'text': '<br><br><br><br><br><br><br><br><br>Your obsession with looking at old couples hehe "is that gna be us next time?" yes it is darling, I promise '
                    'you that I wont give up on us and I will grow old with you my baby girl, you mean the world to me and I will '
                    'continue to be #patient #loyal #loving #kind to you for our future <3',
            'video': 'videos/our_future_old_ppl.MOV',
            'align': 'right'
        },
        {
            'text': '<br><br>You are my home, my rock, my seasons, my sky, my heart, my soul, my person. You remind me of everything this life '
                    'has to offer and you are the reason I want to get up every morning. I want to be with you for life my darling, you '
                    'are my everything and more. They say that there are people that are just the journey, but I see you as the destination. '
                    'I promise to always provide you with whatever I have, be it Muffin Mondays, Wasabi Mayo Prawns or those Harvest Viennese '
                    'Vanilla Sable Butter Cookies :P Happy 20th Birthday my princess, I love you <3',
            'image': 'images/macbook_selfie_dapper.jpg',
            'align': 'left'
        }
    ]

    # Create a container for scrollable content
    with st.container():
        for section in sections:
            if 'image' in section or 'video' in section:
                if section['align'] == 'left':
                    col1, col2 = st.columns([1, 1])
                    with col1:
                        if 'image' in section:
                            st.image(section['image'], use_container_width=True)
                        elif 'video' in section:
                            video_file = open(section['video'], 'rb')
                            video_bytes = video_file.read()
                            st.video(video_bytes)
                    with col2:
                        st.markdown(f"<p style='font-size: 28px; line-height: 1.6;'>{section['text']}</p>", unsafe_allow_html=True)
                elif section['align'] == 'right':
                    col1, col2 = st.columns([1, 1])
                    with col1:
                        st.markdown(f"<p style='font-size: 28px; line-height: 1.6;'>{section['text']}</p>", unsafe_allow_html=True)
                    with col2:
                        if 'image' in section:
                            st.image(section['image'], use_container_width=True)
                        elif 'video' in section:
                            video_file = open(section['video'], 'rb')
                            video_bytes = video_file.read()
                            st.video(video_bytes)
            else:
                st.markdown(f"<p style='font-size: 28px; line-height: 1.6;'>{section['text']}</p>", unsafe_allow_html=True)

def run_sequence():
    # Display the celebration animation with overlaid text
    placeholder = st.empty()
    with placeholder.container():
        celebration_animation()
    # Wait for 5 seconds
    time.sleep(5)
    # Clear the placeholder
    placeholder.empty()

    # Main Content with fade-in effect
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    main_content()
    st.markdown("</div>", unsafe_allow_html=True)

def main():
        run_sequence()

if __name__ == "__main__":
    main()
