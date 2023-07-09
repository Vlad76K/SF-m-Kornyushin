from django.shortcuts import render

# Create your views here.
# # импорт Api новостей
# from django.shortcuts import render
# from newsapi import NewsApiClient
#
# # Создание функции представления
# def index(request):
#     # Для работы функции Api необходмо заменить YOURKEY на соответствующий ключ
#     newsapi = NewsApiClient(api_key ='YOURKEY')
#     top = newsapi.get_top_headlines(sources ='techcrunch')
#
#     l = top['articles']
#     dsc =[]
#     nws =[]
#     im =[]
#
#     for i in range(len(l)):
#       f = l[i]
#       nws.append(f['title'])
#       dsc.append(f['description'])
#       im.append(f['urlToImage'])
#       mylist = zip(nws, dsc, im)
#
#     return render(request, 'index.html', context ={"mylist":mylist})
#
