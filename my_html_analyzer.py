'''
    This is a library for obtaining
    specific information (the ranking of J1) from HTML code
'''
# Get the standings date
def get_standings_date(src) :
    start = src.find("更新日")
    end = src.find("</li>", start)
    if start > 0 and end > 0 :
        s_date = src[start:end]
    else :
        s_date = "error"

    return s_date

# Extract the team name
def extract_team_name(target_line) :
    index = target_line.find("</span>")
    team_name = target_line[index + 7:]
    return team_name

# Extract the standings part from the HTML code
def extract_standings(src) :
    j1_team = list()
    team_number = 18
    # Find start index and end index
    start = src.find("<table class=\"scoreTable01 J1table tablesorter\">")
    end = src.find("</table>")

    # Continue processing if there is the standings
    target_part = ""
    if start > 0 and end > 0:
        target_part = src[start:end]

        # Extract the team name
        # First, get the name of the top team
        start = target_part.find("<td class=\"tdTeam\">")
        end = target_part.find("</a></td>")
        if start > 0 and end > 0 :
            target_line = target_part[start:end]
            team_name = extract_team_name(target_line)
            j1_team.append(team_name)
        # Get the names of the remaining 17 team in order of rank
        for i in range(team_number - 1) :
            start = target_part.find("<td class=\"tdTeam\">", end)
            end = target_part.find("</a></td>", start)
            if start > 0 and end > 0 :
                target_line = target_part[start:end]
                team_name = extract_team_name(target_line)
                j1_team.append(team_name)

    return j1_team