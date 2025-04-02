import json 

def dataEntry(name, email, db, slackid):
    data_file = "/root/Project/birthday_data.json"

    file = open(data_file, "r")     
    content = file.read()       
    python_object = json.loads(content)
    file.close()        

    for i in python_object:
        if slackid == i['slackid']:
            return {'status': 'failed', 'message': 'User already exists', 'code': 409}

    python_object.append({'name': name, 'email': email, 'db': db, 'slackid': slackid})
    json_data = json.dumps(python_object)

    file = open(data_file, "w")   
    content = file.write(json_data)
    file.close()

    return {'status': 'success', 'message': 'User added successfully', 'code': 200}