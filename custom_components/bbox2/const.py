"""Constants for the Bouygues Bbox integration."""

DOMAIN = "bbox2"
BBOX_URL = "https://mabbox.bytel.fr"
CONF_PASSWORD = "password"
CONF_HOST = "host"
TO_REDACT = {
    "username",
    "password",
    "encryption_password",
    "encryption_salt",
    "host",
    "api_key",
    "serial",
    "system_serial",
    "ip4_addr",
    "ip6_addr",
    "account",
    "key",
}
