import subprocess
import time
import random
import webbrowser
import textwrap
import getpass
import math

"""subprocess.call(["say", "Warning, Authorised Tech No Man Sirs Only"])
password = getpass.getpass("What is the password?  ")
if password != "technomancy":
	exit()

subprocess.call(["say", "Welcome to the Tech No Man C Portal. Please enjoy your stay."])"""

#character sheet

#ability scores
str_score = 8
dex_score = 16
con_score = 8
int_score = 20
wis_score = 10
cha_score = 15

#ability modifiers
str_mod = math.floor((str_score-10)/2)
dex_mod = math.floor((dex_score-10)/2)
con_mod = math.floor((con_score-10)/2)
int_mod = math.floor((int_score-10)/2)
wis_mod = math.floor((wis_score-10)/2)
cha_mod = math.floor((cha_score-10)/2)


while True:
	action_taken = input("\nWHAT WOULD YOU LIKE TO DO?  ").lower()

#Displaying character sheet
	if action_taken == "show sheet":

		print(str_score, dex_score, con_score, int_score, wis_score, cha_score)
		print("""\n------------------------------------------------------------------------------------------------------------------------------------------
CHARACTER Radikl|| RACE Human | ALIGNMENT Chaotic Good | SPEED 30ft | LEVEL 9 | BACKGROUND Spy (Hacker) | CLASS Wizard | SCHOOL Abjuration
------------------------------------------------------------------------------------------------------------------------------------------""")

