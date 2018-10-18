import argparse

def client_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('-proc', dest='proc_ip',
                        help='Setting the processor IP')

    parser.add_argument('-action', dest='action_param',
                        help='Setting the action')

    parser.add_argument('-book', dest='book_name',
                        help='Setting the book name')

    parser.add_argument('-count', dest='count_value',
                        help='Set the Bought/Sell Values')

    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    return parser