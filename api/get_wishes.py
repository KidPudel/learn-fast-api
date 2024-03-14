import database
from typing import Any
import logging


async def get_wishes_from_db(amount: int) -> list[Any]:
    async with database.pgpool.connection() as conn:
        async with conn.cursor() as acursor:
            await acursor.execute(
                "select * from wishes limit %(amount)s;", {"amount": amount}, True
            )
            wishes = await acursor.fetchall()
            return wishes
