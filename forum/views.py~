from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from forum.models import Post,Reply
from taggit.models import Tag


def tag(request):
	context=RequestContext(request)
	tags=Tag.objects.all()
	for tag in tags:
		tag.count=len(Post.objects.filter(tags=tag))
	context_dict= {'tags': tags}
	return render_to_response('forum/tags.html', context_dict, context)
	
	
def linktag(request,id):
	context=RequestContext(request)
	tag= Tag.objects.get(pk=id)
	posts= Post.objects.filter(tags=tag).order_by('-created_date')
	posts1= Post.objects.filter(tags=tag).order_by('-count')
	context_dict ={'posts':posts,'mytag':tag,'posts1':posts1}
	return render_to_response('forum/questions.html', context_dict, context)
	
def tag_search(request):
	context=RequestContext(request)
	mytag = request.POST.get('search_text')
	mytag=mytag.upper()
	try:
		tag= Tag.objects.get(name=mytag)
		posts=Post.objects.filter(tags=tag).order_by('-created_date')
		posts1= Post.objects.filter(tags=tag).order_by('-count')
		context_dict={'posts':posts,'mytag':tag,'posts1':posts1}
	except Tag.DoesNotExist:
		context_dict={}
	return render_to_response('forum/questions.html',context_dict,context) 
	
def questions(request,id,tagid):
	context=RequestContext(request)
	post=Post.objects.get(pk=id)
	mytag=Tag.objects.get(pk=tagid)
	reply=Reply.objects.filter(title=post)
	mypost=Post.objects.filter(tags=mytag).exclude(pk=id)
	context_dict={'posts':post,'reply':reply,'mytag':mytag,'mypost':mypost}
	return render_to_response('forum/reply.html',context_dict,context) 



