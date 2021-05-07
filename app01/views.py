from django.shortcuts import redirect, HttpResponse, render
from app01 import models


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)
        user_obj = models.User.objects.filter(username=username).first()
        print(user_obj.password)
        if password == user_obj.password:
            print('1111111')

        if user_obj:
            if password == user_obj.password:
                print('qqq')
                return HttpResponse('登录成功')
            else:
                return HttpResponse('密码错误')
        else:
            return HttpResponse('用户不存在')

    else:
        return render(request, 'login.html')


def register(requset):
    if requset.method == "POST":
        username = requset.POST.get('username')
        password = requset.POST.get('password')
        # user_obj = models.User(username=username,password=password)
        # user_obj.save()
        res = models.User.objects.create(username=username, password=password)
    return render(requset, 'register.html')


def userlist(request):
    user_queryset = models.User.objects.all()

    return render(request, 'userlist.html', locals())


def edit_user(request):
    if request.method == "POST":
        nid = request.GET.get('nid')
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        models.User.objects.filter(id=nid).update(username=username, password=password)
        return redirect('/userlist/')
    nid = request.GET.get('nid')
    res = models.User.objects.filter(id=nid).first()
    return render(request, 'edit_user.html', locals())


def del_user(request):
    nid = request.GET.get('nid')
    models.User.objects.filter(id=nid).delete()
    return redirect('/userlist/')


def add_file(request):
    if request.method == "POST":
        file_obj = request.FILES.get('file')
        with open(file_obj.name, 'wb') as fp:
            for line in file_obj.chunks():
                fp.write(line)
        return HttpResponse('上传成功')
    return render(request, 'form.html')


from django.views import View


class Mylogin(View):
    def get(self, request):
        return render(request, 'form.html')

    def post(self, request):
        return HttpResponse('POST')


def home(request):
    return render(request, 'home.html')

def book_list(request):
    book_queryset = models.Book.objects.all()

    return render(request, 'book_list.html', locals())


def book_add(request):
    publish_queryset = models.Publish.objects.all()
    author_queryset = models.Author.objects.all()
    if request.method == "POST":
        print('ok')
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish_date = request.POST.get('publish_date')
        publish_id = request.POST.get('publish')
        authors_list = request.POST.getlist('authors')
        book_obj = models.Book.objects.create(title=title, price=price, publish_data=publish_date,
                                              publish_id=publish_id)
        book_obj.authors.add(*authors_list)
        print(title)
        print('ok')
        return redirect('/book/')
    else:
        print('error')
        return render(request, 'book_add.html', locals())
def book_del(request):
    nid = request.GET.get('nid')
    models.Book.objects.filter(pk=nid).delete()
    return redirect('/book/')
def book_edit(request):

    nid = request.GET.get('nid')
    book_quryset = models.Book.objects.filter(pk=nid)
    publish_queryset = models.Publish.objects.all()
    author_queryset = models.Author.objects.all()
    if request.method=="POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish_date = request.POST.get('publish_date')
        publish_id = request.POST.get('publish')
        authors_list = request.POST.getlist('authors')
        book_obj = models.Book.objects.get(pk=nid)
        models.Book.objects.filter(pk=nid).update(title=title,price=price,publish_data=publish_date,publish_id=publish_id)
        return redirect('/book/')


    return render(request,'book_edit.html',locals())
def author(request):
    author_queryset = models.Author.objects.all()

    return render(request,'author.html',locals())