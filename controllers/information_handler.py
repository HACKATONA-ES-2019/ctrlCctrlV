from model.information import Information


class InformationManager:
    def __init__(self):
        self.informations = {}

    def add_information(self, information_name, information_text_path, information_images_path):
        if information_name in self.informations:
            return False

        self.informations[information_name] = Information(information_name, information_text_path, information_images_path)
        return True

    def remove_information(self, information_name):
        if information_name not in self.informations:
            return False

        del self.informations[information_name]
        return True

    def check_information(self, information_name):
        return information_name in self.informations

    def get_information(self, information_name):
        return self.informations[information_name].json()
