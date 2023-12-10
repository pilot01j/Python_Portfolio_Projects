# pip install g4f

import g4f


def ask_gpt_3(promt:str)->str:
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": promt}],
        stream=True,
    )

    for message in response:
        print(message, flush=True, end='')


def ask_gpt_4(promt:str)->str:
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": promt}],
    )
    print(response)


print(ask_gpt_3("De ce cerul este albastru??"))
# print(ask_gpt_4("Citi oameni locuiesc in Chisinau?"))
