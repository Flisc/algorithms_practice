def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    return L[1] if len(L) >= 2 else None


l = [1]
print(select_second(l))

def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    return teams[len(teams) - 1][1]

# Check your answer
teams = [['first', 'c1'], ['sec', 'c2']]
print(losing_team_captain(teams))
arrivals = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
name='Gilbert'
halfIdx = int(len(arrivals)/2) if len(arrivals)%2 == 0 else int(len(arrivals)/2)+1
print(halfIdx)
print(arrivals[halfIdx:len(arrivals)-1])
print(name in arrivals[halfIdx:len(arrivals)-2])