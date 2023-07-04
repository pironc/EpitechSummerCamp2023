import random
import time


Products = {
    "Screens" : {
        "name" : "Ecer Gaming",
        "price" : random.randint(180, 230)
    },
    "Console" : {
        "name" : "Nantendo Swatch",
        "price" : random.randint(250, 320)
    },
    "Desktop computer" : {
        "name" : "NSA Gaming",
        "price" : random.randint(1000, 1200)
    },
    "TV" : {
        "name" : "Somsing QLED",
        "price" : random.randint(1000, 1500)
    },
    "Speaker" : {
        "name" : "JPL PoomPox",
        "price" : random.randint(100, 180)
    },
}

Dialogue = [
    "",
    "Voice-over : Hello and welcome to the Fair Price, and as speaker, Vincent FAIGAF !",
    "Vincent Faigaf : MEEP MEEP",
    "The public : YEAAAAA !",
    "Vincent Faigaf : And we're gonna get started right away with the presentation of our candidates!",
    "Our first candidate is : ",
    "Against : ",
    "We're gonna get started right away with the first product.",
]


def CustomPrint(text, sleep_time):
    print(text)
    time.sleep(sleep_time)

def StoryTeller():
    for sentence in Dialogue:
        CustomPrint(sentence, 2)

def PlayerTurnVerification(valuePlayer, price, nextPlayerName):
    if valuePlayer < price:
        print("It's more ! Now the turn is to " + nextPlayerName)
    if valuePlayer > price:
        print("It's less ! Now the turn is to " + nextPlayerName)

def RegisterPlayer(player1, player2):
  Dialogue[5] += player1
  Dialogue[6] += player2

def Main():
    playerOne = input("What's your name ? (First player) : ")
    playerTwo = input("What's your name ? (Second player) : ")
    valuePlayerOne = 0
    valuePlayerTwo = 0
    nb_product = random.choice(list(Products.keys()))
    product = Products.get(nb_product)
    price = product.get("price")
    
    RegisterPlayer(PlayerOne, PlayerTwo)
    StoryTeller()

    print("You need to find the price of this product : ", product.get("name"))

    while valuePlayerOne != price or valuePlayerTwo != price:
        valuePlayerOne = int(input(playerOne + " enter a number : "))
        PlayerTurnVerification(valuePlayerOne, price, playerTwo)
        if (valuePlayerOne == price):
            print(playerOne + " won !")
            break
        valuePlayerTwo = int(input(playerTwo + " enter a number : "))
        PlayerTurnVerification(valuePlayerTwo, price, playerOne)
        if (valuePlayerTwo == price):
            print(playerTwo + " won !")


Main()