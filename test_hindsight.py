import os
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

client = Hindsight(
    base_url="https://api.hindsight.vectorize.io",
    api_key=os.getenv("HINDSIGHT_API_KEY")
)

BANK_ID = "MemoryMeet AI"

# Store a meeting memory
client.retain(
    bank_id=BANK_ID,
    content="""
    ABC Technologies is interested in cloud migration.
    Their main concern is security.
    They are comparing our company with CloudX.
    Their approximate budget is 15 lakh rupees.
    The CTO is involved in the final decision.
    They want implementation completed within 3 months.
    """
)

print("Memory stored successfully!")

# Recall the memory
result = client.recall(
    bank_id=BANK_ID,
    query="What do I know about ABC Technologies?"
)

print("\nRecalled Memories:")
for memory in result.results:
    print("-", memory.text)