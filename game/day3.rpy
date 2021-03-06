﻿label day3:
e "There's a small introduction to your new application, and then you are shown a screen that lists the names of the crew."

e "There is a sort of progress bar for each made of 3 chunks. Bad. Good. Perfect."

e "These are the accuracy levels for the readings."

menu:
    "I should read the summaries.":
        pass

    "I'm going to respect their privacy.":
        pass

e "This new information makes you think that perhaps you should check on the crew."

play sound "sounds/DoorOpen2.mp3"

e "You open the door."

call hall

e "You step out into the hallway. Haruka is laying on the floor with a blanket. Her eyes are closed."

menu:
    "Haruka?":
        pass

    "Are you a sleepwalker?":
        pass

show y h

y h "Oh, hey Cap. How you feeling after the late night?"

menu:
    "Excellent!":
        pass

    "Terrible!":
        pass

y h "There he is, what a champ."

menu:
    "What are you doing?":
        pass

y n "Layin' on the heater."

y h "It feels good, so warm."

y n "It's easy to just zone out and relax."

menu:
    "Thinking time?":
        pass

    "In the hall?":
        pass

y n "Yeah, I s'pose."

play sound "sounds/DoorOpen2.mp3"

e "Hei walks out of his room."

play sound "sounds/DoorClose2.mp3"

show r h:
    linear 0 xalign 0.9

r h "Peeps."

show y n

y n "Loser."

show r s

r s "Why so hostile my pristine lemon cake?"

show y n

y n "No reason, my garbage pile of a crewmate."

show r h

r h "Oooh. Sour like a lemon."

show y n

y n "You know it."

show r n

r n "..."

r n "Yet."

e "Hei gazes at Haru."

r n "(Softly) Sweet like a cake."

show y m

y m "How are you our weapons expert?"

show r n

r n "I was the only one that applied."

show y m

y m "You're kidding."

show r h

r h "PSYCH."
     
r  "I'm the best, put the rest of the applicants to SHAME! I'm smart as hell dude, seriously."

show y n

y n "OK, thank's for clearin' that up."

show r n

r n "You'll see. You'll be all over big daddy he-"

show y m

y m "Don't finish that sentence."

y m "I'll see you at breakfast. Go."

show r h

r h "But I'm just trying to get to know my brand new ship buds. "

menu:
    "Cool it.":
        pass

    "Say nothing.":
        pass

r m "Fine fine, geez, I was just joshin' sir."

hide r m

e "Hei walks away grumbling."

show y h

y h "Cap."

e "There's a hint of a smile on her face."

y n "I'm gonna use my newfound quiet for a bit of a nap."

y h "I'll see you at breakfast, right Cappo?"

menu:
    "Of course.":
        pass

    "No.":
        pass

y n "See ya then."

hide y n

menu:
    "FREE TIME":
        pass

e "REDS ROOM"

call redRoom

show r h

menu:
    "Morning.":
        pass

    "You're up early.":
        pass

show r h

r h "Heya Captain Crunk Incorperated."

r n "I actually have something I want your captainly advice on."

menu:
    "What?":
        pass

r n "This is man to man right?"

r n "Just between us?"

menu:
    "Sure":
        pass

    "No promises.":
        pass

r s "Alright... so..."

r n "I've been having problems with one of the ship's ladies."

menu:
    "Haruka?":
        pass

    "Nema?":
        pass

r h "How'd you guess?"

r s "She's ridiculously mean to me for no real reason man."

r n "I try to keep things lighthearted but she snaps at me the second I come into sight."

r s "Does she really hate me as much as she acts like she does?"

r s "I know I can be a bit annoying but I just be kiddin'."

r n "She sees that right?"

menu:
    "No telling.":
        pass

    "I'm sure she does.":
        pass

r m "Well what the hell."

r s "I just don't get it man."

r n "You've barely said 3 words to you and she's all over ya."

r s "I crack these hilarious jokes and she doesn't even smile."

r n "Forget smiling, she hates my jokes."

r s "And me."

