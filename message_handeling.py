import discord
# I have no idea what I am going to do with this, just made it for funsies
def format_message(message):
    author = message.author.global_name
    message = message.content
    characters = len(message)	

    collected_message = {
         "message": message,
         "author": author,
         "charcters": characters
    }

    return collected_message