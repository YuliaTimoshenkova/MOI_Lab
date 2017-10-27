import requests
from bs4 import BeautifulSoup


def AnalisList(url):
    article_url = url
    r = requests.get(article_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    # Слова в заголовке
    WordsInTitle = len(soup.html.head.title.string.split())
    # Слова в статье
    WordsInArticle = len(soup.html.body.get_text().split())
    # Слова в подзаглоовке 
    WordsInDescription = len(soup.html.meta.get('content').split())
    # Количество изображений в статье
    ImagesNumber = len(soup.html.body.find_all('img'))      
    # Количество ссылок на другие новости e1.ru
    LinksNumber = len(soup.find_all('a', {"class":"news"}))   
    # Количество просмотров
    ViewNumber = int(soup.find_all('strong', {"class":"small_black"})[1].string)
    # Выделение количества комментариев
    text = soup.get_text()
    i1 = text.find('просмотров:')
    i2 = text.find('версия для печати')
    fragment = text[i1:i2-3]
    # Выделение количества комментариев
    if (fragment.find('(') == -1):
        CommentsNumber = 0
    else:
        CommentsNumber = int(soup.find_all('strong', {"class":"small_black"})[2].string[:-1][2:]) 
    # Категория статьи 
    NumberCategories = 19
    AnalisList = [WordsInTitle, WordsInArticle, WordsInDescription, 
           ImagesNumber, LinksNumber, ViewNumber, CommentsNumber, NumberCategories]
    return(AnalisList)