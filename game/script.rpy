define b = Character("Beyoncé")
define m = Character("Michelle")
define k = Character("Kelly")
define j = Character("JAY-Z")
define bl = Character("Blue Ivy")
define dc = Character("Destiny's Child")
define Chika = Character("Deluluhive person 1")
define Pearl = Character("Deluluhive person 2")

image b1 = "images/bey1.png"
image b2 = "images/bey2.png"
image beymad = "images/beymad.png"
image deluluhive = Transform("images/deluluhive.jpg", xysize=(1920, 1080))
image Chika = Transform("images/Chika.png", xysize=(720, 600))
image Pearl = Transform("images/me.png", xysize=(720, 600))
image skitrip = Transform("images/skitrip.jpg", xysize=(1920, 1080))
image hotel = Transform("images/hotel.jpg", xysize=(1920, 1080))
image kelly = Transform("images/kelly.png", xysize=(720, 600))
image m = Transform("images/michelle.jpg", xysize=(720, 600))



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
    show b1
    b "This is so much fun! I looove hanging out with my girls."

    scene skitrip
    show beymad
    b "I probably should hit the studio, haven't been there in like 2 years lol. The beyhive is buzzin tho."
    b "They be making crazy theories too, too bad they will never guess my plans."

    scene skitrip
    show m
    m "Gurl you tease 'em too much"

    scene skitrip
    show beymad
    b "Girl you know nobody can predict me, AND they still play too much."
    b "They still won't forget about the bangs."

menu:
    
    "Destiny's child goes to their hotel.":
        jump hotel

label hotel: 
    scene hotel
    show k

k "WAIT! I have an idea.."
k "How about we make a remake of the 8 days of Christmas album for its' 25th anniversary?"
k "The comeback would be crazy"

menu:
    
    "Everybody agrees":
        jump agree

    "They don't think it's a great idea":
        jump disagree


label agree:

scene hotel
show b2

b "That might be a good idea, but we gotta lay LOW and I mean LOW cause the beyhive finds out anything."

scene hotel
show m 

m ""





