from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseServerError
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import UploadFileForm
from .utils import convert_book_to_json


class HomePageView(View):

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
            chart_type = form.get_charttype()
            if chart_type:
                json_response = convert_book_to_json(book, chart_type=chart_type)
                return HttpResponse(json_response, mimetype='application/json')
            else:
                return HttpResponse(
                    json.dumps({"error": "Undefined chart type"}),
                    mimetype='application/json')
        else:
            return HttpResponse(
                json.dumps({"error": "Invalid API call."}),
                mimetype='application/json')
    else:
        return HttpResponseServerError("Only POSTS")