r n "I don't get it."

menu:
    "She seems to like leadership.":
        pass

    "She seems to hate lazyness.":
        pass

r n "Yeah, I can't disagree there."

r s "but I mean"

r n "I'm sort of a leader in a way."

r n "I built every ounce of weapons technology on this ship."

r h "I was a professional yo-yo artist before I even hit 20."

menu:
    "Stay silent.":
        pass

    "Artist?":
        pass

r n "I played piano in the section 196 orchestra for three years, I was youngest in the whole place!"

r m "I lead myself into that stuff."

r n "Well."

r s "My parents forced me into it. But I worked hard."

r s "Whatever. She'll hate me forever and the rest of my life will be miserable."

r s "I am a cardboard box in the rain. Melting like ice cream on a summer's evening."

r n "I was also the first person under 50 to be featured in my parents monthly poem compendium."

r n "It may not be seeable, but I'm pretty boss when it comes to words and sentences... in an artistic way."

menu:
    "I'm sold.":
        pass

    "You sure?":
        pass

r n "I have a lot to offer. I do."

r s "Why doesn't she like me more?"

menu:
    "Maybe try to prove your worth?":
        pass

    "Why's it so important?":
        pass

r n "That's it... She wants a go-getter."

r h "Thanks bud! I need to get to work. Dinner tonight, prepare your mind to be blown."

e "His eyes have glazed over."

call hall

hide r

e "You walk back out into the hallway."

menu:
    "NEMAS ROOM":
        pass

call pinkRoom

e "Nema is laying on the floor."

menu:
    "Nema?":
        pass
        
#todo change nema to static images

show p s

p s "Nema."

e "There is drool all over her face... and the floor. There's an empty glass bottle in her hand."

menu:
    "Shake her.":
        pass

e "Her eyes shoot open."

e "She looks like a scared owl."

e "Her mouth opens, then her eyes slowly close."

e "She slowly curls up on the bed and closes her eyes."

hide p

call hall

menu:
    "BREAKFAST":
        pass
        
call kitchen

play sound "sounds/DoorOpen2.mp3"

e "You walk into the kitchen just ahead of Haruka and Hei."

play sound "sounds/DoorClose2.mp3"

show r su

r su "No Nema?"

menu:
    "We're going to let her catch up on a bit of rest.":
        pass

r n "Oh, well I'm tired to so I'll catch you guys la-"

show y m:
    linear 0 xalign 0.9

y m "No."

show r su

r su "This trip sucks."

show y m

y m "This isn't a trip, this is your job."

show r s

r s "Still sucks."

menu:
    "I agree, boring.":
        pass

    "I disagree, this has been great.":
        pass

r n "See? Even our (small text)suspiciously quiet captain thinks so."

show y m

y m "Maybe if you both did your jobs then you wouldn't be so bored, yeah?"

menu:
    "Speaking of jobs, what's the agenda for you two today?":
        pass

show r h

r h "Shouldn't you be telling us that?"

show y n

y n "Have you ever served on a ship?"

y n "We're not children and crews arent run that way anymore. You can figure out how to be productive. Do your best to keep us alive so the rest of us can work on our research."

show r n

r n "Fine. Today I'll be doing my BEST to keep us alive so the re-"

show y m

y m "Unbelievable."

show r n

r n "I'm not sure what you expected."

menu:
    "What are you doing Haruka?":
        pass

show y n

y n "I'm gonna start testin' on the training pod that was sent with us."

menu:
    "What?":
        pass

y h "Yup, military grade."

y n "It's gonna be somethin' special. "

menu:
    "But what is it?":
        pass

    "It sounds special.":
        pass

y h "I'll let that be a lil' surprise for everyone."

e "She smirks."

show r n

r n "Is it sexy?"

show y m

y m "What?"

show r n

r n "Like, is it sexy. Is it cool."

show y n

y n "Hei, why do you make it so hard to be around you?"

show r m

r m "Whatever."

e "Everyone eats quietly for a little bit."

e "..."

