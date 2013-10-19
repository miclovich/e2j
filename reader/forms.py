from django import forms
import xlrd


class UploadFileForm(forms.Form):
    file = forms.FileField()
    # TODO -> clean this form

    def convert_excel(self):
        # TODO -> evaluate process for very large files (use processing)
        excel_file = self.cleaned_data['file']
        book = xlrd.open_workbook(file_contents=excel_file.read(),
                                  encoding_override='utf-8')
        return book
