##1 შექმენი გენერატორი, რომელიც ტექსტის თითოეულ სიმბოლოს აბრუნებს.

# word = "CODE"
#
# def char_generator(text):
#     for char in text:
#         yield char
#
# gen = char_generator(word)
#
# print(next(gen))  # C
# print(next(gen))  # O
# print(next(gen))  # D
# print(next(gen))  # E




##2 დაწერე პროგრამა რომელშიც მომხმარებელი შემოიყვანს მხოლოდ ციფრებს, ლოგიკა
# უნდა იყოს შემდეგი: გვაქვს კონკრეტული ლისტი და მომხმარებელი უნდა მიწვდეს
# შემოყვანილი ციფრით რომელიმე ელემენტს, თუ ვერ მიწვდება პროგრამა შეცდომაზე არ
# უნდა გავიდეს.


# arr = [1, 2, 3,4,5,6,7,8,9]
#
# try:
#     index = int(input("Enter index of element: "))
#     your_number = arr[index]
#     print(your_number)
# except ValueError:
#     print("Enter only number!")
# except IndexError:
#     print("We don't have enough elements!")
# finally:
#     print("Goodbye!")




##3შექმენი დეკორატორი, რომელიც ითვლის რამდენჯერ გამოიძახეს ფუნქცია.


# def counter(func):
#     def wrapper():
#         wrapper.count += 1
#         print(f"გამოძახება: {wrapper.count}")
#         return func()
#     wrapper.count = 0
#     return wrapper
#
#
# @counter
# def say():
#     print("Hi")
#
# say()
# say()



##4 მომხმარებელს უნდა დავუსვათ 5 მათემატიკური შეკითხვა, თითოეულზე სწორი
# პასუხი არის 10 ქულა ხოლო არასწორი 0 ქულა, მიღებული პასუხებიდან უნდა
# განვსაზღვროთ რამდენი ქულა აიღო მომხმარებელმა, შევქმნათ ლოფ ფაილი
# game.log და შევინახოთ ყველა ქულა. ბოლოს გამოვუტანოთ მიღებული შედეგი


# import logging
#
# # Logging კონფიგურაცია: ფაილში ჩაწერა
# logging.basicConfig(
#     filename="game.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(message)s"
# )
#
# questions = [
#     ("5 ^ 5 =", 25),
#     ("20 - 10 =", 10),
#     ("2 * 5 =", 10),
#     ("100 / 10 =", 10),
#     ("15 - 5 =", 10)
# ]
#
# score = 0
#
# for q, ans in questions:
#     try:
#         user_input = float(input(f"{q} "))
#         if user_input == ans:
#             score += 10
#             logging.info(f"შეკითხვა '{q}' - პასუხი სწორია, ქულა +10")
#         else:
#             logging.info(f"შეკითხვა '{q}' - პასუხი არასწორია, ქულა +0")
#     except ValueError:
#         print("გთხოვთ ჩაწეროთ მხოლოდ რიცხვი.")
#         logging.error(f"მომხმარებელმა არასწორი რიცხვი ჩაწერა შეკითხვისთვის '{q}'")
#
# logging.info(f"მომხმარებელმა მიიღო {score} ქულა {len(questions)*10}-დან")
# print(f"თქვენ მიიღეთ {score} ქულა {len(questions)*10}-დან")




##5 შექმენით ფაილი quiz.log, შექმენით გენერატორი რომელშიც შენახული იქნება
# 5 შეკითხვა და სათითაოდ დააბრუნებს, მომხმარებელმა უნდა უპასუხოს ყველა
# შეკითხვას და პასუხები შეინახეთ ლოგ ფაილში.


# import logging
#
# logging.basicConfig(
#     filename="quiz.log",
#     format="%(message)s",
#     level=logging.INFO
# )
#
# questions = [
#     ("5 ^ 5 =", 25),
#     ("20 - 10 =", 10),
#     ("2 * 5 =", 10),
#     ("100 / 10 =", 10),
#     ("15 - 5 =", 10)
# ]
#
# def question_generator(questions):
#     for i in questions:
#         yield i
#
# gen = question_generator(questions)
#
# for i, answer in gen:
#     user_input = input(f"{i} ")
#     logging.info(f"შეკითხვა '{i}' - მომხმარებელმა უპასუხა: {user_input}")