r h "Bossman, can you fetch a bottle of soy sauce from the fridge?"

menu:
    "Can you fetch it yourself?":
        pass

    "No problem.":
        pass

r n "Sorry, may you fetch it for me?"

show y m

y m "Get it yourself jackoff."

show r n

r n "You know."

r s "That hurts a little bit."

r n "I'm not tr-"

show y n

y n "Ugh. I'll get it."

show r su

r su "Uh, no that's fine, I'll get it! Don't worry about it!"

show y n

#todo, from here to end, alternate portraits and such

y n "I'm already up, you can continue to be la-"

e "ketchup squirts out of the frige when Haru tries to open it."

y su "Is this... Ketchup?"

show r s

r s "Yeah... pretty funny right?"

e "Haruka grabs a knife from the counter."

r su "Haruka c'mon, it wasn't even meant for you! "

e "She turnes around and looks at Hei for a moment."

r su "Haruka! I swear I would not have done it if I kn-"

e "She begins to swiftly walk towards him."

r su "Haruka please, I'm so sorry I'll clean it up, I'll never bother you again I swear, I do"

e "The moment she reaches him she lashes her arm out and slices his throat."

r su "Grgrlgl-Hargh H-g-"

hide r su

e "He collapses to the floor."

show y m:
    linear .3 xalign 0.5

y m "I just couldn't do it, sorry cap."

menu:
    "Holy shit. ":
        pass

    "Oh... It's cool...":
        pass

y n "You know that was for the best. "

y s "He would have been a major annoyance for the rest of our lives."

y s "He would have driven me crazy."

y n "Maybe he did."

menu:
    "No, this is not OK. ":
        pass

y s "Fine. I knew what I was doing. I took a chance. "

y n "I'm not a coward like you."

y s "Coward."

y n "Coward."

y m "Coward."

y n "COWARD."

e "Her portrait starts to become disfigured, she slowly melts into nothing."

hide y

e "When you try to enter Nema's room."

show p su

p su "Captain."

menu:
    "Nema?":
        pass

    "What's going on?":
        pass

e "The atmosphere gets dark as you enter the room."

menu:
    "Nema?":
        pass

    "Hello?":
        pass

e "No response."

e "Nema is facing away. When you talk to her, jump scare."

hide p

e "Suddenly you're floating in space."

e "Things take a sinister tone again here."

#new devil character to speak

d "Leviathan ov mine, stir..."

d "My burning sea. Rise."

d "I arrive."

d "Blow your horns, devout. Announce me."

d "A total waste. Devoid ov value."

d "Meager, pathetic am I. "

d "Piles of flesh. "

d "Waves of nothing."

d "Do I make you smile?"

menu:
    "Yes?":
        pass

d "A deal is struck."

d "My companion."

d "We shall burn together."

d "We shall be of many skins."

e "You fall back into your chair at the dinner table."

show r s

show y m:
    linear 0 xalign 0.99

r s "Haruka c'mon, it wasn't even meant for you! "

show y m:
    linear .2 xalign 0.94

e "She takes another step forward"

r s "Haruka! I swear I would not have done it if I kn-"

show y m:
    linear .2 xalign 0.89

e "She takes a step forward."

menu:
    "Stop her.":
        pass

    "Let her go.":
        pass

e "She sighs."

show y n

y n "Nope."

show r n

r n "I said I was sorry..."

show y n

y n "I'm not interested. "

show r n

r n "But Haruka.."

show y n

y n "I'm gonna go wash up. "

play sound "sounds/DoorOpen2.mp3"

hide y

e "Haruka leaves the room."

play sound "sounds/DoorClose2.mp3"

show r s

r s "She's not THAT mad right?"

menu:
    "You kidding?":
        pass

    "She'll cool down.":
        pass

r s "I know."

r n "Man. I could use a beer... could you grab me one from the fridge?"

menu:
    "Sure.":
        pass

    "Absolutely not.":
        pass

e "Ketchup squirts."

menu:
    "...":
        pass

    "Thanks. ":
        pass
        
r h "..."        

