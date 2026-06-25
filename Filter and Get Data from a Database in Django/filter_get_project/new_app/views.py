from django.shortcuts import render
from new_app.models import *

def student_info_view(request):
    filter_option = request.GET.get('dept_name')

    student_data = StudentInfoModel.objects.all()
    if filter_option:
        if filter_option == 'all':
          student_data = StudentInfoModel.objects.all()
        else:
          student_data = StudentInfoModel.objects.filter(department=filter_option)
    context = {
        'student_data': student_data,
        'filter_option': filter_option,
    }

    return render(request, 'student-info.html', context)


