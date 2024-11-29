
# Create With ❤️ By Sobhan Musazadeh (Mr.Legend)

# def calculate_average(numbers):
#     total = sum(numbers)
#     length = len(numbers)
#     average = total / length
#     return average

# # مثال استفاده از تابع:
# list_of_numbers = [3, 5, 7, 9, 12]
# result = calculate_average(list_of_numbers)
# print("میانگین اعداد لیست = ", round(result , 0))

# -----------------------------------------------------------------

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# # مثال استفاده از تابع:
# number = int(input("لطفا یک عدد وارد کنید: "))
# print("فاکتوریل", number, "برابر است با:", factorial(number))

# -----------------------------------------------------------------

# def reverse_string(string):
#     return string[::-1]

# # مثال استفاده از تابع:
# text = input("لطفا یک متن وارد کنید: ")
# print("متن معکوس شده:", reverse_string(text))

# -----------------------------------------------------------------


# def even_odd(numbers):
#     even = []
#     odd = []
#     for num in numbers:
#         if num % 2 == 0:
#             even.append(num)
#         else:
#             odd.append(num)
#     return even, odd
    

# # مثال استفاده از تابع:
# numbers = input("لطفا اعداد را با استفاده از کاما جدا کنید: ").split(",")
# numbers = [int(num) for num in numbers]
# even, odd = even_odd(numbers)
# print("اعداد زوج:", even)
# print("اعداد فرد:", odd)

# -----------------------------------------------------------------

# def count_chars_and_digits(input_str):
#     char_count = 0
#     digit_count = 0

#     for char in input_str:
#         if char.isalpha():
#             char_count += 1
#         elif char.isdigit():
#             digit_count += 1

#     return "Char : {}  , Num :  {} ".format(char_count , digit_count)
    
# text = input("Enter Your Text : ")
# print(count_chars_and_digits(text))

# -----------------------------------------------------------------

# numbers = [3, 2, 1, 4, 5]

# # مرتب‌کردن به ترتیب صعودی با استفاده از تابع sorted()
# sorted_numbers_asc = sorted(numbers)
# print("ترتیب صعودی: ", sorted_numbers_asc)

# # مرتب‌کردن به ترتیب نزولی با استفاده از تابع sorted()
# sorted_numbers_desc = sorted(numbers, reverse=True)
# print("ترتیب نزولی: ", sorted_numbers_desc)

# # مرتب‌کردن به ترتیب صعودی با استفاده از تابع sort()
# numbers.sort()
# print("ترتیب صعودی: ", numbers)

# # مرتب‌کردن به ترتیب نزولی با استفاده از تابع sort()
# numbers.sort(reverse=True)
# print("ترتیب نزولی: ", numbers)

# -----------------------------------------------------------------

# num = int(input("Enter a number: "))

# if num < 2:
#     print(num, "is not a prime number")
# else:
#     prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             prime = False
#             break

#     if prime:
#         print(num, "is a prime number")
#     else:
#         print(num, "is not a prime number")

# -----------------------------------------------------------------


# def count_occurrences(lst, num):
#     count = 0
#     for i in lst:
#         if i == num:
#             count += 1
#     return count

# my_list = [1, 3, 5, 3, 2, 1, 7, 9, 3]
# number = 3

# result = count_occurrences(my_list, number)
# print(f"The number {number} occurs {result} times in the list.")

# -----------------------------------------------------------------

#  برنامه ای بنویسید که اعداد مثبت را به باینری تبدیل کند.
# def count_occurrences(lst, num):
#     count = 0
#     for i in lst:
#         if i == num:
#             count += 1
#     return count

# my_list = [1, 3, 5, 3, 2, 1, 7, 9, 3]
# number = 3

# result = count_occurrences(my_list, number)
# print(f"The number {number} occurs {result} times in the list.")

# -----------------------------------------------------------------

# برنامه‌ای بنویسید که یک فایل متنی را باز کند و محتوای آن را به صورت متنی چاپ کند.

# filename = "example.txt"  # نام فایل مورد نظر
# with open(filename, "r") as f:
#     content = f.read()  # خواندن محتوای فایل
#     print(content)  # چاپ محتوای فایل

# -----------------------------------------------------------------

# برنامه‌ای بنویسید که یک فایل متنی را باز کند و تعداد کلمات، تعداد خطوط و تعداد حروف در فایل را محاسبه کند.

