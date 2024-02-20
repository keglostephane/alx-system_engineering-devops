#!/usr/bin/python3
"""
export_data_from_API_to_json
"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <number>")
        sys.exit(0)

    userId = int(sys.argv[1])
    url1 = "https://jsonplaceholder.typicode.com/todos"
    url2 = "https://jsonplaceholder.typicode.com/users"
    data1 = {"userId": userId}
    data2 = {"id": userId}
    req1 = requests.get(url1, params=data1)
    req2 = requests.get(url2, params=data2)
    todos = req1.json()
    userName = req2.json()[0].get('username')

    todoList = []
    for todo in todos:
        entry = {"task": f"{todo.get('title')}",
                 "completed": f"{str(todo.get('completed')).casefold()}",
                 "username": f"{userName}"}
        todoList.append(entry)

    to_json = {f"{userId}": todoList}
    with open(f"{userId}.json", 'w', encoding='utf-8') as jsonfile:
        json.dump(to_json, jsonfile)