#Changing scores during game
	if action_taken == "change score":
		how_score_changed = input("What score to change and how? (STR, DEX, CON, INT, WIS, CHA) Eg. 'STR + 5'  ").lower().split()
		score_changed, change_method, amount_changed = how_score_changed

		if score_changed == "str":
			if change_method == "+":
				print("\nPrevious score: " + str(str_score) + " Previous mod: " + str(str_mod))
				def raise_str():
					global str_score
					str_score = max((str_score + int(amount_changed)),0)
					global str_mod
					str_mod = math.floor((str_score-10)/2)
					print("New score: " + str(str_score) + " New mod: " + str(str_mod))
				raise_str()
			if change_method == "-":
				print("\nPrevious score: " + str(str_score) + " Previous mod: " + str(str_mod))
				def lower_str():
					global str_score
					str_score = max((str_score - int(amount_changed),0))
					global str_mod
					str_mod = math.floor((str_score-10)/2)
					print("New score: " + str(str_score) + " New mod: " + str(str_mod))
				lower_str()
		
	#Casting Spells
	if action_taken == "cast spell":
		subprocess.call(["say", "Spell Net active."])
		spell_cast = input("\nWhat spell are you casting?  ").lower()
		
		#Spell Output
		if spell_cast in {"detect thoughts","neural hack"}:
			print("""\n-----------------------------------------------------------------------------------------------------------------------------
DETECT THOUGHTS || LEVEL 2nd | CASTING TIME 1 Action | RANGE/AREA Self | COMPONENTS V,S,M | DURATION C 1m | SCHOOL Divination
-----------------------------------------------------------------------------------------------------------------------------

For the duration, you can read the thoughts of certain creatures. 
When you cast the spell and as your action on each turn until the spell ends, 
you can focus your mind on any one creature that you can see within 30 feet of you. 
If the creature you choose has an Intelligence of 3 or lower or doesn't speak any language, 
the creature is unaffected.

You initially learn the surface thoughts of the creature--what is most on its mind in that moment. 
As an action, you can either shift your attention to another creature's thoughts or attempt to probe 
deeper into the same creature's mind. If you probe deeper, the target must make a Wisdom saving throw. 
If it fails, you gain insight into its reasoning (if any), its emotional state, and something that looms 
large in its mind (such as something it worries over, loves, or hates). 
If it succeeds, the spell ends. Either way, the target knows that you are probing into its mind, 
and unless you shift your attention to another creature's thoughts, the creature can use its action on its turn 
to make an Intelligence check contested by your Intelligence check; if it succeeds, the spell ends.

Questions verbally directed at the target creature naturally shape the course of its thoughts, 
so this spell is particularly effective as part of an interrogation.

You can also use this spell to detect the presence of thinking creatures you can't see. 
When you cast the spell or as your action during the duration, you can search for thoughts within 30 feet of you. 
The spell can penetrate barriers, but 2 feet of rock, 2 inches of any metal other than lead, or a thin sheet of lead blocks you. 
You can't detect a creature with an Intelligence of 3 or lower or one that doesn't speak any language.

Once you detect the presence of a creature in this way, you can read its thoughts for the rest of the duration as described above, 
even if you can't see it, but it must still be within range.

----------------------------------------------------------------------------------------------------------------------------------
Spell Tags: SOCIAL DETECTION | Available For: BARD SORCERER WIZARD | Basic Rules , pg. 231
----------------------------------------------------------------------------------------------------------------------------------\n""")
			subprocess.call(["say", "Neural Hacking program initiated"])
		
		if spell_cast in {"magic missile","basic malware attack"}:
			print("""\n----------------------------------------------------------------------------------------------------------------------------------
MAGIC MISSILE || LEVEL 1st | CASTING TIME 1 Action | RANGE/AREA 120ft | COMPONENTS V,S | DURATION Instantaneous | SCHOOL Evocation
----------------------------------------------------------------------------------------------------------------------------------

You create three glowing darts of magical force. 
Each dart hits a creature of your choice that you can see within range. 
A dart deals 1d4 + 1 force damage to its target. 
The darts all strike simultaneously, and you can direct them to hit one creature or several.

At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, 
the spell creates one more dart for each slot level above 1st.

----------------------------------------------------------------------------------------------------------------------------------
Spell Tags: SOCIAL DETECTION | Available For: BARD SORCERER WIZARD | Basic Rules , pg. 231
----------------------------------------------------------------------------------------------------------------------------------\n""")
			
			spell_level = int(input("What level are you casting this at?  "))-1
			number_rolls = 3 + spell_level
			spell_damage = [1+random.randint(1,4) for i in range(number_rolls)]
			print("\nDart Rolls:\n")
			print('\n'.join(str(i) for i in spell_damage))
			total_damage = sum(spell_damage)
			print("\nTotal damage: {}".format(sum(spell_damage)))

			subprocess.call(["say", "Basic Malware Attack initiated"])
			subprocess.call(["say", str(number_rolls)+".. D fours rolled. Results are"+str(spell_damage) + "..Total damage equals" + str(sum(spell_damage))])


		if spell_cast in {"shield","personal firewall"}:
			print("""\n------------------------------------------------------------------------------------------------------------------------
SHIELD || LEVEL 1st | CASTING TIME 1 Reaction | RANGE/AREA Self | COMPONENTS V,S | DURATION 1 Round | SCHOOL Abjuration
------------------------------------------------------------------------------------------------------------------------

An invisible barrier of magical force appears and protects you. 
Until the start of your next turn, you have a +5 bonus to AC, including against the triggering attack, 
and you take no damage from magic missile.

------------------------------------------------------------------------------------------------------------------------
Spell Tags: WARDING | Available For: SORCERER WIZARD | Basic Rules , pg. 275
------------------------------------------------------------------------------------------------------------------------\n""")
			subprocess.call(["say", "Personal Firewall activated"])

		if spell_cast in {"knock","brute force attack"}:
			print("""\n---------------------------------------------------------------------------------------------------------------------------
KNOCK || LEVEL 2nd | CASTING TIME 1 Action | RANGE/AREA 60ft | COMPONENTS V | DURATION Instantaneous | SCHOOL Transmutation
---------------------------------------------------------------------------------------------------------------------------

Choose an object that you can see within range. The object can be a door, a box, a chest, a set of manacles, 
a padlock, or another object that contains a mundane or magical means that prevents access.

A target that is held shut by a mundane lock or that is stuck or barred becomes unlocked, unstuck, or unbarred. 
If the object has multiple locks, only one of them is unlocked.

If you choose a target that is held shut with arcane lock, that spell is suppressed for 10 minutes, 
during which time the target can be opened and shut normally.

When you cast the spell, a loud knock, audible from as far away as 300 feet, emanates from the target object.

---------------------------------------------------------------------------------------------------------------------------
Spell Tags: UTILITY | Available For: BARD SORCERER WIZARD | Basic Rules , pg. 254
---------------------------------------------------------------------------------------------------------------------------\n""")
			subprocess.call(["say", "Brute Force Attack initiated."])

		if spell_cast in {"misty step","proxy server"}:
			print("""\n------------------------------------------------------------------------------------------------------------------------------------
MISTY STEP || LEVEL 2nd | CASTING TIME 1 Bonus Action | RANGE/AREA Self | COMPONENTS V | DURATION Instantaneous | SCHOOL Conjuration
------------------------------------------------------------------------------------------------------------------------------------

Briefly surrounded by silvery mist, you teleport up to 30 feet to an unoccupied space that you can see.

------------------------------------------------------------------------------------------------------------------------------------
Spell Tags: TELEPORTATION | Available For: SORCERER WARLOCK WIZARD | Basic Rules , pg. 260
------------------------------------------------------------------------------------------------------------------------------------\n""")
			subprocess.call(["say", "Proxy Server initialized."])

		if spell_cast in {"mirror image","copy/paste"}:
			print("""\n--------------------------------------------------------------------------------------------------------------------------
MIRROR IMAGE || LEVEL 2nd | CASTING TIME 1 Action | RANGE/AREA Self | COMPONENTS V,S | DURATION 1 Minute | SCHOOL Illusion
--------------------------------------------------------------------------------------------------------------------------

Three illusory duplicates of yourself appear in your space. Until the spell ends, the duplicates move with you and mimic 
your actions, shifting position so it's impossible to track which image is real. You can use your action to dismiss the 
illusory duplicates.

Each time a creature targets you with an attack during the spell's duration, roll a d20 to determine whether the attack 
instead targets one of your duplicates.

If you have three duplicates, you must roll a 6 or higher to change the attack's target to a duplicate. 
With two duplicates, you must roll an 8 or higher. With one duplicate, you must roll an 11 or higher.

A duplicate's AC equals 10 + your Dexterity modifier. If an attack hits a duplicate, the duplicate is destroyed. 
A duplicate can be destroyed only by an attack that hits it. It ignores all other damage and effects. 
The spell ends when all three duplicates are destroyed.

A creature is unaffected by this spell if it can't see, if it relies on senses other than sight, such as blindsight, 
or if it can perceive illusions as false, as with truesight.

--------------------------------------------------------------------------------------------------------------------------
Spell Tags: DECEPTION WARDING | Available For: SORCERER WARLOCK WIZARD | Basic Rules , pg. 260
--------------------------------------------------------------------------------------------------------------------------\n""")
			subprocess.call(["say", "Copy/Paste protocol initiated."])

		if spell_cast in {"crown of madness","botnet activation"}:
			print("""\n-----------------------------------------------------------------------------------------------------------------------------------
CROWN OF MADNESS | LEVEL 2nd | CASTING TIME 1 Action | RANGE/AREA 120ft | COMPONENTS V,S | DURATION 1 Minute C | SCHOOL Enchantment
-----------------------------------------------------------------------------------------------------------------------------------

One humanoid of your choice that you can see within range must succeed on a Wisdom saving throw or become charmed by you 
for the duration. While the target is charmed in this way, a twisted crown of jagged iron appears on its head, 
and a madness glows in its eyes. 

The charmed target must use its action before moving on each of its turns to make a melee attack against a creature other than 
itself that you mentally choose. The target can act normally on its turn if you choose no creature or if none are within its reach. 

On your subsequent turns, you must use your action to maintain control over the target, or the spell ends. 
Also, the target can make a Wisdom saving throw at the end of each of its turns. On a success, the spell ends.

-----------------------------------------------------------------------------------------------------------------------------------
Spell Tags: CONTROL COMPULSION | Available For: BARD SORCERER WARLOCK WIZARD | Player's Handbook , pg. 229
-----------------------------------------------------------------------------------------------------------------------------------\n""")
			subprocess.call(["say", "Bott Net activating"])

		if spell_cast in {"fly","drone mode"}:
			print("""\n----------------------------------------------------------------------------------------------------------------------------
FLY | LEVEL 3rd | CASTING TIME 1 Action | RANGE/AREA Touch | COMPONENTS V,S,M | DURATION 10 Minutes C | SCHOOL Transmutation
----------------------------------------------------------------------------------------------------------------------------

You touch a willing creature. The target gains a flying speed of 60 feet for the duration. When the spell ends, the target 
falls if it is still aloft, unless it can stop the fall.

At Higher Levels. When you cast this spell using a spell slot of 4th level or higher, 
you can target one additional creature for each slot level above 3rd.

----------------------------------------------------------------------------------------------------------------------------
Spell Tags: MOVEMENT | Available For: SORCERER WARLOCK WIZARD | Basic Rules , pg. 243
----------------------------------------------------------------------------------------------------------------------------\n""")
			subprocess.call(["say", "Drone mode activated"])

		if spell_cast in {"counterspell","reverse engineer"}:
			print("""\n-----------------------------------------------------------------------------------------------------------------------
COUNTERSPELL | LEVEL 3rd | CASTING TIME 1 Reaction | RANGE/AREA 60ft | COMPONENTS S | DURATION Instantaneous | SCHOOL Abjuration
-----------------------------------------------------------------------------------------------------------------------

You attempt to interrupt a creature in the process of casting a spell. If the creature is casting a spell of 
3rd level or lower, its spell fails and has no effect. If it is casting a spell of 4th level or higher, 
make an ability check using your spellcasting ability. The DC equals 10 + the spell's level. On a success, 
the creature's spell fails and has no effect.

At Higher Levels. When you cast this spell using a spell slot of 4th level or higher, 
the interrupted spell has no effect if its level is less than or equal to the level of the spell slot you used.

-----------------------------------------------------------------------------------------------------------------------
Spell Tags: NEGATION | Available For: SORCERER WARLOCK WIZARD | Basic Rules , pg. 228
-----------------------------------------------------------------------------------------------------------------------\n""")
			subprocess.call(["say", "Reverse engineering complete"])

		if spell_cast in {"lightning bolt","power surge"}:
			print("""\n----------------------------------------------------------------------------------------------------------------------------------------------
LIGHTNING BOLT | LEVEL 3rd | CASTING TIME 1 Action | RANGE/AREA Self (100ft ->) | COMPONENTS V,S,M | DURATION Instantaneous | SCHOOL Evocation
----------------------------------------------------------------------------------------------------------------------------------------------

A stroke of lightning forming a line 100 feet long and 5 feet wide blasts out from you in a direction you choose. Each creature in the line 
must make a Dexterity saving throw. A creature takes 8d6 lightning damage on a failed save, or half as much damage on a successful one. 
The lightning ignites flammable objects in the area that aren't being worn or carried.

At Higher Levels. When you cast this spell using a spell slot of 4th level or higher, 
the damage increases by 1d6 for each slot level above 3rd.

----------------------------------------------------------------------------------------------------------------------------------------------
Spell Tags: DAMAGE | Available For: SORCERER WIZARD | Basic Rules , pg. 255
----------------------------------------------------------------------------------------------------------------------------------------------\n""")
			spell_level = int(input("What level are you casting this at?  "))-3
			number_rolls = 8 + spell_level
			spell_damage = [random.randint(1,6) for i in range(number_rolls)]
			print("\nLightning Rolls:\n")
			print('\n'.join(str(i) for i in spell_damage))
			print("\nTotal damage: {}".format(sum(spell_damage)))
			print("\nHalf damage: {}".format(int((sum(spell_damage)/2))))

			subprocess.call(["say", "Power Surge imminent"])
			subprocess.call(["say", str(number_rolls)+".. D sixes rolled. Results are"+str(spell_damage) + "..Total damage equals" + str(sum(spell_damage)) + "Dexterity throw may halve damage..Half damage equals" + str(int((sum(spell_damage))/2))])


		if spell_cast in {"banishment","delete file"}:
			print("""\n-----------------------------------------------------------------------------------------------------------------------------
BANISHMENT | LEVEL 4th | CASTING TIME 1 Action | RANGE/AREA 60ft | COMPONENTS V,S,M | DURATION 1 Minute C | SCHOOL Abjuration
-----------------------------------------------------------------------------------------------------------------------------

You attempt to send one creature that you can see within range to another plane of existence. 
The target must succeed on a Charisma saving throw or be banished.

If the target is native to the plane of existence you're on, you banish the target to a harmless demiplane. 
While there, the target is incapacitated. The target remains there until the spell ends, at which point the target 
reappears in the space it left or in the nearest unoccupied space if that space is occupied.

If the target is native to a different plane of existence than the one you're on, the target is banished with a 
faint popping noise, returning to its home plane. If the spell ends before 1 minute has passed, 
the target reappears in the space it left or in the nearest unoccupied space if that space is occupied. 
Otherwise, the target doesn't return.

At Higher Levels. When you cast this spell using a spell slot of 5th level or higher, 
you can target one additional creature for each slot level above 4th.

-----------------------------------------------------------------------------------------------------------------------------
Spell Tags: CONTROL BANISHMENT | Available For: CLERIC PALADIN SORCERER WARLOCK WIZARD | Basic Rules , pg. 217
-----------------------------------------------------------------------------------------------------------------------------\n""")
			subprocess.call(["say", "File delete complete"])

		if spell_cast in {"stoneskin","protective case"}:
			print("""\n-------------------------------------------------------------------------------------------------------------------------------
STONESKIN | LEVEL 4th | CASTING TIME 1 Action | RANGE/AREA Touch | COMPONENTS V,S,M*100 | DURATION 1 Hour C | SCHOOL Abjuration
-------------------------------------------------------------------------------------------------------------------------------

This spell turns the flesh of a willing creature you touch as hard as stone. 
Until the spell ends, the target has resistance to nonmagical bludgeoning, piercing, and slashing damage.

-------------------------------------------------------------------------------------------------------------------------------
Spell Tags: BUFF | Available For: DRUID RANGER SORCERER WIZARD | Basic Rules , pg. 278
-------------------------------------------------------------------------------------------------------------------------------\n""")
			subprocess.call(["say", "Protective case applied"])

		if spell_cast in {"wall of force","network firewall"}:
			print("""\n----------------------------------------------------------------------------------------------------------------------------------
WALL OF FORCE | LEVEL 5th | CASTING TIME 1 Action | RANGE/AREA 120ft | COMPONENTS V,S,M | DURATION 10 Minutes C | SCHOOL Evocation
----------------------------------------------------------------------------------------------------------------------------------

An invisible wall of force springs into existence at a point you choose within range. 
The wall appears in any orientation you choose, as a horizontal or vertical barrier or at an angle. 
It can be free floating or resting on a solid surface. 
You can form it into a hemispherical dome or a sphere with a radius of up to 10 feet, 
or you can shape a flat surface made up of ten 10-foot-by-10-foot panels. 
Each panel must be contiguous with another panel. In any form, the wall is 1/4 inch thick. 
It lasts for the duration. If the wall cuts through a creature's space when it appears, 
the creature is pushed to one side of the wall (your choice which side).

Nothing can physically pass through the wall. It is immune to all damage and can't be dispelled by dispel magic. 
A disintegrate spell destroys the wall instantly, however. The wall also extends into the Ethereal Plane, 
blocking ethereal travel through the wall.

----------------------------------------------------------------------------------------------------------------------------------
Spell Tags: CONTROL WARDING | Available For: WIZARD | Basic Rules , pg. 285
----------------------------------------------------------------------------------------------------------------------------------\n""")
			subprocess.call(["say", "Network Firewall activated."])

		if spell_cast in {"telekinesis","file relocation"}:
			print("""\n--------------------------------------------------------------------------------------------------------------------------------
TELEKINESIS| LEVEL 5th | CASTING TIME 1 Action | RANGE/AREA 60ft | COMPONENTS V,S | DURATION 10 Minutes C | SCHOOL Transmutation
--------------------------------------------------------------------------------------------------------------------------------

You gain the ability to move or manipulate creatures or objects by thought. When you cast the spell, and as your action each 
round for the duration, you can exert your will on one creature or object that you can see within range, causing the appropriate 
effect below. You can affect the same target round after round, or choose a new one at any time. 
If you switch targets, the prior target is no longer affected by the spell.

CREATURE: You can try to move a Huge or smaller creature. 
Make an ability check with your spellcasting ability contested by the creature's Strength check. 
If you win the contest, you move the creature up to 30 feet in any direction, 
including upward but not beyond the range of this spell. Until the end of your next turn, 
the creature is restrained in your telekinetic grip. A creature lifted upward is suspended in mid-air.

On subsequent rounds, you can use your action to attempt to maintain your 
telekinetic grip on the creature by repeating the contest.

OBJECT: You can try to move an object that weighs up to 1,000 pounds. 
If the object isn't being worn or carried, you automatically move it up to 30 feet in any direction, 
but not beyond the range of this spell.

If the object is worn or carried by a creature, you must make an ability check with your spellcasting ability 
contested by that creature's Strength check. If you succeed, you pull the object away from that creature and 
can move it up to 30 feet in any direction but not beyond the range of this spell.

You can exert fine control on objects with your telekinetic grip, such as manipulating a simple tool, 
opening a door or a container, stowing or retrieving an item from an open container, or pouring the contents from a vial.

--------------------------------------------------------------------------------------------------------------------------------
Spell Tags: CONTROL MOVEMENT | Available For: SORCERER WIZARD | Basic Rules , pg. 280
--------------------------------------------------------------------------------------------------------------------------------\n""")
			subprocess.call(["say", "File relocation function active"])

		if spell_cast in {"locate creature","gps tracking"}:
			print("""\n--------------------------------------------------------------------------------------------------------------------------------
LOCATE CREATURE | LEVEL 4th | CASTING TIME 1 Action | RANGE/AREA Self | COMPONENTS V,S,M | DURATION 1 Hour C | SCHOOL Divination
--------------------------------------------------------------------------------------------------------------------------------

Describe or name a creature that is familiar to you. You sense the direction to the creature's location, as long as that 
creature is within 1,000 feet of you. If the creature is moving, you know the direction of its movement.

The spell can locate a specific creature known to you, or the nearest creature of a specific kind (such as a human or a 
unicorn), so long as you have seen such a creature up close--within 30 feet--at least once. If the creature you described or 
named is in a different form, such as being under the effects of a polymorph spell, this spell doesn't locate the creature.

This spell can't locate a creature if running water at least 10 feet wide blocks a direct path between you and the creature.

--------------------------------------------------------------------------------------------------------------------------------
Spell Tags: DETECTION | Available For: BARD CLERIC DRUID PALADIN RANGER WIZARD | Basic Rules , pg. 256
--------------------------------------------------------------------------------------------------------------------------------\n""")
			subprocess.call(["say", "GPS tracking initiated"])

		if spell_cast in {"minor illusion","hologram"}:
			print("""\n---------------------------------------------------------------------------------------------------------------------------------------
MINOR ILLUSION | LEVEL Cantrip | CASTING TIME 1 Action | RANGE/AREA 30ft (5ft^3) | COMPONENTS S,M | DURATION 1 Minute | SCHOOL Illusion
---------------------------------------------------------------------------------------------------------------------------------------

You create a sound or an image of an object within range that lasts for the duration. 
The illusion also ends if you dismiss it as an action or cast this spell again.

If you create a sound, its volume can range from a whisper to a scream. 
It can be your voice, someone else's voice, a lion's roar, a beating of drums, or any other sound you choose. 
The sound continues unabated throughout the duration, or you can make discrete sounds at different times before the spell ends.

If you create an image of an object--such as a chair, muddy footprints, or a small chest--it must be no larger than a 5-foot cube. 
The image can't create sound, light, smell, or any other sensory effect. 
Physical interaction with the image reveals it to be an illusion, because things can pass through it.

If a creature uses its action to examine the sound or image, the creature can determine that it is an illusion with a successful 
Intelligence (Investigation) check against your spell save DC. If a creature discerns the illusion for what it is, the illusion 
becomes faint to the creature.

---------------------------------------------------------------------------------------------------------------------------------------
Spell Tags: CONTROL | Available For: BARD SORCERER WARLOCK WIZARD | Basic Rules , pg. 260
---------------------------------------------------------------------------------------------------------------------------------------\n""")
			subprocess.call(["say", "Hologram projection complete"])

		if spell_cast in {"infestation","software bugs"}:
			print("""\n--------------------------------------------------------------------------------------------------------------------------------------
INFESTATION | LEVEL Cantrip | CASTING TIME 1 Action | RANGE/AREA 30ft | COMPONENTS V,S,M | DURATION Instantaneous | SCHOOL Conjuration
--------------------------------------------------------------------------------------------------------------------------------------

You cause a cloud of mites, fleas, and other parasites to appear momentarily on one creature you can see within range. 
The target must succeed on a Constitution saving throw, or it takes 1d6 poison damage and moves 5 feet in a random direction 
if it can move and its speed is at least 5 feet. Roll a d4 for the direction: 1, north; 2, south; 3, east; or 4, west. 
This movement doesn’t provoke opportunity attacks, and if the direction rolled is blocked, the target doesn’t move.

The spell’s damage increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 17th level (4d6).

--------------------------------------------------------------------------------------------------------------------------------------
Spell Tags: SUMMONING DAMAGE CONTROL | Available For: DRUID SORCERER WARLOCK WIZARD | Xanathar's Guide to Everything , pg. 158
--------------------------------------------------------------------------------------------------------------------------------------\n""")
			#Determine number of d6's to role based on level of character casting spell
			character_level = int(input("What level is your character currently?  "))
			if character_level in {1, 2, 3, 4}:
				number_rolls = 1
			if character_level in {5, 6, 7, 8, 9, 10}:
				number_rolls = 2
			if character_level in {11, 12, 13, 14, 15, 16}:
				number_rolls = 3
			if character_level >= 17:
				number_rolls = 4
			#Calculate spell damage based on number of d6's rolled
			spell_damage = [random.randint(1,6) for i in range(number_rolls)]
			#Determine direction moved if target fails constitution saving throw
			direction_roll = random.randint(1,4)
			if direction_roll == 1:
				direction_moved = "North"
			if direction_roll == 2:
				direction_moved = "South"
			if direction_roll == 3:
				direction_moved = "East"
			if direction_roll == 4:
				direction_moved = "West"
			#Print outcomes for reference
			print("\nBug Rolls:\n")
			print('\n'.join(str(i) for i in spell_damage))
			print("\nTotal damage: {}".format(sum(spell_damage)))
			print("Direction Moved:" + direction_moved)
			#Declare outcomes aloud
			subprocess.call(["say", "Software bugs deployed"])
			subprocess.call(["say", str(number_rolls)+".. D sixes rolled. Results are"+str(spell_damage) + "..Total damage equals" + str(sum(spell_damage)) + ".... Constitution save may negate damage."])
			subprocess.call(["say", "If hit target moves 5 feet" + direction_moved])

		if spell_cast in {"message","instant message"}:
			print("""\n-------------------------------------------------------------------------------------------------------------------------------
MESSAGE | LEVEL Cantrip | CASTING TIME 1 Action | RANGE/AREA 120ft | COMPONENTS V,S,M | DURATION 1 Round | SCHOOL Transmutation
-------------------------------------------------------------------------------------------------------------------------------

You point your finger toward a creature within range and whisper a message. 
The target (and only the target) hears the message and can reply in a whisper that only you can hear.

You can cast this spell through solid objects if you are familiar with the target and know it is beyond the barrier. 
Magical silence, 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood blocks the spell. 
The spell doesn't have to follow a straight line and can travel freely around corners or through openings.

-------------------------------------------------------------------------------------------------------------------------------
Spell Tags: COMMUNICATION SOCIAL | Available For: BARD SORCERER WIZARD | Basic Rules , pg. 259
-------------------------------------------------------------------------------------------------------------------------------\n""")
			subprocess.call(["say", "Instant message sent"])

		if spell_cast in {"light","clap on"}:
			print("""\n----------------------------------------------------------------------------------------------------------------------------
LIGHT | LEVEL Cantrip | CASTING TIME 1 Action | RANGE/AREA 20ft sphere | COMPONENTS V,M | DURATION 1 Hour | SCHOOL Evocation
----------------------------------------------------------------------------------------------------------------------------

You touch one object that is no larger than 10 feet in any dimension. 
Until the spell ends, the object sheds bright light in a 20-foot radius and dim light for an additional 20 feet. 
The light can be colored as you like. Completely covering the object with something opaque blocks the light. 
The spell ends if you cast it again or dismiss it as an action.

If you target an object held or worn by a hostile creature, that creature must succeed on a 
Dexterity saving throw to avoid the spell.

----------------------------------------------------------------------------------------------------------------------------
Spell Tags: CREATION UTILITY | Available For: BARD CLERIC SORCERER WIZARD | Basic Rules , pg. 255
----------------------------------------------------------------------------------------------------------------------------\n""")
			subprocess.call(["say", "Clap On protocol initiated"])

		if spell_cast in {"identify","research"}:
			print("""\n-----------------------------------------------------------------------------------------------------------------------------------
IDENTIFY | LEVEL 1st | CASTING TIME 1 Minute R | RANGE/AREA Touch | COMPONENTS V,S,M*100 | DURATION Instantaneous | SCHOOL Divination
-----------------------------------------------------------------------------------------------------------------------------------

You choose one object that you must touch throughout the casting of the spell. If it is a magic item or some 
other magic-imbued object, you learn its properties and how to use them, whether it requires attunement to use, 
and how many charges it has, if any. You learn whether any spells are affecting the item and what they are. 
If the item was created by a spell, you learn which spell created it.

If you instead touch a creature throughout the casting, you learn what spells, if any, are currently affecting it.

-----------------------------------------------------------------------------------------------------------------------------------
Spell Tags: DETECTION | Available For: BARD WIZARD KNOWLEDGE | Basic Rules , pg. 252
-----------------------------------------------------------------------------------------------------------------------------------\n""")
			subprocess.call(["say", "Researching module active"])

		if spell_cast in {"alarm","security alarm"}:
			print("""\n---------------------------------------------------------------------------------------------------------------------
ALARM | LEVEL 1st | CASTING TIME 1 Minute R | RANGE/AREA 30ft | COMPONENTS V,S,M | DURATION 8 Hours | SCHOOL Abjuration
---------------------------------------------------------------------------------------------------------------------

You set an alarm against unwanted intrusion. Choose a door, a window, or an area within range that is no larger 
than a 20-foot cube. Until the spell ends, an alarm alerts you whenever a Tiny or larger creature touches or 
enters the warded area. When you cast the spell, you can designate creatures that won't set off the alarm. 
You also choose whether the alarm is mental or audible.

A mental alarm alerts you with a ping in your mind if you are within 1 mile of the warded area. 
This ping awakens you if you are sleeping.

An audible alarm produces the sound of a hand bell for 10 seconds within 60 feet.

---------------------------------------------------------------------------------------------------------------------
Spell Tags: DETECTION | Available For: RANGER WIZARD | Basic Rules , pg. 211
---------------------------------------------------------------------------------------------------------------------\n""")
			subprocess.call(["say", "Alarm activated"])

		if spell_cast in {"unseen servant","basic ai"}:
			print("""\n------------------------------------------------------------------------------------------------------------------------------
UNSEEN SERVANT | LEVEL 1st | CASTING TIME 1 Action R | RANGE/AREA 60ft | COMPONENTS V,S,M | DURATION 1 Hour | SCHOOL Conjuration
------------------------------------------------------------------------------------------------------------------------------

This spell creates an invisible, mindless, shapeless force that performs simple tasks at your command until the spell ends. 
The servant springs into existence in an unoccupied space on the ground within range. It has AC 10, 1 hit point, and a 
Strength of 2, and it can't attack. If it drops to 0 hit points, the spell ends.

Once on each of your turns as a bonus action, you can mentally command the servant to move up to 15 feet and 
interact with an object. The servant can perform simple tasks that a human servant could do, such as fetching things, 
cleaning, mending, folding clothes, lighting fires, serving food, and pouring wine. Once you give the command, 
the servant performs the task to the best of its ability until it completes the task, then waits for your next command.

If you command the servant to perform a task that would move it more than 60 feet away from you, the spell ends.

------------------------------------------------------------------------------------------------------------------------------
Spell Tags: CONTROL | Available For: BARD WARLOCK WIZARD | Basic Rules , pg. 284
------------------------------------------------------------------------------------------------------------------------------\n""")
			subprocess.call(["say", "Basic artificial intelligence created"])

		if spell_cast in {"illusory script","encrypted message"}:
			print("""\n--------------------------------------------------------------------------------------------------------------------------------
UNSEEN SERVANT | LEVEL 1st | CASTING TIME 1 Minute R | RANGE/AREA Touch | COMPONENTS S,M*10 | DURATION 10 Days | SCHOOL Illusion
--------------------------------------------------------------------------------------------------------------------------------

You write on parchment, paper, or some other suitable writing material 
and imbue it with a potent illusion that lasts for the duration.

To you and any creatures you designate when you cast the spell, the writing appears normal, 
written in your hand, and conveys whatever meaning you intended when you wrote the text. 
To all others, the writing appears as if it were written in an unknown or magical script that is unintelligible. 
Alternatively, you can cause the writing to appear to be an entirely different message, 
written in a different hand and language, though the language must be one you know.

Should the spell be dispelled, the original script and the illusion both disappear.

A creature with truesight can read the hidden message.

--------------------------------------------------------------------------------------------------------------------------------
Spell Tags: COMMUNICATION | Available For: BARD WARLOCK WIZARD | Basic Rules , pg. 252
--------------------------------------------------------------------------------------------------------------------------------\n""")
			subprocess.call(["say", "Message encrypted"])

		if spell_cast in {"find familiar","clockwork toy"}:
			print("""\n---------------------------------------------------------------------------------------------------------------------------------------
FIND FAMILIAR | LEVEL 1st | CASTING TIME 1 Hour R | RANGE/AREA 10ft | COMPONENTS V,S,M*10 | DURATION Instantaneous | SCHOOL Conjuration
---------------------------------------------------------------------------------------------------------------------------------------

You gain the service of a familiar, a spirit that takes an animal form you choose: bat, cat, crab, frog (toad), hawk, lizard, octopus, 
owl, poisonous snake, fish (quipper), rat, raven, sea horse, spider, or weasel. Appearing in an unoccupied space within range, the 
familiar has the statistics of the chosen form, though it is a celestial, fey, or fiend (your choice) instead of a beast.

Your familiar acts independently of you, but it always obeys your commands. 
In combat, it rolls its own initiative and acts on its own turn. A familiar can't attack, but it can take other actions as normal.

When the familiar drops to 0 hit points, it disappears, leaving behind no physical form. It reappears after you cast this spell again.

While your familiar is within 100 feet of you, you can communicate with it telepathically. 
Additionally, as an action, you can see through your familiar's eyes and hear what it hears until the start of your next turn, 
gaining the benefits of any special senses that the familiar has. 
During this time, you are deaf and blind with regard to your own senses.

As an action, you can temporarily dismiss your familiar. It disappears into a pocket dimension where it awaits your summons. 
Alternatively, you can dismiss it forever. As an action while it is temporarily dismissed, 
you can cause it to reappear in any unoccupied space within 30 feet of you.

You can't have more than one familiar at a time. If you cast this spell while you already have a familiar, 
you instead cause it to adopt a new form. Choose one of the forms from the above list. 
Your familiar transforms into the chosen creature.

Finally, when you cast a spell with a range of touch, your familiar can deliver the spell as if it had cast the spell. 
Your familiar must be within 100 feet of you, and it must use its reaction to deliver the spell when you cast it. 
If the spell requires an attack roll, you use your attack modifier for the roll.

---------------------------------------------------------------------------------------------------------------------------------------
Spell Tags: SUMMONING | Available For: WIZARD | Basic Rules , pg. 240
---------------------------------------------------------------------------------------------------------------------------------------\n""")
			subprocess.call(["say", "Clockwork construction complete"])

		if spell_cast in {"magic mouth","pop-up message"}:
			print("""\n--------------------------------------------------------------------------------------------------------------------------------------
MAGIC MOUTH | LEVEL 2nd | CASTING TIME 1 Minute R | RANGE/AREA 30ft | COMPONENTS V,S,M*10 | DURATION Until Dispelled | SCHOOL Illusion
--------------------------------------------------------------------------------------------------------------------------------------

You implant a message within an object in range, a message that is uttered when a trigger condition is met. 
Choose an object that you can see and that isn't being worn or carried by another creature. 
Then speak the message, which must be 25 words or less, though it can be delivered over as long as 10 minutes. 
Finally, determine the circumstance that will trigger the spell to deliver your message.

When that circumstance occurs, a magical mouth appears on the object and recites the message in your voice and at the 
same volume you spoke. If the object you chose has a mouth or something that looks like a mouth (for example, the mouth of a statue), 
the magical mouth appears there so that the words appear to come from the object's mouth. When you cast this spell, you can have 
the spell end after it delivers its message, or it can remain and repeat its message whenever the trigger occurs.

The triggering circumstance can be as general or as detailed as you like, though it must be based on visual or audible conditions 
that occur within 30 feet of the object. For example, you could instruct the mouth to speak when any creature moves within 30 feet 
of the object or when a silver bell rings within 30 feet of it.

--------------------------------------------------------------------------------------------------------------------------------------
Spell Tags: COMMUNICATION | Available For: BARD WIZARD | Basic Rules , pg. 257
--------------------------------------------------------------------------------------------------------------------------------------\n""")
			subprocess.call(["say", "Pop-Up message deployed"])

		if spell_cast in {"tiny hut","hacker space"}:
			print("""\n------------------------------------------------------------------------------------------------------------------------------------------
TINY HUT | LEVEL 3rd | CASTING TIME 1 Minute R | RANGE/AREA Self (10ft sphere) | COMPONENTS V,S,M*10 | DURATION 8 Hours | SCHOOL Evocation
------------------------------------------------------------------------------------------------------------------------------------------

A 10-foot-radius immobile dome of force springs into existence around and above you and remains stationary for the duration. 
The spell ends if you leave its area.

Nine creatures of Medium size or smaller can fit inside the dome with you. The spell fails if its area includes a larger creature 
or more than nine creatures. Creatures and objects within the dome when you cast this spell can move through it freely. 
All other creatures and objects are barred from passing through it. Spells and other magical effects can't extend through the 
dome or be cast through it. The atmosphere inside the space is comfortable and dry, regardless of the weather outside.

Until the spell ends, you can command the interior to become dimly lit or dark. The dome is opaque from the outside, 
of any color you choose, but it is transparent from the inside.

------------------------------------------------------------------------------------------------------------------------------------------
Spell Tags: UTILITY | Available For: BARD WIZARD | Player's Handbook , pg. 255
------------------------------------------------------------------------------------------------------------------------------------------\n""")
			subprocess.call(["say", "Hacker space built"])

		if spell_cast in {"telepathic bond","chat room"}:
			print("""\n--------------------------------------------------------------------------------------------------------------------------------
TELEPATHIC BOND | LEVEL 5th | CASTING TIME 1 Action R | RANGE/AREA 30ft | COMPONENTS V,S,M | DURATION 1 Hour | SCHOOL Divination
--------------------------------------------------------------------------------------------------------------------------------

You forge a telepathic link among up to eight willing creatures of your choice within range, psychically linking each creature 
to all the others for the duration. Creatures with Intelligence scores of 2 or less aren’t affected by this spell.

Until the spell ends, the targets can communicated telepathically through the bond whether or not they have a common language. 
The communication is possible over any distance, though it can’t extend to other planes of existence.

--------------------------------------------------------------------------------------------------------------------------------
Spell Tags: COMMUNICATION | Available For: WIZARD | Player's Handbook , pg. 270
--------------------------------------------------------------------------------------------------------------------------------\n""")
			subprocess.call(["say", "Chat room online"])

		if spell_cast in {"contact other plane","singularity dive"}:
			print("""\n----------------------------------------------------------------------------------------------------------------------------------
CONTACT OTHER PLANE | LEVEL 5th | CASTING TIME 1 Minute R | RANGE/AREA Self | COMPONENTS V | DURATION 1 Minute | SCHOOL Divination
----------------------------------------------------------------------------------------------------------------------------------

You mentally contact a demigod, the spirit of a long- dead sage, or some other mysterious entity from another plane. 
Contacting this extraplanar intelligence can strain or even break your mind. When you cast this spell, make a DC 15 Intelligence 
saving throw. On a failure, you take 6d6 psychic damage and are insane until you finish a long rest. While insane, you can't take 
actions, can't understand what other creatures say, can't read, and speak only in gibberish. 
A greater restoration spell cast on you ends this effect.

On a successful save, you can ask the entity up to five questions. You must ask your questions before the spell ends. 
The GM answers each question with one word, such as "yes," "no," "maybe," "never," "irrelevant," or "unclear" (if the entity 
doesn't know the answer to the question). If a one-word answer would be misleading, the GM might instead offer a short 
phrase as an answer.

----------------------------------------------------------------------------------------------------------------------------------
Spell Tags: COMMUNICATION FOREKNOWLEDGE | Available For: WARLOCK WIZARD | Basic Rules , pg. 226
----------------------------------------------------------------------------------------------------------------------------------\n""")
			subprocess.call(["say", "Preparing dive into singularity"])


