from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q


from .models import BlogProfile,Category,Tag
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger



class baselist(View):
    def basehtml(request):
        return render(request,"base.html")


class indexlist(View):
    def indexhtml(request):
        return render_to_response("index.html")

class LoginView(View):
    def get(self,request):
        return render(request,"login.html",{})


    def post(self, request):
        login_form = LoginForm(request.POST)
        # LoginForm()在传进来的时候有一个参数，这个参数为字典，request.POST就是一个字典
        # 所以此处一般传入request.POST内容
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    from django.core.urlresolvers import reverse
                    return HttpResponseRedirect(reverse("index"))
                    # return render(request, "index.html")
                else:
                    return render(request, "login.html", {"msg": "用户未激活"})
            else:
                return render(request, "login.html", {"msg": "用户名密码错误"})
        else:
            return render(request, "login.html", {"login_form": login_form})


#
# class RegisterView(View):
#     def get(self,request):
#         register_form = RegisterForm()
#         return render(request,"login.html", {'register_form': register_form})
#
#     def post(self,request):
#         register_form = RegisterForm(request.POST)
#         if register_form.is_valid():
#             user_name = request.POST.get("email", "")
#             pass_word = request.POST.get("password", "")
#             if UserProfile.objects.filter(email=user_name):
#                 return render(request, "register.html", {"register_form": register_form, "msg": "用户已存在"})
#             user_profile = UserProfile()
#             user_profile.username = user_name
#             user_profile.email = user_name
#             user_profile.is_active = False
#             # 对明文密码进行加密
#             user_profile.password = make_password(pass_word)
#             user_profile.save()
#
#             # 写入欢迎注册消息
#             user_message = UserMessage()
#             user_message.users = user_profile.id
#             user_message.message = "欢迎注册"
#             user_message.save()
#
#             send_register_email(user_name,"register")
#             return render(request,"login.html")
#         else:
#             return render(request,"register.html", {"register_form": register_form})

class indexlistview(View):
    def get(self,request):
        all_blogs = BlogProfile.objects.all().order_by("-created")
        all_category=Category.objects.all().order_by("-id")
        category_1=all_category[0]
        category_2 = all_category[1]
        category_3 = all_category[2]
        category_1_text=BlogProfile.objects.filter(category=int(category_1.id))[:3]
        category_2_text = BlogProfile.objects.filter(category=int(category_2.id))[:3]
        category_3_text = BlogProfile.objects.filter(category=int(category_3.id))[:3]

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_blogs, 5, request=request)
        all_blog = p.page(page)

        return render(request,"detail.html",{
            'all_blog':all_blog,
            "category_1":category_1,
            "category_2":category_2,
            "category_3":category_3,
            "category_1_text":category_1_text,
            "category_2_text":category_2_text,
            "category_3_text":category_3_text
        })

    def post(self,request):
        search_keyword = request.POST.get('q', "")
        all_blogs = BlogProfile.objects.all()
        all_category=Category.objects.all().order_by("-id")
        category_1=all_category[0]
        category_2 = all_category[1]
        category_3 = all_category[2]
        category_1_text=BlogProfile.objects.filter(category=int(category_1.id))[:3]
        category_2_text = BlogProfile.objects.filter(category=int(category_2.id))[:3]
        category_3_text = BlogProfile.objects.filter(category=int(category_3.id))[:3]
        if search_keyword:
            all_orgs = all_blogs.filter(
                Q(title__icontains=search_keyword))
            # name__icontains django会把name转换为like语句
            # django的model中，出现了i，则不区分大小写
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            p = Paginator(all_orgs, 5, request=request)
            all_blog = p.page(page)
            return render(request, "detail.html", {
                'all_blog': all_blog,
                "category_1": category_1,
                "category_2": category_2,
                "category_3": category_3,
                "category_1_text": category_1_text,
                "category_2_text": category_2_text,
                "category_3_text": category_3_text

            })





        else:
            all_blogs = BlogProfile.objects.all()
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            p = Paginator(all_blogs, 5, request=request)
            all_blog = p.page(page)

            return render(request, "detail.html", {'all_blog': all_blog})




class detailview(View):
    def get(self,request,blog_id):
        blog=BlogProfile.objects.get(id=int(blog_id))
        all_blogs = BlogProfile.objects.all().order_by("-created")
        all_category=Category.objects.all().order_by("-id")
        category_1=all_category[0]
        category_2 = all_category[1]
        category_3 = all_category[2]
        category_1_text=BlogProfile.objects.filter(category=int(category_1.id))[:3]
        category_2_text = BlogProfile.objects.filter(category=int(category_2.id))[:3]
        category_3_text = BlogProfile.objects.filter(category=int(category_3.id))[:3]

        return render(request,"detail2.html",{
            'blog':blog,
            "category_1": category_1,
            "category_2": category_2,
            "category_3": category_3,
            "category_1_text": category_1_text,
            "category_2_text": category_2_text,
            "category_3_text": category_3_text
        })






