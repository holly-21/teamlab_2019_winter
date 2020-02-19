import q as q
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from .models import Wt


# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'webapp/index.html', context)


def about(request):
    context = {

    }
    return render(request, 'webapp/about.html', context)


def search(request):
    context = {

    }
    return render(request, 'webapp/search.html', context)


def list(request):
    qs = Wt.objects.all()

    context = {
        'qs': qs
    }
    return render(request, 'webapp/list.html', context)


def result(request):
    qs = Wt.objects.all()
    search_word = request.GET.get('search_word')
    search_type = request.GET.get('search_type')

    # w_data = qs.filter(search_word)
    # if w_data is None:
    #     context = {
    #         HttpResponse('검색결과가 존재하지 않습니다.')
    #     }
    #     return render(request, 'webapp/result.html', context)
    try:
        if search_type == '작가':
            data = qs.filter(Q(wt_writer__icontains=search_word))
            context = {
                'data': data
            }
            return render(request, 'webapp/result.html', context)
        elif search_type == '요일':
            data = qs.filter(Q(wt_date__icontains=search_word))
            context = {
                'data': data
            }
            return render(request, 'webapp/result.html', context)
        # elif search_type == '제목':
        #     data = qs.filter(Q(wt_title__icontains=search_word))
        #
        #     context = {
        #         'data': data
        #     }
        #     return render(request, 'webapp/result.html', context)
        else:
            # search_type == '제목':
            data = qs.filter(Q(wt_title__icontains=search_word))

            context = {
                'data': data
            }
            return render(request, 'webapp/result.html', context)

    except ValueError:
        context = {
            HttpResponse("검색 결과가 존재하지 않습니다.")
        }
        return render(request, 'webapp/result.html', context)

    #     return HttpResponse("검색 결과가 존재하지 않습니다.")