r s "Today sucks. I'm gonna go to sleep. See ya man."

play sound "sounds/DoorOpen2.mp3"

hide r

e "You finish eating then walk into the hallway."

call hall

e "You have a lot of work to do tonight."

e "Make sure you do everything you want to do before returning to your room, as it may well be evening once you're done."

e "HARUKAS ROOM"

call yellowRoom

show y m

y m "Can you believe that idiot?"

y h "Cap, I'm happy you're here."

y n "At least there's one other sane person on this damn ship."

y n "But..."

y n "If you don't mind, I need to get some work done..."

y n "Sorry Cap."

y n "We'll talk later."

hide y n

e "HEIS ROOM"

call redRoom

show r s

r s "Dude I really fucked up."

r s "My goal has moved down from her liking me, to her not hating me."

r s "I hate my life."

r s "Ughhh..."

r n "Man I'll see you at dinner. I need to mope around for a while."

hide r n

e "DINNER TIME"

call kitchen

e "Only Nema is here."

show p h

p h "Hello Captain!"

menu:
    "Nema, how are you feeling?":
        p h "I'm feeling great, thank you for your leniency sir. "
        
        menu:
            "Of course.":
                pass

            "Good.":
                pass
        pass

    "Finally up?":
        pass

play sound "sounds/DoorOpen2.mp3"

e "Hei walks in"

show r h:
    linear 0 xalign .9

r h "Hey Chicklet. Feeling better?"

e "Nema chuckles."

show p h

p h "Yes Hei, thank you for your concern."

show r n

r n "No prob."

r h "So, what we having for dinner?"

r n "You know, I was sort of thinking that steak sounded good."

r n "Nema, do you know how to mak-"

e "Haruka walks through the still open door."

play sound "sounds/DoorClose2.mp3"

e "The door closes behind her."

show y n:
    linear 0 xalign .1

y n "Cap."

menu:
    "Hello.":
        pass

    "Ay":
        pass

e "Haruka glares at Hei."

show p h

p h "Good evening Haruka, how has your day been?"

show y n

y n "My day's been interesting."

show p su

p su "Why is that? Some excitement this morning or perh-"

show y n

y n "Hei, why has my day been interesting?"

show r n

r n "W-well..."

r h "Today you worked on a new training device, and we're all just so excited b-"

e "Haruka's glare intensified. "

r s "Uh, h-heh. Sorry. Again."

show y n

y n "Don't do that again."

show r n

r n "Never!"

show y n

y n "Alright... Forgiven."

show r su

r su "Wait, really?"

show y n

y n "I'm stuck with ya, aren't I?"
     
y n "Why not."

show r h

r h "Thanks babe, I rea-"

show y n

y n "Stop while you're ahead."

show p h

p h "Hah."

p n "Oh... so uhm... should I make food?"

show y su

y su "You can cook?"

show p n

p n "Well... y-yes. I thought I mentioned that yesterday, my apologies. My parents were bo-"

show y h

y h "Great! Lookin' forward to it."

show p n

p n "Oh! It will be great, I promise! You'll love it!"

show y n

y n "Alright."

show p su

p su "Y-...."

e "Nema looks nervous."

p n "Uhm..."

show r n

r n "What's up Nems?"

show p s

p s "Well... How would you guys like to play a game today after dinner?"

show r h

r h "Hell yeah! What kind of game?"

r n "Maybe a fighting game? "

r n "I can bring out my Game Slab X."

show y n

y n "If we're going to play a game, how about we play somethin' that's... you know."

y n "Not that."

show r s

r s "Man, you really know how to hurt a guy."

show p n

p n "Well... I was thinking..."

show y n

y n "Yeah?"

show p n

p n "Maybe we could play a game to get to know each other better?"

show y n

y n "Twenty questions then."

show p h

p h "Sure! Yes, that sounds fine, thank you Haruka."

show r m

r m "You can't even win 20 questions."

menu:
    "You're right.":
        pass

    "You win by learning about each other!":
        pass

r m "Bah!"

show y n

