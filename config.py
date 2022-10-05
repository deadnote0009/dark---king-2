from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "7171072"))
API_HASH = getenv("API_HASH", "64986f37a544e5c4fe9d551f4c3af68a")
BOT_TOKEN = getenv("BOT_TOKEN","5011267014:AAFsqhK6OJ8S5x0nbaLRTn-MeetXj0cYC7A")
BOT_NAME = getenv("BOT_NAME","Music2_lonelybot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "BQBOd7iU64OXf4GYExxMfQ99d_U10jI80H6HRV4Y3_I9_hnebVF5pgaP3TCm51VkZ3ekIe7qyUmBZiDXORETcgxiAtNtIElJwGkMgqNuAdFmbTQFLb9QzaAxTJlXzM7PKFsG-6OJPrbHQWlC7pdK8CFpJIwd221oTj87Rv-C3UGe4MtTvdOkSUummgkUFvQcLf2QsYHmAagQJozOTnntk3q1TCIcdsgcODmcfqj-BAcXJiDK7sAK-wlzMXzW4KatL30zfMjoiR-UFHcyEuWU2TRJekPk-K0DIpcyc5fVcfMLDjtsORhMXkAog3KksA6qfSKFpvpKNa5UaYd140ODFhf-dRR-LwA")
MASTER_USERNAME = list(getenv("MASTER_USERNAME", "itzyournil"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1805019557 5122474448").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
