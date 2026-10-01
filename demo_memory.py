from agent.meeting_agent import prepare_meeting


print("\n" + "=" * 70)
print("        MEMORYMEET AI - HINDSIGHT LEARNING DEMO")
print("=" * 70)


client_name = "ABC Technologies"


# ============================================================
# MEETING 1
# ============================================================

print("\n\nMEETING 1")
print("-" * 70)

meeting_1 = """
ABC Technologies is interested in cloud migration.
They are exploring solutions for moving their systems to the cloud.
"""

result_1 = prepare_meeting(
    client_name,
    meeting_1
)

print(result_1)


# ============================================================
# MEETING 2
# ============================================================

print("\n\nMEETING 2")
print("-" * 70)

meeting_2 = """
ABC Technologies said that security is their main concern
for the cloud migration.

They are comparing our company with CloudX.

Their approximate budget is 15 lakh rupees.
"""

result_2 = prepare_meeting(
    client_name,
    meeting_2
)

print(result_2)


# ============================================================
# MEETING 3
# ============================================================

print("\n\nMEETING 3")
print("-" * 70)

meeting_3 = """
The CTO of ABC Technologies is involved in the final
decision-making process.

ABC Technologies wants the cloud migration implementation
completed within 3 months.

They want a technical proposal before making the final decision.
"""

result_3 = prepare_meeting(
    client_name,
    meeting_3
)

print(result_3)


# ============================================================
# FINAL PREPARATION
# ============================================================

print("\n\nFINAL MEETING PREPARATION")
print("-" * 70)

final_request = """
Prepare me for tomorrow's meeting with ABC Technologies.

Use everything you remember from our previous meetings.
"""

final_result = prepare_meeting(
    client_name,
    final_request
)

print(final_result)


print("\n" + "=" * 70)
print("        END OF MEMORY LEARNING DEMO")
print("=" * 70)