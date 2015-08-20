from django.shortcuts import render

# Create your views here.


def learn_plan(request):

    return render(request, 'student/my-center-file/learn_plan.html', locals())


def my_favorites(request):

    return render(request, 'student/my-center-file/my-favorites.html', locals())


def my_courses(request):

    return render(request, 'student/my-center-file/my_courses.html', locals())


def my_certificates(request):

    return render(request, 'student/my-center-file/my_certificates.html', locals())


def my_messages(request):

    return render(request, 'student/my-center-file/my_messages.html', locals())


def my_information(request):

    return render(request, 'student/my-center-file/my_information.html', locals())


def modify_email(request):

    return render(request, 'student/modify_email.html', locals())