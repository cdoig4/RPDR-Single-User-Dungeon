"""
Colin Doig A01334230
Kelly Hagg A01324804
"""


import json

"""Read Data"""

read_data = {'RUPAUL_READS': ["I never thought I'd meet a queen whose heels weigh more than her brain",
                "I've always wondered what the female Gremlin would look like in 25 years.\nNow I know.",
                "those other queens have been saying you have terrible makeup skills,\nno fashion sense, and you're dumb as a rock. But they're wrong...\nYou don't have terrible makeup skills."], 'POTENTIAL_READS': ['Legendary you think you are. Legendary? Looks like leg AND dairy.',
                   'Beauty fades, dumb is forever',
                   'The last time you got fucked was by genetics']}

filename = 'read_data.json'
with open(filename, 'w') as file_object:
    json.dump(read_data, file_object)


"""RuPaul Lip Sync"""
# rupaul_lip_sync = {'Correct Answer': ["Who you waiting for? Another savior",
#                                       "Who do you think you are? I'm telling the truth now",
#                                       "I'll say it again It's never been the clothes that make the man"],
#                    'Initial Lyrics': ["Who you waiting for? Another savior",
#                                       "What you waiting for? Your best behaviour",
#                                       "Who is that for? Another favor"],
#                    'Chorus Lyrics': ["Where did you get that car? I'm going to Buick now",
#                                      "Who do you think you are? I'm telling the truth now",
#                                      "Who do you think you are? You're blowing a fuse now"],
#                    'Final Lyrics': ["I'll say it again It's never been me who meets the fans",
#                                     "I'll say it again It's always been the wig that makes the queen",
#                                     "I'll say it again It's never been the clothes that make the man"]}
# filename = 'rupaul_lip_sync.json'
# with open(filename, 'w') as file_object:
#     json.dump(rupaul_lip_sync, file_object)
#

"""Introduction"""
# introduction = ['\n--------------------------------------------------------------------------------\n',"\n\nyou have been selected to compete on the new season of\nRupaul's Drag Race! This season will operate a little differently...\n\nTo obtain the title of 'Greatest Queen of All Time', you must\nfirst win the right to lip-sync on the Main Stage by proving your\nmettle against some fellow queens in the Werk Room. If you win the Lip Sync for\nyour Legacy, you will be invited to RuPaul's dressing room where you will\nLIP SYNC FOR YOUR LIFE against Mother herself.\n\nGood luck, and DON'T fuck it up.\n\nAs you get settled in the Werk Room you hear \"Ooh girl!\" and you see RuPaul\nappear on a TV screen on the side of the room. She says...\n\n\"To be invited to compete in a Lip Sync for your Legacy you must first prove\nthat you are literate. Read enough of your fellow queens for filth and you will\nbe called to the main stage.\n--------------------------------------------------------------------------------"]
#
# filename = 'introduction.json'
# with open(filename, 'w') as file_object:
#     json.dump(introduction, file_object)

""" Queen Challengers """
# potential_queen_challengers = {'queen_aja_labeija': {"Name": "Aja", "Charisma": 14, "Uniqueness": 17, "Nerve": 10},
#                                'queen_jinkx_monsoon': {"Name": "Jinkx", "Charisma": 60, "Uniqueness": 60, "Nerve": 55},
#                                'queen_shea_coulee': {"Name": "Shea", "Charisma": 13, "Uniqueness": 13, "Nerve": 16},
#                                'queen_serena_cha_cha': {"Name": "Serena ChaCha", "Charisma": 13, "Uniqueness": 15, "Nerve": 5},
#                                'queen_derrick_berry': {"Name": "Derrick", "Charisma": 11, "Uniqueness": 14, "Nerve": 9},
#                                'queen_bob_the_drag_queen': {"Name": "Bob", "Charisma": 16, "Uniqueness": 12, "Nerve": 14},
#                                'queen_katya_zamalodchikova': {"Name": "Katya", "Charisma": 13, "Uniqueness": 17, "Nerve": 13},
#                                'queen_kennedy_davenport': {"Name": "Kennedy", "Charisma": 15, "Uniqueness": 15, "Nerve": 15},
#                                'queen_shangela_laquifa_wadley': {"Name": "Shangela", "Charisma": 18, "Uniqueness": 18, "Nerve": 15},
#                                'queen_lashauwn_beyond': {"Name": "LaShauwn", "Charisma": 12, "Uniqueness": 16, "Nerve": 7},
#                                'queen_bitch_rupaul': {"Name": "RuPaul", "Charisma": 80, "Uniqueness": 75, "Nerve": 80}}
#
# filename = 'queens.json'
# with open(filename, 'w') as file_object:
#     json.dump(potential_queen_challengers, file_object)