y n "Eloquent. "

show r n

r n "Fine, whatever. What's your favorite color?"

show y n

y n "Ugh...."

y n "We'll eat and then we can think about the game."

show r n

r n "Speaking of eating, is food ready Nibbles?"

show p h

p h "Nibbles!"

e "Nema smiles."

p n "It is. I'll prepare the plates shortly."

show r h

r h "Damn straaaaaight."

e "Nema doles out the plates."

show y n

y n "Thanks Nematsu."

show r h

r h "Yeah thanks."

menu:
    "Thank you!":
        pass

    "Let's eat!":
        pass

show p h

p h "It was my pleasure everybody!"

show r h

r h "This food is dope."

show y n

y n "It is pretty good, nice job."

show p h

p h "R-Really!? Thank you so much!"

p n "What do you think Captain?"

menu:
    "It's delicious!":
        pass

    "It's not bad.":
        pass

p su "Captain thank you! "

e "Eat in silence."

show r s

r s "Nemo, ya haven't touched your food. Feelin' alright?"

show p h

p h "Yes! I'm just so excited!"

show y n

y n "What?"

show p h

p h "You all like my food. "

e "She smiles."

show r h

r h "Awww"

r n "That's adorable."

show y n

y n "C'mon, just eat up so we can play."

show p n

p n "I'll save it for later, I'm ready!"

menu:
    "Let's start!":
        pass

show y n

y n "Ok. Here are the rules."

y n "We go clockwise, so it'll go me, Hei, Nema, then Caps."

show r n

r n "We're starting with you? I want to start."

show y m

y m "No."

y n "So on your turn, the other 3 each get to ask you a question, and you pick one to answer."

show r n

r n "Whoever gets their question picked the most wins."

show y n

y n "No."

y n "And we just do that around the circle. We can call five times around good."

show p h

p h "Haruka, I've never played the game this way. It sounds interesting."

show y n

y n "Sure. It's how I've always played it."

show r n

r n "So..."

show y m

y m "So ask away, idiot."

show r n

r n "Ok, uhhhhh...."

r n "What age did you have your first kiss?"

show y n

y n "What is this, middle school?"

show r s

r s "Hey, don't make fun of my question. This was your stupid idea for a game."

show y n

y n "Whatever. Nema what do you have?"

show p n

p n "Haruka, what is one thing you are very proud of?"

show y n

y n "Alright, Cap?"

menu:
    "What age did you have your first kiss?":
        pass

    "What is one thing you're very ashamed of?":
        pass

y n "Tryin' to block me in, eh?"

y h "Well, I'll pick something I'm proud of."

y n "This ship."

y n "Being here."

y n "I worked my ass off my entire life."

y n "I've never not had to struggle, y'know?"

y n "
rrh"

y n "Classic from rags to riches. The princess of the stars, they call her."

y m "It's amazing that you can turn my pride into shame with one sentence."

show r n

r n "Eh."

show y n

y n "Alright, next. "

show p n

p n "Uhmmm... Hei, it's your turn."

show r h

r h "Nice. Alright, what do ya got for papa?"

show p h

e "Nema chuckles."

show p n

p n "Hei, what is your crowning achievement?"

menu:
    "Have you always been bad at video games?":
        pass

    "What is your ideal woman?":
        pass

show r n

r n "Ask a real question goddamn it."

menu:
    "No.":
        pass

    "What is your ideal woman?":
        pass

r m "I'm going to SMASH you at that rematch. "

r h "You dick."

show y n

y n "Why do you try so hard to annoy me?"

show r h

r h "Haruka, honey, I never tried to do anything but love you."

r n "Alright, your turn Captain."

e "Nema laughs."

show y n

y n "That was your answer?"

show r n

r n "Straight from my heart."

show y n

y n "Fine, Cap, you can go."

show r s

r s "Haruka..."

menu:
    "Let's do it!":
        pass

show y n

y n "Who is your favorite crewmate?"

show r n

r n "Ohhh, I like that. Same."

r n "Nema, pick the same one..."

