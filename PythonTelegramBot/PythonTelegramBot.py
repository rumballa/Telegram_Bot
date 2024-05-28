import telebot
import mysql.connector
from config import config, token
from telebot import types


# Класи для визначення станів при додаванні рецептів
class RecipeStates:
    ENTER_NAME = 0
    ENTER_INGREDIENTS = 1
    ENTER_STEPS = 2
    ENTER_IMAGE = 3
    CONFIRMATION = 4

# Словник для збереження стану користувача
user_state = {}
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Ініціалізація бота з використанням токена
bot = telebot.TeleBot(token)
#bot = telebot.TeleBot('7180512209:AAEtyX7W9u1vTrvpEOXjae0gB2mqo_LbHvM')

# Обробник команди /start
@bot.message_handler(commands=['start'])
def start_message(message):
    text = f'Привіт😎, <b>{message.from_user.first_name}</b>!\n\nМене звати <b>Кулінарний бот-чарівник🍳</b>, і я буду радий запропонувати тобі чудові рецепти для будь-якої нагоди. Якщо ти не знаєш, що приготувати, я завжди готовий допомогти!\n\n <b>👩‍🍳 Можливості бота:</b>\n\n<b>🥘 Рецепти на всі смаки:</b> Від традиційних страв до екзотичних делікатесів – бот знає все!\n<b>🥑 Здорове харчування:</b> Рецепти для вегетаріанців, веганів, людей з алергіями та тих, хто дотримується спеціальних дієт.\n<b>⏲ Експрес-страви:</b> Ідеї для швидких та легких страв, коли часу обмаль.\n<b>🛒 Пошук за інгредієнтами:</b> Введіть наявні продукти, і бот запропонує вам відповідні рецепти.\n<b>📖 Кулінарні лайфхаки:</b> Корисні поради та хитрощі для ідеальних результатів.\n\n<b>📱 Як користуватися:</b>\n\n<b>Почніть:</b> Наберіть <b>/start</b>, щоб розпочати роботу.\n<b>Функції:</b> Щоб дізнатися, введіть команду <b>/help.</b>\n<b>Готуйте з задоволенням:</b> Дотримуйтесь покрокових інструкцій і створюйте кулінарні шедеври.\n\n<b>Відкрийте нові горизонти смаку та насолоджуйтесь кожним моментом на кухні!🎉</b>'
    bot.send_message(message.chat.id, text, parse_mode='html')

# Обробник команди /help
@bot.message_handler(commands=['help'])
def start_message(message): 
    mess = f'<b>Список команд, який допоможе тобі при роботі зі мною🤓:</b>\n\n/start - Розпочати роботу з ботом😊\n\n/help - Список команд📄\n\n/library - Бібліотека доступних відеорецептів📽\n\n/allrecipe - Список всіх рецептів, які є в базі даних 🗒️\n\n/addrecipe - Введіть цю команду, щоб додати власний рецепт до бази даних. Слідуйте простим інструкціям форми 😊\n\n/buttons - Системні кнопки 🕹\n\nТакож я вмію розпізнавати назви страв та підбирати рецепти за інгредієнтами. Введи назву страви або список продуктів, і я знайду для тебе ідеальний рецепт! ✨\n\n<b>❗❗❗ВАЖЛИВО❗❗❗</b>\n\nЩоб дані нових рецептів, які Ви плануєте додавати до бази даних, відображалися коректно, слідуйте наступним вимогам:\n-Вводьте назву рецепта з великої літери\n-Інгредієнти перелічуйте через кому, та з великої літери\n-Щоб спосіб приготування не зливався в один суцільний текст, розділяйте текст за допомогою клаві Shift+Enter'
    bot.send_message(message.chat.id, mess, parse_mode='html')

# Обробник команди /library
@bot.message_handler(commands=['library'])
def start_message(message): 
    mess = f'<b>Це список відеорецептів та їхні команди за допомогою яких, ти зможеш переглянути відео на веб-сайті😉:</b>\n\n<b>УКРАЇНСЬКА ПАЛЯНИЦЯ</b>🍞 - /website_loaf\n\n<b>ЯБЛУЧНИЙ ПЛЯЦОК</b>🥧 - /website_applepie\n\n<b>СИРНИКИ</b>🧀 - /website_cheesecake\n\n<b>ПОЛТАВСЬКІ ВАРЕНИКИ ТА ГАЛУШКИ</b>🥟 - /website_varenik\n\n<b>БОРЩ З ГРИБАМИ І ЧОРНОСЛИВОМ</b>🥣 - /website_borscht\n\n<b>ГРЕЧАНИКИ</b>🧆 - /website_grechanyk\n\n<b>ДОМАШНЯ ПІЦА</b>🍕 - /website_pizza\n\n<b>ДОМАШНІ ПЕЛЬМЕНІ</b>🥟 - /website_pelmeni\n\n<b>БУРІТО</b>🌯 - /website_burito\n\n<b>ПАСТА КАРБОНАРА</b>🍝 - /website_pasta\n\n'
    bot.send_message(message.chat.id, mess, parse_mode='html')

