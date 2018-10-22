import json
def prep(args):
    if args.action_param == 'ADD' or args.action_param == 'DELETE' or args.action_param == 'COUNT':
        d = json.loads(str(args.book_info))
        name = d['Name']
        author = d['Author']
        dic = {
                'Action' : str(args.action_param),
                'Msg' : {
                'Book Info' : {
                    'Name' : name,
                    'Author' : author
                    }
                }
        }
        return (json.dumps(dic))
    elif args.action_param == 'BUY' or args.action_param =='SELL':
        d = json.loads(str(args.book_info))
        name = d['Name']
        author = d['Author']
        count = args.count_value
        dic = {
                'Action' : str(args.action_param),
                'Msg' : {
                    'Book Info' : {
                        'Name' : name,
                        'Author' : author
                    } ,
                    'Count' : count
                }
        }
        return (json.dumps(dic))
    elif args.action_param == 'LIST':
        dic = {
                'Action' : str(args.action_param),
                'Msg' : {}
                }
        return (json.dumps(dic))
