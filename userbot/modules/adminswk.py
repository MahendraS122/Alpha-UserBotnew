
from telethon.errors import (
    ChatAdminRequiredError,
)
from telethon.tl.types import (
    ChannelParticipantsAdmins,
)

from userbot.events import alphabot


@alphabot(outgoing=True, pattern=r"^\.admin$")
async def get_admin(show):
    info = await show.client.get_entity(show.chat_id)
    title = info.title if info.title else "Grup Ini"
    mentions = f"<b>🙈 Daftar Monyet Di Group {title}:</b> \n"
    try:
        async for user in show.client.iter_participants(
            show.chat_id, filter=ChannelParticipantsAdmins
        ):
            if not user.deleted:
                link = f'<a href="tg://user?id={user.id}">{user.first_name}</a>'
                mentions += f"\n🙉 Monyet {link}"
            else:
                mentions += f"\nMonyet Meningoy <code>{user.id}</code>"
    except ChatAdminRequiredError as err:
        mentions += " " + str(err) + "\n"
    await show.edit(mentions, parse_mode="html")


CmdHelp('adminwk').add_command(
    'admin', None, 'mengejek admin di group wkwk.').add()