##6


# import logging
# import random
#
# logging.basicConfig(filename="rockpapergame.log", format="%(message)s", level=logging.INFO)
#
# options = ["ქვა", "ბადე", "მაკრატელი"]
# wins = {"ქვა": "მაკრატელი", "ბადე": "ქვა", "მაკრატელი": "ბადე"}
#
# user_score = 0
# comp_score = 0
# round_num = 1
#
# while user_score < 3 and comp_score < 3:
#     user_choice = input("აირჩიეთ: ქვა, ბადე, მაკრატელი: ").strip()
#     if user_choice not in options:
#         print("მხოლოდ ქვა, ბადე ან მაკრატელი!")
#         continue
#
#     comp_choice = random.choice(options)
#
#     if user_choice == comp_choice:
#         result = "ფრე"
#     elif wins[user_choice] == comp_choice:
#         user_score += 1
#         result = "მომხმარებელმა მოიგო"
#     else:
#         comp_score += 1
#         result = "კომპიუტერმა მოიგო"
#
#     print(f"{result} რაუნდი {round_num} (მომხმარებელი: {user_choice}, კომპიუტერი: {comp_choice})")
#     logging.info(f"რაუნდი {round_num}: მომხმარებელი={user_choice}, კომპიუტერი={comp_choice}, შედეგი={result}")
#
#     round_num += 1
#
# winner = "მომხმარებელმა" if user_score == 3 else "კომპიუტერმა"
# print(f"{winner} გაიმარჯვა თამაში!")
# logging.info(f"{winner} გაიმარჯვა თამაში!")




##7  კამათლის გეიმი


# import random
#
# while True:
#     game_1 = random.randint(1, 6)
#     game_2 = random.randint(1, 6)
#     print(f"Gamer 1 = {game_1}")
#     print(f"Gamer 2 = {game_2}")
#
#     if game_1 == game_2:
#         print("ფრე! ვიმეორებთ რაუნდს...")
#         continue
#
#     elif game_1 > game_2:
#         winner = "Gamer 1"
#         loser = "Gamer 2"
#     else:
#         winner = "Gamer 2"
#         loser = "Gamer 1"
#
#     print(f"{winner} მოიგო რაუნდი!")
#
#     ask_winner = input(f"{winner}, გსურთ კიდევ ერთი შანსი? (კი/არა): ").strip().lower()
#     if ask_winner != "კი":
#         print(f"{winner} აღარ სურს თამაში! Game over!")
#         break
#
#     ask_loser = input(f"{loser}, გსურთ კიდევ ერთი შანსი? (კი/არა): ").strip().lower()
#     if ask_loser != "კი":
#         print(f"{loser} აღარ სურს თამაში! Game over!")
#         break
#
#     print("გაგრძელება! კიდევ ერთი რაუნდი...")




##8


# import random
#
# words = ["ფუნქცია", "ციკლი", "პარამეტრი", "ლუპი", "ცვლადი",
#          "კონსტანტა", "კლასი", "ობიექტი", "მეთოდი", "მოდული"]
#
#
# word1, word2 = random.sample(words, 2)
#
# # ფუნქცია ორი რენდომ ასოს მოსაშორებლად
# def mask(word):
#     letters = random.sample(word, 2)
#     for l in letters:
#         word = word.replace(l, "", 1)
#     return word
#
#
# print("გამოიცანით სიტყვები:")
# print("1:", mask(word1))
# print("2:", mask(word2))
#
# # მომხმარებლის პასუხი
# answer1 = input("პირველი სიტყვა: ").strip()
# answer2 = input("მეორე სიტყვა: ").strip()
#
#
# score = (answer1 == word1) + (answer2 == word2)
# if score == 2:
#     print("გამარჯვება!")
# elif score == 1:
#     print("50%")
# else:
#     print("დამარცხდი")
