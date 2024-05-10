from fastapi import FastAPI

#Routers
import routers.router_auth, routers.router_todos

# Documentation
from documentations.description import api_description
from documentations.tags import tags_metadata


# Initialiser FastAPI
app = FastAPI(
  title="My Todos API",
  description= api_description,
  opean_api_tags= tags_metadata,
  docs_url='/'
)

# Routers
app.include_router(routers.router_todos.router)
app.include_router(routers.router_auth.router)