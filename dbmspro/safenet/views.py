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
from safenet.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from safenet.models import Plan, Custom, Bookings, ECommerce, Entertainment, Games, Illegal, Messaging, News, SocialMedia
import safenet.utils as utils
import os
import platform
import json

def index(request):
	return render(request,'safenet/index.html')

def plan_info(request):
	return render(request,'safenet/plan_info.html')

@login_required
def special(request):
	return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
	utils.unblockSites()
	logout(request)
	return HttpResponseRedirect(reverse('index'))

@login_required
def yourplans(request):
	return render(request, 'safenet/your_plans.html')

def signup(request):
	signedup = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		if user_form.is_valid(): 
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			signedup = True
		else:
			print(user_form.errors)
	else:
		user_form = UserForm()
	return render(request,'safenet/signup.html',
						  {'user_form':user_form,
						   'signedup':signedup})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request,user)

				OS = platform.system()

				host_file = None

				if OS == 'Windows':
					host_file = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
				elif OS == 'Darwin':
					host_file = '/etc/hosts'
				else:
					host_file = '/etc/hosts'

				cmd_str = 'sudo cp ' + host_file + ' ../etc_hosts'
				os.system(cmd_str)

				try:
					plan_urls = Plan.objects.get(usid=request.user.id)
					custom_urls = Custom.objects.filter(usid=request.user.id)

					urls = [plan_urls.bookings, plan_urls.ecommerce, plan_urls.entertainment, plan_urls.games, plan_urls.illegal, plan_urls.messaging, plan_urls.news, plan_urls.socialMedia]
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
	current_user = request.user
	if request.method == 'POST':
		try:
			plan_urls = Plan.objects.get(usid=current_user)
			custom_urls = Custom.objects.filter(usid=current_user)

			# urls = [plan_urls.bookings, plan_urls.ecommerce, plan_urls.entertainment, plan_urls.games, plan_urls.illegal, plan_urls.messaging, plan_urls.news, plan_urls.socialMedia]
			# for url in custom_urls:
			# 			urls.append(url.block)
			# 			urls.append(url.redirect)
			# with open('./safenet/static/safenet/javascript/urls.json', 'w') as f:
			# 	json.dump(urls, f)

			if plan_urls:
				plan_urls.delete()
			if custom_urls:
				custom_urls.delete()
		except:
			pass

		bookings = 'NULL'
		if request.POST.get('c1'):
			bookings = 'TRUE'
			if request.POST.get('s1'):
				bookings = request.POST.get('u1')
		ecommerce = 'NULL'
		if request.POST.get('c2'):
			ecommerce = 'TRUE'
			if request.POST.get('s2'):
				ecommerce = request.POST.get('u2')
		entertainment = 'NULL'
		if request.POST.get('c3'):
			entertainment = 'TRUE'
			if request.POST.get('s3'):
				entertainment = request.POST.get('u3')
		games = 'NULL'
		if request.POST.get('c4'):
			games = 'TRUE'
			if request.POST.get('s4'):
				games = request.POST.get('u4')
		illegal = 'NULL'
		if request.POST.get('c5'):
			illegal = 'TRUE'
			if request.POST.get('s5'):
				illegal = request.POST.get('u5')
		messaging = 'NULL'
		if request.POST.get('c6'):
			messaging = 'TRUE'
			if request.POST.get('s6'):
				messaging = request.POST.get('u6')
		news = 'NULL'
		if request.POST.get('c7'):
			news = 'TRUE'
			if request.POST.get('s7'):
				news = request.POST.get('u7')
		social_media = 'NULL'
		if request.POST.get('c8'):
			social_media = 'TRUE'
			if request.POST.get('s8'):
				social_media = request.POST.get('u8')

		plan_urls = Plan(usid=current_user, bookings=bookings, ecommerce=ecommerce, entertainment=entertainment,
			games=games, illegal=illegal, messaging=messaging, news=news, socialMedia=social_media)
		plan_urls.save()

		# Also do for without www.

		block1 = block2 = block3 = 'NULL'
		redirect1 = redirect2 = redirect3 = 'NULL'
		if request.POST.get('c9'):
			block1 = request.POST.get('c9')
			if request.POST.get('s9'):
				redirect1 = request.POST.get('u9')
		if request.POST.get('c10'):
			block2 = request.POST.get('c10')
			if request.POST.get('s10'):
				redirect2 = request.POST.get('u10')
		if request.POST.get('c11'):
			block3 = request.POST.get('c11')
			if request.POST.get('s11'):
				redirect3 = request.POST.get('u11')

		block1 = block1.replace('https://', '').replace('http://', '')
		redirect1 = redirect1.replace('https://', '').replace('http://', '')
		block2 = block2.replace('https://', '').replace('http://', '')
		redirect2 = redirect2.replace('https://', '').replace('http://', '')
		block3 = block3.replace('https://', '').replace('http://', '')
		redirect3 = redirect3.replace('https://', '').replace('http://', '')
				
		if block1 != 'NULL':
			url1 = Custom(usid=current_user, block=block1, redirect=redirect1)
			url1.save()
		if block2 != 'NULL':
			url2 = Custom(usid=current_user, block=block2, redirect=redirect2)
			url2.save()
		if block3 != 'NULL':
			url3 = Custom(usid=current_user, block=block3, redirect=redirect3)
			url3.save()

		new = list()
		new.append(plan_urls.bookings)
		new.append(plan_urls.ecommerce)
		new.append(plan_urls.entertainment)
		new.append(plan_urls.games)
		new.append(plan_urls.illegal)
		new.append(plan_urls.messaging)
		new.append(plan_urls.news)
		new.append(plan_urls.socialMedia)
		new.append(block1)
		new.append(redirect1)
		new.append(block2)
		new.append(redirect2)
		new.append(block3)
		new.append(redirect3)
		b = Bookings.objects.all()
		ec = ECommerce.objects.all()
		e = Entertainment.objects.all()
		g = Games.objects.all()
		il = Illegal.objects.all()
		m = Messaging.objects.all()
		n = News.objects.all()
		s = SocialMedia.objects.all()

		with open('./safenet/static/safenet/javascript/urls.json', 'w') as f:
			json.dump(new, f)

		utils.updateBlockedSites(new, b, ec, e, g, il, m, n, s)
		return render(request, 'safenet/your_plans.html', {})
	else:
		try:
			plan_urls = Plan.objects.get(usid=current_user)
			custom_urls = Custom.objects.filter(usid=current_user)

			urls = [plan_urls.bookings, plan_urls.ecommerce, plan_urls.entertainment, plan_urls.games, plan_urls.illegal, plan_urls.messaging, plan_urls.news, plan_urls.socialMedia]
			for url in custom_urls:
						urls.append(url.block)
						urls.append(url.redirect)
			with open('./safenet/static/safenet/javascript/urls.json', 'w') as f:
				json.dump(urls, f)

		except:
			urls = ['NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL']
			with open('./safenet/static/safenet/javascript/urls.json', 'w') as f:
				json.dump(urls, f)

		return render(request, 'safenet/your_plans.html', {})
