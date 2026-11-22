define b = Character("Beyoncé")
define m = Character("Michelle")
define k = Character("Kelly")
define j = Character("JAY-Z")
define bl = Character("Blue Ivy")
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
    show




    