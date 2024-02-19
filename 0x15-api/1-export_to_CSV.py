#!/usr/bin/python3
"""
export_data_from_API_to_csv
"""
import csv
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

    with open(f"{userId}.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([f"{userId}", f"{userName}",
                             f"{todo.get('completed')}",
                             f"{todo.get('title')}"])
