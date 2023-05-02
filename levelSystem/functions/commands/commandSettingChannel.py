import addons.LevelSystem.handlers.handlerSettings as handlerSettings

import settings.settingThumbnail as settingThumbnail

async def setChannel(ctx, channel):

    # PERMISSIONS CHECK
    import addons.LevelSystem.functions.services.servicePermission as servicePermission
    if await servicePermission.permissionCheck(ctx, "cmdSettingChannel") == False:
        return

    handlerSettings.setChannelID(ctx.guild.id, channel.id)

    await ctx.respond(f"Successfully set the level system channel to {channel.mention}.", ephemeral=True, delete_after=10)