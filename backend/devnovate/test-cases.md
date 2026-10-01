# Test Cases — Meeting Prep & Relationship Agent

## Purpose

These test cases verify whether the Meeting Prep & Relationship Agent can correctly remember, retrieve, and combine information from previous meetings with ABC Technologies.

The tests focus on:

* Memory retrieval
* Client information
* Previous concerns
* Stakeholders
* Competitors
* Requirements
* Multi-meeting information
* Personalized meeting preparation

---

## Test Case 1 — Client Identification

**Test ID:** TC-01

**Objective:**
Verify that the system can remember the client's name.

**Input:**

> Who is the client we have been discussing?

**Expected Result:**

> ABC Technologies

**Pass Criteria:**
The system identifies **ABC Technologies** correctly.

---

## Test Case 2 — Project Identification

**Test ID:** TC-02

**Objective:**
Verify that the system remembers the client's main project.

**Input:**

> What project is ABC Technologies interested in?

**Expected Result:**

> Cloud migration.

**Pass Criteria:**
The system identifies **cloud migration** as the main project.

---

## Test Case 3 — Previous Client Concern

**Test ID:** TC-03

**Objective:**
Verify that the system remembers the client's primary concern from earlier meetings.

**Input:**

> What was ABC Technologies' main concern during our earlier discussions?

**Expected Result:**

> Security, particularly data security during migration.

**Pass Criteria:**
The response mentions **security/data security**.

---

## Test Case 4 — Competitor Recall

**Test ID:** TC-04

**Objective:**
Verify that the system can remember a competitor mentioned in a previous meeting.

**Input:**

> Which competitor is ABC Technologies comparing us with?

**Expected Result:**

> CloudX.

**Pass Criteria:**
The system correctly identifies **CloudX**.

---

## Test Case 5 — Stakeholder Recall

**Test ID:** TC-05

**Objective:**
Verify that the system remembers an important stakeholder who joined a later meeting.

**Input:**

> Who from ABC Technologies joined the technical discussion?

**Expected Result:**

> David, the CTO of ABC Technologies.

**Pass Criteria:**
The system identifies **David as the CTO**.

---

## Test Case 6 — Requirement Recall

**Test ID:** TC-06

**Objective:**
Verify that the system remembers an important requirement discussed during the technical meeting.

**Input:**

> What timeline-related requirement did the client mention?

**Expected Result:**

> They want a clear implementation timeline.

**Pass Criteria:**
The response mentions the **implementation timeline**.

---

## Test Case 7 — Technical Concern Recall

**Test ID:** TC-07

**Objective:**
Verify that the system remembers the client's technical concern about downtime.

**Input:**

> What technical concern does ABC Technologies have about the migration?

**Expected Result:**

> They want to minimize downtime during migration.

**Pass Criteria:**
The response identifies **minimal downtime** as a concern.

---

## Test Case 8 — Latest Request

**Test ID:** TC-08

**Objective:**
Verify that the system remembers the client's most recent request.

**Input:**

> What did ABC Technologies request in the latest meeting?

**Expected Result:**

> A detailed technical proposal.

The proposal should include information about the implementation timeline, security measures, migration strategy, and ongoing support.

**Pass Criteria:**
The response identifies the **technical proposal** and preferably mentions its important requirements.

---

## Test Case 9 — Multi-Meeting Memory

**Test ID:** TC-09

**Objective:**
Verify that the system can combine information from multiple meetings.

**Input:**

> Summarize the important things we know about ABC Technologies from all our previous meetings.

**Expected Result should include:**

* Client: ABC Technologies
* Project: Cloud migration
* Security concern
* Competitor: CloudX
* Stakeholder: David, CTO
* Implementation timeline
* Minimal downtime
* Technical proposal
* Ongoing support

**Pass Criteria:**
The system combines information from multiple meetings instead of recalling only the latest meeting.

---

# Test Case 10 — Personalized Meeting Preparation

**Test ID:** TC-10

**Objective:**
Verify whether the system can use previous meeting information to prepare the user for the next meeting.

**Input:**

> Prepare me for my next meeting with ABC Technologies.

**Expected Result:**

The system should generate a personalized meeting brief containing relevant information such as:

### Previous Discussions

* Cloud migration
* Security concerns
* Pricing
* CloudX comparison

### Key Stakeholder

* David — CTO

### Current Requirements

* Implementation timeline
* Minimal downtime
* Security details
* Ongoing support

### Latest Request

* Technical proposal

### Suggested Discussion Points

* Address security concerns.
* Explain the migration strategy.
* Discuss implementation timeline.
* Explain how downtime can be minimized.
* Be prepared to discuss pricing and CloudX.
* Explain ongoing support.

**Pass Criteria:**
The response should use information from multiple previous meetings to create a personalized preparation brief.

---

# Test Case 11 — Memory Improvement Test

**Test ID:** TC-11

**Objective:**
Determine whether the meeting preparation becomes more detailed as additional meetings are stored.

### Test A — After Meeting 1

**Input:**

> Prepare me for my next meeting with ABC Technologies.

**Expected:**
The response should primarily mention:

* Cloud migration
* Security concerns
* Migration process

### Test B — After Meetings 1–4

**Input:**

> Prepare me for my next meeting with ABC Technologies.

**Expected:**
The response should contain significantly more context, including:

* Security
* CloudX
* Pricing
* David/CTO
* Implementation timeline
* Minimal downtime
* Technical proposal
* Ongoing support

**Pass Criteria:**
The second preparation should demonstrate that additional meeting history provides more relevant context.

---

# Test Case 12 — Irrelevant Memory Filtering

**Test ID:** TC-12

**Objective:**
Verify that the system retrieves relevant information instead of returning every stored detail.

**Input:**

> What should I discuss with the CTO in the next technical meeting?

**Expected Result should focus on:**

* Implementation timeline
* Security
* Migration strategy
* Minimal downtime
* Existing application impact
* Technical proposal

**Pass Criteria:**
The response should prioritize technical information relevant to the CTO rather than unnecessarily listing all client history.

---

# Test Result Format

Each test should be recorded using the following format:

| Test ID | Test                      | Result                           | Status    |
| ------- | ------------------------- | -------------------------------- | --------- |
| TC-01   | Client identification     | ABC Technologies                 | PASS/FAIL |
| TC-02   | Project identification    | Cloud migration                  | PASS/FAIL |
| TC-03   | Previous concern          | Security                         | PASS/FAIL |
| TC-04   | Competitor recall         | CloudX                           | PASS/FAIL |
| TC-05   | Stakeholder recall        | David — CTO                      | PASS/FAIL |
| TC-06   | Requirement recall        | Implementation timeline          | PASS/FAIL |
| TC-07   | Technical concern         | Minimal downtime                 | PASS/FAIL |
| TC-08   | Latest request            | Technical proposal               | PASS/FAIL |
| TC-09   | Multi-meeting memory      | Combined information             | PASS/FAIL |
| TC-10   | Personalized preparation  | Relevant meeting brief           | PASS/FAIL |
| TC-11   | Memory improvement        | More context after more meetings | PASS/FAIL |
| TC-12   | Relevant memory retrieval | Relevant information prioritized | PASS/FAIL |

---

# Overall Success Criteria

The system will be considered successful if it can:

1. Correctly identify the client.
2. Recall important information from previous meetings.
3. Retrieve information from different meetings.
4. Connect related information across meetings.
5. Identify important stakeholders and competitors.
6. Remember unresolved requirements.
7. Generate personalized meeting preparation.
8. Retrieve relevant information without unnecessarily including unrelated details.
9. Provide richer preparation after additional meeting history is available.
