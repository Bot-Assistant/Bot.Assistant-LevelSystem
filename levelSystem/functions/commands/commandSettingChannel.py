import addons.levelSystem.handlers.handlerSettings as handlerSettings

async def setChannel(ctx, channel):
    handlerSettings.setChannelID(ctx.guild.id, channel.id)
    await ctx.respond(f"Successfully set the level system channel to {channel.mention}.", ephemeral=True, delete_after=10)