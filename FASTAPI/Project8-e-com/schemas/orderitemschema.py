from pydantic import BaseModel

class OrderItemSchema(BaseModel):
    order_id: int
    product_id: int
    quantity: int