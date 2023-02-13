# Telegram-бот для личного учёта бюджета

Информацию можно экспортировать в xlsx для просмотра в Excel(e) в дальнейшем на локальных персональных устройствах

## Команды бота (планое):

- `/start` — приветственное сообщение
- `/help` — справка
- `/add-income` - добавление прихода
- `/add-expense` - добавление расхода
- `/add-storage` - добавление накоплений (цели, а также даальнейшая привязка с наполнением)
- `/amass-storage` - наполнение конкретного накопления (в виде учёта)
- `/see-day` - получение справки по конкретному дню
- `/see-weeks` - получение справки по первой или второй половине выбранного месяца
- `/see-delta` - получение разности за определённый день / период
- `/income-categories` - получение списка категорий дохов
- `/expenses-categories` - получение списка категорий расходов

Подключение бота доступно только к определённым, подтверждённым автором, профилям (усмотрение для личного пользования)

## Запуск

Скопируйте `.env.example` в `.env` и отредактируйте `.env` файл, заполнив в нём все переменные окружения:

```bash
cp /.env.example /.env
```

Для управления зависимостями используется [poetry](https://python-poetry.org/),
требуется Python 3.11.

Установка зависимостей и запуск бота:

```bash
poetry install
poetry run python -m tg-budget-bot
```

## Ideas

## Деплой

[Описание того, как можно развернуть бота на сервере](DEPLOY.md)
