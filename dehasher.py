import discord
import hashlib
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!')

def dehash(string, hash_type):

  if hashlib.new('md4', string.encode()).hexdigest() == string:
    return 'md4'

  elif hashlib.md5(string.encode()).hexdigest() == string:
    return 'md5'

  elif hashlib.sha1(string.encode()).hexdigest() == string:
    return 'sha1'

  elif hashlib.sha256(string.encode()).hexdigest() == string:
    return 'sha256'

  elif hashlib.sha384(string.encode()).hexdigest() == string:
    return 'sha384'

  elif codecs.decode(string, 'base64') and codecs.encode(codecs.decode(string, 'base64'), 'base64').decode() == string:
    return 'base64'

  elif codecs.decode(string, 'base32') and codecs.encode(codecs.decode(string, 'base32'), 'base32').decode() == string:
    return 'base32'

  else:
    return 'Type de hash non reconnu'

@client.command()
async def dehash(ctx, hash_type: str, *, message: str):

  result = dehash(message, hash_type)

  await ctx.send(f'Le message dehashed est : {result}')

client.run('BOT TOKEN')