from os import getenv

debug = True

if debug:
    from dotenv import load_dotenv

    load_dotenv(override=True)


token = getenv("TOKEN")
suggestion_channel = int(getenv("SUGGESTION_CHANNEL"))
role1 = int(getenv("ROLE1"))
role2 = int(getenv("ROLE2"))
debug = bool(getenv("DEBUG"))
pr_testing = bool(getenv("PR_TESTING"))
