define b = Character("Beyoncé")
define m = Character("Michelle")
define k = Character("Kelly")
define j = Character("JAY-Z")
define blue = Character("Blue Ivy")
define dc = Character("Destiny's Child")
define Chika = Character("Deluluhive person 1")
define Pearl = Character("Deluluhive person 2")
define r = Character("Rihanna")

image b1 = Transform("images/bey1.png", xysize=(600, 700))
image b2 = Transform("images/bey2.png", xysize=(600, 700))
image beymad = Transform("images/beymad.png", xysize=(600, 700))
image beysnow = Transform("images/beysnow.png", xysize=(600, 700))
image m2 = Transform("images/m2.png", xysize=(600, 700))
image k2 = Transform("images/k2.png", xysize=(600, 700))
image deluluhive = Transform("images/deluluhive.jpg", xysize=(1920, 1080))
image Chika = Transform("images/Chika.png", xysize=(600, 700))
image Pearl = Transform("images/me.png", xysize=(600, 700))
image skitrip = Transform("images/skitrip.jpg", xysize=(1920, 1080))
image hotel = Transform("images/hotel.jpg", xysize=(1920, 1080))
image k = Transform("images/k.png", xysize=(600, 700))
image m = Transform("images/m.png", xysize=(600, 700))
image call1 = Transform("images/call1.png", xysize=(600, 700))
image call2 = Transform("images/call2.png", xysize=(600, 700))
image room = Transform("images/room.jpg", xysize=(1920, 1080))
image studio = Transform("images/studio.jpg", xysize=(1920, 1080))
image computer = Transform("images/beyandhercomputer.png", xysize=(700, 700))
image r = Transform("images/rihanna.png", xysize=(700, 700))
image sb = Transform("images/Spongebob1.jpg", xysize=(1920, 1080))
image ri = Transform("images/riri.png", xysize=(600, 700))

label start:


    scene skitrip
    show b1
    b "This is so much fun! I looove hanging out with my girls."
    b "Ski trips are soooo fun"

    scene skitrip 
    show m
    m "Ikr? feels just like the old times."

    scene skitrip
    show k
    k "Yuhhh"

    scene skitrip
    show m
    m "Okay y'all it's FREEZING outside (ahem ahem, emphasis on freezing) we should probably go inside..."

    menu :
        "Go inside":
            jump inside
        "Stay in the cold":
            jump outside
        
label outside:
    scene skitrip
    show b2
    b "This is so fun"
    b "Maybe we should stay here for a couple of years?"
    b "Okay, we're pushing act III to 2028.."
    return
    

label inside:
    scene hotel
    show k2 
    k "I haven't gotten to chill like this in a while"
    
    scene hotel
    show beymad
    b "You guys I sorta just thought a bit about sth"
    b "I probably should hit the studio, haven't been there in like 2 years lol. The beyhive is buzzin tho."
    b "They be making crazy theories too, too bad they will never guess my plans."

    menu:
        "Beyoncé is making an album with Jay-Z":
            jump album

        "Beyoncé is releasing more merch":
            jump merch

        "Beyoncé is releasing act III (you wish)":
            jump actIII

        "Destiny's Child is reuniting":
            jump reunion

        "Jay-Z cheated and beyoncé is moving to Paris with her children (again)":
            jump paris

label album:
    scene hotel
    
    "Wrong guess, she will NOT be making an album with Jay."
    jump doing

label merch:
    "Correct! She will be giving us more merch."
    jump doing

label actIII:
    "You wish!"
    jump doing

label reunion:
    "Maybe?"
    jump doing

label paris:
    "Nah, he's scared of Solange."
    jump doing


label doing:
    b "They will never guess this. Okay they actually might."
    b "I'm making a co-album with Rihanna."
    
    menu:
        "Call Rihanna":
            jump Rihanna

        "Quit cause you don't want an album with Rihanna":
            return

label Rihanna:
    scene hotel
    show call1
    b "Heyyy, Rihanna, how are you??"

    scene room
    show r
    r "Heyyy, I'm good, why are you ringing me?"

    scene hotel
    show call1
    "RING THE ALARM"
    b "Sooo, I was thinking, could we make an album together?"
    b "I can fly over to the studio rn"

    scene room
    show r
    r "I mean I'm definitely down, we can meet up at the studio, lmk when you're near there"

    menu:
        "Fly to the studio.":
            jump studio

label studio:
    
    scene studio
    show computer
    b " I cooked up some lyrics here and I have an idea for the beat too"

    scene studio
    show r
    r "Let me see"
    "a couple minutes later"
    r "Bey, this is greattt, now we just need to make like 15 more songs so we'd have variety to choose from."

    scene sb
    "..."

    scene studio
    show ri

    r "Okay, seems like we're done with recording these songs, these are fire."

    scene studio
    show b2 

    b "Yessss, what should we name these?"

    scene studio
    show riri
    
    ri "uhh let me see"
    ri "the first one could be FREEZE TIME"
    ri "the second could be BREATHE AGAIN and so on"

    scene studio
    show b2

    b "Yeah, we'll figure sth out"
    b "What about the album? It's kinda RnB, Pop and yeah a combination of everything."

    menu:
        "A FEELING":
            jump name

        "EVERYTHING":
            jump name

        "FROZEN IN TIME":
            jump name

        "STILL GOT LOVE":
            jump name

        "PERMANENT":
            jump name


label name:
    scene studio
    show ri

    r "Yesss, girl this is gooood, we still have music videos to film, but when should we announce it? Or are we gonna release it without any notice, like you did with Self-Titled?"

    scene studio
    show b2

    b "hold on, let me check what my manager recommends"












    