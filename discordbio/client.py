"""
MIT License

Copyright (c) 2020 GamingGeek (Jake Ward)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from .models.user_details import UserDetails, PartialUser
from .models.connections import UserConnections
from .errors import HTTPException, DBioError
from typing import List
import aiohttp


class DBioClient:
    def __init__(self):
        self._session = aiohttp.ClientSession()
        self.BASE_URL = "https://api.discord.bio/v1"

    async def api(self, path: str) -> tuple:
        if not path.startswith('/'):
            path = '/' + path
        try:
            res = await self._session.get(self.BASE_URL + path)
        except Exception as e:
            raise HTTPException(str(e))
        try:
            return (await res.json()), res.status
        except Exception as e:
            raise HTTPException(str(e), res)

    async def details(self, query: str) -> UserDetails:
        details, status = await self.api(f'/user/details/{query}')
        if status == 200:
            return UserDetails(details['payload'])
        if status == 404:
            raise DBioError(f'Bio for {query} could not be found')
        raise DBioError(f'An unknown error occurred. Status: {status}')

    async def connections(self, query: str, with_discord: bool = False) -> UserConnections:
        details, status = await self.api(f'/user/details/{query}')
        if status == 404:
            raise DBioError(f'User {query} could not be found')
        elif status == 200:
            if with_discord:
                return UserConnections(details['payload']['user']['userConnections'], details['payload']['user']['discordConnections'])
            return UserConnections(details['payload']['user']['userConnections'])
        raise DBioError(f'An unknown error occurred. Status: {status}')

    async def total_users(self) -> int:
        raise DeprecationWarning('The "totalUsers" endpoint no longer exists')

    async def top_upvoted(self) -> List[PartialUser]:
        upvoted, status = await self.api(f'/topLikes')
        if status == 200 and isinstance(upvoted['payload'], list):
            return [PartialUser(u) for u in upvoted['payload']]
        raise DBioError(f'Failed to retrieve top upvoted users')
