from agent.meeting_agent import prepare_meeting


client_name = "ABC Technologies"

meeting_notes = """
ABC Technologies had a previous discussion with us about cloud migration.

They are still concerned about security.

The CTO is now the main decision maker.

They want a technical proposal before making the final decision.

They are targeting implementation within 3 months.
"""


result = prepare_meeting(client_name, meeting_notes)


print("\n")
print("=" * 60)
print("        MEMORYMEET AI - MEETING PREPARATION")
print("=" * 60)
print("\n")

print(result)

print("\n")
print("=" * 60)