# filename = "example.txt"  # نام فایل مورد نظر
# with open(filename, "r") as f:
#     content = f.read()  # خواندن محتوای فایل
#     num_words = len(content.split())  # تعداد کلمات
#     num_lines = content.count('\n') + 1  # تعداد خطوط
#     num_chars = len(content)  # تعداد حروف
#     print("تعداد کلمات: ", num_words)
#     print("تعداد خطوط: ", num_lines)
#     print("تعداد حروف: ", num_chars)


# -----------------------------------------------------------------

# input_str = input("Enter a string: ")
# if input_str == input_str[::-1]:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

# -----------------------------------------------------------------

# برنامه‌ای بنویسید که دو رشته را از ورودی بگیرد و مشخص کند که آیا این دو رشته یک جفت آناگرام هستند یا نه.
# input_str1 = input("Enter the first string: ")
# input_str2 = input("Enter the second string: ")

# # Convert strings to lowercase and remove whitespace
# input_str1 = input_str1.lower().replace(" ", "")
# input_str2 = input_str2.lower().replace(" ", "")

# # Create a dictionary to store the frequency of characters in the strings
# freq_dict1 = {}
# freq_dict2 = {}

# for char in input_str1:
#     freq_dict1[char] = freq_dict1.get(char, 0) + 1

# for char in input_str2:
#     freq_dict2[char] = freq_dict2.get(char, 0) + 1

# # Compare the frequency of characters in the two strings
# if freq_dict1 == freq_dict2:
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")


# -----------------------------------------------------------------

# import requests

# def get_weather(city):
#     url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=API_KEY'
#     # جای API_KEY باید کلید API شما قرار گیرد
    
#     response = requests.get(url.format(city))
#     data = response.json()

#     # بررسی موفقیت آمیز بودن دریافت داده‌ها
#     if data['cod'] != 200:
#         print('مشکل در دریافت اطلاعات')
#     else:
#         # بازیابی داده‌های هواشناسی مورد نیاز
#         weather_data = {
#             'توضیحات': data['weather'][0]['description'],
#             'دما (درجه سلسیوس)': data['main']['temp'] - 273.15,
#             'رطوبت': data['main']['humidity'],
#             'فشار': data['main']['pressure']
#         }
#         return weather_data

# # تست کردن تابع
# city = input('نام شهر را وارد کنید: ')
# weather_data = get_weather(city)
# if weather_data:
#     print(f"وضعیت هوای {city}:")
#     for key, value in weather_data.items():
#         print(f"{key}: {value}")

# -----------------------------------------------------------------

# # دریافت دمای هوا به درجه فارنهایت از کاربر
# fahrenheit = float(input("لطفا دمای هوا را به درجه فارنهایت وارد کنید: "))

# # محاسبه دمای هوا به درجه سلسیوس
# celsius = (fahrenheit - 32) * 5/9

# # چاپ دمای هوا به درجه سلسیوس
# print("دمای هوا به درجه سلسیوس: ", celsius)



# -----------------------------------------------------------------


# def amplify(num):
#     listNum = []
#     if(num >= 1):
#         for i in range(1 , num +1 ):
#             # TODO: write code...
#             if(i % 4 == 0):
#                  listNum.append(i*10)
#             else:
#                  listNum.append(i)
           
#         return listNum    
#     else:
#         return "Your Num Not Current :("

# getNum = int(input("Enter Your Num : "))
# print(amplify(getNum))

# -------------------------------------------------------------

# def jadvalZarb(num):
#     for i in range(1 , num +1):
#         list = []
#         for j in range(1 , i+1):
#             list.append(i*j)
#         print(list)    
# getNum = int(input("Enter Your Num : "))
# jadvalZarb(getNum)

# -------------------------------------------------------------

# num1 = int(input("Enter Your Num1 : "))
# num2 = int(input("Enter Your Num2 : "))
# num3 = int(input("Enter Your Num3 : "))

# print("Avg : " ,(num1 + num2 + num3) // 3)

# -------------------------------------------------------------
# import random
# num = round(random.random()*100)

# print(num)
# def play (name , status):
#     # x =( status == h) ? 7 : 10
#     x = 0
#     if(status == "h"):
#         x= 7
#     else :
#         x=10
        
        
#     for i in range(1 , x+1):
#         enterNumber = int(input(f"Enter Number{i} : "))
#         if(enterNumber == num):
#             print(f"you are win ********** {name}")
#             return False
#         else:
#             if(enterNumber > num):
#                 print("Kochek tar Vared kon")
#             else:
#                 print("Bozorg tar Vared kon")
    
#     print(f"you are lost ------- {name}")
    

# name = str(input("Enter Your Name : "))
# status = input("Enter Your Level : ")
# play(name , status)








































