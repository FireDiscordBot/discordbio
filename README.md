# discordbio

An asynchronous Python wrapper for the [discord.bio API](https://api.discord.bio/v1)

### Installing

As of now, the wrapper is not yet on PyPi, but you can install directly from GitHub

```
pip install -U git+https://github.com/GamingGeek/discordbio@master
```

### Usage

* Setting up the client
> This will be used to make requests to the API

```py
from discordbio import DBioClient

client = DBioClient()
```

* Getting a user's details, via username or Discord ID
> All methods of DBioClient are typed meaning your IDE should auto complete the attributes
> If not, you can import the types (UserDetails and UserConnections) and manually set the type

```py
details = await client.details("geek")

# With Type
from discordbio import UserDetails

details: UserDetails = await client.details("geek")
```

* Getting a specific value from a user's details, e.g. description

```py
description = (await client.details("geek")).settings.description
```

* Getting a user's connections

```py
connections = await client.connections("geek")

# With Discord connections
connections = await client.connections("geek", with_discord=True)

# With Type
from discordbio import UserConnections

connections: UserConnections = await client.connections("geek", with_discord=True)
```

### Attributes

* Details (from client.details)
```py
settings: Settings
discord: Discord
```

* Settings
```py
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
```

* Discord
```py
id: int
username: str
avatar: Optional[str]
discriminator: str
```

* Connections (from client.connections)
```py
github: Optional[str]
website: Optional[str]
instagram: Optional[str]
snapchat: Optional[str]
linkedin: Optional[str]
discord: List[DiscordConnection]
```

* Discord Connections
```py
connection_type: str
name: str
url: str
```