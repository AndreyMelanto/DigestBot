from aiogram.utils.formatting import Text, TextLink, as_list
from utils import FetchError


def format_news(news_list: list[dict] | FetchError) -> Text:
    if isinstance(news_list, FetchError):
        return Text('Не удалось загрузить новости. Попробуйте снова.')
    return as_list(
        *[TextLink(el['title'], url=el['link']) for el in news_list],
        sep='\n\n'
    )


def format_fact(fact_data: str | FetchError) -> str:
    if isinstance(fact_data, FetchError):
        return 'Не удалось загрузить факт. Попробуйте снова.'
    return fact_data


def format_currency(data: list[dict] | FetchError) -> str:
    if isinstance(data, FetchError):
        return 'Не удалось загрузить курсы валют Попробуйте снова.'
    return '\n\n'.join([f"{el['Name']}    {el['Value']} ₽" for el in data])


def format_digest(news_data: list[dict], fact_data: str, currency_data: list[dict]) -> Text:
    return Text(f'ДАЙДЖЕСТ\n\n\n   Факт:\n{format_fact(fact_data)}\n\n   Курсы валют:\n{format_currency(currency_data)}\n\n\n   Новости:\n\n') + format_news(news_data)
