'''
    You can get the ranking of J1 league when this program is executed
    and the standings date from the J league official website.
'''
import sys, requests, my_html_analyzer as ha

j1_team = list()

# Get the information of "https://www.jleague.jp/standings/j1/"
response = requests.get("https://www.jleague.jp/standings/j1/")

# If abnormality is detected, the program is terminated
status_code = str(response.status_code)
if status_code != "200" :
    print("Error Occurred")
    print("HTTP Status Code: " + status_code)
    sys.exit()

# Get the page source(HTML code) of the page
page_src = str(response.text)

# Get the standings date
s_date = ha.get_standings_date(page_src)

# Extract the standings part from the HTML code
j1_team = ha.extract_standings(page_src)

# OutPut
print(s_date)
for i in range(0, len(j1_team)) :
    print(i + 1, j1_team[i])
# response.url
