def show_movies():

vijay_movies = [
    "Ghilli", "Thuppakki", "Pokkiri", "Master", "Leo",
    "Kaththi", "Mersal", "Bigil", "Sarkar", "Beast"
]

ajith_movies = [
    "Mankatha", "Billa", "Vedalam", "Viswasam", "Veeram",
    "Arrambam", "Dheena", "Yennai Arindhaal", "Thunivu", "Valimai"
]

surya_movies = [
    "Ghajini", "Ayan", "Singam", "24", "Jai Bhim",
    "Soorarai Pottru", "Kaakha Kaakha", "Vel", "Vaaranam Aayiram", "NGK"
]

dhanush_movies = [
    "Asuran", "VIP", "Karnan", "Maari", "Polladhavan",
    "Aadukalam", "Kodi", "Captain Miller",
    "Thiruchitrambalam", "Yaaradi Nee Mohini"
]

top_x = int(input("Please enter top x number (1-10): "))
actor = input("Please enter actor name: ").lower()

if top_x < 1 or top_x > 10:
    print("Error: Please enter a number between 1 and 10")
    return

if actor == "vijay":
    movies = vijay_movies
elif actor == "ajith":
    movies = ajith_movies
elif actor == "surya":
    movies = surya_movies
elif actor == "dhanush":
    movies = dhanush_movies
else:
    print("Error: Unknown actor")
    return

print(f"\nHere are the top {top_x} super hit movies of {actor.title()}")

for i in range(top_x):
    print(f"{i + 1}. {movies[i]}")

show_movies()
