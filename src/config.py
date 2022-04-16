from os import getenv

debug = True

if debug:
    from dotenv import load_dotenv

    load_dotenv(override=True)


# token = getenv("TOKEN")
suggestion_channel = int(960446827579199488)
maintainer_role1 = int(830875873027817484)
maintainer_role2 = int(959723229805707285)
debug = bool(getenv("DEBUG") or False)
pr_testing = bool(getenv("PR_TESTING") or False)
