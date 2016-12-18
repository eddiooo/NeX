## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

define e = Character('Eileen', color ="#f9c5c2")

image bgClassroom ="classroom.jpg"
image bgPark = "Park.jpg"
image bgCClassroom ="creepyClassroom.jpg"
image bgPHome = "PathHome.png"

image eHappy = "eileen happy.png"
image eVHappy = "Eileen vhappy.png"
image eConcerned ="Eileen concerned.png"


## The game starts here.

label start:

    ## Show a background. This uses a placeholder by default, but you can add a
    ## file (named either "bg room.png" or "bg room.jpg") to the images
    ## directory to show it.

    scene bgClassroom

    ## This shows a character sprite. A placeholder is used, but you can replace
    ## it by adding a file named "eileen happy.png" to the images directory.

    show eHappy

    ## These display lines of dialogue.

    "Hello, world."

    e "You've created a new Ren'Py game."
    
    show eVHappy

    e "Once you add a story, pictures, and music, you can release it to the world!"
    
    e "Now, take me somewhere?"
        
    menu:
            
        "Let's go outside!":
                
            jump Park
                
        "Let's go home!":
                
            jump Home
                
        "I'll surprise you!":
                
            jump cClassroom
                
label Park:
    
    
    scene bgPark
    with dissolve
    
    show eVHappy
    with moveinleft
    
    e "Aww, this is a nice place!"
    
    e "I'll see you tomorrow!"

    return
    
label Home:
    
    scene bgPHome
    with dissolve
    
    show eVHappy
    with moveinright
    
    e "Thanks for walking me partway."
    
    e "I'll see you tomorrow!"
    
    return
    
label cClassroom:

    scene bgCClassroom
    with dissolve
    
    show eConcerned
    
    e "..."
    
    e "Why'd you take me here?"
    
    e "Jerk."
    
    $ renpy.play('punch.wav')
    with vpunch
    
    scene black
    with fade
    
    "You die."
    

    ## This ends the game.

    return
