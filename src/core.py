from transformers import pipeline

clf = pipeline(
    task='sentiment-analysis',
    model='SkolkovoInstitute/russian_toxicity_classifier',
)


def data_pipline(text):
    data_rezult = []
    if type(text) is str:
        for sentence in text.split('.'):
            if sentence != '':
                rezult = clf(sentence)
                rezult[0].update({'string': f'{sentence}'})
                data_rezult.append(rezult)
            else:
                continue
    else:
        for i in text:
            data_rezult.append(data_pipline(i))
    return data_rezult
