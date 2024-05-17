#Пример того, как с помощью Selenium можно выполнить скрейпинг 100 лучших фильмов IMDb:
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.imdb.com/chart/top")
movie_title_elements = driver.find_elements(By.CSS_SELECTOR, "a.ipc-title-link-wrapper h3")
rating_elements = driver.find_elements(By.CSS_SELECTOR, "span.ratingGroup--imdb-rating")

titles = [element.text for element in movie_title_elements]
# print(titles)
ratings = [element.text for element in rating_elements]
# print(ratings)
for i in range(10):
    print("Rank {}: {} ({} stars)".format(i + 1, titles[i], ratings[i]))
driver.quit()