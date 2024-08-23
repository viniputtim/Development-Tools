import os
import requests


def create_project_structure(project_name):
    structure = {
        'resources': {
            'graphics': ['raylib_logo.png'],
            'fonts': [],
            'sounds': [],
            'strings': {'en': [], 'pt': []}
        },
        'source': {
            'scenes': ['loading.cpp'],
            'utils': ['surf.cpp', 'resource_manager.cpp', 'rect.cpp', 'scheduled_event.cpp'],
            'ui': ['text.cpp', 'button.cpp'],
            'include':
            {
                'scenes': ['scene.hpp', 'loading.hpp'],
                'utils': ['surf.hpp', 'scheduled_event.hpp', 'rect.hpp', 'resource_manager.hpp'],
                'ui': ['button.hpp', 'text.hpp']
            }
        },

    }


    def create_structure(base_path, structure):
        for key, value in structure.items():
            path = os.path.join(base_path, key)
            if not os.path.exists(path):
                os.makedirs(path)
            if isinstance(value, dict):
                create_structure(path, value)
            elif isinstance(value, list):
                for item in value:
                    file_path = os.path.join(path, item)
                    if not os.path.exists(file_path):
                        if item.endswith('.png'):
                            download_raylib_logo(file_path)
                        else:
                            with open(file_path, 'w') as f:
                                pass


    def download_raylib_logo(file_path):
        url = 'https://upload.wikimedia.org/wikipedia/commons/f/f4/Raylib_logo.png'
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(response.content)
        else:
            print(f"Falha ao baixar o arquivo {file_path}. Status code: {response.status_code}")

    create_structure(project_name, structure)
    print(f"Projeto '{project_name}' criado com sucesso!")


if __name__ == '__main__':
    project_name = 'other_game'
    create_project_structure(project_name)
