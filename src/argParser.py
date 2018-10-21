import argparse
import optparse

def client_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('-proc', dest='proc_ip',required = True,
                        help='Setting the processor IP')

    parser.add_argument('-action', dest='action_param',required = True,
                        help='Setting the action')

    parser.add_argument('-book', dest='book_info',required = False,
                        help='Setting the book info')

    parser.add_argument('-count', dest='count_value',required = False,
                        help='Set the Bought/Sell Values')

    return parser

def processor_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('-storage', dest='bt_addr',required = True,
                        help='Setting the Bluetooth Mac Addr')

    parser.add_argument('-p', dest='port_num',required = True,
                        help='Setting the port number')

    parser.add_argument('-z', dest='socket_size',required = True,
                        help='Setting the socket size')

    return parser

def storage_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', dest='port_num',
                        help='Setting the port number')

    parser.add_argument('-b', dest='backlog',
                        help='Setting the backlog size')

    parser.add_argument('-z', dest='socket_size',
                        help='Setting the socket size')

    return parser