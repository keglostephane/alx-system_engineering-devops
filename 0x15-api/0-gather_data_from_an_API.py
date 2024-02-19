#!/usr/bin/python3
"""data_from_api
Gather datat from an API
"""
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
    userName = req2.json()[0].get('name')
    done = 0
    undone = 0
    doneTitles = []
    for todo in todos:
        done += 1 if todo.get('completed') else 0
        undone += 1 if not todo.get('completed') else 0
        if todo.get('completed'):
            doneTitles.append(todo.get('title'))

    print(f"Employee {userName} is done with tasks({done}/{done + undone}):")
    for title in doneTitles:
        print(f"\t {title}")
