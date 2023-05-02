# Github informations
enableGithub = True
author = "Ted-18"
repository = "Bot.Assistant-LevelSystem"
version = "1.2.0"

# To activate this addon
cogEnabled = True

# Name of the addon
cogName = "levelsystem"

# Name of the file containing the cog
cogFile = "cogLevelSystem"

# List of packages required by the addon
packageDependencies = [
    "py-cord",
    "mysql-connector-python"
]

# List of addons required by the addon
addonDependencies = []

# List of permissions required by the addon
addonPermissions = [
    "manage_roles",
    "send_messages"
]

commandPermissions = {
    # Permission to check the addon's permissions
    "cmdRequirements" : "discord.permission.manage_guild",

    # Permission to get the level of a user
    "cmdLevel" : "discord.permission.send_messages",

    # Permission to create a reward
    "cmdCreateReward" : "discord.permission.manage_roles",

    # Permission to remove a reward
    "cmdRemoveReward" : "discord.permission.manage_roles",

    # Permission to list rewards
    "cmdRewardList" : "discord.permission.manage_roles",

    # Permission to set the channel of the level system messages
    "cmdSettingChannel" : "discord.permission.manage_channels",

    # Permission to get top users
    "cmdTop" : "discord.permission.send_messages"
}