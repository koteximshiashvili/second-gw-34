import random

def text_game():
    print("welcome user this is a text game.")
    
    words = [
    "apple", "bread", "grape", "stone", "water", 
    "light", "plane", "watch", "fruit", "dance", 
    "laugh", "chair", "quick", "smile", "music", 
    "paint", "cloud", "start", "learn", "track", 
    "scout", "plant", "table", "happy", "heart", 
    "drink", "peace", "shoes", "house", "piano", 
    "front", "candy", "party", "watch", "daisy", 
    "clear", "build", "stick", "apple", "earth", 
    "grill", "sweet", "peace", "stone", 
    "flute", "punch", "brush", "lunar", "creek", 
    "clamp", "light", "field", "lunch", "bingo", 
    "track", "sight", "crown", "sweep", "sword", 
    "mango", "pouch", "purse", "shylo", "poker", 
    "chalk", "blast", "sword", "globe", "frown", 
    "swoop", "twist", "grape", "quilt", "beach", 
    "sweep", "proud", "gloom", "shine", "crisp", 
    "silly", "flash", "chore", "liver", "spicy", 
    "scoop", "drain", "stone", "plaza", "flame", 
    "roast", "truck", "clear", "flock"
]

    def secret_word():
        return random.choice(words)

    def game_rules():
        print("game rules:")
        print("hello user this is the text game")
        print("in this game you have to type a 5 letter word")
        print("if one of the letters you wrote is in the correct place")
        print("it will be displayed as green (🟩)")
        print("if one of the letters you wrote is in the word but not")
        print("in the correct position it will display as yellow (🟨)")
        print("lastly if it's not in the word or not in the right position")
        print("it will be displayed as red (🟥)")

    game_rules()

    def playing_game(user, answer):
        result = []
        for i in range(len(user)):
            if user[i] == answer[i]:
                result.append("🟩")
            elif user[i] in answer:
                result.append("🟨")
            else:
                result.append("🟥")
        return "".join(result)

    def check():
        answer = secret_word()
        attempts = 5
        
        while attempts > 0:
            user = input("enter a 5 letter word: ").lower()
            
            if len(user) != 5:
                print("please enter a 5 letter word")
                continue
            
            if user == answer:
                print("congratulations you guessed the word")
                break
            
            result = playing_game(user, answer)
            print("result: " + result)
            attempts -= 1

            if attempts == 0:
                print(f"you don't have any attempts left the word was {answer}")

    check()

text_game()
