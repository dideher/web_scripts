import os
from openpyxl import load_workbook, Workbook #, utils

from django.shortcuts import render

from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.http import Http404, HttpResponse, FileResponse, HttpResponseRedirect
from .models import *
from .utilities import generate_curriculum_report
# Create your views here.



# Create your views here.
class HomePageView(TemplateView):
    template_name = "webscripts/home.html"
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
        # print(self.request.META['HTTP_REFERER'])
        # context['latest_articles'] = Article.objects.all()[:5]
        # return context
    # print(request.GET.referer)
    
    


def upload_curriculum_status_file(request):
    context = {'error_string': "",}
    if request.method == 'POST':
        # print('Method is post')
        # print(request.FILES)
        uploaded_file = request.FILES['document']
        generate_curriculum_report(uploaded_file)
        return FileResponse(open('./templates/webscripts/curriculum_report.xlsx', 'rb'), as_attachment=True, filename='Report.xlsx')
    else:
        return render(request, 'webscripts/upload_curriculum_status_file.html', context)