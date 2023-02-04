import re
import requests
import xlsxwriter
from time import sleep
from bs4 import BeautifulSoup



my_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = "https://www.mealty.ru/"
column = 0
row = 1

response = requests.get(url, headers=my_headers)
soup = BeautifulSoup(response.text, "lxml")
data = soup.find_all("div", class_="meal-card")
data_file = open( 'data.txt', 'w' )
workbook = xlsxwriter.Workbook('/home/el/data.xlsx')
worksheet = workbook.add_worksheet()

worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 50)
worksheet.set_column('C:C', 6)
worksheet.set_column('D:D', 6)
worksheet.set_column('E:E', 6)
worksheet.set_column('F:F', 6)
worksheet.set_column('G:G', 6)
worksheet.set_column('H:H', 6)
worksheet.set_column('I:I', 40)
worksheet.set_column('J:J', 15)
worksheet.set_column('K:K', 6)
worksheet.set_column('L:L', 15)
bold = workbook.add_format({'bold': True})
worksheet.write('A1', 'Наименование', bold)
worksheet.write('B1', 'Описание', bold)
worksheet.write('C1', 'Mass, грамм', bold)
worksheet.write('D1', 'Белки', bold)
worksheet.write('E1', 'Жиры', bold)
worksheet.write('F1', 'Углеводы', bold)
worksheet.write('G1', 'Калл', bold)
worksheet.write('H1', 'Калл в порции', bold)
worksheet.write('I1', 'Состав', bold)
worksheet.write('J1', 'Срок годности', bold)
worksheet.write('K1', 'Цена', bold)
worksheet.write('L1', 'URL фото', bold)


for element in data:

    title = element.find("div", class_="meal-card__name").text
    worksheet.write(row, column, title)
    column += 1
    description = element.find("div", class_="meal-card__description").text
    worksheet.write(row, column, description)
    column += 1
    weight = element.find("div", class_="meal-card__weight").text
    worksheet.write(row, column, weight)
    column += 1
    proteins = element.find("div", class_="meal-card__proteins").text
    worksheet.write(row, column, proteins)
    column += 1
    fats = element.find("div", class_="meal-card__fats").text
    worksheet.write(row, column, fats)
    column += 1
    carbohydrates = element.find("div", class_="meal-card__carbohydrates").text
    worksheet.write(row, column, carbohydrates)
    column += 1
    calories = element.find("div", class_="meal-card__calories").text
    worksheet.write(row, column, calories)
    column += 1
    calories__portion = element.find("div", class_="meal-card__calories__portion").text
    worksheet.write(row, column, calories__portion)
    column += 1
    productes = element.find("div", class_="meal-card__products").text
    worksheet.write(row, column, productes)
    column += 1
    shelf_life = element.find("div", class_="meal-card__shelf_life").text
    worksheet.write(row, column, shelf_life)
    column += 1
    price = element.find("div", class_="meal-card__price").text
    worksheet.write(row, column, price)
    column += 1
    photo_url = "https://www.mealty.ru" + element.find("div", class_="hidden").find("div", class_="meal-card__photo").find("img").get("data-fancybox-src")
    worksheet.write(row, column, photo_url)
    column += 1

    row += 1
    column = 0

    # sleep(3)

workbook.close()