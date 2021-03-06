import random
import praw
import requests
import hikari
import tanjun
from aiohttp import request
from bot.bot.client import Client

component = tanjun.Component()

try:
    reddit = praw.Reddit(client_id='7gZghVq_G973pA',
                         client_secret='0llvlOaEUfzZaFvHVJ6GS2NKg27yew',
                         user_agent='Red.py')
                         
    CLIENT_ID = "7gZghVq_G973pA"
    SECRET_KEY = "0llvlOaEUfzZaFvHVJ6GS2NKg27yew"
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
    data = {
        'grant_type': 'password',
        'username': 'Coler21gamer',
        'password': 'U289ulso'
    }
    headers = {'User-Agent': 'RedBotAPI/1.0.0'}
    res = requests.post("https://www.reddit.com/api/v1/access_token", auth=auth, data=data, headers=headers)
    TOKEN = res.json()
    headers['Authorization'] = f'bearer {TOKEN}'
    res = requests.get('https://oauth.reddit.com/r/python/wholesomememes/', headers=headers)
    res.json
except:
    pass


@component.with_command
@tanjun.as_message_command("memes", "meme")
async def memes(self, ctx, subreddits=None):
        if subreddits == "wholesomememes":
            sub = "wholesomememes"
        if subreddits == "memes":
            sub = "memes"
        if subreddits == "dankmemes":
            sub = "dankmemes"
        if subreddits == None:
            reddits = 'wholesomememes','memes','dankmemes'
            sub = random.choice(reddits)
            random_tip = 'none','none','none','none','tip','none','none','none'
            tip = random.choice(random_tip)
            if tip == "tip":
                await ctx.send("Tip: You can choice the subreddit you get your memes from! Choice from wholesomememes, memes, or dankmemes!")
        memes_submissions = reddit.subreddit(f'{sub}').hot()
        post_to_pick = random.randint(1, 50)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        title = submission.title
        embed = Embed(title=f'{sub}', description=f"{title}", color=0xff0000)
        embed.set_image(url=submission.url)
        await ctx.send(embed=embed)
        
    
    
@component.with_command
@tanjun.as_message_command("goats", "goat")
async def goats(self, ctx):
    """Shows a pic of some cute goats!"""
    responses = ["https://i.imgur.com/GaPoxOD.jpg",
                "https://i.imgur.com/Sb7aaeA.jpg",
                "https://i.imgur.com/XRZFBUQ.jpg",
                "https://i.imgur.com/GYtW2rj.jpg",
                "https://i.imgur.com/wBVcBy2.jpg",
                "https://i.imgur.com/bh1rjHU.jpg",
                "https://i.imgur.com/nWtjVb7.jpg",
                "https://i.imgur.com/sMHl52t.jpg",
                "https://i.imgur.com/43EKJqB.jpg",
                "https://i.imgur.com/VmzPmOd.jpg",
                "https://i.imgur.com/GYtW2rj.jpg",
                "https://i.imgur.com/SMvWukk.jpg",
                "https://i.imgur.com/EjDdZUF.jpg",
                "https://i.imgur.com/1jE0hQZ.jpg",
                "https://i.imgur.com/G4tAGGq.jpg",
                "https://i.imgur.com/bEkgXeX.jpg",
                "https://i.imgur.com/hGatqXD.jpg",
                "https://i.imgur.com/iLcF3dI.jpg",
                "https://i.imgur.com/lbD1ULo.jpg",
                "https://i.imgur.com/HLphakw.jpg",
                "https://i.imgur.com/EVMNhq3.jpg",
                "https://i.imgur.com/i8obDzJ.jpg",
                "https://i.imgur.com/fS8UVaG.jpg",
                "https://i.imgur.com/vQdh5eL.jpg",
                "https://i.imgur.com/EkqJG5m.jpg",
                "https://i.imgur.com/RnHej9b.jpg",
                "https://i.imgur.com/4tr2OPW.jpg",
                "https://i.imgur.com/to9mALS.jpg",
                "https://i.imgur.com/BZkNTDG.jpg",
                "https://i.imgur.com/zHCmO6q.jpg",
                "https://i.imgur.com/cd6vYSC.jpg",
                "https://i.imgur.com/g96nPYf.jpg",
                "https://i.imgur.com/vWq4Q2x.jpg",
                "https://i.imgur.com/2fHDgJf.jpg",
                "https://i.imgur.com/u2ghRCK.jpg",
                "https://i.imgur.com/zK8ur8t.jpg",
                "https://i.imgur.com/ec350EO.jpg",
                "https://i.imgur.com/FL2nUQz.jpg",
                "https://i.imgur.com/KaHM9ZS.jpg",
                "https://i.imgur.com/2p9r7YG.jpg",
                "https://i.imgur.com/4LuhRoW.jpg",
                "https://i.imgur.com/RQmPVLE.jpg",
                "https://i.imgur.com/9drPkys.jpg",
                "https://i.imgur.com/qW9J550.jpg",
                "https://i.imgur.com/2ThV2Of.jpg",
                "https://i.imgur.com/9ucdAuz.jpg",
                "https://i.imgur.com/tJXlOPV.jpg",
                "https://i.imgur.com/htW5PLI.jpg",
                "https://i.imgur.com/qzQtY4O.jpg",
                "https://i.imgur.com/K2DkcDw.jpg",
                "https://i.imgur.com/jVqdXRj.jpg",
                "https://i.imgur.com/Ziukby7.jpg",
                "https://i.imgur.com/jGFoA5e.jpg",
                "https://i.imgur.com/uZpogzn.jpg",
                "https://i.imgur.com/9iAnJ6L.jpg",
                "https://i.imgur.com/y3XU87y.jpg",
                "https://i.imgur.com/tDUheKs.jpg"]
    await ctx.send(f'Goated! {random.choice(responses)}')

@component.with_command
@tanjun.as_message_command("eightball", "8ball")
async def eightball(self, ctx, *, question):
    """Ask a question and see what the wise goat says."""
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    embed = Embed(title = f'Question: {question}\nAnswer: {random.choice(responses)}', color = (0x0036FF))
    await ctx.send(embed = embed)

@component.with_command
@tanjun.as_message_command("fact")
async def fact(self, ctx, animal: str):
    """Shows a random fact and a image of either a dog, cat, panda, fox, bird, or koala."""
    if (animal == animal.lower()) in ("dog", "cat", "panda", "fox", "bird", "koala"):
        fact_url = f"https://some-random-api.ml/facts/{animal}"
        image_url = f"https://some-random-api.ml/img/{'birb' if animal == 'bird' else animal}"

        async with request("GET", image_url, headers={}) as response:
            if response.status == 200:
                data = await response.json()
                image_link = data["link"]

            else:
                image_link = None

        async with request("GET", fact_url, headers={}) as response:
            if response.status == 200:
                data = await response.json()

                embed = Embed(title=f"{animal.title()} fact",
                                description=data["fact"],
                                color=ctx.author.color)
                if image_link is not None:
                    embed.set_image(url=image_link)
                await ctx.send(embed=embed)

            else:
                await ctx.send(f"API returned a {response.status} status")

    else:
        await ctx.send("No facts are available for that animal.")

def load_component(client: Client) -> None:
    client.add_component(component.copy())