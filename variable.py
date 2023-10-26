import discord

def formatter(message,membre: discord.Member=None, server=None):
    if membre:

        member_variable = {
            "{user}": str(membre),
            "{user.id}": str(membre.id),
            "{user.display_name}": str(membre.display_name),
            "{user.avatar}": str(membre.display_avatar.url),
            "{user.mention}": str(membre.mention),
            "{user.name}": str(membre.name),
            "{user.badges}": str(membre.public_flags.all()),
            "{user.create_account}": membre.created_at.strftime(" %d/%m/%Y %H:%M:%S"),
            "{user.create_account.timestamp}": str(round(membre.created_at.timestamp())),
            "{user.join_server}": str(membre.joined_at.strftime("%d/%m/%Y %H:%M:%S")),
            "{user.join_server.timestamp}": str(round(membre.joined_at.timestamp())),
        }       
    if server:    
        guild_variable = {
            "{guild.name}": str(membre.guild.name),
            "{guild.membercount}": str(membre.guild.member_count),
            "{guild.icon}": str(membre.guild.icon.url),
            "{guild.id}": str(membre.guild.id)    
        }
            

        
    formated_message = message
    if membre:
        for key, value in member_variable.items():
            formated_message = formated_message.replace(key, value)
    if server:
        for key, value in guild_variable.items():
            formated_message = formated_message.replace(key, value)
    return formated_message