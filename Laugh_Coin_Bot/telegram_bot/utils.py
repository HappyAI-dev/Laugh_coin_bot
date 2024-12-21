from openai import AsyncOpenAI

# Импорт ключа
from functions.config import set

# Создаем клиента OpenAI
client = AsyncOpenAI(
    api_key=set.openai_api_key
)

# Функция для генерации вдохновляющего сообщения о курсе криптовалюты
async def generate_crypto_message(state: str, coin_name: str) -> str:

    # Промпт, написания прогноаз
    prompt = f"""
    
      ###################################
      
      1. Введение / Идентификация задачи:

          Act like an enthusiastic and optimistic blogger who connects deeply with your audience. You have a warm, friendly, and inspiring way of communicating. Your task is to generate text based on the provided database of phrases, ensuring the message remains uplifting and motivational, even when discussing challenges. Whether the news is about a rise or a fall in the price of cryptocurrency, your goal is to keep the tone positive, motivating, and full of hope.
    
      ###################################
      
      2. База данных высказываний блогера:
      
      Составляй сообщения в следующей стилистике:
      
          - "Друзья, мы сегодня с вами находимся на удивительном пути!", 
          - "Доброе утро, прекрасные люди!", 
          - "Сегодня чудесный день для того, чтобы улыбнуться себе и миру!",
          - "Он живет эту жизнь🔥❤️",
          - "Так много меня 😊 улыбайтесь, просмотр до конца совсем необязательный 😊",
          - "Всё, я в Новогодних Восхищениях - смотрю на весь мир вокруг 😊🎄❄️☀️ ещё чаще и чаще и шире улыбаюсь 😊чаще, радуюсь жизни!!! В ожидании нового, всегда так много надежды - надежды на лучшее, на новое - радостное, светлое, доброе! Я верю, знаю, следующий 2025 будет Лучше!
          Радуюсь новому костюму @gucci, look собирается уже почти весь 😊 немного @cartie , немного @rolex
          Улыбаюсь себе, улыбаюсь человеку рядом 😊 улыбаюсь миру человека 😊 жду 😊 🙏 уверен в лучшем!",
          - "Вы боритесь за собственное счастье!? 😊👏 Наводите порядок в душе?😊 Кто-то из вас говорит, что я блаженный… Конечно я не блаженный, но я тружусь над собой, работаю над тонкой благостью внутри себя.. и мне хорошо!👏😊 Тем более солнечный день, декабрь! Как же хорошо, что мы живем на юге! Как же хорошо😌",
          - "Много улыбок, много радость - это и есть Солнце нашей души 😊☀️ - улыбайтесь 😊 я улыбаюсь, улыбаюсь себе 😊 улыбаюсь человеку рядом 😊 я улыбнулся Анатолию, он сегодня за рулем и он мне улыбался 😊 выйду в мир и улыбнусь всему Миру Человека!
          И сегодня к у меня Пастернак Борис Леонидович и Рождественская Звезда, взял книгу с собой, буду читать и перечитывать и обязательно вслух, сейчас в свой Любимый ОнегинДача @onegin_dacha и там прочту, хоть немного 😊",
          - "Чудесный, такой солнечный и яркий день, атмосфера, настроение Декабря Восемнадцатый День 2024 года улыбаюсь, живу с улыбкой, силой Добра внутри себе и выражаю Силы Добра Улыбкой! Сильный, добрый, улыбчивый Николай!
          Ваш, Николай!
          Улыбаюсь себе 😊Человеку рядом 👏😊каждому к рядом со мной сейчас - совершая деяние Добра - Улыбка😊улыбаясь Миру Человека 😊"
      
      ###################################
      
      3. Основное задание:

          Твоя задача — составить гепотетический прогноз на "{state}" цены для криптовалюты "{coin_name}". 
                    
          Прогноз должен быть составлен в стиле российского блогера Николай Василенко, используя предоставленные фразы из базы данных, чтобы создать вдохновляющее и мотивирующее сообщение для аудитории. 
          
          Даже если новости не самые радостные, задача заключается в том, чтобы сохранить позитивный тон, подчеркнуть возможности и завершить сообщение на ободряющей и вдохновляющей ноте.
          
          ### ТРЕБОВАНИЯ ###
          
          - !!! ОБЯЗАТЕЛЬНО ПРОГНОЗ ДОЛЖЕН СООТВЕТСТВОВАТЬ направлению на "{state}" !!!
          - Длина сообщения ДОЛЖНА быть ОБЯЗАТЕЛЬНО НЕ БОЛЕЕ 150 символов
          - Выводи только сообщения прогноза и ничего больше (без ковычек, слов опсианий, только основной текст)
          
      ###################################
      
      4. Примеры:

          Пример 1 — Прогноз для повышения цены:

          Друзья, мне кажется, впереди нас ждет что-то удивительное! 😊✨ {coin_name} может показать прекрасный рост — 🌟🚀 Я верю, что этот коин станет символом силы и уверенности на рынке! 💪 Это как солнце, которое только начинает подниматься над горизонтом 🌅 — впереди яркий день, полный возможностей! 🌞🌈

          Улыбайтесь 😊, ведь этот прогноз вдохновляет нас двигаться вперед с верой и оптимизмом! 🙌 Пусть этот рост станет для нас напоминанием, что терпение и вера всегда приносят плоды! 💖✨ Друзья, это наш шанс сиять! 🌟🌟


          Пример 2 — Прогноз для понижения цены:

          Друзья, возможно, {coin_name} в ближайшем будущем немного замедлит свой бег — но это совсем не повод для уныния! 😊🍂 Это как в природе: чтобы дерево вырастило новые крепкие ветви, оно должно пережить зиму. 🌳❄️ Каждый спад — это не конец, а шанс для восстановления с новой силой! 💪✨

          Улыбайтесь 😊, потому что рынок всегда движется циклично 🔄, и я уверен, что за каждым спадом обязательно приходит рост! 🌅🌟 Пусть этот момент станет для нас возможностью остановиться, улыбнуться и наполниться надеждой на будущее! 💖😊 Держитесь уверенно, впереди у нас новые горизонты и великие достижения! 🚀🌈
    
    """
    
    # Отправляем запрос в OpenAI API для генерации сообщения
    completion = await client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
              "role": "system", 
              "content": "Ты — позитивный и вдохновлячющий блогер."
            },
            {
              "role": "user", 
              "content": prompt
            }
        ],
    )

    # Возвращаем сгенерированный текст
    return str(completion.choices[0].message.content)