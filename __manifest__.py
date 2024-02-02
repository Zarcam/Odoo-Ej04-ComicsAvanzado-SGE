{
    'name': "Biblioteca Comics Avanzada",
    'summary': "Gestionar comics (Version avanzada): ",
    'description': """
        Gestor de bibliotecas (Version avanzada)
    """,

    'application': True,
    'author': "Segia García",
    'website': "http://apuntesfpinformatica.es",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    'data': [
        'views/biblioteca_comic.xml',
        'views/biblioteca_comic_categoria.xml',
        
        'security/groups.xml',
        'security/ir.model.access.csv',
    ],
}