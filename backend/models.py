from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from enum import Enum

class DebtStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    CANCELLED = "cancelled"

class Debt(BaseModel):
    id: Optional[int] = None
    creditor_wallet: str = Field(..., description="The wallet address of the person owed money")
    debtor_wallet: str = Field(..., description="The wallet address of the person who owes money")
    amount_zar: float = Field(..., gt=0, description="Amount in South African Rand")
    description: str = Field(..., min_length=3, max_length=100)
    status: DebtStatus = DebtStatus.PENDING
    created_at: datetime = Field(default_factory=datetime.now)
    tx_hash: Optional[str] = Field(None, description="The blockchain transaction hash once settled")

class UserProfile(BaseModel):
    wallet_address: str
    nickname: str
    trust_score: float = 50.0  # Everyone starts with a neutral score
    total_debts_paid: int = 0