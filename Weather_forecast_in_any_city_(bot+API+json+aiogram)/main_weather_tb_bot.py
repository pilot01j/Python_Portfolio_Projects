import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import executor as executor


# pip install --force-reinstall -v "aiogram==2.23.1"


bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_hendler(commands=["start"])
async def start_command(message: type.Message):
    await message.reply("Hello! Write the city name and I will send information about weather.")

@dp.message_hendler()
async def get_weather(message: types.Message):
    code_to_smile = {'Clear': "Clear \U00002600",
                     'Clouds': "Clouds \U00002601",
                     'Rain': "Rain \U00002614",
                     'Drizzle': "Drizzle \U00002614",
                     'Thunderstorm': "Thunderstorm \U000026A1",
                     'Snow': "Snow \U0001F328",
                     'Mist': "Mist \U0001F32B"}

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric")
        data = r.json()
        # pprint(data)

        city = data['name']
        current_temp = data['main']['temp']
        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            print("Look outside,  I can't understand how the weather is. ")
        current_humidity = data['main']['humidity']
        current_pressure = data['main']['pressure']
        current_wind_speed = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(
            data['sys']['sunrise'])
        await message.reply(f"-------{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}-------\n"
              f"City: {city}\nTemperature: {current_temp}℃ {wd}\n"
              f"Pressure: {current_pressure} mm.Hg\n"
              f"Humidity: {current_humidity} %\n"
              f"Wind: {current_wind_speed} m/s\n"
              f"Sunrise at: {sunrise_timestamp}\n"
              f"Sunset at: {sunset_timestamp}\n"
              f"Length of the day: {length_of_the_day}")

    except Exception as ex:
        print(ex)
        await message.reply('\U00002620 Check the city name! \U00002620 ')


if __name__ == "__main__":
    executor.start_polling(dp)

