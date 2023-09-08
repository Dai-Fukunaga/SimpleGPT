def get_api_key():
    f = open("api_key.txt", "r")
    text = f.readlines()
    return text[0].replace("\n", "")
