from collections import OrderedDict

class GeneratePrintingFile(object):
    def __init__(self, filename):
        # TODO: READ IN FILE
        self.filename = filename
        self.input_file = open(filename, 'r')

    def get_file_properties(self):
        input = self.input_file.readlines()

        headers = {}
        body = OrderedDict()

        counter = 0

        for line in input:
            if len(line.split(':')) > 1:
                headers[line.split(':')[0]] = line.split(':')[1]
            else:
                # build voucher dictionary
                row = {}
                column_list = headers['voucher_fields'].split(',')
                voucher_values = line.split(',')
                for c in range(len(column_list)):
                    row[column_list[c]] = voucher_values[c]

                body[counter] = row
                counter += 1

        print headers, body

    def get_entry(self, field):
        space = ' '
        return field + (space * (25 - len(field)))

    def column_format(self):

        # TODO: the column
        # TODO: new row (column%number_of_columnd)
        # have representation of space
        # have representation of
        # print every line separately
        return

c = GeneratePrintingFile('input.txt')
c.get_file_properties()
