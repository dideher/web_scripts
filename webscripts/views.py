import os
from openpyxl import load_workbook, Workbook #, utils

from django.shortcuts import render

from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from django.http import Http404, HttpResponse, FileResponse, HttpResponseRedirect
from .models import MyMainMenu
from .utilities import generate_curriculum_report
from .forms import UploadFileForm
# Create your views here.



# Create your views here.
class MyMainMenuView(ListView):
    # template_name = "webscripts/mymainmenu_list.html"
    model = MyMainMenu
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # print(self.request.META['HTTP_REFERER'])
    #     context['main_menu_entries'] = MyMainMenu.objects.all()
    #     return context
    # # print(request.GET.referer)
    

def upload_curriculum_status_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Remove potentially existing deprecated versions of the output xlsx file. 
            if os.path.exists("/tmp/curriculum_report.xlsx"):
                os.remove("/tmp/curriculum_report.xlsx")
            generate_curriculum_report(request.FILES['file']) 
            return FileResponse(open('/tmp/curriculum_report.xlsx', 'rb'), as_attachment=True, filename='curriculum_report.xlsx')
    else:
        form = UploadFileForm()
    context = {"form": form}
    return render(request, 'webscripts/upload_curriculum_status_file.html', context)