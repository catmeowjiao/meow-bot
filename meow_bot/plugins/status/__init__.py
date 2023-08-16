import inspect
import contextlib
from typing import Any, Dict

from jinja2 import Environment
from nonebot import get_driver
from nonebot.log import logger
from nonebot.matcher import Matcher
from nonebot.permission import SUPERUSER
from nonebot.plugin import PluginMetadata
from jinja2.meta import find_undeclared_variables

from .config import Config
from .helpers import humanize_date, relative_time, humanize_delta
from .data_source import (
    get_uptime,
    get_cpu_status,
    get_disk_usage,
    per_cpu_status,
    get_swap_status,
    get_memory_status,
    get_bot_connect_time,
    get_nonebot_run_time,
)

global_config = get_driver().config
status_config = Config.parse_obj(global_config)
status_permission = (status_config.server_status_only_superusers or None) and SUPERUSER

_ev = Environment(
    trim_blocks=True, lstrip_blocks=True, autoescape=False, enable_async=True
)
_ev.globals["relative_time"] = relative_time
_ev.filters["relative_time"] = relative_time
_ev.filters["humanize_date"] = humanize_date
_ev.globals["humanize_date"] = humanize_date
_ev.filters["humanize_delta"] = humanize_delta
_ev.globals["humanize_delta"] = humanize_delta

_t_ast = _ev.parse(status_config.server_status_template)
_t_vars = find_undeclared_variables(_t_ast)
_t = _ev.from_string(_t_ast)

KNOWN_VARS = {
    "cpu_usage": get_cpu_status,
    "per_cpu_usage": per_cpu_status,
    "memory_usage": get_memory_status,
    "swap_usage": get_swap_status,
    "disk_usage": get_disk_usage,
    "uptime": get_uptime,
    "runtime": get_nonebot_run_time,
    "bot_connect_time": get_bot_connect_time,
}
"""Available variables for template rendering."""


if not set(_t_vars).issubset(KNOWN_VARS):
    raise ValueError(
        f'Unknown variables in status template: {", ".join(set(_t_vars) - set(KNOWN_VARS))}'
    )


async def _solve_required_vars() -> Dict[str, Any]:
    """Solve required variables for template rendering."""
    return (
        {
            k: await v() if inspect.iscoroutinefunction(v) else v()
            for k, v in KNOWN_VARS.items()
            if k in _t_vars
        }
        if status_config.server_status_truncate
        else {
            k: await v() if inspect.iscoroutinefunction(v) else v()
            for k, v in KNOWN_VARS.items()
        }
    )


async def render_template() -> str:
    """Render status template with required variables."""
    message = await _t.render_async(**(await _solve_required_vars()))
    return message.strip("\n")


async def server_status(matcher: Matcher):
    """Server status matcher handler."""
    await matcher.send(message=await render_template())


from . import common

with contextlib.suppress(ImportError):
    import nonebot.adapters.onebot.v11

    from . import onebot_v11
