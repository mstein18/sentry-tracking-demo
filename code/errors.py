import sentry_sdk
import subprocess

# Gets the git HEAD commit hash to use as the release identifier. 
def get_release():
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"]
    ).decode().strip()

# Initialize Sentry
sentry_sdk.init(
    dsn="https://c97008fa69ad7303f784aa302fc5be41@o4505644778979328.ingest.us.sentry.io/4511140175085568",
    release=get_release()
)

# Force an error
1 / 0