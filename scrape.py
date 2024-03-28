import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
import sys

from selenium.webdriver.chrome.service import Service
service = Service(executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe')

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Owner\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
driver = webdriver.Chrome(options=options)
driver.get('https://ucsandiego-ncaabaseball.trumedianetworks.com/baseball')
time.sleep(3)

team = sys.argv[1].replace(".", " ")

#Find team using search bar
def find_team():
    search_bar = (
        driver
        .find_elements(By.CSS_SELECTOR, "*")[-2] #tmn-ferp-app
        .shadow_root.find_element(By.CSS_SELECTOR, "tmn-app-toolbar") #toolbar
        .find_element(By.CSS_SELECTOR, "tmn-baseball-site-search") #tmn-baseball-site-search
        .shadow_root.find_element(By.CSS_SELECTOR, '#search-input')
    )
    search_bar.clear()
    search_bar.send_keys(team)
    time.sleep(3)
    dropdown = (
    driver 
    .find_elements(By.CSS_SELECTOR, "*")[-2] #tmn-ferp-app
    .shadow_root.find_element(By.CSS_SELECTOR, "tmn-app-toolbar") #toolbar
    .find_element(By.CSS_SELECTOR, "tmn-baseball-site-search") #tmn-baseball-site-search
    # .shadow_root.find_elements(By.CSS_SELECTOR, "div[class='tmn-dropdown-section']")[-1] #team search results
    # .find_element(By.CSS_SELECTOR, 'div[class="tmn-dropdown-item]') #first team
    # .find_element(By.CSS_SELECTOR, "tmn-routed-link") #tmn-routed-link
    .shadow_root.find_elements(By.CSS_SELECTOR, "tmn-routed-link")[-1]
    .shadow_root.find_element(By.CSS_SELECTOR, "a")) #link


    driver.get(dropdown.get_attribute("href"))
    print("Team found")

#Overview -> Roster
def switch_to_roster():
    roster = (
        driver
        .find_elements(By.CSS_SELECTOR, "*")[-2] #tmn-ferp-app
        .shadow_root.find_elements(By.CSS_SELECTOR, "tmn-navbar[navlevel='3']")[0] #Overview, roster, etc toolbar
        .shadow_root.find_elements(By.CSS_SELECTOR, "tmn-nav-item[navlevel='3']")[2] #roster grid square
        .shadow_root.find_elements(By.CSS_SELECTOR, "*")[0] #tmn nav link
        .shadow_root.find_elements(By.CSS_SELECTOR, "*")[0] #tmn routed link
        .shadow_root.find_elements(By.CSS_SELECTOR, "*")[0] #thing with link
    )
    driver.get(roster.get_attribute("href"))
    print("Switched to roster page")


#Rate -> Counting
def switch_to_counting():
    rate = (
        driver
        .find_elements(By.CSS_SELECTOR, "*")[-2] #tmn-ferp-app
        .shadow_root.find_elements(By.CSS_SELECTOR, "main[role='main']")[0] #main
        .find_elements(By.CSS_SELECTOR, "tmn-page-router")[0] #tmn page router
        .shadow_root.find_elements(By.CSS_SELECTOR, "*")[0] #tmn team roster baseball
        .shadow_root.find_elements(By.CSS_SELECTOR, "tmn-table-controls-baseball")[0] #view options
        .shadow_root.find_elements(By.CSS_SELECTOR, "tmn-custom-report-select")[0] #rate button
        .shadow_root.find_elements(By.CSS_SELECTOR, "*")[0] #tmn select tabindex = 0
        .shadow_root.find_elements(By.CSS_SELECTOR, "*")[0] #tmn click away listener
    )
    rate.click()
    actions = ActionChains(driver)
    actions.send_keys("Counting")
    actions.send_keys(Keys.RETURN)
    actions.perform()
    print("Switched to counting stats")

#While on team -> Currently on team
def switch_to_currently_on_team():
    currently_on_team = (
        driver
        .find_elements(By.CSS_SELECTOR, "*")[-2] #tmn-ferp-app
        .shadow_root.find_elements(By.CSS_SELECTOR, "main[role='main']")[0] #main
        .find_elements(By.CSS_SELECTOR, "tmn-page-router")[0] #tmn page router
        .shadow_root.find_elements(By.CSS_SELECTOR, "*")[0] #tmn team roster baseball
        .shadow_root.find_elements(By.CSS_SELECTOR, "tmn-table-controls-baseball")[0] #view options
        .shadow_root.find_elements(By.CSS_SELECTOR, "tmn-page-control-set")[0] #row 1 stuff
        .shadow_root.find_elements(By.CSS_SELECTOR, "*")[1]
    )
    currently_on_team.click()
    actions = ActionChains(driver)
    actions.send_keys("Currently on team")
    actions.send_keys(Keys.RETURN)
    actions.perform()
    print("Switched to currently on team")


#Function to switch pitcher handedness in search filter
def switch_pitcher_hand(hand):
    search_filters = (
        driver
        .find_elements(By.CSS_SELECTOR, "*")[-2] #tmn-ferp-app
        .shadow_root.find_elements(By.CSS_SELECTOR, "main[role='main']")[0] #main
        .find_elements(By.CSS_SELECTOR, "tmn-page-router")[0] #tmn page router
        .shadow_root.find_elements(By.CSS_SELECTOR, "*")[0] #tmn team roster baseball
        .shadow_root.find_elements(By.CSS_SELECTOR, "context-provider > div.widthConstrainedContent > tmn-collapsible:nth-child(2) > tmn-filter-set:nth-child(1)")[0]
        .shadow_root.find_elements(By.CSS_SELECTOR, "tmn-filter-search")[0]
        .shadow_root.find_elements(By.CSS_SELECTOR, "tmn-select")[0]
        .shadow_root.find_elements(By.CSS_SELECTOR, "tmn-click-away-listener")[0]
    )


    collapse_button = (
        driver
        .find_elements(By.CSS_SELECTOR, "*")[-2] #tmn-ferp-app
        .shadow_root.find_elements(By.CSS_SELECTOR, "main[role='main']")[0] #main
        .find_elements(By.CSS_SELECTOR, "tmn-page-router")[0] #tmn page router
        .shadow_root.find_elements(By.CSS_SELECTOR, "*")[0] #tmn team roster baseball
        .shadow_root.find_elements(By.CSS_SELECTOR, "context-provider > div.widthConstrainedContent > tmn-collapsible:nth-child(2)")[0] #tmn-collapsable
        .shadow_root.find_elements(By.CSS_SELECTOR, "tmn-grid > tmn-grid.iconContainer > tmn-icon-button")[0] #tmn icon button
        #.shadow_root.find_elements(By.CSS_SELECTOR, "*")[0] #button
    )

    filters = (
        driver
        .find_element(By.CSS_SELECTOR, "tmn-ferp-app")
        .shadow_root.find_element(By.CSS_SELECTOR, "tmn-page-router")
        .shadow_root.find_element(By.CSS_SELECTOR, "tmn-team-roster-baseball")
        .shadow_root.find_element(By.CSS_SELECTOR, "tmn-filter-set")
        .shadow_root.find_elements(By.CSS_SELECTOR, "tmn-filter")
    )
    if len(filters) > 1:
        hand_x = (
            filters[1]
            .shadow_root.find_element(By.CSS_SELECTOR, "tmn-filter-type-select")
            .shadow_root.find_element(By.CSS_SELECTOR, "tmn-filter-chip")
            .shadow_root.find_element(By.CSS_SELECTOR, 'tmn-icon-button[slot="startIcon"]')
            #.shadow_root.find_element(By.CSS_SELECTOR, "tmn-grid") #
            #.find_element(By.CSS_SELECTOR, "tmn-grid")
        )
        hand_x.click()
    try:
        search_filters.click()
    except:
        collapse_button.click()
        search_filters.click()
        
    actions = ActionChains(driver)
    actions.send_keys("Pitcher Hand: " + hand)
    actions.send_keys(Keys.RETURN)
    actions.perform()
    print("Switched to " + hand)

#Function to download the stats with current filters
def download_stats():
    exports_button = (
        driver
        .find_elements(By.CSS_SELECTOR, "*")[-2] #tmn-ferp-app
        .shadow_root.find_elements(By.CSS_SELECTOR, "main[role='main']")[0] #main
        .find_elements(By.CSS_SELECTOR, "tmn-page-router")[0] #tmn page router
        .shadow_root.find_elements(By.CSS_SELECTOR, "*")[0] #tmn team roster baseball
        .shadow_root.find_elements(By.CSS_SELECTOR, "context-provider > div.widthConstrainedContent > tmn-collapsible.reportControls > tmn-table-controls-baseball")[0] #tmn controls baseball
        .shadow_root.find_elements(By.CSS_SELECTOR, "div > div.row2-right > tmn-exports-list-baseball")[0] #tmn-exports-list-baseball
    )
    exports_button.click()
    export_button = (
        driver
        .find_elements(By.CSS_SELECTOR, "*")[-2] #tmn-ferp-app
        .shadow_root.find_elements(By.CSS_SELECTOR, "main[role='main']")[0] #main
        .find_elements(By.CSS_SELECTOR, "tmn-page-router")[0] #tmn page router
        .shadow_root.find_elements(By.CSS_SELECTOR, "*")[0] #tmn team roster baseball
        .shadow_root.find_elements(By.CSS_SELECTOR, "context-provider > div.widthConstrainedContent > tmn-collapsible.reportControls > tmn-table-controls-baseball")[0] #tmn controls baseball
        .shadow_root.find_elements(By.CSS_SELECTOR, "div > div.row2-right > tmn-exports-list-baseball")[0] #tmn-exports-list-baseball
        .shadow_root.find_elements(By.CSS_SELECTOR, "tmn-modal > div:nth-child(1) > tmn-grid > tmn-button:nth-child(1)")[0] #
        .shadow_root.find_elements(By.CSS_SELECTOR, "button")[0] #button
    )
    export_button.click()
    print("Downloaded")



#Function to switch season filter
def switch_season(season):
    season_button = (
        driver
        .find_element(By.CSS_SELECTOR, "tmn-ferp-app")
        .shadow_root.find_element(By.CSS_SELECTOR, "tmn-page-router")
        .shadow_root.find_element(By.CSS_SELECTOR, "tmn-team-roster-baseball")
        .shadow_root.find_element(By.CSS_SELECTOR, 'tmn-filter-set[slot="collapsedContent"]')
        .shadow_root.find_element(By.CSS_SELECTOR, "tmn-filter")
        .shadow_root.find_element(By.CSS_SELECTOR, "tmn-filter-type-select")
        .shadow_root.find_element(By.CSS_SELECTOR, "tmn-filter-chip")
    )
    season_button.click()
    actions = ActionChains(driver)
    actions.send_keys(Keys.BACKSPACE)
    actions.send_keys(str(season))
    actions.send_keys(Keys.RETURN)
    actions.perform()
    return 

def load_most_recent_sheet():
    sheet = list(filter(lambda x: "export " in x, os.listdir("C:/Users/Owner/Downloads")))[-1]
    return pd.read_csv("C:/Users/Owner/Downloads/" + sheet)

find_team()
time.sleep(3)
switch_to_roster()
time.sleep(3)
switch_to_counting()
time.sleep(3)
switch_to_currently_on_team()
time.sleep(3)
switch_pitcher_hand("Lefty")
time.sleep(4)
download_stats()
time.sleep(3)
lefty_currrent = load_most_recent_sheet()
switch_pitcher_hand("Righty")
time.sleep(4)
download_stats()
time.sleep(3)
righty_current = load_most_recent_sheet()
switch_season(2023)
time.sleep(3)
switch_pitcher_hand("Lefty")
time.sleep(4)
download_stats()
time.sleep(3)
lefty_previous = load_most_recent_sheet()
switch_pitcher_hand("Righty")
time.sleep(4)
download_stats()
time.sleep(3)
righty_previous = load_most_recent_sheet()
driver.close()

lefty_previous = lefty_previous.assign(Against = "L")
lefty_currrent = lefty_currrent.assign(Against = "L")
righty_previous = righty_previous.assign(Against = "R")
righty_current = righty_current.assign(Against = "R")
current_season = pd.concat([lefty_currrent, righty_current])
current_season = current_season.assign(Time = "")
current_season = current_season.assign(Bunt = "")
current_season = current_season.groupby(['playerFullName', 'Against', 'Time', "Bunt"]).max()
current_season = current_season.drop(columns=["playerId", "abbrevName", "player", "newestTeamName", "newestTeamAbbrevName", "newestTeamId", "newestTeamLocation", "newestTeamLevel"])

previous_season = pd.concat([lefty_previous, righty_previous])
previous_season = previous_season.assign(Time = "")
previous_season = previous_season.assign(Bunt = "")
previous_season = previous_season.groupby(['playerFullName', 'Against', 'Time', "Bunt"]).max()
previous_season = previous_season.drop(columns=["playerId", "abbrevName", "player", "newestTeamName", "newestTeamAbbrevName", "newestTeamId", "newestTeamLocation", "newestTeamLevel"])

def assign_in_prev():
    in_prev = []
    prev_names = previous_season.reset_index().get("playerFullName")[::2]
    prev_names = list(prev_names)
    for i in range(current_season.shape[0]):
        if current_season.index[i][0] in prev_names:
            in_prev += [True]
        else:
            in_prev += [False]
    current_season["inPrev"] = in_prev

assign_in_prev()

to_add = current_season[current_season.get("inPrev") == False]
to_add = to_add.drop(columns = ["inPrev"])

combined = pd.concat([previous_season, to_add])

combined.to_csv("C:/Users/Owner/Downloads/" + team.replace(" ", "-") + "-sheet.csv")



