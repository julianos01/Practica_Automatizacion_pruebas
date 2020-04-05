import requests

url = "https://fakerestapi.azurewebsites.net/api"


def get_url():
    return url

def get_books_id(id):
    endpoint = "/authors/books/{}".format(str(id))
    peticion = requests.get(url + endpoint)
    return peticion



def get_all_authors():
    endpoint = "/Authors"
    peticion = requests.get(url + endpoint)
    return peticion


def create_authors(id, id_book, first_name, last_name):
    endpoint = "/Authors"
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": id,
        "IDBook": id_book,
        "FirstName": "{}".format(first_name),
        "LastName": "{}".format(last_name),
    }
    peticion = requests.post(url + endpoint, data=payload, headers=headers)
    return peticion


def delete_authors(id):
    endpoint = "/Authors/{}".format(str(id))
    peticion = requests.delete(url + endpoint)
    return peticion


def get_authors(id):
    endpoint = "/authors/{}".format(str(id))
    peticion = requests.get(url + endpoint)
    return peticion


def put_authors(id, id_book, first_name, last_name):
    endpoint = "/authors/{}".format(str(id))
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": id,
        "IDBook": id_book,
        "FirstName": "{}".format(first_name),
        "LastName": "{}".format(last_name),
    }
    peticion = requests.put(url + endpoint, data=payload, headers=headers)
    return peticion

def get_all_books():
    endpoint = "/Books"
    peticion = requests.get(url + endpoint)
    return peticion


def create_books(id, title, description, page_count, excerpt, publish_date):
    endpoint = "/Books"
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": id,
        "Title": "{}".format(title),
        "Description": "{}".format(description),
        "PageCount": page_count,
        "Excerpt": "{}".format(excerpt),
        "PublishDate":  "".format(publish_date),

    }
    peticion = requests.post(url + endpoint, data=payload, headers=headers)
    return peticion


def delete_books(id):
    endpoint = "/Books/{}".format(str(id))
    peticion = requests.delete(url + endpoint)
    return peticion


def get_books(id):
    endpoint = "/Books/{}".format(str(id))
    peticion = requests.get(url + endpoint)
    return peticion


def put_books(id, title, description, page_count, excerpt, publish_date):
    endpoint = "/Books/{}".format(str(id))
    headers = {"Content-Type": "application/json"}
    payload = {
         "ID": id,
        "Title": "{}".format(title),
        "Description": "{}".format(description),
        "PageCount": page_count,
        "Excerpt": "{}".format(excerpt),
        "PublishDate": "".format(publish_date),
    }
    peticion = requests.put(url + endpoint, data=payload, headers=headers)
    return peticion



