from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, RequestContext
from django.views.generic import View
from .forms import UploadFileForm
from .utils import handle_uploaded_excel, convert_book_to_json


class ReadJson(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("hello world")


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            import ipdb; ipdb.set_trace()
            book = form.convert_excel()
            json_response = convert_book_to_json(book)
            # handle_uploaded_excel(request.FILES)
            return redirect('home')
    else:
        form = UploadFileForm()
    return render_to_response('reader/upload.html', {'form': form}, RequestContext(request))
