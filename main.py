import random

# Climbing drill definitions.
silent_feet = "Silent Feet \n"\
              "\033[1mObjective:\033[0m Improve intentional foot placement for more deliberate movement and setting yourself up for subsequent moves or sequence of movements. \n"\
              "\033[1mDetails:\033[0m Climb routes without making a sound."

hover_hands = "Hover Hands \n"\
              "\033[1mObjective:\033[0m  Improve intentional hand placement to reduce impact to hands, arms, and shoulders. \n"\
              "\033[1mDetails:\033[0m Hold hands over each hold for ~3 seconds before placing them fully throughout the entire route."

soft_hands = "Soft Hands \n"\
             "\033[1mObjective:\033[0m Improve intentional hand placement to reduce impact to hands, arms, and shoulders. \n" \
             "\033[1mDetails:\033[0m Treat each hand hold as though they are incredibly brittle. Focus on carefully placing hands throughout the entire route."

mind_the_feet = "Mind the Feet \n"\
                "\033[1mObjective:\033[0m Shift attention from the hands to the feet to keep them engaged with the wall to prevent feet from cutting away from the wall and relying on upper body strength to compensate unnecessarily. \n" \
                "\033[1mDetails:\033[0m When climbing on steep overhang, perform each hand movement while keeping your mind totally engaged on your feet. maintain constant pressure on your toes while your body extends."

one_touch = "One Touch \n"\
            "\033[1mObjective:\033[0m Make a decision and stick with it. Improve movement sequencing and avoid unecessary movements to conserve energy on the wall and climb more effectively. \n" \
            "\033[1mDetails:\033[0m No matching, no foot swaps, no additional hand adjustments throughout the entire route. Shorten move counts, use different flags, contact each hold with accuracy and intention."

sag_and_push = "Sag and Push \n"\
               "\033[1mObjective:\033[0m Loosen up your body to avoid climbing with too much stiffness, which can waste energy. \n" \
               "\033[1mDetails:\033[0m Set up each move by sagging your body down, opposite of the target hold. Focus on initiating the movement by pushing with your toes whil pulling with your arms at the same time."

dynamic_warmup = "Dynamic Warm-up \n"\
                 "\033[1mObjective:\033[0m Warm up arms, forearms, and shoulders in preparation of dynamic movements and routes. Practice the feeling of having both hands off the wall simultaneously for larger dynamic moves. \n" \
                 "\033[1mDetails:\033[0m Focus on moving both hands to new holds at the same time. Hands can land on the same or different holds, but most both be disconnected from the wall at the same time."

the_robot = "The Robot \n"\
            "\033[1mObjective:\033[0m Focus on body positioning and reach awareness. \n" \
            "\033[1mDetails:\033[0m Only when all four limbs are on holds or securely on the wall can you move your body. When a limb leaves contact with the wall, you must freeze your entire body except for that limb."

pogo_climb = "Pogo Climb \n"\
             "\033[1mObjective:\033[0m Practice and warm up limb utilization using pogo movements with every limb. \n" \
             "\033[1mDetails:\033[0m Choose a route and expect to climb it 4 times - once for each limb. Choose one limb and use that as a pogo counter weight to dynamically jump to holds without using that limb to grab any holds throughout the route."

# List containing climbing drill definitions.
climbing_drills = [silent_feet, hover_hands, soft_hands, mind_the_feet, one_touch, sag_and_push, dynamic_warmup, the_robot, pogo_climb]

# Show a random climbing drill from the climbing_drills list.
print(random.choice(climbing_drills))