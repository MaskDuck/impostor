def setup(bot):
  @_bot.slash_command()
  async def test1(inter):
    await inter.guild.create_auto_moderation_rule(name='test1',actions[AutoModerationAction(type=AutoModerationActionType.block_message)],trigger_metadata=AutoModerationTriggerMetadata(keyword_filter=["i hate maskduck"]))

  @_bot.slash_command()
  async def test2(inter):
    await inter.guild.create_auto_moderation_rule(name='test2',actions[AutoModerationAction(type=AutoModerationActionType.block_message)],trigger_metadata=AutoModerationTriggerMetadata(keyword_filter=["i hate maskduck"]))
