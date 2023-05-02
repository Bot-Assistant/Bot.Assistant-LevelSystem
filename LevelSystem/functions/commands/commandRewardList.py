import addons.LevelSystem.handlers.handlerReward as handlerReward

import settings.settingColors as settingColors
import settings.settingThumbnail as settingThumbnail

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()


async def getRewardList(ctx, level):

    # PERMISSIONS CHECK
    import addons.LevelSystem.functions.services.servicePermission as servicePermission
    if await servicePermission.permissionCheck(ctx, "cmdRewardList") == False:
        return

    if level is None:
        rewardLevelsDatabase = handlerReward.getRewardLevels(ctx.guild.id)
        rewardsDatabase = handlerReward.getAllRewards(ctx.guild.id)

        if len(rewardLevelsDatabase[0]) > 25:
            await ctx.respond("There are too many rewards to display. Please specify a level.", ephemeral=True, delete_after=5)
            return


        rewardLevelsDatabase = [rewardLevel[0] for rewardLevel in rewardLevelsDatabase]
        
        # Remove duplicates
        rewardLevelsDatabase = list(dict.fromkeys(rewardLevelsDatabase))

        embed = discord.Embed(
            title="Reward List",
            color=settingColors.green
        )

        for rewardLevel in rewardLevelsDatabase:
            
            fieldText = ""
            
            for reward in rewardsDatabase:
                if rewardLevel == reward[2]:

                    role = ctx.guild.get_role(reward[3])

                    if reward[4] == 1:
                        actionType = "+"
                    else:
                        actionType = "-"

                    fieldText += f"`{actionType}{role}`\n"

            embed.add_field(name=f"Level {rewardLevel}", value=fieldText)
                    

        await ctx.respond(embed=embed)
    
    else:
        rewardLevelsDatabase = handlerReward.getAllRewards(ctx.guild.id)

        embed = discord.Embed(
            title="Reward List",
            color=settingColors.green
        )

        fieldText = ""

        for rewardLevel in rewardLevelsDatabase:
            if rewardLevel[2] == level:
                role = ctx.guild.get_role(rewardLevel[3])

                if rewardLevel[4] == 1:
                    actionType = "+"
                else:
                    actionType = "-"

                fieldText += f"`{actionType}{role}`\n"

        embed.add_field(name=f"Level {level}", value=fieldText)
                
        await ctx.respond(embed=embed)