from collections import OrderedDict


class GeneratePrintingFile(object):
    def __init__(self, filename):
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
                row = {}
                column_list = headers['voucher_fields'].split(',')
                voucher_values = line.split(',')

                for c in range(len(column_list)):
                    row[column_list[c]] = voucher_values[c]
                body[counter] = row
                counter += 1

        data = self.store_data(column_list, body)
        self.print_data(data)

    def prepare_row(self, fields):
        str_ = ''
        print fields
        for c in fields:
            str_ += '{}   '.format(str(c))

    def store_data(self, column_list, body):
        data = {}
        for column_heading in column_list:
            data[column_heading] = []

        for entry in body:
            voucher = body[entry]
            for row in voucher:
                data[row].append(voucher[row])
        return data

    def print_data(self, data):
        counter = 0
        num_of_vouchers = len(data['pin'])
        num_columns = 5
        temp_counter = 0

        while counter < num_of_vouchers:
            for i in data:
                temp_counter = 0
                doc_row = []
                voucher_field = data[i]
                while temp_counter < num_columns:
                    doc_row.append(voucher_field[counter])
                    counter += 1
                    temp_counter += 1
                counter -= temp_counter
                self.prepare_row(doc_row)

            counter += temp_counter

c = GeneratePrintingFile('input.txt')
c.get_file_properties()
