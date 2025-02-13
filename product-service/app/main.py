from fastapi import FastAPI
from app.db.db_connector import create_db_and_tables
from app.routes import category_and_gender_routes, product_routes
                           
                           #Gandu ho tum gandu 

async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
                              #Gandu ho tum gandu 
app = FastAPI(
    title="Product and Category Service",
    description="API for managing products",
    version="1.0.0",
    lifespan=lifespan,
    openapi_tags=[
        {"name": "Products", "description": "Operations with products."}
    ]
)
                            #Gandu ho tum gandu 

@app.get("/")
def home():
    return "Welcome to Product service"


app.include_router(router=product_routes.router,
                   prefix="/api/v1/product", tags=["Products"])
app.include_router(router=category_and_gender_routes.router,
                   prefix="/api/v1/product", tags=["Category"])




