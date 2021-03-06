﻿label day8:

e "There's a knock at your door."

menu:
    "Hello?":
        pass

    "...":
        pass

play sound "sounds/DoorOpen2.mp3"

show p s

p s "Captain, may I speak with you?"

menu:
    "Sure.":
        pass

    "About last night?":
        pass

p s "Sir I just wanted to apologize for last night."

p s "Hei told me how I was acting and I... There's just no excuse sir."

p s "I apologize."

menu:
    "No worries.":
        pass

    "Try to not do that again. You know how Haruka gets.":
        pass

p su "B-...Of course sir."

p s "I've made breakfast in the kitchen if you're interested sir. We'll be waiting."

hide p

e "Nema leaves."

menu:
    "Get up and move to kitchen.":
        pass

play sound "sounds/DoorClose2.mp3"

call kitchen

e "Nema and Hei are standing at the counter joking."

e "Haru is at the table."

show y h:
    linear 0 xalign 0.1 yalign 1.0

y h "Hey Cap!"

show r h:
    linear 0 xalign 0.5 yalign 1.0
    
show p h:
    linear 0 xalign 0.9 yalign 1.0

r h "Mornin' dude."

r h "Ready to fill that tummy."

e "Nema giggles."

menu:
    "Oh yeah.":
        pass

    "Uh.":
        pass

r n "Well. I think we should do something about that, don't you?"

show p h

p h "Hehe, oh, most definitely! "

show r n

r n "But..."

show p su

p su "But what?!"

show r n

r n "You thinking what I'm thinking?"

show p s

p s "Oh. Uhm."

p n "I hope that you're thinking pancak-"

show r h

r h "PANCAKES!"

e "Both laugh"

show y s

y s "They've been like this all morning."

y m "Kill me."

show r n

r n "Here you are, the \"Kill me\" deluxe for the lady."

show p h

p h "Hehe"

show r n

r n "And the tummy filler for... "

r s "Who had the tummy filler?"

show p h

p h "The captain did!"

show r h

r h "Right, the captain! Tummy filler for sir Capitol."

menu:
    "Thank you?":
        pass

    "...":
        pass

e "Hei and Nema share a plate."

r n "So Mr. Boss, what's the plan for today?"

show y n

y n "Actually, today I'm going to be giving you all a briefing on how to compound the engine."

y s "I should have did it from the start, but better late than never I guess."

show p h

p h "That sounds great Haruka, I can't wait."

show r s

r s "Seriously? That souns like the worst."

show p h

p h "Oh Hei."

e "Nema smiles."

show y m

y m "Dear god."

show r su

r su "What."

show y m

y m "It's sickening. Just being near you."

y s "Just get it on with already and bang, we can wait."

show p h

p h "Hehe"

show r h

r h "Too late?"

show y su

y su "Woah, what?"

y n "Are you serious?"

e "Hei smiles sheepishly."

y m "Hei she was drunk, you disgu-"

show r h

r h "No, this morning."

show y su

y su "This morning?"

y m "Nema... what the hell."

show p su

p su "W-what?"

show y m

y m "Do you have absolutely no self-respect?"

show p su

p su "Self re-...what?"

show y m

y m "It's great to know you two can't do ANYTHING on your own other than screw this loser."

y m "We're doomed. This mission was DOA. What am I even doing trying so hard."

show r su

r su "Uh, what?"

show p su

p su "H-haruka... it's not a big deal, we were just having fun."

show y su

y su "Having fun? You're sick."

y m "If you don't value your body nobody else will, I just- I just can't believe it."

show r su

r su "Woah, where's this comin' from? Lay off her man."

show y m

y m "Oh fuck you, you've never thought of another person in your life, don't pretend like ya have her best interest in mind."

show r su

r su "Captain?"

menu:
    "Haruka lay off a little bit.":
        pass

    "She can say what she wants.":
        pass

show y n

y n "Whatever, I'm done. "

y m "Thanks for the pancakes."

play sound "sounds/DoorOpen2.mp3"

hide y

e "Haruka walks out of the room."

show p s

p s "..."

show r s

r s "..."

e "She pops her head back in the door."

show y m:
    linear 0 xalign -0.1 yalign 1.0

y m "And we're still having our goddamn meeting later. "

play sound "sounds/DoorClose2.mp3"

hide y

e "Nema and Hei sit in silence as the door closes again and Haruka disappears."

show r m

r m "Shit, what was her problem."

menu:
    "Jealous.":
        pass

    "Stressed.":
        pass

r su "Jealous? You think so?"

r n "I am a pretty buff daddy..."

