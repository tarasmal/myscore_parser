#!C:/Users/Family/python374/
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.myscore.ua/soccer/england/premier-league-2018-2019/")
parent = driver.current_window_handle
iteration = 0
players = {}
while iteration <= 2:
	try:
		WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"a.event__more.event__more--static")))
		sleep(3)
		driver.find_element(By.CSS_SELECTOR,"a.event__more.event__more--static").click()
		iteration += 1
		print("clicked")
	except:
		iteration += 1
		print(":(")
sleep(5)
scroll = driver.find_element_by_tag_name("html")
scroll.send_keys(Keys.HOME)
driver.maximize_window()
m = 0	
print(len(driver.find_elements(By.XPATH,"//div[@title='Подробиці матчу!']")))	
for match in driver.find_elements(By.XPATH,"//div[@title='Подробиці матчу!']"):
	match.click()
	m += 1
	if m % 5 == 0:
				for p in players:
					print(p,players[p])		
	print(m)
	WebDriverWait(driver,10).until(EC.number_of_windows_to_be(2))
	for handle1 in driver.window_handles:
		if handle1 != parent:
			driver.switch_to_window(handle1)
			WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"a#a-match-lineups")))
			driver.find_element(By.CSS_SELECTOR,"a#a-match-lineups").click()
			WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.team-text.tname-home")))
			WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"span.scoreboard")))
			team1_goals = driver.find_elements(By.CSS_SELECTOR,"span.scoreboard")[0].text
			team2_goals = driver.find_elements(By.CSS_SELECTOR,"span.scoreboard")[1].text
			team1 = driver.find_element(By.CSS_SELECTOR,"div.team-text.tname-home").text
			team2 = driver.find_element(By.CSS_SELECTOR,"div.team-text.tname-away").text
			WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.name")))
			for x in range(21):

				if "(К)" in driver.find_elements(By.CSS_SELECTOR,"div.name")[x].text:
						name = driver.find_elements(By.CSS_SELECTOR,"div.name")[x].text[:-3]
				else:
					name = driver.find_elements(By.CSS_SELECTOR,"div.name")[x].text
					
				if x % 2 == 0:
					team = team1
					if name in players:
						if team1_goals > team2_goals:
							players[name]["matches"] += 1
							players[name]["wins"] += 1
						if team1_goals < team2_goals:
							players[name]["matches"] += 1
							players[name]["loses"] += 1
						if team1_goals == team2_goals:
							players[name]["matches"] += 1
							players[name]["draws"] += 1
					if name not in players:
						if team1_goals > team2_goals:
							matches = 1
							wins = 1
							loses = 0
							draws = 0
							players[name] = {"matches":matches,
											"wins":wins,
											"loses":loses,
											"draws":draws,
											"team":team}
						if team1_goals < team2_goals:
							matches = 1
							wins = 0
							loses = 1
							draws = 0
							players[name] = {"matches":matches,
											"wins":wins,
											"loses":loses,
											"draws":draws,
											"team":team}
						if team1_goals == team2_goals:
							matches = 1
							wins = 0
							loses = 0
							draws = 1
							players[name] = {"matches":matches,
											"wins":wins,
											"loses":loses,
											"draws":draws,
											"team":team}

				if x % 2 != 0:
					team = team2
					if name in players:
						if team2_goals > team1_goals:
							players[name]["matches"] += 1
							players[name]["wins"] += 1
						if team2_goals < team1_goals:
							players[name]["matches"] += 1
							players[name]["loses"] += 1
						if team1_goals == team2_goals:
							players[name]["matches"] += 1
							players[name]["draws"] += 1
					if name not in players:
						if team2_goals > team1_goals:
							matches = 1
							wins = 1
							loses = 0
							draws = 0
							players[name] = {"matches":matches,
											"wins":wins,
											"loses":loses,
											"draws":draws,
											"team":team}
						if team2_goals < team1_goals:
							matches = 1
							wins = 0
							loses = 1
							draws = 0
							players[name] = {"matches":matches,
											"wins":wins,
											"loses":loses,
											"draws":draws,
											"team":team}
						if team2_goals == team1_goals:
							matches = 1
							wins = 0
							loses = 0
							draws = 1
							players[name] = {"matches":matches,
											"wins":wins,
											"loses":loses,
											"draws":draws,
											"team":team}

			driver.close()
			driver.switch_to_window(parent)