from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Text , Optional, Union
from datetime import datetime
from router.router import user



app= FastAPI()

# Post Model

app.include_router(user)