from django.shortcuts import render
from django.http import Http404
import markdown
from .models import Topic
from .models import Entry

# Create your views here.

def index(request):
	"""homepage of myblog"""
	return render(request, 'myblog/index.html')

def topics(request):
	topics = Topic.objects.order_by('date_added')
	context = {'topics':topics}
	return render(request, 'myblog/topics.html', context)

def entries(request):
	entries = Entry.objects.order_by('date_added')
	context = {'entries':entries}
	return render(request, 'myblog/entries.html', context)

def detail(request, entry_id):
	try:
		entry = Entry.objects.get(pk=entry_id)
		entry.text = markdown.markdown(entry.text, extensions=['markdown.extensions.extra','markdown.extensions.codehilite','markdown.extensions.toc'])
	except Entry.DoesNotExist:
		raise Http404("Entry does not exist")
	return render(request, 'myblog/detail.html', {'entry': entry})