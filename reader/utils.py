import os
import json


def handle_uploaded_excel(request_FILE):
    xl = request_FILE['file']
    extension = os.path.splitext(xl.name)[1]

    if extension.startswith('.'):
        temp_file_name = u'temp_excel' + extension
    else:
        temp_file_name = u'temp_excel.' + extension

    with open(temp_file_name, 'wb+') as destination:
        for chunk in xl.chunks():
            destination.write(chunk)
        print "destination created"
    # return some JSON output


def convert_book_to_json(workbook):
    """
    It has been assumed that the format of the work is as follows;
    The first row is always a collection of words or terms defining the heading
    of each column.
    The consequent rows will therefore be part of the dataset and values.

    The json output will be in a form where the keys in the hash represent columns,
    and the values in the hash represent corresponding data values (dataset).
    """

    # read the book's content
    worksheets = workbook.sheet_names()
    for sheet_name in worksheets:
        worksheet = workbook.sheet_by_name(sheet_name)

        # extract data from this worksheet
        num_rows = worksheet.nrows - 1
        curr_row = -1
        all_rows = []
        dict_return = {}  # dataset collection per column
        dict_collection = []
        num_cells = worksheet.ncols - 1
        while curr_row < num_rows:
            curr_row += 1
            row = worksheet.row(curr_row)
            all_rows.append(row)

        heading_rows = all_rows.pop(0)
        print all_rows
