"""Discovery service for AdGuard."""
import voluptuous as vol

from hassio.validate import network_port

from ..const import ATTR_HOST, ATTR_PORT


SCHEMA = vol.Schema(
    {vol.Required(ATTR_HOST): vol.Coerce(str), vol.Required(ATTR_PORT): network_port}
)