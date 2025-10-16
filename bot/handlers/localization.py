import re
from typing import Dict, Any, Optional

from config_reader import config


def remove_emojis(text: str) -> str:
    """Remove emojis from the text.

    Args:
        text (str): Text to remove emojis from.

    Returns:
        str: Text without emojis.
    """
    lines = text.split('\n')
    cleaned_lines = [re.sub(r'\s*\[:\w+-?\w*\]\s*', ' ', line).strip() for line in lines]
    return '\n'.join(cleaned_lines)


def start_message(first_name: str) -> str:
    return f"👋 Привет, <b>{first_name}</b>!\n\n" \
           "🔸 Я помогу тебе следить за проектами на бирже <b>Kwork</b> и откликаться на них быстрее остальных!\n" \
           "🔸 Это увеличит шансы на то, что заказчик выберет именно тебя!\n\n" \
           "🚀 Чтобы начать, перейди в раздел <i>👤 Профиль</i> и включи отслеживание проектов.\n" \
           "🔎 Советуем ознакомиться с инструкцией перед использованием бота в разделе <i>💬 Помощь</i>."


def project_info(data: Dict[str, Any], attachment: bool) -> str:
    username = data['wantUserGetProfileUrl'].split('/')[-1]
    profile_url = f"https://kwork.ru/user/{username}"
    projects_url = f"https://kwork.ru/projects/list/{username}"
    
    cleaned_name = remove_emojis(data['name'])
    cleaned_description = remove_emojis(data['description'])
    
    text = f"<blockquote><b>{cleaned_name}</b>\n\n" \
           f"{cleaned_description.replace('\n', '\n\n')}</blockquote>\n\n" \
           f"Желаемый бюджет: до {int(float(data['priceLimit']))} ₽\n" \
           f"Допустимый: до {int(float(data['possiblePriceLimit']))} ₽\n\n" \
           f"Покупатель: <a href='{profile_url}'>{username}</a>\n" \
           f"Размещено проектов на бирже: {data['user']['data']['wants_count']}   " \
           f"<a href='{projects_url}'>Смотреть открытые ({data['getWantsActiveCount']})</a>\n" \
           f"Нанято: {data['user']['data']['wants_hired_percent']}%\n\n" \
           f"Осталось: {data['timeLeft']}\n" \
           f"Предложений: {data['kwork_count']}"
           
    if attachment:
        text += "\n\n📎 Над сообщением прикреплены вложения"
        
    return text
    
    
def user_profile(first_name: str, user_id: int) -> str:
    return f"👤 <b>{first_name}</b>\n\n" \
           f"🏷 <b>ID:</b> <code>{user_id}</code>"

            
def auth() -> str:
    return "📲 Войди в свой аккаунт Kwork, чтобы бот мог отслеживать проекты по твоим любимым категориям."


def error_auth(err: Optional[str] = None) -> str:
    if not err:
        return f"⚠️ Произошла ошибка при входе в Kwork.\nПопробуй пройти авторизацию еще раз."
    return f"⚠️ Произошла ошибка при входе в Kwork: <i>{err}</i>.\nПопробуй пройти авторизацию еще раз."


def successful_auth() -> str:
    return "✅ Авторизация прошла успешно.\n\nНе забудь включить отслеживание проектов в разделе <i>👤 Профиль</i>."


def projects_tracking_enabled() -> str:
    return "🔔 Отслеживание проектов включено"


def projects_tracking_disabled() -> str:
    return "🔕 Отслеживание проектов выключено"


def help_sections() -> str:  
    return "Выбери раздел:"


def manual() -> str:
    return "<b>1.</b> На сайте kwork.ru в разделе «Биржа» выбери любимые рубрики, по ним бот будет отслеживать проекты.\n\n" \
           "(❗️Важно: в настройках аккаунта Kwork должно быть выбрано <i>Я продавец</i>)\n\n" \
           "<b>2.</b> Зайди в свой аккаунт Kwork через бота, введя команду /start или нажав на кнопки <i>Профиль</i> » <i>Включить отслеживание проектов</i>.\n\n" \
           "<b>3.</b> После включения отслеживания бот будет отправлять тебе проекты по выбранным рубрикам сразу после их размещения на бирже.\n\n" \
           "(❗️Важно: при первом нажатии на кнопку <i>Открыть проект</i> или <i>Предложить услугу</i>, необходимо зайти в свой аккаунт Kwork в открывшемся приложении)"


def support() -> str:
    return "❗️Перед обращением в поддержку, проверь, нет ли ответа на твой вопрос в разделе <i>📜 Инструкция</i>.\n\n" \
           f"☎️ Контакт: <span class='tg-spoiler'>{config.SUPPORT_CONTACT}</span>"
           

def get_login() -> str: 
    return "Введи электронную почту или логин:"


def get_password() -> str:
    return "Введи пароль:"


def canceled() -> str:
    return "Ввод отменён"
