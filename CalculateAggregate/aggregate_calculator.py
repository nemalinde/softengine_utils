import sys
import logging


class AggregateCalculator(object):
    """A AggregateCalculator calculates the aggregate loans by the tuple of (Network, Product, Month)
    and write the results to a csv file.

     Attributes:
         filename: A name of the input file
         filters: A tuple of specified columns to filter with
     """
    def __init__(self, filename, filters):
        """Return a AggregateCalculator object and opens a specified file"""
        self.input_file = self.get_input_file(filename)
        self.filters = filters

    @staticmethod
    def get_input_file(filename):
        try:
            input_file = open(filename, 'r')
            return input_file
        except IOError:
            logging.exception("Could not read file: %s" % filename)
            sys.exit()

    def calculate_aggregate(self):
        input_file = self.input_file
        heading = input_file.readline().split(',')

        filters_positions = self.get_filters_positions(heading)

        input_list = input_file.readlines()
        aggregated_data = self.aggregate_input(input_list, filters_positions)
        self.write_to_file(aggregated_data)

        logging.info("Successfully written %s" % len(aggregated_data))
        return aggregated_data

    def get_filters_positions(self, input_heading):
        """
        :params input_heading: transactions heading
        Returns: a tuple of numbers representing the index of columns specified in filters
        """
        filter_positions = []
        for filter in self.filters:
            filter_positions.append(input_heading.index(filter))

        return tuple(filter_positions)

    def aggregate_input(self, input_list, filter_positions):
        """
        :params input_list: list of loan transactions
        :params filter_positions: position for a column to filter with
        Returns: dict containing transactions aggregated by filter positions
        """
        aggregated_data = {}
        for transaction_string in input_list:
            listified_transaction = transaction_string.split(',')
            key = [listified_transaction[index] for index in filter_positions]
            key[-1] = key[-1].split('-')[1]

            if tuple(key) in aggregated_data:
                aggregated_data[tuple(key)] = self.get_updated_transaction(listified_transaction,
                                                                           aggregated_data[tuple(key)])
            else:
                aggregated_data[tuple(key)] = self.transform_transaction(transaction_string)
        return aggregated_data

    def transform_transaction(self, transaction_string):
        """
        :params transaction_string: string for a single record of a loan transaction
        Returns: a list of columns for a transaction that's transformed for output
        """
        listified_trans_string = transaction_string.split(',')
        new_trans_string = '{}, {}, {}, {}, {}'.format(int(1), listified_trans_string[1],
                                                       self.extract_month(listified_trans_string[2]),
                                                       listified_trans_string[3], float(listified_trans_string[4]))

        new_listified_trans_string = new_trans_string.split(',')
        new_listified_trans_string[0] = int(new_listified_trans_string[0])
        new_listified_trans_string[-1] = float(new_listified_trans_string[-1])
        return new_listified_trans_string

    @staticmethod
    def extract_month(transaction_date):
        # extract the month part of the transaction date
        return transaction_date.split('-')[1]

    @staticmethod
    def get_updated_transaction(new_listified_transaction, old_listified_transaction):
        """
        :params new_listified_transaction: new transaction to be aggregated with an existing one
        old_listified_transaction: old transaction to be updated
        Returns: updated old_listiefied transaction
        """
        # increment loan type count
        old_listified_transaction[0] += 1
        # update loan amount
        old_listified_transaction[-1] += float(new_listified_transaction[-1])
        return old_listified_transaction

    @staticmethod
    def write_to_file(aggregated_data):
        """
        :params aggregated_data: dictionary containing transactions aggregated by specified filters
        Returns:
        """
        try:
            output_file = open('Output.csv', 'w')
            heading = ['Count, ', 'Network, ', 'Month, ', 'Product, ', 'Amount']
            for column in heading:
                output_file.write('%s' % column)
            output_file.write('\n')

            aggregate_values = aggregated_data.values()
            for transaction in aggregate_values:
                for column in transaction:
                    output_file.write('%s' % column)
                output_file.write('\n')

            output_file.close()
        except IOError:
            logging.exception("Could not open new file")
            sys.exit()
