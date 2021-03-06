﻿label day2:
    
hide black

e "You wake up to the quiet sound of the ship drifting through space."

e "The room is lit up by the mail notification on your computer screen."

menu:
    "Check mail.":
        pass

e "There's a faint sound of music coming from the hallway."

menu:
    "Check it out.":
        pass
        
call hall

play sound "sounds/DoorOpen2.mp3"

e "The music seems to be coming from the kitchen."

play sound "sounds/DoorOpen2.mp3"

menu:
    "Enter kitchen.":
        pass

call kitchen

e "You walk in to find Nema sitting at the table with a small music player."

e "She seems surprised to see you walk in, and quickly turns off her music."

stop music fadeout 1

show p s

p s "C-captain I apologize if my music bothered you. I tried to keep it at a reasonable volume but I'll be sure to use headphones from now on sir."

menu:
    "It didn't bother me at all.":
        pass

    "What were you listening to?":
        pass

p s "Well, I will be sure to continue being cautious."

p n "Anyways, I was just heading back to my room."

p n "Have a good morning captain."

menu:
    "Join me?":
        pass

    "Have a good morning, Nema.":
        pass

p s "No, I really should be back to work. Thank you though captain."

play sound "sounds/DoorClose2.mp3"

hide p

e "Nema bows slightly and walks out of the room."

e "You pour yourself a bowl of cereal and sit at the table to eat."

menu:
    "Turn on radio":
        pass

    "Eat in silence. (Cut to asking for anime)":
        pass

e "The radio starts to quietly play the music that Nema had been listening to."

e "A moment goes by as you continue to eat, and Haruka walks in."

show y h

y h "Morrrrnin'."

menu:
    "Good morning.":
        pass

    "Nod.":
        pass

y n "Listenin' to some tunes, yeah?"

e "Nema creeps back into the picture, just outside the room."

y n "This is that one band that was popular a few years ago right?"

y s "What was their name?"

menu:
    "Little Legs?":
        pass

    "Penguin Boys?":
        pass

y s "No..."

y n "Whatever."

y h "I was obsessed for a bit, this is a major throwback."

menu:
    "They do sound great.":
        pass

    "They sound terrible...":
        pass

y n "Really?"

y s "Can't say they've held up for me."

y h "I'm glad you're happy though cap."

e "Her voice is a little patronizing."

e "Nema blushes in the hallway and runs off."

y n "Anyways, was just heading back to my room."

y h "Wanna come and watch some anime with me?"

menu:
    "Yes.":
        pass
    "No.":
        pass


y m "Fine, I get it. Busy man."

hide y m

play sound "sounds/DoorOpen2.mp3"

e "Haruka walks over to her room."

e "You finish your food and walk out into the hallway."

call hall

play sound "sounds/DoorClose2.mp3"

e "YOU ARE NOW ABLE TO EXPLORE A LITTLE"

e "NAV ROOM CONTINUES MAIN STORYtodo"

e "HARUKAS ROOM"

call yellowRoom

show y hR

y h "Hey champ, came to visit me after all?"

y n "Quite the rebel aren't ya?"

menu:
    "Yes. Yes I am.":
        pass

    "Just checking in.":
        pass

y h "Very impressive, what a hero."

e "She smiles."

y n "Watch a little with me, I need a break."

e "You sit and look at the screen with her."

y n "He's gonna get wrecked."

y n "Just wait. Right here."

e "Somebody on the screen explodes."

y h "Boom!"

y h "God. I love this show."

e "Times passes.todo"

y n "And that's it. What'd ya think?"

menu:
    "Awesome.":
        pass

    "Pretty dumb.":
        pass

y h "Agreed."

y n "Mako's just too damn sexy. Do I have that kinda ass?"

y s "I don't think I do."

y su "Do I?"

y s "No."

e "She looks troubled."

y h "Well, I'll work on it."

y n "But, I'm gonna take a little nap."

y h "I'll talk to you in a bit Cap."

menu:
    "Exit the room.":
        hide y
        call hall
        pass

hide m2

e "NEMAS ROOM"

call pinkRoom

show p n

p n "Oh, good afternoon captain."

e "Nema smiles bashfully."

p h "Good timing, I was just about to come looking for you."

menu:
    "Whats up?":
        pass

    "How can I help you, Nema?":
        pass

p n "I just finished my report for my first day of findings. Would you mind going over it for me?"

menu:
    "Sure.":
        pass

    "No thanks.":
        pass

p h "Excellent!"

p n "It's sitting at the desk, feel free to look it over."

hide p

e "Nema grabs a small notebook and lays down on her bed."

menu:
    "Pick up the paper on Nema's desk.":
        pass

e "..."

e "...."

e "....."

e "The report basically just says \"no findings yet\" in a much more verbose way."

e "She's still absorbed in the notebook on her bed."

e "She doesn't appear to be paying attention."

e "One of the drawers is just barely open and you can make out some sort of object inside."