#Research option opens DnD Beyond page for spell searched
	if action_taken == "research":
		subprocess.call(["say", "Research module loaded"])
		thing_researched = input("What do you want to know about?  ").lower()
		if thing_researched == ("detect thoughts"):
			webbrowser.open_new("https://www.dndbeyond.com/spells/detect-thoughts")

		if thing_researched in {"cube of force","security portfolio"}:
			print("""\n------------------------------------------------------------------------------------------------------
CUBE OF FORCE | MAGIC ITEM Rare, Wonderous | RANGE/AREA 15ft | REQUIRES Attunement | DURATION 1 Minute
------------------------------------------------------------------------------------------------------

This cube is about an inch across. Each face has a distinct marking on it that can be pressed. 
The cube starts with 36 charges, and it regains 1d20 expended charges daily at dawn.

You can use an action to press one of the cube's faces, expending a number of charges based 
on the chosen face, as shown in the Cube of Force Faces table. Each face has a different effect. 
If the cube has insufficient charges remaining, nothing happens. Otherwise, a barrier of invisible 
force springs into existence, forming a cube 15 feet on a side. The barrier is centered on you, 
moves with you, and lasts for 1 minute, until you use an action to press the cube's sixth face, 
or the cube runs out of charges. You can change the barrier's effect by pressing a different face 
of the cube and expending the requisite number of charges, resetting the duration.

If your movement causes the barrier to come into contact with a solid object that can't pass 
through the cube, you can't move any closer to that object as long as the barrier remains.

---------------------------------------------------------------------------------
FACE | CHARGES | EFFECT
---------------------------------------------------------------------------------
  1  |    1    | Gasses, wind, fog can't pass through the barrier
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  2  |    2    | Nonliving matter can't pass through the barrier. 
     |         | Walls, floors, and ceilings can pass through at your discretion.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  3  |    3    | Living matter can't pass through the barrier.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  4  |    4    | Spell effects can't pass through the barrier.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  5  |    5    | Nothing can pass through the barrier. 
     |         | Walls, floors, and ceilings can pass through at your discretion.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  6  |    6    | The barrier deactivates.
---------------------------------------------------------------------------------

The cube loses charges when the barrier is targeted by certain spells or comes into 
contact with certain spell or magic item effects, as shown in the table below.

-------------------------------
SPELL or ITEM    | CHARGES LOST
-------------------------------
Disintegrate     |     1d12
- - - - - - - - - - - - - - - - 
Horn of Blasting |     1d10
- - - - - - - - - - - - - - - - 
Passwall         |     1d6
- - - - - - - - - - - - - - - - 
Prismatic Spray  |     1d20
- - - - - - - - - - - - - - - - 
Wall of Fire     |     1d4
-------------------------------

------------------------------------------------------------------------------------------------------
Item Tags: CONTROL WARDING | Basic Rules , pg. 159
------------------------------------------------------------------------------------------------------\n""")
			subprocess.call(["say", "Security Portfolio information loaded"])

