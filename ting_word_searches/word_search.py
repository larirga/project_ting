def exists_word(word, instance):
    counter = []
    occrr = []
    for index in range(len(instance)):
        row = instance.search(index)
        for index, line in enumerate(row['linhas_do_arquivo']):
            if word.lower() in line.lower():
                occrr.append({'linha': index + 1})
        if occrr:
            counter.append({
                'palavra': word,
                'arquivo': row['nome_do_arquivo'],
                'ocorrencias': occrr,
            })

    return counter


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
