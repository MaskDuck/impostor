from os import getenv

debug = True

if debug:
    from dotenv import load_dotenv

    load_dotenv(override=True)


# token = getenv("TOKEN")
suggestion_channel = int(960446827579199488)
maintainer_role = int(830875873027817484)
admin_role = int(959723229805707285)
# Because it returns a string
pr_testing = bool((getenv("PR_TESTING") or "").lower() in ["true", "1"])