menu:
    "Don't snoop.":
        e "You decide to give her privacy."
        pass

    "Snoop it up!":
        pass

e "You take a moment to observe the room."

e "The room smells like a flower garden. Sort of earthy, but pleasant."

e "She has pencils and books lined up on her desk. "

e "One of her drawers is slightly open."

menu:
    "Report looks great. Good job.":
        pass

    "What's with the alchohol in your desk?":
        pass

p n "Thank you sir. I do my best."

p n "Anyways sir, I have a lot to attend to, and I don't want to keep you."

p n "Please have a wonderful day captain, and feel free to inform me of any way I can be of help."

call hall

e "You walk out her door into the hallway."

hide p

menu:
    "HEI ROOMtodo":
        call redRoom
        pass

show r h

r h "Hey dude. Wanna play?"

e "Hei is sitting in front of an old gaming system on the floor."

e "He motions his hand to the second controller."

menu:
    "Sure.":
        e "You pick up the controller and start playing with him."
        pass

    "No, just checking in.":
        pass

r n "I don't have the newest one, but Soft and Moist Vegetables: 2 Turbo Vegetable Edition is the best anyways."

r h "Best games ever made, if you ask me."

r n "Like, yeah, it's not a epic story with a huge budget and whatever."

r n "But you get to kick people in the face and I think it does that well."

menu:
    "You have tough standards.":
        pass

    "I do like face kicking.":
        pass

r h "I like what I like man."

r h "I used to play this all the time when I was a kid. My family had a maid, and she would bring her kid over on the weekends."

r n "I totally kicked his ass every time."

r m "He didn't even stand a chance against the MANGLER."

r n "I could have probably played pro."

menu:
    "Pro, huh?":
        pass

    "The Mangler. Right.":
        pass

r n "Yeah, I barely even played by myself. I was just that good."

r su "I tell you it ju-"

r n "..."

r su "Did you just beat me?"

menu:
    "Yes.":
        pass

    "What does it look like?":
        pass

r n "Well... Shit."

e "He's stopped functioning. "

e "He no longer appears to be breathing."

e "He's probably joking, but... it's getting weird."

menu:
    "I think... I'm gonna go.":
        pass

    "Wanna play again?":
        pass

r m "NO! REMAAAAATCH."

e "He slapped you in the face and frowned."

r m "Les go, bitch."

e "Not being left much of a choice, you play another round with him."

e "..."

e "..."

e "..."

r su "You won... again."

r n "Did you used to have this game?"

menu:
    "Soft and Moist Vegetables: 2 Turbo Vegetable Edition? No.":
        pass

    "Uh, sure. ":
        pass

r m "Psh, right. You probably used to play this all the time."

r m "Nerd."

e "..."

e "..."

e "He looks sad."

e "You turn to leave."

r s "Wait."

e "He walks up behind you."

r s "I have to tell you something sir."

r s "I..."

r s "I never beat my maids son in the game."

r s "I never even won a match against another person."

r n "I've been practicing since we got on this ship, it's been at least 20 hours of nothing but intense training. I really tried."

menu:
    "This is all you've been doing?":
        pass
    "...":
        pass

r s "I thought I could reinvent my image. This was to be my big debut."

r s "I'm... sorry."

e "You see tears well up in his eyes. "

menu:
    "Rematch. One week from today.":
        pass

    "*Blow raspberry*":
        pass

e "He looks surprised for a second."

r n "..."

r h "Bring your big boy pants."

r m "'Cuz I'm gonna F**K YOU UP!"

r h "YEEEEEEHAW!"

r n "Get out."

e "He goes back to the game."

hide r

e "You make your way back out into the hallway."

call hall

menu:
    "NAV ROOM":
        call navRoom
        pass

e "Everyone shows up right behind you."

menu:
    "What's going on?":
        pass

    "Ah, just in time for the meeting.":
        pass

show y n

y n "You called a meeting remember?"

menu:
    "Yes.":
        pass

y h "No you didn't, ass. I grabbed everyone."

show p n:
    linear 0.5 xalign 0.1

p n "Captain, Haruka expressed an interest in setting a sort of schedule."

show r m:
    linear 0 xalign 0.9 yalign 1.0

r m "I don't see why we need one. We'll be fine. "

show y n

y n "What have you done so far Mr. Babe?"

show r n

r n "I've been productive."

show y m

y m "No. Ya haven't."

show r s

e "Hei frowns."

y h "They say a schedule is the best way to ensure productivity."

y n "So what do you have for us? Ideas?"

menu:
    "Yes.":
        pass

    "What do you think?":
        pass

y h "Great lets hear it!"

e "You did not plan for this."

y s "...You don't have a clue do you?"

y h "Fine. Points for trying. "

y n "Anyone else?"

show r su

r su "What?"

e "Hei obviously had not been listening."

e "Nema was fidgeting with her hands."

show p s

p s "Well, we c-could... maybe..."

show y m

