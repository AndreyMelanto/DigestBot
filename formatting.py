from aiogram.utils.formatting import Text, TextLink, as_line
from utils import FetchError


def format_news(news_list: list[dict]) -> Text:
    if isinstance(news_list, FetchError):
        return Text('Не удалось загрузить новости')
    return Text(
        *[as_line(as_line(TextLink(el['title'], url=el['link']))) for el in news_list],
    )


def format_currency(data: list[dict]) -> str:
    if isinstance(data, FetchError):
        return 'Не удалось загрузить курсы валют'
    return '\n\n'.join([f"{el['Name']}    {el['Value']} ₽" for el in data])


def format_digest(news_data: list[dict], fact_data: str, currency_data: list[dict]) -> Text:
    return Text(f'ДАЙДЖЕСТ\n\n\n   Факт:\n{fact_data}\n\n   Курсы валют:\n{format_currency(currency_data)}\n\n\n   Новости:\n\n') + format_news(news_data)
