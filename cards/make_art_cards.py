#!/usr/bin/env python3

landscape_art_card_data = {
    "sedlan_falls": ("Sedlan Falls", "sedlan_falls.png", "Sina Abbasnia"),
}

portrait_art_card_data = {
    "ns_inquisitor_001": ("Inquisitor", "ns_inquisitor_001.png",  "Marko Djurdjevic"),
    "ns_crusader_001":   ("Crusader",   "ns_crusader_001.png",    "_MOOWM_"),
    "ns_observer_001":   ("Observer",   "basic_observer_bot.png", "Sam Brown"),
    "ns_militia_001":   ("Militia",     "ns_militia_001.png",     "Porino"),
}

def generate_the_cards(template_fn, card_data):
    with open(template_fn,"r") as template_file:
        template_lines = template_file.readlines()
        for card_name, card_tuple in card_data.items():
            output_lines = []
            title, image_fn, illustrator = card_tuple
            with open("./output/ns_card_{}.svg".format(card_name),"w") as output_file:
                for line in template_lines:
                    if "{{title}}" in line:
                        line = line.replace("{{title}}", title)
                    if "{{image_fn}}" in line:
                        line = line.replace("{{image_fn}}", "../../images/{}".format(image_fn))
                    if "{{illustrator}" in line:
                        line = line.replace("{{illustrator}}", illustrator)
                    output_lines.append(line)
                output_file.writelines(output_lines)

if __name__ == "__main__":
    generate_the_cards("genesys_card_art_landscape.svg", landscape_art_card_data)
    generate_the_cards("genesys_card_art_portrait.svg", portrait_art_card_data)