show p su

p su "Buff daddy?"

show r h

r h "Yeah babe, it's slang for cool guy."

show p h

p h "Buff daddy..."

e "Nema smiles."

show r s

r s "I should probably go talk to Haruka, huh Heli-Capter?"

menu:
    "Yes.":
        pass

    "No.":
        pass

r n "Alright, I'll give it a shot."

r h "Wish me luck!"

show p h

p h "Good luck."

e "The smile warmly at one another."

e "Hei leaves"

hide r

p s "I hope... I hope he sorts things out."

menu:
    "Why?":
        pass

    "Me too.":
        pass

p n "Why? I want us all to be happy. "

p n "This is our life now sir."

menu:
    "Don't you like Hei?":
        pass

p n "Oh, yes. He's a great friend."

p h "That's why I want him and Haruka to get along."

p s "When they fight, they make their feelings a public thing."

p s "It brings the mood of everyone down, I feel."

menu:
    "That's true.":
        pass

    "That's putting it lightly.":
        pass

p n "That's the kind of people they are."

p h "I bet they could make good friends."

menu:
    "Maybe.":
        pass

    "I doubt that.":
        pass

p h "No, I'm sure of it."

p n "They're both so passionate. "

p n "How could things not work out?"

menu:
    "That seems to be working against them.":
        pass

    "I guess.":
        pass

p h "For now."

p n "I believe that will change."

e "Hei enters."

play sound "sounds/DoorClose2.mp3"

show r s

r s "It didn't work."

show p s

p s "I'm sorry Hei..."

show r h

r h "It's cool, I didn't expect much."

menu:
    "What did you say?":
        pass

show p su

p su "Yeah, what did you say to her?"

show r n

r n "Just the truth."

r s "I said to her, I said, \"Haruka...\""

r n "\"I know you're worried darlin'...\""

r s "\"And I know you're hungry...\""

show p s

p s "Oh Hei..."

show r n

r n "\"But don't worry...\""

r n "\"This meal feeds two.\""

menu:
    "And that didn't work?":
        pass

    "At least you... tried?":
        pass

r h "Weird, right?"

r n "I'm not totally convinced she heard me but whatever. She'll get over it."

r h "Anyways I'm gonna go play some games until dinner, you wanna come Nebs?"

show p h

p h "O-of course I'd like to!"

e "Nema smiles again."

p n "I look forward to seeing you at the meeting Captain."

show r h

r h "Cya dude."

hide r

hide p

e "The two of them walk out of the room."

play sound "sounds/DoorClose2.mp3"

e "You have some free time."

define day8Hei = True

define day8Haru = True

label day8Free:
    
call hall

menu:
    "Haruka's Room" if day8Haru:
        $ day8Haru = False
        call yellowRoom
        pass
    "Hei's Room" if day8Hei:
        $ day8Hei = False        
        call redRoom
        e "In hei's room, her and Nema are just playing games."
        e "The don't acknowledge you."
        jump day8Free
    "Go back to your room" if day8Haru == False and day8Hei == False:
        call blueRoom
        jump day8AfterFree

show y h

y h "Oh, hey Cap."

y n "Whatsup?"

menu:
    "Came to check on you.":
        pass

    "Just saying hi.":
        pass

y n "Yeah I figured."

y m "I'm not apologizing."

y n "It's not my fault that I'm the only one here with standards."

y m "Seriously, am I imagining it, or am I the only one who gives a shit?"

menu:
    "They're adults, they can do what they want.":
        pass

    "No, the others are pretty lax.":
        pass

y s "Well duh. Thanks Captain, gee."

y n "Of course they can."

y n "I just wish that they cared about quality in any part of their lives."

y m "Or having some semblence of respect for themselves, or anyone around them."

menu:
    "Are you jealous?":
        pass

    "Is this really about self-respect?":
        pass

y n "Jealous of those idiots?"

y m "I thought I'd be surrounded by greats on this mission, y'know?"

y m "I thought I'd be among people who worked hard and gave a shit like me, so I wouldn't have to be the bad guy all the time."

y s "I'm sick of being the odd one out, and I'm tired of always feeling like an asshole."

y m "I want everyone to be the best they can, and I refuse to hide it."

y m "It's not fair that all it gets me is hated."

menu:
    "Maybe you can try being a bit more gentle?":
        pass

    "Don't hide how you feel, I get it.":
        pass

y n "Cap I kind of want to be alone, thanks."

y s "I know you mean well, but... please?"

menu:
    "No problem.":
        pass

    "No.":
        pass

y s "Thank you."

