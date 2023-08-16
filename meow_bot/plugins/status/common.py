from nonebot import on_command

from . import server_status, status_config, status_permission

if status_config.server_status_enabled:
    command = on_command(
        "status",
        aliases={"状态"},
        permission=status_permission,
        priority=2,
        block=True,
        handlers=[server_status],
    )
    """`status`/`状态` command matcher"""
