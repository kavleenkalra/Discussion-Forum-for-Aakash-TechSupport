from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from forum.models import Post
from taggit.models import Tag


def tag(request):
	context=RequestContext(request)
	tags=Tag.objects.all			
	context_dict= {'tags': tags}
	return render_to_response('forum/tags.html', context_dict, context)
	
	
def linktag(request,id):
	context=RequestContext(request)
	tag= Tag.objects.get(pk=id)
	posts= Post.objects.filter(tags=tag)
	context_dict ={'posts':posts}
	return render_to_response('forum/questions.html', context_dict, context)
	
def tag_search(request):
	context=RequestContext(request)
	mytag = request.POST.get('search_text')
	try:
		tag= Tag.objects.get(name=mytag)
		posts=Post.objects.filter(tags=tag)
		#flag=1
		context_dict={'posts':posts}
	except Tag.DoesNotExist:
		#flag=0
		context_dict={}
		
	#context_dict={'flag':flag}	
		
	return render_to_response('forum/questions.html',context_dict,context) 
	
	

#def link_tag(request,tag_name_url):
#	context=RequestContext(request)
#	tag_name = tag_name_url.replace('_', ' ')
#	try:
#       tag= Tag.objects.get(name=tag_name)
#       posts= Post.objects.filter(tag=tag)
#        context_dict['posts'] = posts
#    except Tag.DoesNotExist:
#        pass
#    return render_to_response('forum/posts.html', context_dict, context)


