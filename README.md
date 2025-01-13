# project_2025.01.12
Применяются технологии: 
- FastAPI
- Python 3.11.9
- Docker / Docker compose
- Uvicorn

Сервис для автоматической классификации речевой агрессии, применяется модель SkolkovoInstitute/russian_toxicity_classifier. 
Микросервис принимает POST запрос с файлом json:

{
  "text": ["У нас в есть убунты и текникал превью.",
    	"Как минимум два малолетних дегенерата в треде, мда."]
}

Сервис вернет json:

[
    [
        [
            {
                "label": "neutral",
                "score": 0.9921925663948059,
                "string": "У нас в есть убунты и текникал превью"
            }
        ]
    ],
    [
        [
            {
                "label": "toxic",
                "score": 0.9854377508163452,
                "string": "Как минимум два малолетних дегенерата в треде, мда"
            }
        ]
    ]
]


Для развертывания необходимо скопировать фаил:
- docker-compose.production.yml
запустить файл командой:
```sh
docker compose -f docker-compose.production.yml up
```
Докер скачает образ контейнера (6,83 GB) и запустит контейнер с микросервисом.
Протестировать можно из документации по адресу:
- http://127.0.0.1:8000/docs


