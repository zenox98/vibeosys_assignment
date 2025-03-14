from sqlalchemy import Column, BigInteger, String, Enum, Integer, TIMESTAMP, func
from database import Base

class Product(Base):
  __tablename__ = "product"

  product_id = Column(BigInteger, primary_key=True, autoincrement=True)
  name = Column(String(100), nullable=False)
  category = Column(Enum('finished', 'semi-finished', 'raw', name="category_enum"), nullable=False)
  description = Column(String(250))
  product_image = Column(String(250))  # Storing image URL
  sku = Column(String(100), unique=True, nullable=False)
  unit_of_measure = Column(
      Enum('mtr', 'mm', 'ltr', 'ml', 'cm', 'mg', 'gm', 'unit', 'pack', name="unit_enum"),
        nullable=False
  )
  lead_time = Column(Integer, nullable=False, default=0)  # Lead time in days
  created_date = Column(TIMESTAMP, server_default=func.current_timestamp())
  updated_date = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())

  def __repr__(self):
    return f"<Product(product_id={self.product_id}, name='{self.name}', sku='{self.sku}')>"