y m "Ugh."

y n "Well, I don't want to babysit you all, but I sort of assumed you guys would be a little more excited to get stuff done."

y n "Maybe we don't need to have a strict schedule, but there should be some sort of periodic progress update."

y n "We need some way of knowing things are getting done, that's part of a captains job, right?"

e "She looks accusingly at you."

menu:
    "You're not children. ":
        pass

    "Do what you want.":
        pass

y n "Fair enough, I think we can trust each other to do what we need to, right?"

y n "Any concerns?"

show r s

r s "Do I have to get up early."

show y m

y m "Seriously? Only if you want."

y m "Idiot."

e "Hei smiles."

menu:
    "Say nothing.":
        pass

    "Good work Haruka.":
        pass

y n "Cap, I'd use any time you have today to get comfortable with the ship and your new equipment."

y n "I want you to be comfortable with the basic functions of the ship in case I'm not available for some reason."

show p h

p h "Haruka, th-"

show y n

y n "What."

show p s

p s "Thank you for your hard work. "

e "Haruka looked blankly at Nema for a brief moment then turned back to you."

show y n

y n "Alright, well how do you guys feel about getting some food in us? I'll cook?"

show r h

r h "Yes mumsy."

e "There is silence."

r n "..."

show y n

y n "What is wrong with you?"

show p y

show r h

e "Hei chuckles and Nema smiles."

show r h

r h "Let's go, I'm starving."

call hall

e "Everyone moves into the kitchen."

play sound "sounds/DoorOpen2.mp3"

call kitchen

r n "What are we having Haru?"

show y h

y h "Ramen. My specialty."

show p n

p n "My mother used to run a ramen stand when I was a kid."

show y n

y n "Cool. "

show p h

p h "Yes. I am told my ramen is quite good."

show y n

y n "Oh. Cool."

e "It's mostly silent while Haruka cooks."

y h "So who wants the first dish?"

menu:
    "Give it to me.":
        pass

    "Give it to Nema.":
        pass

y n "Sure thing boss."

menu:
    "It's great! / Stay silent":
        pass

y h "I know! / Good right?"

y n "I know it is. You don't have to tell me."

e "Haruka is beaming with confidence."

y n "Alright. The rest of you get your own."

e "Everyone grabs their food and sits down to the table."

show r s

r s "Man, I'm tired."

show y n

y n "Tired from what. You haven't done a single today."

show r s

r s "Why do you try so hard to hurt me?"

e "Haruka rolls her eyes."

r n "I'm looking forward to a nice sleep."

r n "How about you *name of whoever is staying up*"

e "Hei sticks his tongue out."

menu:
    "Are you volunteering Hei? / Yeah Yeah.":
        pass

e "Nema chuckles."

e "Hei slowly withdraws his tongue. / Hei smiles."

show y n

y n "Hei you're pathetic."

show r h

r h "Oh c'mon. I know you think I'm charming."

show y n

y n "Not even close."

show r h

r h "You think I'm charming."

e "Hei smiles. Haruka sighs. Nema giggles."

show p h

p h "I think you're plenty charming Hei."

e "Nema gives a sweet smile."

show y m

y m "God, please."

show r n

r n "Loved by all, saught after by many, tamed by none."

show y m

y m "You sound like a damn car commercial."

y n "What gives you this huge ego? "

y n "Are you secretly not a huge waste of space?"

show r n

r n "Yes. Secretly, I am a great use of space."

e "Nema chuckles."

show p h

p h "High value to volume ratio."

show r h

r h "Precicely. I'm the bargain of the century ergonomically."

show y n

y n "Ergonomic. You sure that's the word you want?"

show r h

r h "That's what it says, right on the box."

r n "Premium label baby."

show y m

y m "Alright. I thought you were tired?"

show r su

r su "You know... I am."

r n "I think I'll have myself a snooze."

r h "Captain! Good luck my fearless captain."

menu:
    "Thanks! / Your turn next time!":
        pass

r n "Hei smiles / Heis eyes get wide. He walks away."

e "Hei walks out into the hallway."

hide r

e "for a moment there is silence."

show p s

p s "Haruka, do you plan on staying up for a while?"

show y n

y n "Actually, I thought I might help cap pass the time tonight."

menu:
    "What do you mean? / You want to stay up?":
        pass

y n "I'm gonna stay up with you."

y h "It'll be fun! "

show p s

p s "Oh. I see, nice. Ok."

p s "Then I guess I'll just retreat to my room for the night."

p n "U-unless... you'd like another pair of hands to help?"

show y n

y n "I think we got it, right cap?"

menu:
    "Yeah, we're good.":
        pass

show p n

p n "Yes sir... I'll gladly take the shift next week, if that would help?"

hide p n

e "Nema walks out of the room and heads to bed."

show y n

y n "So, take an hour and meet in the nav room, yeah?"

menu:
    "Sounds good":
        pass

y h "Right-o"

hide y h

return