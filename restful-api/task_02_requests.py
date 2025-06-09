#!/usr/bin/python3
""""""


import requests
import csv


URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetches posts via GET request and prints their titles"""
    response = requests.get(URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))
    else:
        print("Error fetching the data.")


def fetch_and_save_posts():
    """fetches posts and saves them to a CSV file"""
    response = requests.get(URL)

    if response.status_code == 200:
        posts = response.json()

        data_to_save = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        with open(
            "posts.csv",
            mode="w",
            newline='',
            encoding="utf-8"
        ) as csv_file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(data_to_save)
    else:
        print("Error fetching the data.")
