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
SESSION_NAME = getenv("SESSION_NAME", "BQAJOtxnkjASELFTHBW3aoLlavMhFL4qY3JaSVDvSHNFve9GOHi6TWZyR-SoHHSgDj5_3KI9KvGDizbUSOYx2d3oWxmSidZmKhh-XgDde0UEAILX2962ary-QtyOFhiSFwgkjPkLvBBOAmeSj2j-AHmOp0T--eDE16HSDRGjgne6q_hT3ig1ZeiUiU6sAa7rP8tVYOplVooVnkXXz1VKUqbakLSjpuMn0oYXVl_eFE0TH6IivdcnwCObmSODfzcmOGVT__IeU9h3jPjKsNQ_qy-t4xcD6ukL-V_cVwbXiW-ZKbFulql7tXfwJCad4YX2tKdw3YO5YVdFPYzXOMD57WojecdCVgA")
MASTER_USERNAME = list(getenv("MASTER_USERNAME", "DhrubaXD"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1805019557 5122474448").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
