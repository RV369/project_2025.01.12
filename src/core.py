import uuid

from transformers import pipeline

clf = pipeline(
    task='sentiment-analysis',
    model='SkolkovoInstitute/russian_toxicity_classifier',
)


def data(text):
    data_rezult = []
    for row in text.split('.'):
        if row != '':
            data = clf(row)
            for m in data:
                m.update({f'{uuid.uuid4()}': f'{row}'})
            data_rezult.append(data)
        else:
            continue
    return data_rezult


def data_list(text_list):
    data_rezult = []
    for sentence in text_list:
        for row in sentence.split('.'):
            if row != '':
                data = clf(row)
                for m in data:
                    m.update({f'{uuid.uuid4()}': f'{row}'})
                data_rezult.append(data)
            else:
                continue
    return data_rezult
