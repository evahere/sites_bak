from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from blog.models import Article,Category
from django.core.paginator import Paginator

# Create your views here.


def get_index_page(request):
    category_list = Category.objects.exclude(pk=1)
    # 通过for循环找出live对象
    live_obj = None
    for category in category_list:
        if category.name == 'live':
            live_obj = category

    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    # article_list = Article.objects.all()
    article_list = Article.objects.order_by('-publish_date')
    paginator = Paginator(article_list,7)
    page_num = paginator.num_pages
    print('page num:',page_num)
    page_article_list = paginator.page(page)
    if page_article_list.has_next():
        next_page = page+1
    else:
        next_page = page
    if page_article_list.has_previous():
        previous_page = page-1
    else:
        previous_page = page

    return render(request,'blog/index.html',
                  {'article_list':page_article_list,
                   'page_num':range(1,page_num+1),
                   'cur_page':page,
                   'next_page':next_page,
                   'previous_page':previous_page,
                   'category_list': category_list,
                   'live_obj': live_obj,
                   })


# def get_details_page(request,article_id):
#     previous_article = None
#     cur_article = None
#     next_article = None
#     article_list = Article.objects.all()
#     for article in article_list:
#         # if article_id == 1 and article.article_id == 1:
#         #     previous_article = article
#         #     continue
#         if article_id == 1:
#             previous_article = article
#         elif article_id == len(article_list):
#             next_article = article
#         if article.article_id == article_id-1:
#             previous_article = article
#         elif article.article_id == article_id:
#            cur_article = article
#         elif article.article_id == article_id+1:
#             next_article = article
#             break
#     section_list = cur_article.content.split('\n')
#     return render(request,'blog/details.html',
#                   {'article_list':article_list,
#                    'section_list':section_list,
#                    'article':cur_article,
#                    'previous_article':previous_article,
#                    'next_article':next_article})


def get_details_page(request,article_id):
    previous_article = None
    cur_article = None
    next_article = None
    previous_index = 0
    next_index = 0
    article_list = Article.objects.all()
    top7_article_list = Article.objects.order_by('-publish_date')[0:7]
    for index,article in enumerate(article_list):
        if index == 0:
            previous_index = 0
            next_index = index+1
        elif index == len(article_list)-1:
            previous_index = index-1
            next_index = index
        else:
            previous_index = index-1
            next_index = index+1
        if article.article_id == article_id:
           cur_article = article
           previous_article = article_list[previous_index]
           next_article = article_list[next_index]
           views_details = get_object_or_404(Article,pk=article_id)
           views_details.increase_views()
           break
    return render(request,'blog/details.html',
                  {'article_list':article_list,
                   # 'section_list':section_list,
                   'article':cur_article,
                   'previous_article':previous_article,
                   'next_article':next_article,
                   'top7_article_list':top7_article_list})


def get_category_list(request,category_id):
    cate = get_object_or_404(Category,pk=category_id)
    categorys = Article.objects.filter(category=cate)
    return render(request,'blog/category_page.html',{'categorys':categorys})


def get_live_page(request):
    cate = get_object_or_404(Category,pk=1)
    lives_list = Article.objects.filter(category=cate)
    category_list = Category.objects.exclude(pk=1)
    return render(request,'blog/live.html',{'lives_list':lives_list,
                                            'category_list':category_list})


def get_about_page(request):
    return render(request,'blog/about.html')
