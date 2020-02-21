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


from typing import Optional, List


class DiscordConnection:
    connection_type: str
    name: str
    url: str

    def __init__(self, obj: dict) -> 'DiscordConnection':
        assert isinstance(obj, dict)
        connection_type = obj.get("connection_type")
        name = obj.get("name")
        url = obj.get("url")


class UserConnections:
    github: Optional[str]
    website: Optional[str]
    instagram: Optional[str]
    snapchat: Optional[str]
    linkedin: Optional[str]
    discord: List[DiscordConnection]

    def __init__(self, obj: dict, discord: list = list) -> 'UserConnections':
        assert isinstance(obj, dict)
        self.github = obj.get("github", None)
        self.website = obj.get("website", None)
        self.instagram = obj.get("instagram", None)
        self.snapchat = obj.get("snapchat", None)
        self.linkedin = obj.get("linkedin", None)
        self.discord = [DiscordConnection(c) for c in obj.get("discord", [])]
