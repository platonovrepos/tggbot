import os
from dotenv_vault import load_dotenv

load_dotenv()
s3_fdf = os.getenv("hello")
print(s3_fdf)

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.

