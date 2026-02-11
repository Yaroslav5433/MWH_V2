from redis.asyncio.connection import ConnectionPool

from .config import get_config

cfg = get_config()

pool = ConnectionPool.from_url(cfg.redis_url)

