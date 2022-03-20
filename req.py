import requests   #импорт библиотеки

url = 'https://www.youtube.com/watch?v=4NcSDmuqsoY'    #url запрос
query = {'search_query':'audi'}
response = requests.post(url, data = query)


print('status code:   ', response.status_code)  #статус кода
print('url:   ', response.url)     #вывод url 