from django.shortcuts import render
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,UpdateView,
                                DeleteView)
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import School

# Create your views here.
def index(request):
    return render(request,'posts/index.html')
    
class CBView(View):
    def get(self, request):
        return HttpResponse("실행완료!!!")
    
class IndexView(TemplateView):
    template_name = 'posts/cbv_index.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['greeting'] = "안녕하세요!!"
        return context

class SchoolListView(ListView):
    model = School
    # schools = School.objects.all()
    template_name = 'posts/school_list.html'
    # return render(request,'posts/school_list.html',{'schools':schools})
    
class SchoolDetailView(DetailView):
    model = School
    template_name = 'posts/school_detail.html'

class SchoolCreateView(CreateView):
    model = School
    fields = ('name','location')
    
class SchoolUpdateView(UpdateView):
    model = School
    fields = ('name',)

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy("posts:list")