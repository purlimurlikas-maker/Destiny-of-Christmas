define b = Character("Beyoncé")
define m = Character("Michelle")
define k = Character("Kelly")
define j = Character("JAY-Z")
define bl = Character("Blue Ivy")
define dc = Character("Destiny's Child")
define Chika = Character("Deluluhive person 1")
define Pearl = Character("Deluluhive person 2")
define r = Character("Rihanna")

image b1 = "images/bey1.png"
image b2 = "images/bey2.png"
image beymad = "images/beymad.png"
image deluluhive = Transform("images/deluluhive.jpg", xysize=(1920, 1080))
image Chika = Transform("images/Chika.png", xysize=(720, 600))
image Pearl = Transform("images/me.png", xysize=(720, 600))
image skitrip = Transform("images/skitrip.jpg", xysize=(1920, 1080))
image hotel = Transform("images/hotel.jpg", xysize=(1920, 1080))
image k = Transform("images/k.png", xysize=(720, 600))
image m = Transform("images/m.png", xysize=(720, 600))
image call1 = Transform("images/call1.png", xysize=(720, 600))
image call2 = Transform("images/call2.png", xysize=(720, 600))



label start:

    
    scene deluluhive
    show Chika
    Chika "Oh my gosh, I think I have a theory about Bey."

    scene deluluhive
    show Pearl
    Pearl "let's hear it."

    scene deluluhive
    show Chika
    Chika "Okay so yk how she hasn't announced act III yet?"

    scene deluluhive
    show Pearl
    Pearl "Yuh?"
    Pearl "What about it?"

    scene deluluhive
    show Chika
    Chika "Sooo.. basically maybe she's planning on releasing a co-album with Jay?"

    scene deluluhive
    show Pearl
    Pearl "Uhh idk bout that cause Beyhive can't behave so maybe we're just getting the album in like 2030?"

    menu:
        "See what Beyoncé is doing":
            jump beyonce

label beyonce:

     
    scene skitrip
    "Meanwhile Beyoncé"
    show b1
    b "This is so much fun! I looove hanging out with my girls."

    scene skitrip 
    show m
    m "Ikr? feels just like the old times."

    scene skitrip
    show k
    k "Yuhhh"

    scene skitrip
    show beymad
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

        "Jay-Z cheated and beyoncé is moving to Paris with her chidren (again)":
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
    return

    

    