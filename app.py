import requests

def get_random_joke():
    """
    Récupère une blague aléatoire à partir de l'API JokeAPI.
    """
    url = "https://v2.jokeapi.dev/joke/Any"
    params = {
        "format": "json",  # Format de la réponse
        "blacklistFlags": "nsfw,religious,political,racist,sexist",  # Filtrer les blagues inappropriées
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Vérifie si la requête a réussi
        joke_data = response.json()

        # Vérifie si la blague est de type "single" ou "two-part"
        if joke_data.get("type") == "single":
            return joke_data.get("joke")
        elif joke_data.get("type") == "twopart":
            return f"{joke_data.get('setup')} - {joke_data.get('delivery')}"
        else:
            return "Une erreur est survenue lors de la récupération de la blague."
    except requests.exceptions.RequestException as e:
        return f"Erreur de connexion : {e}"
    except Exception as e:
        return f"Erreur : {e}"

def main():
    print("Bienvenue dans l'application de blagues ! 🎉")
    while True:
        user_input = input("\nAppuyez sur Entrée pour obtenir une blague ou 'q' pour quitter : ").strip().lower()
        if user_input == "q":
            print("Merci d'avoir utilisé l'application. À bientôt ! 👋")
            break
        else:
            joke = get_random_joke()
            print("\nVoici une blague pour vous :")
            print(joke)

if __name__ == "__main__":
    main()
