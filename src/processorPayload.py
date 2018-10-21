import json

def answerPayload(question):
    d = json.loads(question)
    #implementing OK functions
    if d['Action'] == 'ADD':
        #try adding to MongoDB here 
        res = "OK: Successfully inserted. Book id 5baea84374fece21a1b2f5e1"
        return res
    elif d['Action'] == 'DELETE':
        res = "OK: Successfully deletion"
        return res
    elif d['SELL'] == 'DELETE':
        res = "OK: Successfully deletion"
        return res
    elif d['LIST'] == 'DELETE':
        res = "OK: Successfully deletion"
        return res