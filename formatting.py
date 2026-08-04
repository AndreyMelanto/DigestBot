from aiogram.utils.formatting import Text, TextLink, as_line


def format_news(news_list: list[dict]) -> Text:
    if 'error' in news_list:
        return Text('Не удалось загрузить новости')
    return Text(
        'Последние новости:\n\n',
        *[as_line(as_line(TextLink(el['title'], url=el['link']))) for el in news_list],
    )


def format_currency(data: list[dict]) -> str:
    if 'error' in data:
        return 'Не удалось загрузить курсы валют'
    return '\n\n'.join([f"{el['Name']}    {el['Value']} ₽" for el in data])