#Enables the rolling of dice. Asks user how many of each to roll, then displays and announces results and sum of rolls. 
	if action_taken == "d4":
		number_rolls = int(input("How many should I roll?  "))
		roll_total = [random.randint(1,4) for i in range(number_rolls)]
		print("\n:: d4 Roll Results ::\n")
		print('\n'.join(str(i) for i in roll_total))
		roll_outcome = sum(roll_total)
		print("\nSum of rolls: {}".format(sum(roll_total)))
		subprocess.call(["say", str(number_rolls)+".. D fours rolled. Results are"+str(roll_total) + "..Sum of rolls equals" + str(sum(roll_total))])

	if action_taken == "d6":
		number_rolls = int(input("How many should I roll?  "))
		roll_total = [random.randint(1,6) for i in range(number_rolls)]
		print("\n:: d6 Roll Results ::\n")
		print('\n'.join(str(i) for i in roll_total))
		roll_outcome = sum(roll_total)
		print("\nSum of rolls: {}".format(sum(roll_total)))
		subprocess.call(["say", str(number_rolls)+".. D sixes rolled. Results are"+str(roll_total) + "..Sum of rolls equals" + str(sum(roll_total))])

	if action_taken == "d8":
		number_rolls = int(input("How many should I roll?  "))
		roll_total = [random.randint(1,8) for i in range(number_rolls)]
		print("\n:: d8 Roll Results ::\n")
		print('\n'.join(str(i) for i in roll_total))
		roll_outcome = sum(roll_total)
		print("\nSum of rolls: {}".format(sum(roll_total)))
		subprocess.call(["say", str(number_rolls)+".. D eights rolled. Results are"+str(roll_total) + "..Sum of rolls equals" + str(sum(roll_total))])

	if action_taken == "d10":
		number_rolls = int(input("How many should I roll?  "))
		roll_total = [random.randint(1,10) for i in range(number_rolls)]
		print("\n:: d10 Roll Results ::\n")
		print('\n'.join(str(i) for i in roll_total))
		roll_outcome = sum(roll_total)
		print("\nSum of rolls: {}".format(sum(roll_total)))
		subprocess.call(["say", str(number_rolls)+".. D tens rolled. Results are"+str(roll_total) + "..Sum of rolls equals" + str(sum(roll_total))])

	if action_taken == "d12":
		number_rolls = int(input("How many should I roll?  "))
		roll_total = [random.randint(1,12) for i in range(number_rolls)]
		print("\n:: d12 Roll Results ::\n")
		print('\n'.join(str(i) for i in roll_total))
		roll_outcome = sum(roll_total)
		print("\nSum of rolls: {}".format(sum(roll_total)))
		subprocess.call(["say", str(number_rolls)+".. D twelves rolled. Results are"+str(roll_total) + "..Sum of rolls equals" + str(sum(roll_total))])

	if action_taken == "d20":
		number_rolls = int(input("How many should I roll?  "))
		roll_total = [random.randint(1,20) for i in range(number_rolls)]
		print("\n:: d20 Roll Results ::\n")
		print('\n'.join(str(i) for i in roll_total))
		roll_outcome = sum(roll_total)
		print("\nSum of rolls: {}".format(sum(roll_total)))
		subprocess.call(["say", str(number_rolls)+".. D twentys rolled. Results are"+str(roll_total) + "..Sum of rolls equals" + str(sum(roll_total))])

	if action_taken == "d100":
		number_rolls = int(input("How many should I roll?  "))
		roll_total = [random.randint(1,100) for i in range(number_rolls)]
		print("\n:: d100 Roll Results ::\n")
		print('\n'.join(str(i) for i in roll_total))
		roll_outcome = sum(roll_total)
		print("\nSum of rolls: {}".format(sum(roll_total)))
		subprocess.call(["say", str(number_rolls)+".. D one hundreds rolled. Results are"+str(roll_total) + "..Sum of rolls equals" + str(sum(roll_total))])

	#Joke time!
	if action_taken == "joke":
		joke_selected = random.randint(1,15)
		if joke_selected == 1:
			print("""What do you call a mountaintop guarded by rogues?
...

"A Sneak Peak" """)
			subprocess.call(["say", "What do you call a mountaintop guarded by rogues?"])

		if joke_selected == 2:
			print("""What do you call the unfair advantage the undead have in Necropolis?
...

"Wight Priviledge" """)
			subprocess.call(["say", "What do you call the unfair advantage the undead have in Necropolis?"])

		if joke_selected == 3:
			print("""Why do paladins prefer chainmail?
...

"Because it's holey armour." """)
			subprocess.call(["say", "Why do paladins prefer chainmail?"])

		if joke_selected == 4:
			print("""What social platform do elves use?
...

"Vine" """)
			subprocess.call(["say", "What social platform do elves use?"])

		if joke_selected == 5:
			print("""How can you tell if a Necromancer is a nerd?
...

"If he lives with his mummy" """)
			subprocess.call(["say", "How can you tell if a Necromancer is a nerd?"])

		if joke_selected == 6:
			print("""Why was the werebat scared to fly outside?
...

"Because he heard every cloud has a silver lining" """)
			subprocess.call(["say", "Why was the where batt scared to fly outside?"])

		if joke_selected == 7:
			print("""What happens if you step on a 1d4 barefoot?
...

"You take 1d4 damage" """)
			subprocess.call(["say", "What happens if you step on a 1d4 barefoot?"])

		if joke_selected == 8:
			print("""Why do dragons refuse to eat paladins?
...

"Because they taste so Lawful" """)
			subprocess.call(["say", "Why do dragons refuse to eat paladins?"])

		if joke_selected == 9:
			print("""What do you call a group of all rogue players?
...

"A suprise party" """)
			subprocess.call(["say", "What do you call a group of all rogue players?"])

		if joke_selected == 10:
			print("""Why did the barbarian try to learn lightning spells?
...

"the Wizard told him he needed an outlet for his anger" """)
			subprocess.call(["say", "Why did the barbarian try to learn lightning spells?"])

		if joke_selected == 11:
			print("""Why does everyone love hit points?
...

"Because they're the life of the Party" """)
			subprocess.call(["say", "Why does everyone love hit points?"])

		if joke_selected == 12:
			print("""Did you hear about the druid who could wild weapons while using wildshape?
...
"He had the right to bear arms" """)
			subprocess.call(["say", "Did you hear about the druid who could wild weapons while using wild shape?"])

		if joke_selected == 13:
			print("""Two of my players were frusterated that I wouldn't let them play as Chinese Necromancer Twins...
...
"I told them two Wongs can't make a Wight" """)
			subprocess.call(["say", "Two of my players were frusterated that I wouldn't let them play as Chinese Necromancer Twins..."])

		if joke_selected == 14:
			print("""How do you get a D&D player to go out with you?
...
"You ask them for a d8" """)
			subprocess.call(["say", "How do you get a D and D player to go out with you?"])

		if joke_selected == 15:
			print("""A warlock threw a teacup at me...
...
"I guess I should have seen that coming from a tiefling" """)
			subprocess.call(["say", "A warlock threw a teacup at me..."])

	#exit program
	if action_taken == "exit":
		exit()























