from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext
from django.views.generic import View
from .forms import UploadFileForm
from .utils import convert_book_to_json


class ReadJson(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("This is just an API.")


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.convert_excel()
            json_response = convert_book_to_json(book)
            return HttpResponse(json_response, mimetype='application/json')
    else:
        form = UploadFileForm()
        return render_to_response('reader/upload.html', {'form': form},
                                  RequestContext(request))
