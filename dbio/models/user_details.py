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


from datetime import datetime
from typing import Optional
import dateutil.parser


GENDER = {
    1: "Male",
    2: "Female"
}


def from_datetime(x: str) -> Optional[datetime]:
    try:
        return dateutil.parser.parse(x)
    except ValueError:
        return None


class Discord:
    id: int
    username: str
    avatar: Optional[str]
    discriminator: str

    def __init__(self, obj: dict) -> 'Discord':
        assert isinstance(obj, dict)
        self.id = int(obj.get("id"))  # int for easy use with discord.py
        self.username = obj.get("username")
        self.avatar = obj.get("avatar", None)
        self.discriminator = obj.get("discriminator")


class Settings:
    user_id: int
    name: str
    status: Optional[str]
    description: Optional[str]
    verified: bool
    upvotes: int
    premium: bool
    location: Optional[str]
    gender: Optional[str]
    birthday: Optional[datetime]
    email: Optional[str]
    occupation: Optional[str]
    created_at: datetime
    banner: Optional[str]

    def __init__(self, obj: dict) -> 'Settings':
        assert isinstance(obj, dict)
        self.user_id = int(obj.get("user_id"))  # int for easy use with discord.py
        self.name = obj.get("name")
        self.status = obj.get("status", None)
        self.description = obj.get("description", None)
        self.verified = bool(obj.get('verified', 0))
        self.upvotes = obj.get('upvotes', 0)
        self.premium = bool(obj.get('premium_status', 0))
        self.location = obj.get("location", None)
        self.gender = GENDER.get(obj.get("gender"), None)
        self.birthday = None
        if obj.get("birthday", None):
            self.birthday = from_datetime(obj.get("birthday"))
        self.email = obj.get("email", None)
        self.occupation = obj.get("occupation", None)
        self.created_at = from_datetime(obj.get("created_at"))
        self.banner = obj.get("banner", None)


class UserDetails:
    settings: Settings
    discord: Discord

    def __init__(self, obj: dict) -> 'UserDetails':
        assert isinstance(obj, dict)
        self.settings = Settings(obj.get("settings"))
        self.discord = Discord(obj.get("discord"))
