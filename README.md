# discordbio

An asynchronous Python wrapper for the [discord.bio API](https://api.discord.bio/v1)

### Installing

```
pip install discordbio
```

### Usage

* Setting up the client
> This will be used to make requests to the API

```py
from discordbio import DBioClient

client = DBioClient()
```

* Exceptions

| Error | Description |
| ----- | ----------- |
| discordbio.errors.BaseDBioException | Exception others subclass from, can be used to catch any error thrown from the wrapper |
| discordbio.errors.DBioError | Raised when discord.bio doesn't return a successful response |
| discordbio.errors.HTTPException | Raised when the request to discord.bio itself fails |

* Getting a user's details, via username or Discord ID
> All methods of DBioClient are typed meaning your IDE should auto complete the attributes
> If not, you can import the types (UserDetails and UserConnections) and manually set the type

```py
details = await client.details("geek")
```

```py
# With Type
from discordbio import UserDetails

details: UserDetails = await client.details("geek")
```

* Getting a specific value from a user's details, e.g. description or a users flags

```py
description = (await client.details("geek")).settings.description

flags = (await client.details("geek")).discord.flags
# Flags can be used to determine a user's badges
```

* Getting a user's connections

```py
connections = await client.connections("geek")

# With Discord connections
connections = await client.connections("geek", with_discord=True)
```

```py
# With Type
from discordbio import UserConnections


connections: UserConnections = await client.connections("geek", with_discord=True)
```

* Miscellaneous Endpoints

```py
users: int = await client.total_users()  # Returns total user count
```

```py
from discordbio import PartialUser
from typing import List


upvoted: List[PartialUser] = await client.top_upvoted() 
```

### Attributes

* UserDetails (from client.details)
```py
user: DBioUser
discord: Discord
```

* DBioUser
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
avatar_url: str
is_avatar_animated: bool
discriminator: str
flags: int
```

* Partial User (from client.top_upvoted)
```py
user_id: int
name: str
description: Optional[str]
verified: bool
upvotes: int
premium: bool
discord: Discord
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
