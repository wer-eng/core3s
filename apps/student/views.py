from typing import TYPE_CHECKING
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.student.form import StudentFilter
from .models import Student
from django.conf import settings
from django.views.generic.list import ListView
# Create your views here.
@login_required(login_url="/login/")
def studentUpdate(request):
    context={}
    return render(request, "student/std-profile.html", context)

@login_required(login_url="/login/")
def studentView(request):
    context={}
    return render(request, "student/std-profile.html", context)

@login_required(login_url="/login/")
def studentShowList(request):
    students = Student.objects.all()
    context = {
        'students' : students,
        'media_url':settings.MEDIA_URL
    }
    return render(request, "student/std-list.html", context)

@login_required(login_url="/login/")
def studentDelete(request):
    context={}
    return render(request, "student/std-profile.html", context)

@login_required(login_url="/login/")
def studentIndex(request):
    context={}
    return render(request, "student/std-profile.html", context)

@login_required(login_url="/login/")
def studentShowListFiltered(request,filterBy,filterValue):
    #...is there some way, given:
    filtertext = '{0}__{1}'.format(filterBy, 'startswith')
    filtersNames=['firstName','lastName']


 #...that you can run the equivalent of this ?
    
    students = Student.objects.filter(**{filtertext: filterValue})
    context = {
        'filtersKeys':filtersNames,
        
        'students' : students,
        'media_url':settings.MEDIA_URL
    }
    return render(request, "student/std-list.html", context)
class StudentFilterView(ListView):
    paginate_by = 3
    model = Student
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter']=StudentFilter(self.request.GET,queryset=self.get_queryset())
        
        return context
    
    template_name="student/std-list.html"
    def get_queryset(self):
        queryset = Student.objects.all()
        if self.request.GET.get("browse"):
            selection =  Student.objects.all()
            if selection == "firstname":
                queryset = Student.objects.all()
            elif selection == "lastname":
                queryset = Student.objects.all()
            elif selection == "TC":
                queryset = Student.objects.all()
            else:
                queryset = Student.objects.all()
        return queryset
