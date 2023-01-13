import discord
from discord.ext import commands
import openai

bot = commands.Bot(command_prefix='.', intents=discord.Intents.default())

key = "open ai api key here"
openai.api_key = key

@bot.event
async def on_ready():
    print("Bot online")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

@bot.tree.command(name = 'ai_bot', description='responds with a ai respons')
async def ai(interaction : discord.Interaction, prompt : str):
    await interaction.response.send_message("Thinking...")
    response = openai.Completion.create(engine='text-davinci-003', prompt=prompt, temperature=0.1, top_p=1, max_tokens=1000)
    try:
        await interaction.edit_original_response(content='', embed=discord.Embed(title=f'Ai Response to "{prompt}"', description="```" + response['choices'][0]['text'] + "```"))
    except:
        await interaction.edit_original_response(content='Failed to answer.')

bot.run("discord bot token here")
