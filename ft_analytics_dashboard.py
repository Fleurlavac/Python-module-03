# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_analytics_dashboard.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: Fleur <Fleur@student.42.fr>               +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/28 09:41:05 by Fleur           #+#    #+#               #
#  Updated: 2026/01/29 21:21:44 by Fleur           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

play = [
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


def main():
    print("\n=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")
    high_scores = [p["name"] for p in play if p["score"] > 2000]
    print(f"High scores (>2000): {high_scores}")
    score_doubled = [p["score"]*2 for p in play]
    print(f"Scores doubled: {score_doubled}")
    active_players = [p["name"] for p in play if p["active"] == True]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    player_scores = {p["name"]: p["score"] for p in play}
    print(f"Player scores: {player_scores}")
    score_categories = {
        'high': len([p["score"] for p in play if p["score"] > 2100]),
        'medium': len([p["score"] for p in play if 2100 > p["score"] > 2000]),
        'low': len([p["score"] for p in play if p["score"] < 2000]),
    }
    print(f"Score categories: {score_categories}")
    achivement_counts = {p["name"]: len(p["achievements"]) for p in play if p["active"] == True}
    print(f"Achievement counts: {achivement_counts}")

    print("\n=== Set Comprehension Exemples ===")
    unique_player = {p["name"] for p in play}
    print(f"Unique players: {unique_player}")
    unique_achievements = {achievement for p in play for achievement in p["achievements"]}
    print(f"Unique achivements: {unique_achievements}")
    active_regions = {p["region"] for p in play}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    total_players = len(unique_player)
    print(f"Total players: {total_players}")
    total_achievements = [achi for p in play for achi in p["achievements"]]
    print(f"Total unique achievements: {len(total_achievements)}")
    

main()