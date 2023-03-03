import addons.LevelSystem.handlers.handlerReward as handlerReward

from settings.settingColors import *

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

# Remove a reward 
async def removeReward(ctx, level, role):
    
    # Get the role by name
    role = discord.utils.get(ctx.guild.roles, name=role)

    handlerReward.deleteReward(ctx.guild.id, level, role.id)

    embed = discord.Embed(title="Reward removed", color=green)
    embed.add_field(name="Level", value=f"```{level}```", inline=True)
    embed.add_field(name="Role", value=f"```{role.name}```", inline=True)

    await ctx.respond(embed=embed)