import base64
import discord
import hashlib
import codecs
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!')

def detect_hash(string):

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
    return 'inconnu'

@client.command()
async def detecter(ctx, *, message: str):

  message_hash = detect_hash(message)

  await ctx.send(f'Le type de hash du message est : {message_hash}')

client.run('BOT TOKEN')
