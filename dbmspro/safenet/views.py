'''from django.shortcuts import render


def index(request):
    return render(request,'safenet/index.html')

def plan_info(request):
    return render(request,'safenet/plan_info.html')

def login(request):
    return render(request,'safenet/login.html')

def signup(request):
    return render(request,'safenet/signup.html')
'''


from django.shortcuts import render
from safenet.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from safenet.models import Plan, Custom, Bookings, ECommerce, Entertainment, Games, Illegal, Messaging, News, SocialMedia
import safenet.utils as utils

def index(request):
    return render(request,'safenet/index.html')

def plan_info(request):
    return render(request,'safenet/plan_info.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def yourplans(request):
    return render(request, 'safenet/your_plans.html')

def signup(request):
    signedup = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid(): 
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            signedup = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'safenet/signup.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'signedup':signedup})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)

                try:
                    plan_urls = Plan.objects.get(usid=user.id)
                    custom_urls = Custom.objects.get(usid=user.id)
                
                    
                    urls = list(plan_urls.bookings, plan_urls.ecommerce, plan_urls.entertainment, plan_urls.games, plan_urls.illegal, plan_urls.messaging,
                    plan_urls.news, plan_urls.social_media)
                    for url in custom_urls:
                        urls.append(url.block)
                        urls.append(url.redirect)
                    b = Bookings.objects.all()
                    ec = ECommerce.objects.all()
                    e = Entertainment.objects.all()
                    g = Games.objects.all()
                    il = Illegal.objects.all()
                    m = Messaging.objects.all()
                    n = News.objects.all()
                    s = SocialMedia.objects.all()

                    utils.blockSites(urls, b, ec, e, g, il, m, n, s)
                    
                except:
                    plan_urls=None
                    custom_urls=None
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'safenet/login.html', {})

def your_plans(request):
    current_user_id = request.user.id
    if request.method == 'POST':
        try:
            plan_urls = Plan.objects.get(usid=current_user_id)
            custom_urls = Custom.objects.filter(usid=current_user_id)

            old = list(plan_urls.bookings, plan_urls.ecommerce, plan_urls.entertainment, plan_urls.games, plan_urls.illegal, plan_urls.messaging,
                plan_urls.news, plan_urls.social_media)
            for url in custom_urls:
                old.append(url.block)
                old.append(url.redirect)

            if plan_urls:
                plan_urls.delete()
            if custom_urls:
                custom_urls.delete()

            bookings = None
            if request.POST.get('c1'):
                bookings = 'TRUE'
                if request.POST.get('s1'):
                    bookings = request.POST.get('u1')
            ecommerce = None
            if request.POST.get('c2'):
                ecommerce = 'TRUE'
                if request.POST.get('s2'):
                    ecommerce = request.POST.get('u2')
            entertainment = None
            if request.POST.get('c3'):
                entertainment = 'TRUE'
                if request.POST.get('s3'):
                    entertainment = request.POST.get('u3')
            games = None
            if request.POST.get('c4'):
                games = 'TRUE'
                if request.POST.get('s4'):
                    games = request.POST.get('u4')
            illegal = None
            if request.POST.get('c5'):
                illegal = 'TRUE'
                if request.POST.get('s5'):
                    illegal = request.POST.get('u5')
            messaging = None
            if request.POST.get('c6'):
                messaging = 'TRUE'
                if request.POST.get('s6'):
                    messaging = request.POST.get('u6')
            news = None
            if request.POST.get('c7'):
                news = 'TRUE'
                if request.POST.get('s7'):
                    news = request.POST.get('u7')
            social_media = None
            if request.POST.get('c8'):
                social_media = 'TRUE'
                if request.POST.get('s8'):
                    social_media = request.POST.get('u8')

            plan_urls = Plan(usid=current_user_id, bookings=bookings, ecommerce=ecommerce, entertainment=entertainment,
                games=games, illegal=illegal, messaging=messaging, news=news, socialMedia=social_media)
            plan_urls.save()

            block1 = block2 = block3 = None
            redirect1 = redirect2 = redirect3 = None
            if request.POST.get('c9'):
                block1 = request.POST.get('c9')
                if request.POST.get('s9'):
                    redirect1 = request.POST.get('u9')
            if request.POST.get('c10'):
                block1 = request.POST.get('c10')
                if request.POST.get('s10'):
                    redirect1 = request.POST.get('u10')
            if request.POST.get('c11'):
                block1 = request.POST.get('c11')
                if request.POST.get('s11'):
                    redirect1 = request.POST.get('u11')
                    
            url1 = Custom(usid=current_user_id, block=block1, redirect=redirect1)
            url2 = Custom(usid=current_user_id, block=block2, redirect=redirect2)
            url3 = Custom(usid=current_user_id, block=block3, redirect=redirect3)
            url1.save()
            url2.save()
            url3.save()

            new = list(plan_urls.bookings, plan_urls.ecommerce, plan_urls.entertainment, plan_urls.games, plan_urls.illegal, plan_urls.messaging,
                plan_urls.news, plan_urls.social_media, url1.block, url1.redirect, url2.block, url2.redirect ,url3.block, url3.redirect)
            b = Bookings.objects.all()
            ec = ECommerce.objects.all()
            e = Entertainment.objects.all()
            g = Games.objects.all()
            il = Illegal.objects.all()
            m = Messaging.objects.all()
            n = News.objects.all()
            s = SocialMedia.objects.all()

            utils.updateBlockedSites(old, new, b, ec, e, g, il, m, n, s)
        except:
            plan_urls=None
            custom_urls=None
        return render(request, 'safenet/your_plans.html', {})
    else:
        return render(request, 'safenet/your_plans.html', {})