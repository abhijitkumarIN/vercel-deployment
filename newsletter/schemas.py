from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class NewsletterSubscriptionBase(BaseModel):
    email: EmailStr

class NewsletterSubscriptionCreate(NewsletterSubscriptionBase):
    pass

class NewsletterSubscriptionResponse(NewsletterSubscriptionBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True