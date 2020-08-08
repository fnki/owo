import random


import discord
from redbot.core import commands


class Stay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def stay(self, ctx, seconds: int = 15):
        """Slows a channel"""
        assert seconds >= 0
        assert seconds <= 21600
        await ctx.channel.edit(
            slowmode_delay=seconds,
            reason=f"{ctx.message!r} invoked by {ctx.author!s} ({ctx.author.id})",
        )
        await ctx.send(
            random.choices(
                [
                    "https://cdn.discordapp.com/attachments/723743082687758447/730961247176097842/marrowstayvariant1.png",
                    "https://cdn.discordapp.com/attachments/723743082687758447/730961254620987493/marrowstayvariant2.png",
                    "https://cdn.discordapp.com/attachments/723743082687758447/730961262552285224/marrowstayvariant3.png",
                    "https://cdn.discordapp.com/attachments/723743082687758447/730961270517399603/marrowstayvariant4.png",
                    "https://cdn.discordapp.com/attachments/723743082687758447/730961281699414046/marrowstayvariant5.png",
                    "https://cdn.discordapp.com/attachments/723743082687758447/730961295242952794/marrowstayvariant6.png",
                    "https://cdn.discordapp.com/attachments/723743082687758447/730961313093779506/marrowstayvariant7.png",
                    "https://cdn.discordapp.com/attachments/723743082687758447/730961322430169219/marrowstayvariant8.png",
                    "https://cdn.discordapp.com/attachments/723743082687758447/730961333436153876/marrowstayvariant9.png",
                    # "https://cdn.discordapp.com/attachments/368178286435762177/675795960844255293/marrowstay.png",
                ]
            )
        )


    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unstay(self, ctx):
        """Unslows a channel"""
        await ctx.channel.edit(
            slowmode_delay=0,
            reason=f"{ctx.message!r} invoked by {ctx.author!s} ({ctx.author.id})",
        )
        await ctx.send(
            "https://cdn.discordapp.com/attachments/156665719109582850/729108439040786522/Yatsworram.png"
        )


def setup(bot):
    cog = Stay(bot)
    bot.add_cog(cog)
