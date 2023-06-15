from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for index in range(len(instance)):
        instance_data = instance.search(index)
        if instance_data['nome_do_arquivo'] == path_file:
            return None
    lines_txt = txt_importer(path_file)
    dict = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(lines_txt),
        'linhas_do_arquivo': lines_txt,
    }
    instance.enqueue(dict)
    print(dict, file=sys.stdout)


def remove(instance):
    if not instance:
        print('Não há elementos', file=sys.stdout)
        return None
    file_removed = instance.dequeue()
    file_path = file_removed['nome_do_arquivo']
    print(f'Arquivo {file_path} removido com sucesso', file=sys.stdout)


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        print(file, file=sys.stdout)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
