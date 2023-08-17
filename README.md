# The-Sniper-Game
A fun sniper game that could be made into a reinforcement learning ai

Rules of the game are:
1. The game can be played by 2 or more people. Each person can be replaced by an AI.
2. Each turn is played simultaneously between all players.
3. In each turn, a person can choose to charge, attack or defend.
4. Each charge increases 1 attack point, and attack points can be stacked
5. Each attack can be dealt to one specific opponent based on the amount of attack points one has. However, the attacker may choose to deal less attack points that what he has stored. Eg: if he has 4 attack points, and he deals 2 to an opponent, he still has 2 attack points remaining unless he charges in future rounds. Attack points dealt  each round are capped at 6, but a person may stack an infinite number of attack points
6. A person may also defend via defensive points, ranging from one to 6 defensive points. Defensive points cost nothing.
7. If a person charges, they are vulnerable to being attacked, and will lose the game if he is attacked by any attack points by any opponent.
8. If two people attack each other, the person who deals more attack points survives while the other loses. The person who survives also loses the amount of attack points he deals.
9. If a person attacks and another defends, the person that defends must produce the same amount of defensive points that the attacker deals in attacking points. The person defending loses if the amount of defensive points do not equal attacking points. If equal, the person attacking loses the amount of attacking points dealt that round.
10. A person wins if they defeat all opponents.