hide y s

call hall

e "You walk out into the empty hallway."

jump day8Free

label day8AfterFree:

menu:
    "I guess I can get some work done now?":
        pass

e "Go back to computer."

e "Time passes."

e "There's a knock on your door."

play sound "sounds/DoorOpen2.mp3"

call hall

show y

y s "Time of the thing, c'mon."

play sound "sounds/DoorClose2.mp3"

menu:
    "Yes Ma'am.":
        pass
        
call navRoom

e "You head into into the navigation room together."

show y n:
    linear 0.5 xalign 0.1 yalign 1.0

show p n:
    linear 0 xalign 0.5 yalign 1.0

p n "Hello sir."

show r n:
    linear 0 xalign 0.9 yalign 1.0

r n "Yo."

menu:
    "Hello.":
        pass

    "Yo.":
        pass

show y s

y s "Alright, I'm just going to get through this. "

y n "Everyone open up the MonEn.exe program on your station."

y n "Now look at the red bar. "

y n "That's the missing info. Our sensors aren't perfect and this shows how imperfect."

y n "Now green bar. "

y n "That's the stability."

y n "You want that to be above 2c's. "

y n "That's give or take the missing information, which could go either way."

y s "So you- Hei."

y n "..."

y m "HEI."

show r su

r su "Oh, yeah?"

show y m

y m "Are you paying attention?"

show r s

r s "Uh. Yeah."

show y m

y m "Ya better be."

y n "Now finally, the last bar is the transfer rate."

y n "You want this to mostly be stable, between 2 and 4 C's."

y n "If anything goes out of range, then you can type in the emergency code that applies and it will walk you through steps to remedy the problem, or you can come get me."

y n "The codes are all in an email I sent you on our first or second day."

y n "Really as long as you know that, you'll be fine in nine out of ten situations."

y n "The most important bar to watch is green."

show r n

r n "What's the green bar do?"

show y su

y su "What?"

show r n

r n "Actually what do all the bars stand for? There's no words on this screen."

show y m

y m "..."

y m "Hei."

y m "You have got to be the most incompetent person I have ever met."

show r h

r h "Hah, well, gee."

show y m

y m "No, I mean it."

y m "The whole fucking damn I worked my ass off my entire life-"

show y s

y s "and threw my life away to go on this mission..."

show r su

r su "Hey hold on I wa-"

show y m

y m "Was to get away from the sort of ignorant, drunk, filth that I grew up surrounded by."

y s "I thought I'd be among brilliant minds."

y s "I thought I wouldn't have to be the one babysitting for once."

y m "But here I am surrounded by the same filth."

show p su

p su "H-haruka, tha-that's not fair..."

p s "We're not p-"

show y m

y m "It's not fair, NOTHING is."

y s "That's my point."

y m "I'm sick of working myself to death, being the odd one out because I care about doing something with my life."

y s "I want a friend, Nema."

y s "I want to relax for one day."

y m "I want to close my eyes and know that one other person out there has my back."

y s "..."

y s "Not in this lifetime."

y m "What a goddamn joke this all turned out to be."

y m "I threw EVERYTHING away for this."

y m "Fuck this and fuck you."

play sound "sounds/DoorOpen2.mp3"

hide y

e "Haruka walks away."

show r su

r su "Geesh."

r n "Somebody's in a bad mood lately."

show p m

p m "Hei! You should have paid attention!"

show r su

r su "I did, I was just joshin'."

menu:
    "Probably a bad move.":
        pass

r m "Well duh, I see that now dude."

r n "Still, wasn't that sort of an overreaction? I mean c'mon."

show p s

p s "I cannot say I'd have responded the same, but she has seemed to be a bit irritable lately."

show r n

r n "Should I go apologize?"

show p s

p s "I'm sorry Hei, but I'm not sure that would help right now."

p n "Perhaps if Captain went to see her?"

menu:
    "Not a good idea.":
        pass

    "Alright.":
        pass

show r n

r n "Well, you know best man."

r s "If we're done here though, I think I'm gonna go snooze."

show p s

p s "Given the circumstances that might be the best thing for all of us."

menu:
    "Goodnight you two.":
        pass

    "\"Snooze\" or...?":
        pass

p s "Goodnight Cap."

play sound "sounds/DoorClose2.mp3"

hide p

hide r

e "Hei and Nema walk off to their individual rooms."

call hall

play sound "sounds/DoorOpen2.mp3"

e "You make your way back to yours as well."

call blueRoom

play sound "sounds/DoorClose2.mp3"

e "You lay down on your bed."

e "..."



return