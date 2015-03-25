#coding:utf8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from models import News
from django.core.paginator import Paginator

# Create your views here.



def index(req):
	news_list= News.objects.order_by('id')[:5].reverse()
	return render_to_response('index.html', {'news_list': news_list})

def news(req,newsid=''):
	single_news = News.objects.get(id=newsid)

	previous_id = int(newsid)
	while 1:
		previous_id = previous_id - 1
		try:
			previous_title = News.objects.get(id=previous_id).title 
			previous_news = '<a href="/cn/news/%s">%s</a>' % (previous_id, previous_title)
			break
		except Exception,e:
			if previous_id > 0:
				continue
			else:
				previous_title = ''
				previous_news = '没有了'
				break

	next_id = int(newsid)
	while 1:
		next_id = next_id + 1
		try:
			next_title = News.objects.get(id=next_id).title
                	next_news = '<a href="/cn/news/%s">%s</a>' % (next_id, next_title)
			break
		except Exception,e:
			if next_id < int(News.objects.latest('id').id):
				continue
			else:
				next_title = ''
                		next_news = '没有了'
				break
	return render_to_response('html/newsbase.html', locals())

def newsmain(req):
	news_list= News.objects.order_by('id').reverse()
        return render_to_response('html/news.html', {'news_list': news_list}, context_instance=RequestContext(req))


def contact(req):
	return render_to_response('html/contact.html')
def hr(req):
	return render_to_response('html/hr.html')
def service(req):
	return render_to_response('html/service.html')
def release(req):
	return render_to_response('html/release.html')
def bookprodmain(req):
        return render_to_response('html/bookprod.html')
def partners(req):
	return render_to_response('html/partners.html')
def bookservice(req):
	return render_to_response('html/bookservice.html')
def hewentong(req):
	return render_to_response('html/hewentong.html')
def hwtprod(req):
	return render_to_response('html/hwtprod.html')
def hwtsoftware(req):
	return render_to_response('html/hwtsoftware.html')
def hwtsource(req):
	return render_to_response('html/hwtsource.html')
def about(req,aboutid=''):
	if aboutid == '1':
		return render_to_response('html/about1.html')
	if aboutid == '2':
		return render_to_response('html/about2.html')
	if aboutid == '3':
		return render_to_response('html/about3.html')
def aboutmain(req):
	return render_to_response('html/about1.html')
def othernews(req):
	news_list= News.objects.order_by('pub_date').reverse()
        return render_to_response('html/othernews.html', {'news_list': news_list}, context_instance=RequestContext(req))

def bookprod(req,bookid=''):
        if bookid == '1':
                return render_to_response('html/book1_page.html')
        if bookid == '2':
                return render_to_response('html/book2_page.html')
        if bookid == '3':
                return render_to_response('html/book3_page.html')

def vedio(req,vedioid=''):
	if vedioid== '1':
		return render_to_response('html/vedio1.html')
