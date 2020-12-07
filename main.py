import discord
import random
from discord.ext import commands
from command_handler import CommandHandler
from config import settings

client = discord.Client()
#client = commands.Bot(command_prefix='%')
bot = commands.Bot(command_prefix = '!')
channel = bot.get_channel('channel-numb')

@client.event
async def on_message(message):
    if message.content.startswith('!member'):
        for guild in client.guilds:
            for member in guild.members:
                print(member)

@bot.command()
async def hello(ctx):
    channel = bot.get_channel('channel-numb')
    author = ctx.message.author
    await channel.send(f"И тебе ауф, {author.mention}! Я Волчонок Ульф и я могу тебе "
                       "рассказать о своей стае Ulfhednar. \n Если хочешь, чтоб я рассказал тебе о: "
                       "\n Нашей стае - напиши *!pack* \n Нашей религии - напиши *!religion* \n Том, "
                       "что мы делаем - напиши *!craft* \n Если хочешь рассказать о нас кому-то ещё, "
                       "можешь показать им нашу визитку - напиши *!CV*, чтоб посмотреть её\n ")

@bot.command()
async def easter_egg(channel):
    await channel.send('Хочешь узнать больше обо мне? Ну, хорошо... \n\n'
                       'Моя мама - рыжая кошка -  felis. Её хозяйка fie поспособствовала моему появлению на свет.\n'
                       'Мама говорит, что я "её маленький пушистый щекастый волчонок" и кормит меня салом - lard. \n'
                       'Его я оооочень люблю :relaxed: А ещё я люблю своих друзей - sera, lil и rugaru. \n'
                       'Мы часто с ними играемся, когда они не спят.\n'
                       'Иногда, когда небо озаряет свет полной луны, я забираюсь на саааамую высокую гору и делаю auf! Для того, чтоб позвать их на прогулку.\n'
                       'Их хозяева - koshak, drew и erik - очень хорошие люди... Со своими... особенностями. \n'
                       'Порой к нам приходит дядюшка little и учит нас всяким умным штукам! Он наш Папа Волк!\n'
                       'Ещё у нас есть тётенька lavo, её я ещё не видел, но ходят слухи, что она жутко красивая :flushed: \n'
                       'Есть у нас и joseph, к нему я прихожу за умными советами.\n'
                       'Как-то так...')

@bot.command()
async def religion(channel):
    await channel.send('Мы, Звери, не признаём никаких богов. Ведь создали нас не они, а Матушка '
                       'Природа. Она поддерживает нас на протяжении многих лет, а мы в ответ остаёмся '
                       'верны в своей вере и защищаем её. Подробнее можешь узнать здесь: '
                       'https://docs.google.com/document/d/1hzah3goq8kWM2BPQP5m7w8muNED870sP_4apEiuvOkI/edit?usp=sharing')

@bot.command()
async def CV(channel):
    await channel.send('Здесь можешь посмотреть нашу визитку и показать её собратьям, которые хотели '
                       'бы присоединиться! --> https://docs.google.com/document/d/1FMmzqQ3hvruk33ycQTvpYCtarCNQQxp8kk5mkXEZc5A/edit?usp=sharing')

@bot.command()
async def pack(channel):
    await channel.send('Моя стая очень большая! Самый главный в ней вожак Лил, который основал её вместе с Ругару, '
                       'Серой и Угольком. Подробнее можно узнать здесь: https://docs.google.com/document/d/1qEl_44yNHaxXuEchiGQEULNYVILRzrOHtz9M_i7ZNP4/edit?usp=sharing')

@bot.command()
async def craft(channel):
    await channel.send('Мама защищает нас, а чтоб Она могла узнавать нас даже в человеческом обличье мы носим '
                       'специальные амулеты, которые делают наши люди. \n Порой нам нужно поговорить с Мамой, '
                       'тогда мы проводим специальный ритуал и главной изюминкой, без которой ничего не получится '
                       'является особый напиток из разных трав и ягод, с его помощью наша связь с Природой становится '
                       'сильнее и мы можем увидеть Её! \n Подробнее можно узнать здесь: https://docs.google.com/document/d/1sMF46Wec3xIPehKq9ssbp7EJblJSSbdTtRl-a0Lt3W4/edit?usp=sharing')

@bot.command()
async def little(channel):
    await channel.send('Где алименты?')

@bot.command()
async def carter(channel):
    occupations = ['*прилетает в гости на вертолёте*',
                '*придумывает ивент, где оборотни пашут*',
                '*ищет заглушку для авто*'
                  ]
    i_rand = random.randint(0, (len(occupations) - 1))

    await channel.send(occupations[i_rand])

