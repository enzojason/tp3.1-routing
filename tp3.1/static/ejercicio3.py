#ejercicio 3
def about_funcion():
    return {
        'app_name':app.config['APP_NAME'],
        'description':app.config['DESCRIPTION'],
        'version':app.config['VERSION'],
        'developers':app.config['DEVELOPERS']
    }
