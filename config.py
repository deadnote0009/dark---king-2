from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "15235059"))
API_HASH = getenv("API_HASH", "352269b9e97005ffbe7f577dd89911e6")
BOT_TOKEN = getenv("BOT_TOKEN","5257312176:AAFqDe_Q81xkv3u9SCF_i0vIfIQfu6rZxRI")
BOT_NAME = getenv("BOT_NAME","Itscrazy2_bot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "BQCE9Ll8CjjHsWVLGDYI4YKStjrzFfJDDZdMl89W-9cRnHVycMki0hdDEVJQ0UE0wUniTap9MkpmimOHfElY9kP9ZyDO_gR3mWwy-qZVekvcJpTI1WnSMw0XZ4ik8Xbayb7_o4J5cPXpni6qcqPSnx418fV_HHiKohtc_bQoAwfAcfNKL0n2E_zadlMeQeT0giEuboiPsKGfeYgSdqo6lll9G0gK44lOeX0vsLC6vuKASUkfQqQtJnFNknox_BqMsxYsvZQeEnRLzlUvmtfb5bWiC68nFGR1WE1oaAdfj4CY-FcA48IY1L-RxC6mCSk6BgW8Fn2Ho-7KiF6FYt8TyRHxbmUSywA")
MASTER_USERNAME = list(getenv("MASTER_USERNAME", "DhrubaXD"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1805019557 5122474448").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
