def format_name(f_name,l_name):
    """isim ve soyisim yaz ve bunu tittle tipinde döndürsün"""
    if f_name == "" or l_name == "":
        return "",""

    formated_name = f_name.title()
    formated_last_name = l_name.title()

    return formated_name , formated_last_name


first_name , last_name = format_name(input("what is your firs name"),input("what is your last name"))

print(first_name + last_name)