# Обробники команд для відеорецептів, які надсилають посилання на відповідні відео
@bot.message_handler(commands=['website_loaf'])
def website_message(message): 
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Для перегляду, натисніть на кнопку", url="https://www.youtube.com/watch?v=J5wrgg-nO4o"))
    bot.send_message(message.chat.id, "<b>УКРАЇНСЬКА ПАЛЯНИЦЯ</b>🍞 - посилання на відеорецепт👇", reply_markup=markup, parse_mode='html')

@bot.message_handler(commands=['website_applepie'])
def website_message(message): 
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Для перегляду, натисніть на кнопку", url="https://www.youtube.com/watch?v=HAcNbanOtBU"))
    bot.send_message(message.chat.id, "<b>ЯБЛУЧНИЙ ПЛЯЦОК</b>🥧 - посилання на відеорецепт👇", reply_markup=markup, parse_mode='html')

@bot.message_handler(commands=['website_cheesecake'])
def website_message(message): 
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Для перегляду, натисніть на кнопку", url="https://www.youtube.com/watch?v=xwMooZHSJqE"))
    bot.send_message(message.chat.id, "<b>СИРНИКИ</b>🧀 - посилання на відеорецепт👇", reply_markup=markup, parse_mode='html')

@bot.message_handler(commands=['website_varenik'])
def website_message(message): 
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Для перегляду, натисніть на кнопку", url="https://www.youtube.com/watch?v=wB42gZzx2Xs"))
    bot.send_message(message.chat.id, "<b>ПОЛТАВСЬКІ ВАРЕНИКИ ТА ГАЛУШКИ</b>🥟 - посилання на відеорецепт👇", reply_markup=markup, parse_mode='html')

