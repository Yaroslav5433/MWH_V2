from os import getppid
import redis.asyncio as aredis
from config import get_config


cfg = get_config()


async def first_run() -> bool:
    ppid = getppid()
    redis = await aredis.from_url(cfg.redis_url)
    save_ppid = await redis.get('tg_bot_ppid')
    if save_ppid and int(save_ppid) == ppid:
        await redis.close()
        return False
    await redis.set('tg_bot_ppid', ppid)
    await redis.close()
    return True