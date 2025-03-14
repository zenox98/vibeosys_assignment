from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List

import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

api = FastAPI()

models.Base.metadata.create_all(bind=engine)

class ProductBase(BaseModel):
  name: str = Field(..., min_length=1, max_length=100)
  category: str = Field(..., min_length=1, max_length=100)
  description: str = Field(..., min_length=1, max_length=250)
  product_image: str = Field(..., min_length=1, max_length=100)
  sku: str = Field(..., min_length=1, max_length=100)
  unit_of_measure: str = Field(..., min_length=1, max_length=100)
  lead_time: int = Field(..., gt=0)


@api.get("/product/list", response_model=List[ProductBase])
def list_products(page : int = Query(1,ge=1), limit : int = Query(10, le=100)):
  offset = (page - 1) * limit

  with Session(engine) as session:
    products = session.query(models.Product).offset(offset).limit(limit).all()
    return products

@api.get("product/{pid}/info", response_model=ProductBase)
def get_product(pid : int):
  with Session(engine) as session:
    product = session.get(models.Product, pid)
    if product is None:
      raise HTTPException(status_code=404, detail="Product not found")
    return product

@api.post("/product/add", response_model=ProductBase)
def add_product(product: ProductBase):
  with Session(engine) as session:
    db_product = models.Product(**product.dict())
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product

@api.put("product/{pid}/update", response_model=ProductBase)
def update_product(pid : int, product: ProductBase):
  with Session(engine) as session:
    db_product = session.get(models.Product, pid)
    if db_product is None:
      raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product.dict().items():
      setattr(db_product, key, value)
    session.commit()
    session.refresh(db_product)
    return db_product
