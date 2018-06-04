 Loan Aggregate Calculator
 The Loan Aggregate Calculator calculates the aggregate of loans by the tuple of (Network, Product, Date(month))

 Usage:
 Calculate the aggregate of loan transactions for a given aggregate factors
 i.e aggr_calculator = AggregateCalculator('input.csv', ('Network', 'Product', 'Date'))
     aggr_calculator.calculate_aggregate()

 Assumptions:
 * The first line in the file is a heading
 * Each line's columns matches that of the heading
 * The Aggregate filters will match the heading names
 * The date format will always be 'dd-mm-yyyy'
 * The order of columns will remain consistent
    * heading : MSISDN,Network,Date,Product,Amount
    * Values: 27729554427,'Network 1','12-Mar-2016','Loan Product 1',1000.00

Why Python:
Supports all requirements for this project and portable

Performance:
The algorithm complexity for finding the matching transaction in O(1)

Scaling:
It would require minimal work to make it work for different input

Quality:
Well tested
