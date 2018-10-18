import json
import time

def check(args):
    if args.action_param == 'ADD' or args.action_param == 'DELETE' or args.action_param == 'COUNT':
        d = json.loads(str(args.book_info))
        if args.book_info and not args.count_value:
                NameFlag = True if 'Name' and 'Author' in d else False
                if NameFlag:
                        print("["+time.ctime()+"]" + " Checkpoint  01: Valid Payload")
                        return True
                else:
                        print("["+time.ctime()+"]" + " Checkpoint  01: Invalid Payload")
                        return False
        else:
                print("["+time.ctime()+"]" + " Checkpoint  01: Invalid Payload")
                return False

    elif args.action_param == 'BUY' or args.action_param =='SELL':
        d = json.loads(str(args.book_info))
        if args.book_info and args.count_value: 
                NameFlag = True if 'Name' and 'Author' in d else False
                countFlag = (int(args.count_value) >= 0)
                if NameFlag and countFlag:
                        print("["+time.ctime()+"]" + " Checkpoint  01: Valid Payload")
                        return True
                else :
                        print("["+time.ctime()+"]" + " Checkpoint  01: Invalid Payload")
                        return False
        else:
                print("["+time.ctime()+"]" + " Checkpoint  01: Invalid Payload")
                return False

    elif args.action_param != 'LIST':
        print("["+time.ctime()+"]" + " Checkpoint  01: Invalid Payload")
        return False
        
