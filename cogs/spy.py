import discord
import random
import asyncio
from discord.ext import commands
from discord.ext.commands import Context

class Spy(commands.Cog, name="spy"):
    def __init__(self, bot):
        self.bot = bot
        self.spy_quotes = [
            "Diamondback user spotted, kill yourself and stream it tagging my channel in the title.",
            "STOP INGULFING IN FLAMES EVERY SQUARE INCH OF THE MAP RETARD AND GO PLAY THE OBJECTIVE",
            "Still watching CRD huh nigga?",
            "I am the Spy.",
            "Their medic pees sitting down, litterally why is he there and all his swings are crits ffs",
            "Off to visit your mother!"
        ]

    @commands.hybrid_command(
        name="disguise",
        description="The Spy disguises as another user.",
    )
    async def disguise(self, context: Context, member: discord.Member):
        """The bot takes the name of a target user."""
        old_nick = context.guild.me.display_name
        try:
            await context.guild.me.edit(nick=member.display_name)
            await context.send(f"*{member.display_name} is not one of us!* (Disguised as {member.mention})")
            
            # Wait 30 seconds then remove disguise
            await asyncio.sleep(30)
            await context.guild.me.edit(nick=old_nick)
            await context.channel.send("(Uncloacks) *Right behind you.*")
        except discord.Forbidden:
            await context.send("I don't have 'Manage Nicknames' permissions nigga.")

    @commands.hybrid_command(
        name="backstab",
        description="Try to backstab a member of the opposing team.",
    )
    async def backstab(self, context: Context, member: discord.Member):
        """A 50/50 chance to successfully backstab someone."""
        if random.choice([True, False]):
            embed = discord.Embed(
                title="CRITICAL HIT!",
                description=f"Successfully trickstabbed {member.mention}!\n*\"Fucking retard! My headfakes are too good and also stock is better than kunai!\"*",
                color=0xE02B2B
            )
        else:
            embed = discord.Embed(
                title="FAIL",
                description=f"You missed the stab on {member.mention}!\n*\"WHAT AM I PLAYING MAN?! What the fuck are these players man eu is so trash omg!\"*",
                color=0x7289DA
            )
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="sap",
        description="Sap a user (simulated)."
    )
    async def sap(self, context: Context, member: discord.Member):
        """Sends the sapper message."""
        await context.send(f"**[SAPPER PLACED]** ⚡ {member.mention}'s balls are being drained! \n*\"Sapping your sentry uwu!\"*")

    @commands.hybrid_command(
        name="spycheck",
        description="Identify if someone is a RED Spy."
    )
    async def spycheck(self, context: Context, member: discord.Member):
        """Randomly accuses someone of being a spy."""
        is_spy = random.choice(["is a Spy!", "is not one of us!", "is on our side."])
        await context.send(f"That {member.display_name} {is_spy}")

async def setup(bot):
    await bot.add_cog(Spy(bot))
