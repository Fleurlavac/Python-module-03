# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_analytics_dashboard.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: Fleur <Fleur@student.42.fr>               +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/28 09:41:05 by Fleur           #+#    #+#               #
#  Updated: 2026/01/28 21:44:26 by Fleur           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

players = [
    {
        "name": "alice",
        "score": 2300,
        "active": True,
        "region": "north",
        "achievements": ["Survive the Witch’s Woods",
                         "Defeat Magni and Modi",
                         "Retrieve the Blades of Chaos", "Rescue Atreus"]
    },
    {
        "name": "bob",
        "score": 1800,
        "active": True,
        "region": "east",
        "achievements": ["Defeat Magni and Modi", "Defeat Baldur",
                         "Spread the ashes"]
    },
    {
        "name": "charlie",
        "score": 2150,
        "active": True,
        "region": "central",
        "achievements": ["Survive the Witch’s Woods", 
                         "Ride the ship out of Helheim"]
    },
    {
        "name": "diana",
        "score": 2050,
        "active": False,
        "region": "central",
        "achievements": ["Survive the Witch’s Woods", 
                        "Ride the ship out of Helheim"]
    }
]


def list_comprehension():
    print("=== List Comprehension Examples ===")

    high_score = []
    for player in players:
        if player["score"] > 2000:
            high_score.append(player["name"])
    print(f"High scores (>2000): {high_score}")


    score_doubled = []
    for player in players:
        tmp = player["score"]
        if tmp > 0:
            tmp *= 2
            score_doubled.append(tmp)
    print(f"Scores doubled: {score_doubled}")

    active_players = []
    for player in players:
        if player["active"] == True:
            active_players.append(player["name"])
    print(f"Active players: {active_players}")


def dict_comprehension():
    player_scores = {}
    for player in players:
        name = player["name"]
        score = player["score"]
        player_scores[name] = score
    print(f"Player scores: {player_scores}")

    score_categories = {'high': 0, 'medium': 0, 'low': 0}
    for player in players:
        if player["score"] > 2100:
            score_categories["high"] += 1
        elif 1900 <= player["score"] <= 2100:
            score_categories["medium"] += 1
        else:
            score_categories["low"] += 1
    print(f"Score categories: {score_categories}")

    achievements_count = {}
    for player in players:
        if player["active"] == True:
            name = player["name"]
            achievements = len(player["achievements"])
            achievements_count[name] = achievements
    print(f"Achievement counts: {achievements_count}")


def set_comprehension():
            

def main() -> None:
    print("\n=== Game Analytics Dashboard ===\n")

    list_comprehension()
    print()
    
    dict_comprehension()
    print()

    set_comprehension()
    print()
         

main()