@bot.command()
async def lard(ctx):
    channel = bot.get_channel('channel-numb')
    author = ctx.message.author
    await channel.send(f'{author.mention}, Сало будешь?')

@bot.command()
async def lard_yes(ctx):
    channel = bot.get_channel('channel-numb')
    author = ctx.message.author
    await channel.send(f'{author.mention}, НА! \n *даёт сало*')

@bot.command()
async def lard_no(channel):
    await channel.send('Ты что, сало не уважаешь? *хомячит сало за обе щеки*')

@bot.command()
async def koshak(channel):
    await channel.send('Да чо вы опять до меня доволчились?')

@bot.command()
async def erik(channel):
    await channel.send('*успокаивает всех обиженных, улаживает конфликты и возвращает fie*')

@bot.command()
async def rugaru(channel):
    await channel.send('Опять молодняк обучать... *закатил глаза*')

@bot.command()
async def felis(channel):
    await channel.send('Невероятной красоты антропоморфное существо очень похожее на кошку. '
                       'Красивый, длинный и пушистый хвост, изящные изгибы тела, превосходная, '
                       'мягкая тёмно-рыжая шёрстка и светящиеся изумрудно-зелёные глаза с вытянутыми кошачьими зрачками.')

@bot.command()
async def felis_do(channel):
    await channel.send('*делает мяу и точит коготки о дерево*')

@bot.command()
async def lavo(channel):
    await channel.send('*поперхнулась медовухой с наркотиками и, почесав знак Уробороса на спине, изящно поправила ожерелье индейцев на шее*')

@bot.command()
async def lil(channel):
    await channel.send('Кто такой Лил? Это наш местный завод по производству молодняка.')

@bot.command()
async def sera(channel):
    await channel.send('Отстаньте, весь молодняк идёт к Ругару! *идёт социалить*')

@bot.command()
async def drew(channel):
    await channel.send('Где лампочки?')

@bot.command()
async def fie(channel):
    await channel.send('*ливает с сервера*')

@bot.command()
async def sulfur(channel):
    await channel.send('Дурак, это химический элемент, а не имя!')

@bot.command()
async def joseph(channel):
    quotations = ["В принципе, если заменить музыку на Дору Дуру, то можно и лайк поставить (с)",
                  "Гуляй рука, балдей писюн (с)",
                  "Видимо он похавал, но он голодный и идёт на меня. (с)",
                  "Компьютерные игры для дебилов (с)",
                  "2 Биг Мозга (с)",
                  "Внимание! Спасибо за внимание (с)",
                  "Зато за православные треки страйки не дают (с)",
                  "Отношения для дебилов (с)",
                  "Будущее за гомосексуализмом (с)",
                  "Помощь богов. Овощ предков. (с)",
                  "Зашел в медпункт, вышел инвалидом (с)",
                  "ВайтПенис (с)"
                  ]

    i_rand = random.randrange(0, (len(quotations)-1), 1)
    #i_rand = random.randrange(0,(len(quotations)-1), random.randint(1,9))
    #i_rand = random.randint(0,(len(quotations)-1))
    await channel.send(quotations[i_rand])

@bot.command()
async def dazachto(channel):
    await channel.send('За себя и за Змея!')

@bot.command()
async def advice(channel):
    advices = ["При охоте используй ПКМ+Q!",
            "Люди маленькие и слабые, их тело не выдерживает нашей звериной мощи.. \nПотому для спаривания лучше искать себеподобных...:flushed:",
            "Скверна из Палето продолжает надвигаться... Что сильно влияет на нашу силу. Нынче оборотни вынуждены пользоваться допингом - алым мёдом.\nЧтоб его получить достаточно смешать мёд с кровью братьев наших меньших 2 к 3 в 1 пластиковой бутылке.",
            "Раньше оборотни убивали кровососов. Но сейчас уже давно позабыли с чего началась эта война...:thinking: Гораздо выгоднее продавать их хитиновые панцыри.:yum:"
               ]

    i_rand = random.randint(0, (len(advices) - 1))
    await channel.send(advices[i_rand])

@bot.command()
async def auf(channel):
    await channel.send('AUF', tts=True)


@bot.command()
async def on_mess(self, message):
    channel = bot.get_channel('channel-numb')
    mentioned = message.mentions

    for user in mentioned:
        if user.id in afk_list:
            await self.client.send_message(message.channel, '{} is AFK'.format(user.display_name))

    print(message.channel.name)
    print(message.channel.id)


bot.run('TOKEN')