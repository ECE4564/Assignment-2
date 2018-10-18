import json

def check(args):
    #check if BUY/SELL
    # temp1 = ('ADD','DELETE','COUNT')
    # if args.action_param is in temp:
    #     r=1
    # el
    if args.action_param == 'ADD':
        d = json.loads(str(args.book_info))
        NameFlag = True if 'Name' in d['Msg'][0]['BookInfo'] else False
        return NameFlag