@bot.message_handler(commands=['website_borscht'])
def website_message(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Для перегляду, натисніть на кнопку", url="https://www.youtube.com/watch?v=eYkLcIKfm1c"))
    bot.send_message(message.chat.id, "<b>БОРЩ З ГРИБАМИ І ЧОРНОСЛИВОМ</b>🥣 - посилання на відеорецепт👇", reply_markup=markup, parse_mode='html')

@bot.message_handler(commands=['website_grechanyk'])
def website_message(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Для перегляду, натисніть на кнопку", url="https://www.youtube.com/watch?v=_0P90Pc8bro"))
    bot.send_message(message.chat.id, "<b>ГРЕЧАНИКИ</b>🧆 - посилання на відеорецепт👇", reply_markup=markup, parse_mode='html')

@bot.message_handler(commands=['website_pizza'])
def website_message(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Для перегляду, натисніть на кнопку", url="https://www.youtube.com/watch?v=FLNSVA1f-z8"))
    bot.send_message(message.chat.id, "<b>ДОМАШНЯ ПІЦА</b>🍕 - посилання на відеорецепт👇", reply_markup=markup, parse_mode='html')

@bot.message_handler(commands=['website_pelmeni'])
def website_message(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Для перегляду, натисніть на кнопку", url="https://www.youtube.com/watch?v=B5rS8doCqyc"))
    bot.send_message(message.chat.id, "<b>ДОМАШНІ ПЕЛЬМЕНІ</b>🥟 - посилання на відеорецепт👇", reply_markup=markup, parse_mode='html')

@bot.message_handler(commands=['website_burito'])
def website_message(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Для перегляду, натисніть на кнопку", url="https://www.youtube.com/watch?v=BHrba_xyr4w"))
    bot.send_message(message.chat.id, "<b>БУРІТО</b>🌯 - посилання на відеорецепт👇", reply_markup=markup, parse_mode='html')

@bot.message_handler(commands=['website_pasta'])
def website_message(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Для перегляду, натисніть на кнопку", url="https://www.youtube.com/watch?v=mT8B9fE_vdg"))
    bot.send_message(message.chat.id, "<b>ПАСТА КАРБОНАРА</b>🍝 - посилання на відеорецепт👇", reply_markup=markup, parse_mode='html')

# Обробник команди /buttons для відображення системних кнопок
@bot.message_handler(commands=['buttons'])
def buttons_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    start = types.KeyboardButton('/start')
    help = types.KeyboardButton('/help')
    markup.add(start, help)
    bot.send_message(message.chat.id, "Кнопки, які виконують системні команди знаходяться під текстовим полем👇", reply_markup=markup)

# Обробник команди /allrecipe для відображення всіх рецептів з бази даних
@bot.message_handler(commands=['allrecipe'])
def print_allRecipe(message):
    cursor.execute("SELECT Name FROM Recipes")
    names = cursor.fetchall()
    text = f"<b>Наші рецепти</b>!\n\n"
    index = 1; 
    for name in names:
        text += str(index) + ". " + name[0] + "\n"
        index += 1
    bot.send_message(message.chat.id, text, parse_mode='html')

# Обробник команди /addrecipe для ініціювання процесу додавання рецепту
@bot.message_handler(commands=['addrecipe'])
def handle_add_recipe_command(message):
    user_state[message.chat.id] = RecipeStates.ENTER_NAME
    bot.send_message(message.chat.id, "Введіть назву рецепту:")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    chat_id = message.chat.id
    if chat_id in user_state:
        state = user_state[chat_id]
        if state == RecipeStates.ENTER_IMAGE:
            user_state[chat_id] = RecipeStates.CONFIRMATION
            file_id = message.photo[-1].file_id

            # Отримуємо інформацію про файл
            file_info = bot.get_file(file_id)
        
            # Отримуємо вміст файлу безпосередньо
            user_state[str(chat_id) + "_photo"] = bot.download_file(file_info.file_path)
            # Надсилаємо користувачеві попередній перегляд рецепту
            recipe_name = user_state[str(chat_id) + "_recipe_name"]
            ingredients = user_state[str(chat_id) + "_ingredients"]
            steps = user_state[str(chat_id) + "_steps"]
            photo = user_state[str(chat_id) + "_photo"]




            preview_recipe = f"<b>{recipe_name}</b>\n\n<b>Інгрідієнти:</b> {ingredients}\n\n<b>Етапи приготування</b>:\n\n{steps}\n\n"
            bot.send_photo(chat_id, photo)
            bot.send_message(chat_id, preview_recipe, parse_mode="HTML")
            # Запитуємо у користувача підтвердження додавання рецепта в базу даних
            confirmation_message = "Ви дійсно бажаєте додати цей рецепт?"
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add(types.KeyboardButton("Так"), types.KeyboardButton("Ні"))
            bot.send_message(chat_id, confirmation_message, reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_user_messages(message):
    chat_id = message.chat.id
    if chat_id in user_state:
        state = user_state[chat_id]
        if state == RecipeStates.ENTER_NAME:
            user_state[chat_id] = RecipeStates.ENTER_INGREDIENTS
            user_state[str(chat_id) + "_recipe_name"] = message.text
            bot.send_message(chat_id, "Введіть інгрідієнти через кому:")
        elif state == RecipeStates.ENTER_INGREDIENTS:
            user_state[chat_id] = RecipeStates.ENTER_STEPS
            user_state[str(chat_id) + "_ingredients"] = message.text
            bot.send_message(chat_id, "Введіть кроки приготування:")
        elif state == RecipeStates.ENTER_STEPS:
            user_state[chat_id] = RecipeStates.ENTER_IMAGE
            user_state[str(chat_id) + "_steps"] = message.text  # Зберігаємо кроки приготування
            bot.send_message(chat_id, "Надішліть фото:")
        elif state == RecipeStates.ENTER_IMAGE:
            user_state[chat_id] = RecipeStates.CONFIRMATION
            user_state[str(chat_id) + "_photo"] = "-"  # Зберігаємо кроки приготування
            recipe_name = user_state[str(chat_id) + "_recipe_name"]
            ingredients = user_state[str(chat_id) + "_ingredients"]
            steps = user_state[str(chat_id) + "_steps"]
            photo = user_state[str(chat_id) + "_photo"]

            preview_recipe = f"<b>{recipe_name}</b>\n\n<b>Інгрідієнти:</b> {ingredients}\n\n<b>Етапи приготування</b>:\n\n{steps}\n\n"
            if photo != "-":
                bot.send_photo(chat_id, photo)
            bot.send_message(chat_id, preview_recipe, parse_mode="HTML")
             # Запитуємо у користувача підтвердження додавання рецепта в базу даних
            confirmation_message = "Ви дійсно бажаєте додати цей рецепт?"
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add(types.KeyboardButton("Так"), types.KeyboardButton("Ні"))
            bot.send_message(chat_id, confirmation_message, reply_markup=markup)
        elif state == RecipeStates.CONFIRMATION:
            if message.text.lower() == "так":
                recipe_name = user_state.pop(str(chat_id) + "_recipe_name")
                ingredients = user_state.pop(str(chat_id) + "_ingredients")
                steps = user_state.pop(str(chat_id) + "_steps")  # Використовуємо збережені кроки приготування
                photo = user_state.pop(str(chat_id) + "_photo")
                add_new_recipe(recipe_name, [ingredient.strip() for ingredient in ingredients.split(',')], steps, photo)
                bot.send_message(chat_id, "Рецепт успішно додано!")
            else:
                bot.send_message(chat_id, "Додавання рецепта відмінено.")

            # Видаляємо стан користувача
            del user_state[chat_id]
    else:
        response = search_by_name(message.text, chat_id)
        if(response == "Рецепта не було знайдено!"):
            ingredients = [ingredient.strip() for ingredient in message.text.split(',')]
            response = search_by_ingredients(ingredients)

        bot.send_message(chat_id, response, parse_mode='html')

# Функція для пошуку рецепту за назвою
def search_by_name(name, chat_id):
    query = """
    SELECT r.Name, r.StepCooking, GROUP_CONCAT(i.Name SEPARATOR ', ') AS Ingredients, r.Photo
    FROM Recipes r
    JOIN RecipeIngredients ri ON r.id = ri.recipe_id
    JOIN Ingredients i ON ri.ingredient_id = i.id
    WHERE r.Name = %s
    GROUP BY r.id, r.Name, r.StepCooking;
    """
    cursor.execute(query, (name,))
    result = cursor.fetchall()
    if result:
        for (name, step_cooking, ingredients, photo) in result:
            if photo is not None:
                bot.send_photo(chat_id, photo)
            text = f"<b>{name}</b>\n\n<b>Інгрідієнти:</b> {ingredients}\n\n<b>Етапи приготування</b>:\n\n{step_cooking}"
    else:
        text = "Рецепта не було знайдено!"
    
    return text

# Функція для пошуку рецепту за інгредієнтами
def search_by_ingredients(ingredients_list):
    placeholders = ', '.join(['%s'] * len(ingredients_list))
    
    query = f"""
    SELECT r.Name
    FROM Recipes r
    JOIN RecipeIngredients ri ON r.id = ri.recipe_id
    JOIN Ingredients i ON ri.ingredient_id = i.id
    WHERE i.Name IN ({placeholders})
    GROUP BY r.id, r.Name
    HAVING COUNT(DISTINCT i.Name) = %s;
    """
    
    cursor.execute(query, (*ingredients_list, len(ingredients_list)))
    results = cursor.fetchall()
    
    if results:
        response = "\n".join([name[0] for name in results])
    else:
        response = "No recipes found with these ingredients."

    return response

# Функція для додавання нового рецепту в базу даних
def add_new_recipe(name, ingredients, steps, file_data):
    # Вставка нового рецепту в таблицю Recipes
    insert_recipe_query = "INSERT INTO Recipes (Name, StepCooking, Photo) VALUES (%s, %s, %s)"
    if file_data == "-":
        recipe_data = (name, steps, None)
    else: 
        recipe_data = (name, steps, file_data)
    cursor.execute(insert_recipe_query, recipe_data)
    recipe_id = cursor.lastrowid

    # Вставка інгредієнтів в таблицю Ingredients (якщо вони нові)
    insert_ingredient_query = """INSERT INTO Ingredients (Name)
                                SELECT * FROM (SELECT %s) AS tmp
                                WHERE NOT EXISTS (
                                    SELECT Name FROM Ingredients WHERE Name = %s
                                ) LIMIT 1;"""
    for ingredient in ingredients:
        cursor.execute(insert_ingredient_query, (ingredient, ingredient))

    # Отримання ID інгредієнтів
    select_ingredient_query = "SELECT id FROM Ingredients WHERE Name = %s"
    ingredient_ids = []
    for ingredient in ingredients:
        cursor.execute(select_ingredient_query, (ingredient,))
        result = cursor.fetchone()
        while cursor.nextset():  # Переконатися, що попередній набір результатів очищений
            pass
        if result:
            ingredient_id = result[0]
            ingredient_ids.append(ingredient_id)

    # Вставка зв'язків між рецептом і інгредієнтами в таблицю RecipeIngredients
    insert_recipe_ingredient_query = "INSERT INTO RecipeIngredients (recipe_id, ingredient_id) VALUES (%s, %s)"
    for ingredient_id in ingredient_ids:
        cursor.execute(insert_recipe_ingredient_query, (recipe_id, ingredient_id))
        while cursor.nextset():  # Переконатися, що попередній набір результатів очищений
            pass
    
    
    conn.commit()
    
    
# Запуск бота
bot.polling(none_stop=True)

# Закриваємо курсор
cursor.close()
conn.commit()
conn.close()