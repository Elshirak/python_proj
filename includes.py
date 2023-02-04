import requests
from bs4 import BeautifulSoup
from time import sleep
import re

my_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = "https://www.mealty.ru/"

response = requests.get(url, headers=my_headers)
soup = BeautifulSoup(response.text, "lxml")
data = soup.find_all("div", class_="meal-card")
data_file = open( 'data.txt', 'w' )

for element in data:

    title = element.find("div", class_="meal-card__name").text
    description = element.find("div", class_="meal-card__description").text
    weight = element.find("div", class_="meal-card__weight").text
    proteins = element.find("div", class_="meal-card__proteins").text
    fats = element.find("div", class_="meal-card__fats").text
    carbohydrates = element.find("div", class_="meal-card__carbohydrates").text
    calories = element.find("div", class_="meal-card__calories").text
    calories__portion = element.find("div", class_="meal-card__calories__portion").text
    productes = element.find("div", class_="meal-card__products").text
    shelf_life = element.find("div", class_="meal-card__shelf_life").text
    price = element.find("div", class_="meal-card__price").text
    photo_url = "https://www.mealty.ru" + element.find("div", class_="hidden").find("div", class_="meal-card__photo").find("img").get("data-fancybox-src")

    data_file.write("Наименование: %s\n" % title)
    data_file.write("Описание:%s\n" % description)
    data_file.write("Mass, грамм: %s\n" % weight)
    data_file.write("Белки: %s\n" % proteins)
    data_file.write("Жиры: %s\n" % fats)
    data_file.write("Углеводы: %s\n" % carbohydrates)
    data_file.write("Калл: %s\n" % calories)
    data_file.write("калл в порции: %s\n" % calories__portion)
    data_file.write("Состав: %s\n" % productes)
    data_file.write("Срок годности: %s\n" % shelf_life)
    data_file.write("Цена: %s\n" % price)
    data_file.write("URL фото: %s\n\n\n" % photo_url)

    sleep(3)


data_file.close()