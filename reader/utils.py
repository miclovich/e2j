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


def convert_book_to_json(workbook, chart_type=None):
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
    dict_return = {}  # dataset collection per row
    dict_return['data_values'] = []
    # default is 1 worksheet
    try:
        worksheet = workbook.sheet_by_name(worksheets[0])

        # extract data from this worksheet
        num_rows = worksheet.nrows - 1
        curr_row = -1
        all_rows = []
        # num_cells = worksheet.ncols - 1

        # TODO => use chart type to define how we label our JSON output
        while curr_row < num_rows:
            curr_row += 1
            row = worksheet.row(curr_row)
            row_set = set([val.value == '' for val in row])
            if True in row_set and len(row_set) == 1:
                # if a single row has all empty values; this is considered an
                # illegal entry
                pass
            else:
                all_rows.append(row)

        if chart_type in ['spline', 'column', 'bar', 'basic_bar', 'basic_column', 'stacked_bar', 'stacked_column']:

            heading_rows = all_rows.pop(0)
            heading_rows = [item.value for item in heading_rows][1:]  # the first cell is empty
            dict_return['headings'] = heading_rows

            for single_row in all_rows:
                temp = {}
                _key_item = single_row.pop(0)
                temp['name'] = _key_item.value
                temp['data'] = [i.value for i in single_row]
                dict_return['data_values'].append(temp)
        elif chart_type == 'basic_pie':
            heading_rows = all_rows.pop(0)
            heading_rows = [item.value for item in heading_rows]
            remaining_row = [item.value for item in all_rows[0]]
            temp = zip(heading_rows, remaining_row)
            dict_return['data_values'] = [list(_item) for _item in temp]
        else:
            pass
    except IndexError:
        # Return convenient error
        pass

    return json.dumps(dict_return)