""" Lip Sync Challenge Data"""
# lip_sync_data = {'CHER_LIP_SYNC_CHALLENGE': {'Song Title': 'Believe by Cher',
#                            'Correct Answer': ['No matter how hard I try, you keep pushing me aside',
#                                               'Do you believe in life after love?',
#                                               "Well I know that I'll get through this, Cause I know that I am strong"],
#                            'Initial Lyrics': ['No matter how hard I try, you keep pushing me aside',
#                                               'No matter how much effort I put in, you never let me win',
#                                               'Regardless of what I do, I can never get to you'],
#                            'Chorus Lyrics': ['Do you believe in sun after rain?',
#                                              'Do you believe that you know the words?',
#                                              'Do you believe in life after love?'],
#                            'Final Lyrics': ["I know that I'll get through this, because I found a really cool frog",
#                                             "Well I know that I'll get through this, Cause I know that I am strong",
#                                             "Well I know that I'll get through this, Cause I know that I'm not wrong"]},
#                                'MADONNA_LIP_SYNC_CHALLENGE': {'Song Title': 'Vogue by Madonna',
#                               'Correct Answer':
#                                   ['When all else fails and you long to be Something better than you are today',
#                                    'Come on, vogue. Let your body move to the music',
#                                    "Magical, life's a ball So get up on the dance floor"],
#                               'Initial Lyrics':
#                                   ['When all else fails and you long to be Somewhere other than you are right now',
#                                    'When all else fails and you take a stand To make tomorrow a brighter day',
#                                    'When all else fails and you long to be Something better than you are today'],
#                               'Chorus Lyrics': ['Come on, vogue. Let your body move to the music',
#                                                 'Come on, vogue. Let yourself get into the groovin',
#                                                 "Hey let's vogue. Nod your head to the beat"],
#                               'Final Lyrics': ["Beautiful, life's magical So let the music take you home",
#                                                "Magic, in the ballroom So get onto the cat walk",
#                                                "Magical, life's a ball So get up on the dance floor", ]},
#                                'CARLY_RAE_JEPSEN_LIP_SYNC_CHALLENGE':
#                                    {'Song Title': 'Run Away With Me by Carly Rae Jepsen', 'Correct Answer':
#                                            ["You're stuck in my head, stuck in my heart, stuck in my body- body",
#                                             'When the lights go out, Run away with me! Run away with me!',
#                                             'Over the weekend, we could turn the world to gold'],
#                                        'Initial Lyrics':
#                                            ["You're stuck on my shoe, stuck on my sole, please get off me- off me",
#                                             "You're stuck in my head, stuck in my heart, stuck in my body- body",
#                                             "You're stuck in my head, stuck in my heart, we're both at the party-party"],
#                                        'Chorus Lyrics': ['When the power goes out, Come and look for me! Come and look for me!',
#                                                          'When the lights go out, Run away with me! Run away with me!',
#                                                          'When the lights go out, We have to leave! We have to leave!'],
#                                        'Final Lyrics': ["What's that smell, I think it might be mold.",
#                                                         'Over the weekend, we could turn the world to gold',
#                                                         'Over the summer, we could make the world turn gold']}}
# filename = 'lip_sync_data.json'
# with open(filename, 'w') as file_object:
#     json.dump(lip_sync_data, file_object)

""" Location Descriptions """
# location_descriptions = {'werk_room': ('You are currently in the Drag Race Werk Room. '
#                                        'There are mirrors along the side\nof the room, a '
#                                        'fabric wall covered in rolls of fabric, and several '
#                                        'tables with\nsewing machines.', ''),
#                          'main_stage': ('You are currently on the main stage. As you walk along '
#                                         'the runway, the lights\nshine and flash. The anticipation'
#                                         ' hangs heavy in the air.',
#                                         '\nWhen you are ready, move to the centre of the downstage'
#                                         ' area.'),
#                          'judges_panel': ('You can see the judges looking down on you as you make '
#                                           'your way towards\nRuPaul\'s Dressing Room. With every '
#                                           'step it feels like one of them might'
#                                           ' open\ntheir mouth to say something.', ''),
#                          'dressing_room': ('You see Mother herself standing in the centre of the '
#                                            'room, posing imperiously\nas her eyes watch you like a '
#                                            'hawk.',
#                                            'When you are ready, approach RuPaul.')}
# filename = 'location_descriptions.json'
# with open(filename, 'w') as file_object:
#     json.dump(location_descriptions, file_object)
