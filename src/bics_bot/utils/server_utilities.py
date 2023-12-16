import yaml
from nextcord import Guild, Role


def get_role_id_by_name(guild: Guild, name: str):
    """
    Get the id of a role given the name of it.

    Args:
        guild: Channels and users
        name: Role name
    Returns:
        Role id
    """
    for role in guild.roles:
        if role.name == name:
            return role.id
    return None


def get_category_id_by_name(guild: Guild, name: str):
    """
    Get the id of a category given the name of it.

    Args:
        guild: Channels and users
        name: Category name
    Returns:
        Category id
    """
    for category in guild.categories:
        if category.name == name:
            return category.id
    return None


def get_channel_id_by_name(guild: Guild, name: str):
    """
    Get the id of a channel given the name of it.

    Args:
        guild: Channels and users
        name: Channel name
    Returns:
        Channel id
    """
    for channel in guild.channels:
        if channel.name == name:
            return channel.id
    return None


def retrieve_server_ids(guild: Guild):
    """
    Get the ids in a server.

    Args:
        guild: Channels and users
    Returns:
        list of ids
    """
    with open("./bics_bot/config/server_ids.yaml", "r") as f:
        server_ids = yaml.safe_load(f)
        config = {"roles": {}, "channels": {}, "categories": {}}

        for role in server_ids["roles"]:
            name = role.replace(" ", "-").lower()
            role_id = get_role_id_by_name(guild, role)
            if role_id is None:
                print(f"Role {role} not found")
                continue
            config["roles"][name] = role_id

        for category in server_ids["categories"]:
            name = category.replace(" ", "-").lower()
            category_id = get_category_id_by_name(guild, category)
            if category_id is None:
                print(f"Category {category} not found")
                continue
            config["categories"][name] = category_id

        for channel in server_ids["channels"]:
            name = channel.replace(" ", "-").lower()
            channel_id = get_channel_id_by_name(guild, channel)
            if channel_id is None:
                print(f"Channel {channel} not found")
                continue
            config["channels"][name] = channel_id
    return config

def get_member_by_id(guild: Guild, id:int):
    """
    Search for a guild member based on an id.
    Returns the Member object if there is a matching id in the guild, otherwise returns None.
    """
    for member in guild.members:
        if member.id == id:
            return member
    return None