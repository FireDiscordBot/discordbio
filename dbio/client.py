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


from .models.connections import UserConnections
from .models.user_details import UserDetails
import aiohttp


class DBioClient:
    BASE_URL = "https://api.discord.bio/v1"

    def __init__(self):
        self._session = aiohttp.ClientSession()

    async def api(self, path: str):
        res = await self._session.get(path)
        try:
            return await res.json()
        except Exception:
            return  # Raise custom exception here

    async def details(self, query: str) -> UserDetails:
        details = await self.api(f'/getUserDetails/{query}')
        if details['success']:
            return UserDetails(details)
        return  # Raise custom exception here

    async def connections(self, query: str, with_discord: bool = False) -> UserConnections:
        connections = await self.api(f'/getUserConnections/{query}')
        if with_discord:
            discord = await self.api(f'/getDiscordConnections/{query}')
            return UserConnections(connections, discord)
        return UserConnections(connections)
