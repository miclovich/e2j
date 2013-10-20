from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseServerError
from django.shortcuts import render_to_response, RequestContext
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from .forms import UploadFileForm
from .utils import convert_book_to_json


class ReadJson(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("This is just an API.")


@csrf_exempt
def upload_file(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed('Only POST based API.')
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.convert_excel()
            json_response = convert_book_to_json(book)
            return HttpResponse(json_response, mimetype='application/json')
        else:
            return HttpResponseServerError("Invalid API call.")
