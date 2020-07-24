#!/usr/bin/env python3

card_data = {}

def generate_the_cards():
    with open("genesys_card_archetype_template.svg","r") as template_file:
        template_lines = template_file.readlines()
        for card_name, card_dict in card_data.items():
            output_lines = []
            with open("./output/{}.svg".format(card_name),"w") as output_file:
                for line in template_lines:
                    for key,val in card_dict.items():
                        if key in line:
                            line = line.replace("{{{}}}".format(key), val)
                    output_lines.append(line)
                output_file.writelines(output_lines)

unicode_symbols_for_copy_paste = """ ⯀ ⯁ ⬟ ✷ ✸ """

card_data["average_human"] = {
    "card_title": "Average Human",
    "card_type": "Archetype",
    "page_number": "CRB 36",
    
    "brawn_value":     "2",    "agility_value":   "2",
    "intellect_value": "2",    "cunning_value":   "2",
    "willpower_value": "2",    "presence_value":  "2",
    
    "starting_wounds": "10+B", "starting_strain": "10+W", "starting_xp": "110",
    
    "starting_skills": "Any two non-career skills",
    
    "ability_one_offset": "90",
    "ability_one_title": "Ready for Anything",
    "ability_one_description": "Once per session as an out-of-turn incidental, you may move one Story Point from the Game Master's pool to the players' pool.",
    
    "ability_two_offset": "248",
    "ability_two_title": "",
    "ability_two_description": "",

    "ability_three_offset": "258",
    "ability_three_title": "",
    "ability_three_description": "",
}

card_data["laborer"] = {
    "card_title": "Laborer",
    "card_type": "Archetype",
    "page_number": "CRB 37",
    
    "brawn_value":     "3",    "agility_value":   "2",
    "intellect_value": "2",    "cunning_value":   "2",
    "willpower_value": "1",    "presence_value":  "2",
    
    "starting_wounds": "12+B", "starting_strain": "8+W", "starting_xp": "100",
    
    "starting_skills": "Athletics",
    
    "ability_one_offset": "90",
    "ability_one_title": "Tough as Nails",
    "ability_one_description": "Once per session, your character may spend a Story Point as an out-of-turn incidental immediately after suffering a Critical Injury and determining the result. If they do so, the count the result rolled as '01'.",
    
    "ability_two_offset": "248",
    "ability_two_title": "",
    "ability_two_description": "",

    "ability_three_offset": "258",
    "ability_three_title": "",
    "ability_three_description": "",
}

card_data["intellectual"] = {
    "card_title": "Intellectual",
    "card_type": "Archetype",
    "page_number": "CRB 38",
    
    "brawn_value":     "2",    "agility_value":   "1",
    "intellect_value": "3",    "cunning_value":   "2",
    "willpower_value": "2",    "presence_value":  "2",
    
    "starting_wounds": "8+B", "starting_strain": "12+W", "starting_xp": "100",
    
    "starting_skills": "Knowledge (any)",
    
    "ability_one_offset": "90",
    "ability_one_title": "Brilliant!",
    "ability_one_description": "Once per session, your character may spend a Story Point as an incidental. If they do so, during the next check they make during that turn, you count their ranks in the skill being used as equal to their Intellect.",
    
    "ability_two_offset": "248",
    "ability_two_title": "",
    "ability_two_description": "",

    "ability_three_offset": "258",
    "ability_three_title": "",
    "ability_three_description": "",
}

card_data["aristocrat"] = {
    "card_title": "Aristocrat",
    "card_type": "Archetype",
    "page_number": "CRB 39",
    
    "brawn_value":     "1",    "agility_value":   "2",
    "intellect_value": "2",    "cunning_value":   "2",
    "willpower_value": "2",    "presence_value":  "3",
    
    "starting_wounds": "10+B", "starting_strain": "10+W", "starting_xp": "100",
    
    "starting_skills": "Cool",
    
    "ability_one_offset": "90",
    "ability_one_title": "Forceful Personality",
    "ability_one_description": "Once per session, your character may spend a Story Point as an incidental. If they do so, during the next skill check they make during that turn, your character doubles the strain they inflict or the strain they heal (you choose before making the check).",
    
    "ability_two_offset": "248",
    "ability_two_title": "",
    "ability_two_description": "",

    "ability_three_offset": "258",
    "ability_three_title": "",
    "ability_three_description": "",
}

card_data["dwarf"] = {
    "card_title": "Dwarf",
    "card_type": "Archetype",
    "page_number": "CRB 142",
    
    "brawn_value":     "2",    "agility_value":   "1",
    "intellect_value": "2",    "cunning_value":   "2",
    "willpower_value": "3",    "presence_value":  "2",
    
    "starting_wounds": "11+B", "starting_strain": "10+W", "starting_xp": "90",
    
    "starting_skills": "Resilience",
    
    "ability_one_offset": "90",
    "ability_one_title": "Dark Vision",
    "ability_one_description": "When making skill checks, dwarves remove up to ⯀⯀ imposed due to darkness.",
    
    "ability_two_offset": "150",
    "ability_two_title": "Tough as Nails",
    "ability_two_description": "Once per session, a dwarf character may spend a Story Point as an out-of-turn incidental immediately after suffering a Critical Injury and determining the result. If they do so, the count the result rolled as '01'.",

    "ability_three_offset": "258",
    "ability_three_title": "",
    "ability_three_description": "",
}

card_data["elf"] = {
    "card_title": "Elf",
    "card_type": "Archetype",
    "page_number": "CRB 142",
    
    "brawn_value":     "2",    "agility_value":   "3",
    "intellect_value": "2",    "cunning_value":   "2",
    "willpower_value": "1",    "presence_value":  "2",
    
    "starting_wounds": "9+B", "starting_strain": "10+W", "starting_xp": "90",
    
    "starting_skills": "Perception",
    
    "ability_one_offset": "90",
    "ability_one_title": "Nimble",
    "ability_one_description": "Elves have a melee and ranged defense of 1.",
    
    "ability_two_offset": "248",
    "ability_two_title": "",
    "ability_two_description": "",

    "ability_three_offset": "258",
    "ability_three_title": "",
    "ability_three_description": "",
}

card_data["fused"] = {
    "card_title": "Fused",
    "card_type": "Archetype",
    "page_number": "Custom",
    
    "brawn_value":     "2",    "agility_value":   "2",
    "intellect_value": "3",    "cunning_value":   "2",
    "willpower_value": "2",    "presence_value":  "1",
    
    "starting_wounds": "12+B", "starting_strain": "8+W", "starting_xp": "90",
    
    "starting_skills": "Computers",
    
    "ability_one_offset": "90",
    "ability_one_title": "Whispers of the Machine",
    "ability_one_description": "Fused characters can interact with the subtle energies of ancient technology. They can communicate silently with machines, constructs, and other Fused within line of sight.",
    
    "ability_two_offset": "180",
    "ability_two_title": "Life Support Protocols",
    "ability_two_description": "Once per session when your character recieves a critical injury result higher than 90, the result is reduced to 90 and they are incapacitated until the end of their next turn.",

    "ability_three_offset": "258",
    "ability_three_title": "",
    "ability_three_description": "",
}

if __name__ == "__main__":
    generate_the_cards()