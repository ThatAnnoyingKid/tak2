import discord

# There will be no bad words in my Christan Discord server
with open('bad_words.txt', 'r') as file:
    words_list = file.read().split()

def has_bad_words(message):
    for word in words_list:
         if word in message.content:
              return True
    return False