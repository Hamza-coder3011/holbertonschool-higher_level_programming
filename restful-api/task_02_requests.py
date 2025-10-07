#!/usr/bin/python3
import requests
import csv


# Fonction 1 : Récupérer les posts et afficher leurs titres
def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Affiche le code de statut
    print(f"Status Code: {response.status_code}")

    # Si la requête a réussi
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])  # Afficher le titre de chaque post


# Fonction 2 : Récupérer les posts et les enregistrer dans un fichier CSV
def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        data = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        # Écrire dans un fichier CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()  # Écrit les noms des colonnes
            writer.writerows(data)  # Écrit toutes les lignes
