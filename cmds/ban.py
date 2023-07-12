def ban(bot, discord, commands):
    '''
    Bans a member of the discord server. Prints who was banned in the same channel.
    Can only be done by a user with sufficient permissions.
    '''
    @bot.command()
    @commands.has_permissions(ban_members = True)
    async def ban(ctx, member: discord.Member, *, reason=None): #reason = none, bot won't give a reason for ban. Change so user can give a reason in the future.
        channel = bot.get_channel(839557877567455233)
        await member.ban(reason = reason)
        await ctx.send(f"{member} has been banned.")#sends who was banned in the same channel as where the command was executed.
        await channel.send(f"{member} has been banned from the server.")#sends who was banned in #admin-only.
        print(f"{member} has been banned.") #prints who was banned in terminal.
    
    @ban.error #if someone who isn't a mod or admin tries to ban, it tells them that they don't have permissions.
    async def ban_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to ban people.")