show p s

p s "B-but... I'd much rather know his greatest accomplishment to be quite honest."

show y n

y n "What's with you and your hokey questions? You're supposed to dig out their darkest secrets, not help them write a resume."

show p s

p s "I don't want to make anyone uncomfortable."

show y h

y h "Life is pain. "

y n "Her question is the same. Answer."

menu:
    "Haruka":
        pass

    "Nema":
        pass

y h "Shucks Cap, I knew the answer, but to hear it makes me smile. What a smooth operator."

show p h

p h "No surprise, Haruka is very charasmatic and strong. "

e "Nema smiles."

show r m

r m "Eh."

e "Haruka glares."

r h "Haha, you know I joke babe. "

show y n

y n "Whatever, back to me. "

show r n

r n "What's your ideal woman? Or man."

show y n

y n "Idiot. Anybody that isn't you."

show r s

r s "Hey, if you're choosing mine you have to be serious."

show y n

y n "Hmph, Nema?"

show p n

p n "Oh, well..."

p s "Not hokey right? Uhm..."

p n "Could I ask... why do you seem to dislike Hei so much?"

show y h

y h "You can, that's the point of the game."

y n "Cap?"

menu:
    "Same as Nema":
        pass

    "Same as Hei":
        pass

y n "You know what, why don't I answer 'em all at once?"

y n "The ideal man for me is strong."

y n "Not because I need to be taken care of."

y n "Strong mind, strong opinions, strong will. Someone to stand beside me."

y h "I want somebody who puts effort into their life, y'know?"

y h "Somebody who understands that you need to work hard, and take control, or else you're throwing your time away. "

y n "Looks don't matter so much to me. Strength does."

show r n

r n "So... what about the other part? About me?"

show y h

y h "I already answered it."

y n "I like strong people, and you are not one of those."

y m "You're soft, you bend under the slightest amount of pressure, ya have no convictions, you're the place that time goes to die."

show r s

r s "Hey, that's not true."

show y n

y n "Then prove me wrong. If you were that kind of person I'd see it, but I don't."

show r n

r n "I have a lot to offer, I-"

show y n

y n "Well show me. I don't see it."

show r s

r s "That's... well..."

show y n

y n "That's what I thought."

y m "Do your own thing, I don't care."

y n "But don't try to force your friendship on me, please."

y n "I'm not trying to hurt you, but I wont slow down."

y n "I need to do what I'm passionate about, and I want to be around passionate people."

y n "When I look at you, I see a weaker me, and that puts me on edge."

y su "I don't mean to be so rude to you, but something about you brings that out in me. I'm sorry, but that's how it is."

show r s

r s "Oh... Ok."

r s "I think... I'm done with this game. Can you let me out Nema."

show p n

p n "Yes, of course..."

show r s

r s "Goodnight."

play sound "sounds/DoorOpen2.mp3"

e "Hei opens the door and walks out of the room."

hide r

show y n

y n "Well, looks like the game is over."

show p s

p s "Yes, it does."

p s "..."

p s "I'm going to go check on Hei."

p n "Goodnight. It's been nice getting a chance to know you both more."

e "Nema walks out after Hei."

play sound "sounds/DoorClose2.mp3"

hide p

show y n:
    linear 0.5 xalign .5

e "There's a moment of silence between you and Haruka."

y s "..."

y n "You think I was too harsh?"

menu:
    "It's better to be direct.":
        pass

    "You could have been more sensitive.":
        pass

y n "I agree."

y n "I honestly don't think he's a bad guy."

y n "I know it doesn't look that way, but it's true."

y n "But I'd rather he knew exactly how I feel instead of leading him on and hurting him every day."

y s "It didn't feel good to say that, I know I look like a jerk..."

y n "But I think it was the best thing to do."

y h "And I'm happy you agree."

y n "..."

y n "Anyways, I'm going to take a shower and get to bed."

y s "This has been a shitty night. "

play sound "sounds/DoorOpen2.mp3"

hide y

e "Haruka walks out and goes to bed."

return