

class Information:
    def __init__(self, title, text_path, images_path):
        self.title = title
        self.text_path = text_path
        self.images_path = images_path

    def json(self):
        return {
            'title': self.title,
            'text': open(self.text_path, 'r').read(),
            'images': str(self.images_path)
        }

    def insert_string(self):
        return f'INSERT INTO INFORMACOES VALUES ("{self.title}", "{self.text_path}", "{self.images_path}");'
