import time
import g4f
from g4f.errors import RetryProviderError


def ask_gpt_4(promt: str) -> str:
    time.sleep(6)
    check_status = True
    while check_status:
        try:
            response = g4f.ChatCompletion.create(
                model=g4f.models.gpt_4,
                messages=[{"role": "user", "content": promt}],
                max_tokens=1
            )
            check_status = False
            return response.lower()
        except RetryProviderError:
            print("RetryProviderError occurred in ask_gpt_4. Retrying...")
            time.sleep(6)


# Verificăm dacă șirul conține cuvântul "negativ"
def check_word(text):
    text = text.lower()

    if 'negativ' in text:
        return 'negativ'
    elif 'pozitiv' in text:
        return 'pozitiv'
    else:
        return 'neutru'


def add_tip_articol(title, company_name):
    check_status = True
    while check_status:
        try:
            gpt_result = ask_gpt_4(f'raspunde scurt daca stirea "{title}" este pozitiva, negativa sau neutru '
                                   f'despre compania {company_name}')

            article_type = check_word(str(gpt_result).lower())
            check_status = False
            return article_type

        except RetryProviderError:
            print("RetryProviderError occurred in add_tip_articol. Retrying...")
            time.sleep(6)


