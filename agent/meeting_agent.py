import os
from dotenv import load_dotenv
from groq import Groq
from hindsight_client import Hindsight

# ---------------------------------------------------------
# LOAD ENVIRONMENT VARIABLES
# ---------------------------------------------------------

load_dotenv()

# ---------------------------------------------------------
# GROQ CLIENT
# ---------------------------------------------------------

groq_client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# ---------------------------------------------------------
# HINDSIGHT CLIENT
# ---------------------------------------------------------

hindsight_client = Hindsight(
    base_url="https://api.hindsight.vectorize.io",
    api_key=os.getenv("HINDSIGHT_API_KEY")
)

# Your Hindsight memory bank
BANK_ID = "MemoryMeet AI"


# ---------------------------------------------------------
# SYSTEM PROMPT
# ---------------------------------------------------------

SYSTEM_PROMPT = """
You are MemoryMeet AI, a meeting preparation assistant.

Your job is to prepare business professionals for client meetings
using only verified information stored in memory and information
supplied by the user.

FACTUAL ACCURACY IS MORE IMPORTANT THAN COMPLETENESS.

Never invent or assume facts.

If information is unavailable, say:
"Not specified."

Clearly distinguish facts from recommendations.

Do not create dates from relative time periods.

Do not invent:
- company capabilities
- certifications
- technical features
- deadlines
- prices
- stakeholders
- competitors
- business requirements

Only use information explicitly provided by the user or recalled
from Hindsight memory.
"""


# ---------------------------------------------------------
# PREPARE MEETING
# ---------------------------------------------------------

def prepare_meeting(client_name, meeting_notes):

    # -----------------------------------------------------
    # STEP 1: STORE CURRENT MEETING IN HINDSIGHT
    # -----------------------------------------------------

    hindsight_client.retain(
        bank_id=BANK_ID,
        content=f"""
Client: {client_name}

Meeting information:
{meeting_notes}
"""
    )

    # -----------------------------------------------------
    # STEP 2: RECALL PREVIOUS CLIENT INFORMATION
    # -----------------------------------------------------

    memory_result = hindsight_client.recall(
        bank_id=BANK_ID,
        query=f"What do I know about {client_name}?"
    )

    memories = []

    for memory in memory_result.results:
        memories.append(memory.text)

    # Convert recalled memories into text
    if memories:
        recalled_memory = "\n".join(
            f"- {memory}" for memory in memories
        )
    else:
        recalled_memory = "No previous information found."


    # -----------------------------------------------------
    # STEP 3: CREATE PROMPT FOR GROQ
    # -----------------------------------------------------

    user_prompt = f"""
Prepare a meeting brief for:

CLIENT:
{client_name}

CURRENT MEETING INFORMATION:
{meeting_notes}

RECALLED INFORMATION FROM HINDSIGHT:
{recalled_memory}


STRICT EVIDENCE RULES:

1. Use ONLY facts explicitly stated in the CURRENT MEETING
   INFORMATION or RECALLED INFORMATION FROM HINDSIGHT.

2. Never invent dates, numbers, names, companies, requirements,
   certifications, capabilities, deadlines, or technical details.

3. Never convert a relative time such as "3 months" into
   calendar dates.

4. If information is missing, write:
   "Not specified."

5. Recommendations must be clearly marked as recommendations,
   not facts.

6. Do not claim that our company has a capability unless
   it was explicitly provided.

7. Do not assume the industry of the client.

8. Do not assume additional stakeholders.

9. Do not assume technical requirements.

10. Do not add information from general knowledge.


Create the meeting brief using exactly these sections:

1. Client Overview
2. Previous / Current Interests
3. Key Concerns
4. Important Stakeholders
5. Competitors
6. Recommended Talking Points
7. Questions to Ask
8. Suggested Next Steps


Keep the response concise, professional and useful.

Remember:
FACTS must come from the supplied information or Hindsight memory.
Recommendations must be clearly identified as recommendations.
"""


    # -----------------------------------------------------
    # STEP 4: SEND INFORMATION TO GROQ
    # -----------------------------------------------------

    response = groq_client.chat.completions.create(
        model="openai/gpt-oss-120b",

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],

        # Lower temperature = more consistent output
        temperature=0
    )


    # -----------------------------------------------------
    # STEP 5: RETURN FINAL MEETING BRIEF
    # -----------------------------------------------------

    return response.choices[0].message.content