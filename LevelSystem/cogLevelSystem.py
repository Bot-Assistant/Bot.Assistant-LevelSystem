# 𝗔𝗨𝗧𝗛𝗢𝗥: Ted.
# 𝗖𝗢-𝗔𝗨𝗧𝗛𝗢𝗥: Mr.Se6un

# 𝗘𝗫𝗧𝗘𝗥𝗡𝗔𝗟 𝗜𝗠𝗣𝗢𝗥𝗧
# -

# 𝗕𝗢𝗧𝗔𝗦𝗦𝗜𝗦𝗧𝗔𝗡𝗧 𝗜𝗠𝗣𝗢𝗥𝗧𝗦
# Services
from services.serviceLogger import consoleLogger as Logger
from services.serviceDiscordLogger import discordLogger as DiscordLogger
# Settings
from settings.settingBot import debug

# 𝗕𝗢𝗧𝗔𝗦𝗦𝗜𝗦𝗧𝗔𝗡𝗧 𝗕𝗢𝗧 
import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()
discordCommands = serviceBot.classBot.getDiscordCommands()
commands = serviceBot.classBot.getCommands()
bot = serviceBot.classBot.getBot()


# 𝗔𝗗𝗗𝗢𝗡
# Init file
import addons.LevelSystem.init as init
# Handlers
import addons.LevelSystem.handlers.handlerDatabaseInit as handlerDatabaseInit
import addons.LevelSystem.handlers.handlerReward as handlerReward
# Commands
import addons.LevelSystem.functions.commands.commandRequirements as commandRequirements
import addons.LevelSystem.functions.commands.commandLevel as commandLevel
import addons.LevelSystem.functions.commands.commandRewardCreate as commandRewardCreate
import addons.LevelSystem.functions.commands.commandRewardList as commandRewardList
import addons.LevelSystem.functions.commands.commandRewardRemove as commandRewardRemove
import addons.LevelSystem.functions.commands.commandSettingChannel as commandSettingChannel
import addons.LevelSystem.functions.commands.commandTop as commandTop
# Events
import addons.LevelSystem.functions.events.eventOnGuildJoin as eventOnGuildJoin
import addons.LevelSystem.functions.events.eventOnGuildRemove as eventOnGuildRemove
import addons.LevelSystem.functions.events.eventOnMemberJoin as eventOnMemberJoin
import addons.LevelSystem.functions.events.eventOnMemberRemove as eventOnMemberRemove
import addons.LevelSystem.functions.events.eventOnMessage as eventOnMessage
import addons.LevelSystem.functions.events.eventOnReady as eventOnReady
import addons.LevelSystem.functions.events.eventOnVoiceStateUpdate as eventOnVoiceStateUpdate


class LevelSystem(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    

    # 𝗘𝗩𝗘𝗡𝗧𝗦
    # Event on Ready
    @commands.Cog.listener()
    async def on_ready(self):
        await eventOnReady.onReady()

    # Event on guild join
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await eventOnGuildJoin.addServer(guild)

    # Event on guild remove
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        await eventOnGuildRemove.deleteServer(guild)

    # Event on member join
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await eventOnMemberJoin.addUser(member)

    # Event on member remove
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await eventOnMemberRemove.deleteUser(member)

    # Event on message
    @commands.Cog.listener()
    async def on_message(self, message):
        await eventOnMessage.addXPMessage(message)

    # Event on voice state update*
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        await eventOnVoiceStateUpdate.addXPVoice(member, before, after)  


    # 𝗔𝗨𝗧𝗢𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘
    # Autocomplete for level
    async def getLevels(ctx: discord.AutocompleteContext):
        levels = handlerReward.getRewardLevels(ctx.interaction.guild_id)
        levels = [level[0] for level in levels]
        levels = list(dict.fromkeys(levels))
        return levels

    # Autocomplete for role from level
    async def getRolesFromLevel(ctx: discord.AutocompleteContext):
        level = ctx.options["level"]
        roles = handlerReward.getRewardRoles(ctx.interaction.guild_id, level)
        guild = ctx.interaction.guild
        roles = [guild.get_role(role[0]).name for role in roles]
        return roles


    # 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦
    groupLevelSystem = discordCommands.SlashCommandGroup(init.cogName, "🔶 Group of commands to manage the level system.")
    groupReward = groupLevelSystem.create_subgroup("reward", "🔶 Group of commands to manage the rewards of the level system.")
    groupSettings = groupLevelSystem.create_subgroup("settings", "🔶 Group of commands to manage the settings of the level system.")
    
    # Verify if the bot has the prerequisites permissions
    @groupLevelSystem.command(name="requirements", description="Check the prerequisites permissions of the addon.")
    async def cmdPermissions(self, ctx: commands.Context):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the requirements command.", str(ctx.command))
        await commandRequirements.checkRequirements(ctx)
    
    # Command to get the level of a user
    @groupLevelSystem.command(name="level", description="Command to get the level of a user.")
    async def cmdLevel(
        self,
        ctx: discord.ApplicationContext,
        user: discord.Option(
            discord.SlashCommandOptionType.user,
            required=False)
    ):
        await commandLevel.getUserLevel(ctx, user)

    # Command to create a reward
    @groupReward.command(name="create", description="Command to create a reward.")
    async def cmdCreate(
        self,
        ctx: discord.ApplicationContext,
        level: discord.Option(
            discord.SlashCommandOptionType.integer,
            required=True),
        role: discord.Option(
            discord.SlashCommandOptionType.role,
            required=True),
        type: discord.Option(
            str,
            choices=["Add role", "Remove role"],
            required=True)
    ):
        await commandRewardCreate.createReward(ctx, level, role, type)

    # Command to remove a reward
    @groupReward.command(name="remove", description="Command to remove a reward.")
    async def cmdRemove(
        self,
        ctx: discord.ApplicationContext,
        level: discord.Option(int , autocomplete=getLevels, description="Sound to delete", required=True),
        role: discord.Option(str , autocomplete=discord.utils.basic_autocomplete(getRolesFromLevel), description="Sound to delete", required=True)
        
    ):
        await commandRewardRemove.removeReward(ctx, level, role)

    # Command to list rewards
    @groupReward.command(name="list", description="Command to get the list of rewards.")
    async def cmdList(
        self,
        ctx: discord.ApplicationContext,
        level: discord.Option(int , autocomplete=getLevels, description="Sound to delete", required=False)
    ):
        await commandRewardList.getRewardList(ctx, level)

    # Command to define the channel for the level system
    @groupSettings.command(name="channel", description="Command to define the channel for the level system.")
    async def cmdChannel(
        self,
        ctx: discord.ApplicationContext,
        channel: discord.Option(
            discord.SlashCommandOptionType.channel,
            required=True)
    ):
        await commandSettingChannel.setChannel(ctx, channel)

    # Command to get the top 10 of the server
    @groupLevelSystem.command(name="top", description="Command to get the top 10 of the server.")
    async def cmdTop(
        self,
        ctx: discord.ApplicationContext
    ):
        await commandTop.getTop(ctx)
        

def setup(bot):
    if debug: Logger.debug("Loading Join Role")
    handlerDatabaseInit.databaseInit()
    bot.add_cog(LevelSystem(bot))
    
    