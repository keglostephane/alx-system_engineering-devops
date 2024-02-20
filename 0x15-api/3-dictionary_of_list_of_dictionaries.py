#!/usr/bin/python3
"""
export_all_data_from_API_to_json
"""
import json
import requests
import sys


def get_user_task(user_id, username):
    """Get a user tasks

    :param user_id: the id of the user
    :type user_id: int
    :param username: username of user
    :type username: str
    :return: a list of user's tasks
    :rtype: list
    """
    url = "https://jsonplaceholder.typicode.com/todos"
    data = {"userId": user_id}
    req = requests.get(url, params=data)
    todos = req.json()

    todolist = []
    for todo in todos:
        entry = {"username": f"{username}",
                 "task": f"{todo.get('title')}",
                 "completed": todo.get('completed')}
        todolist.append(entry)

    return todolist


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/users"
    req = requests.get(url)
    users = req.json()

    to_json = {}
    for user in users:
        to_json[f"{user.get('id')}"] = get_user_task(user.get('id'),
                                                     user.get('username'))

    with open('todo_all_employees.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(to_json, jsonfile)
