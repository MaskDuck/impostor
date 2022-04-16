from os import getenv

debug = True

if debug:
    from dotenv import load_dotenv

    load_dotenv(override=True)


token = getenv("TOKEN")
suggestion_channel = int(getenv("SUGGESTION_CHANNEL"))
maintainer_role1 = int(getenv("MAINTAINER_ROLE1"))
maintainer_role2 = int(getenv("MAINTAINER_ROLE2"))
debug = bool(getenv("DEBUG"))
pr_testing = bool(getenv("PR_TESTING"))

