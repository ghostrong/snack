#coding=utf8


import xlrd
import xlwt


def read_data(filename):
    data = xlrd.open_workbook(filename)
    print data.sheet_names()
    # different ways for getting the worksheet:
    # data.sheets()[index]
    # data.sheet_by_index(index)
    # data.sheet_by_name(name)
    table = data.sheet_by_index(0)
    nrows = table.nrows
    ncols = table.ncols
    header = table.row_values(0)
    print header
    # get values from every row
    # string-value is unicode
    row_list = []
    for i in xrange(1, nrows):
        row = table.row_values(i)
        row_list.append(row)

    # get values from a column
    colname = header[0]  # you can specify the colname
    idx = header.index(colname)
    vals = table.col_values(idx)
    print vals[1:]

    # get value by index
    print table.cell(1, 0).value
    print table.cell(1, 1)


def write_data(filename):
    f = xlwt.Workbook()
    table = f.add_sheet('Sheet1', cell_overwrite_ok=True)
    header = [u'name', u'age', u'school', u'city']
    values = [(u'Tom', u'30', u'PKU', u'北京'),
              (u'John', u'25', u'JHU', u'巴尔的摩')
             ]

    for j, v in enumerate(header):
        table.write(0, j, v)

    # how to set the value type ?  (str, int, ...)
    for i, row in enumerate(values):
        for j, v in enumerate(row):
            table.write(i+1, j, v)

    f.save(filename)


def main():
    import optparse
    parser = optparse.OptionParser()
    parser.add_option('-f', '--filename', dest='filename')
    options, args = parser.parse_args()
    if not options.filename:
        parser.print_help()
        return

    write_data(options.filename)
    read_data(options.filename)


if __name__ == '__main__':
    main()
