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
        if details['success']:
            return UserDetails(details['payload'])
        if status == 404:
            raise DBioError(f'Bio for {query} could not be found')
        raise DBioError(f'An unknown error occurred. Status: {status}')

    async def connections(self, query: str, with_discord: bool = False) -> UserConnections:
        connections, status = await self.api(f'/user/connections/{query}')
        if status == 202:
            raise DBioError(f'Connections for {query} could not be found')
        if with_discord:
            discord, status = await self.api(f'user/discordConnections/{query}')
            if connections['success'] and discord['success']:
                return UserConnections(connections['payload'], discord['payload'])
            else:
                if not connections['success']:
                    raise DBioError(f'Failed to retrieve connections')
                else:
                    raise DBioError(f'Failed to retrieve discord connections')
        if connections['success']:
            return UserConnections(connections['payload'])
        else:
            raise DBioError(f'Failed to retrieve connections')

    async def total_users(self) -> int:
        users, status = await self.api(f'/totalUsers')
        if status != 200:
            raise DBioError(f'Non success status code {status} when fetching total users')
        return users['payload']

    async def top_upvoted(self) -> List[PartialUser]:
        upvoted, status = await self.api(f'/topUpvoted')
        if isinstance(upvoted['payload'], list):
            return [PartialUser(u) for u in upvoted['payload']]
        else:
            raise DBioError(f'Failed to retrieve top upvoted users')
