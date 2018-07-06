﻿label day10:

show y n

y n "..."

hide black

y h "Hey, we're fine."

y n "Neat."

y h "Thanks for the quick decision Cap."

show p h

p h "W-wow... "

show r su

r su "Ooof..."

r s "I'm gonna be sick..."

r s "Why me?"

show y m

y m "We're alive dude, be thankful."

show p n

p n "She's right Hei... "

p n "We're lucky, {w=0.15}there was no telling what was going to happen."

show r n

r n "Lucky."

show y n

y n "Yeah..."

show r m

r m "No, {w=0.15}this wasn't mere luck..."

show p n

p n "You don't think so, Hei?"

show r n

r n "No... "

r h "This was me."

r h "I must be good luck,{w=0.15} huh Haru-baru?"

show y m

y m "..."

y n "I won't lie."

y h "Guy did surprisingly well."

show r su

r su "What?"

show p su

p su "Are you talking about Hei?"

show y m

y m "Yes. Hei."

y h "Ya came up with a plan of action quickly."

y h "I'm proud, {w=0.15}ya did awesome dude."

show y n

y n "Maybe I underestimated you?"

show r h

r h "Hell yeah baby! "

r h "Daddy's beeh here all along baby-girl, {w=0.15}come sit on my lap and I'll tell you a story."

show y n

y n "..."

show r n

r n "Uh."

show p n

p n "..."

show y n

y n "I'll ignore what you just said. "

y n "That is my thanks."

y n "Now let's figure out where we stand."

e "Haruka presses a few keys on her computer."

show y su

y su "Weird..."

menu:
    "What is it?":
        pass

    "Forgot your password?":
        pass

y n "Cap, my station isn't reacting..."

y n "Seems like it's in low power mode..."

show p su

p su "Mine too!"

show r s

r s "Shit shit shit."

r s "Mine too."

show y n

y n "One sec."

e "Haruka walks over to the wall and removes a panel."

y n "I'm going to divert a little of our emergency energy to my computer."

e "She flips a small switch and her monitor turns on."

y h "There we go."

y n "So let's see..."

show p n

p n "Can you see what the problem may be, {w=0.15}Haruka?"

show y n

y n "Yeah.{w=0.15}.{w=0.15}. "

y n "No big deal!"

show r h

r h "Hoo, {w=0.15}really? Nice."

show y n

y n "One of power sources is dead since we made that emergency compund."

show r su

r su "That sounds...{w=0.15} pretty bad."

show p su

p su "What does that mean for us Haruka?"

show y n

y n "Well for one,{w=0.15} it means that life support systems aren't working at full capacity. "

show r s

r s "We're dead already.{w=0.15} I knew it."

r s "I didn't even get a chance to form my harem."

show y m

y m "Oh shut up.{w=0.15} You'll be fine."

show y n

y n "There's a system in place for this."

menu:
    "Great!":
        pass

    "What system?":
        pass

y h "It is great!"

show p n

p n "What's the system Haruka?"

show y n

y n "Well basically, the starboard side of the ship will be shut down to conserve energy."

y n "Until the one power source recharges that is."

show r su

r su "Starboard!"

r n "Am I on the starboard side?"

show p n

p n "No Hei, starboard is the right side of the ship when facing the bow. "

show r n

r n "Bow..."

show p h

p h "The bow is the di-"

show y m

y m "Front."

y n "My room and Nema's room are dead for probably about two days."

show p su

p su "Oh my..."

show r su

r su "So that means..."

show r h

r h "Sharing rooms?"

r n "I call Haruka."

show y n

y n "I'm staying with Cap."

show r su

r su "What?!"

r n "Should we stick in same gender pairs?"

menu:
    "Didn't you just call Haruka as a roommate?":
        pass

    "I'm fine with it.":
        pass

r s "Whatever. "

show y h

y h "This will be fun."

e "Haruka pats you on the back."

show r m

r m "We'll have TONS of fun too."

r h "Right Nema?"

show p su

p su "Oh, right."

p h "We'll be staying together?"

p h "That will be fun, I agree Hei."

show r n

r n "Oh right, Haru."

r h "What happens if we go into one of the dead rooms?"

show y n

y n "Uh, don't do that."

show r n

r n "Why."

show y n

y n "There wont really be air?"

show r n

r n "Right."

r n "Well."

r h "Let's get going!"

r n "C'mon neebs,{w=0.15} sleepover!"

show p h

p h "Oh my, I've never been to a sleepover."

r h "Not like we'll get much sleeping done."

show y m

p su "Hei!"

y m "Come on, idiot."

r h "Just sayin'."

p n "Are we safe to walk through the hallway, Haruka?"

show y n

y n "You are for now, but once you get into your room I'm locking us all up for the rest of the night."

y n "Stock up on food and whatever you'll need."

y n "We'll have a meeting once one day is up and see where we stand then."

show r n

r n "Sounds good, smell ya later chumps."

e "Hei starts to walk out the door."

show p s

p s "Chumps?"

show r h

r h "Not you Nebs,{w=0.15} c'mon."

show p h

p h "Ah.{w=0.15} Of course."

hide p

hide r

play sound "sounds/DoorOpen2.mp3"

e "Nema and Hei trot out into the hallway."

show y n

y n "I'll grab some food and meet you in your room, 'kay?"

menu:
    "Sounds good!":
        pass

    "I guess...":
        pass

y n "See ya in a few Cap."

hide y

play sound "sounds/DoorClose2.mp3"

call hall

e "You walk out into the hallway."

e "Nema and Hei seem to have already settled down in Hei's room."

play sound "sounds/DoorOpen2.mp3"

call blueRoom

hide y

e "Haruka enters the kitchen as you continue on into your room."

e "You lay on your bed to wait for Haruka and slowly drift off to sleep."

show black

return