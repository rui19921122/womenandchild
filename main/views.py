from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import RequestContext, render_to_response
from django.views.decorators.csrf import csrf_exempt
from xpinyin import Pinyin

from news.models import Article, Models, Comment, Picture, MainPic, SecondaryPic


# Create your views here.

def index(requests):
    if requests.method == 'GET':
        pic = MainPic.objects.filter(on_home=True)
        secondary = SecondaryPic.objects.filter()[:3]
        a = {'pic': pic, 'sec': secondary}
        return render_to_response('index.html', a)
    else:
        return Http404


def dep(requests, id, ):
    if requests.method == 'GET':
        page = requests.GET.get('page')
        try:
            model = Models.objects.filter(id=id)[0]
            article = Article.objects.filter(model=model)
        except:
            return Http404
        paginator = Paginator(article, 10)
        page_num = paginator.num_pages
        try:
            articles = paginator.page(page)
        except:
            return HttpResponseRedirect('/dep/{}?page={}'.format(id, 1))
        dic = {'articles': articles, 'page_num': int(page_num), 'cur_num': int(page), 'id': id, 'title': model.name}
        return render_to_response('news_display.html', dic)


def article(requests, id):
    if requests.method == 'GET':
        article_detail = Article.objects.get(id=id)
        comment = Comment.objects.filter(news=article_detail).order_by('create_time')[:15]
        dic = {'comments': comment, 'article': article_detail}
        return render_to_response('news.html', dic, context_instance=RequestContext(requests))


def comment(requests):
    if requests.method == 'POST' and requests.user.is_authenticated():
        article_id = requests.POST.get('article')
        content = requests.POST.get('content')
        if len(content) > 1:
            new_obj = Comment(user=User.objects.get(username=requests.user.username), content=content,
                              news=Article.objects.get(
                                      id=article_id))
            new_obj.save()
        return HttpResponseRedirect('article/{}'.format(article_id))
    elif requests.method == 'POST' and not requests.user.is_authenticated():
        article_id = requests.POST.get('article')
        if requests.META.get('HTTP_X_FORWARDED_FOR'):
            ip = requests.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = requests.META['REMOTE_ADDR']
        content = requests.POST.get('content')
        if len(content) > 1:
            new_obj = Comment(content=content, news=Article.objects.get(id=article_id), ip=ip)
            new_obj.save()
        return HttpResponseRedirect('article/{}'.format(article_id))


def register(requests):
    if requests.method == 'POST' and not requests.user.is_authenticated():
        username = requests.POST.get('username')


def search(requests):
    if requests.method == 'GET':
        query = requests.GET.get('search')
        if query:
            a = Article.objects.filter(name__contains=query)
            returned_dic = {'articles': a}
        else:
            returned_dic = {}
        return render_to_response('search.html', returned_dic)


@csrf_exempt
def uploads(request):
    if request.method == 'POST' and request.user.is_superuser:
        _image = request.FILES['upload']
        # _image = request.FILES.get('camera.jpg')
        number = request.GET.get('CKEditorFuncNum')
        # try:
        #     image = Image.open(_image, 'r')
        # except IOError as e:
        #     return render_to_response('ckeditor_return.html', {'error': '格式不正确{}'.format(e), 'number': number})
        # width, height = image.size
        # if width > 700:
        #     image = image.resize((700, int(700 * height / width)), Image.ANTIALIAS)
        f = Pinyin()
        new = Picture(pic=_image, name=f.get_pinyin(_image.name))
        new.save()
        url = new.pic.url
        return render_to_response('ckeditor_return.html', {'path': url, 'number': number})
