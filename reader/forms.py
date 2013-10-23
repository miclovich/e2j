from django import forms
import xlrd


class UploadFileForm(forms.Form):
    chart_type = forms.CharField()
    upload_file = forms.FileField()
    # TODO -> clean this form

    def convert_excel(self):
        # TODO -> evaluate process for very large files (use processing)
        excel_file = self.cleaned_data['upload_file']
        book = xlrd.open_workbook(file_contents=excel_file.read(),
                                  encoding_override='utf-8')
        return book

    def get_charttype(self):
        chart_type = self.cleaned_data['chart_type']
        if chart_type:
            return chart_type
        return None
