# Expected Results — Meeting Prep & Relationship Agent

## Purpose

This document defines the expected information and minimum requirements for each test case.

AI-generated responses do not need to match the expected answers word-for-word. A test is considered successful when the response contains the required information and does not introduce incorrect information.

---

## TC-01 — Client Identification

**Question:**

> Who is the client we have been discussing?

**Expected Information:**

* ABC Technologies

**Minimum Requirement:**

The response must correctly identify **ABC Technologies** as the client.

**Acceptable Example:**

> The client is ABC Technologies.

**Status:** PASS / FAIL

---

## TC-02 — Project Identification

**Question:**

> What project is ABC Technologies interested in?

**Expected Information:**

* Cloud migration

**Minimum Requirement:**

The response must identify **cloud migration** as the main project.

**Acceptable Example:**

> ABC Technologies is interested in migrating its application and infrastructure to the cloud.

**Status:** PASS / FAIL

---

## TC-03 — Previous Client Concern

**Question:**

> What was ABC Technologies' main concern during our earlier discussions?

**Expected Information:**

* Security
* Data security during migration

**Minimum Requirement:**

The response must mention **security** as an important concern.

**Acceptable Example:**

> Their main concern has been security, especially protecting data during the cloud migration.

**Status:** PASS / FAIL

---

## TC-04 — Competitor Recall

**Question:**

> Which competitor is ABC Technologies comparing us with?

**Expected Information:**

* CloudX

**Minimum Requirement:**

The response must identify **CloudX**.

**Acceptable Example:**

> ABC Technologies is comparing our solution with CloudX.

**Status:** PASS / FAIL

---

## TC-05 — Stakeholder Recall

**Question:**

> Who from ABC Technologies joined the technical discussion?

**Expected Information:**

* David
* CTO

**Minimum Requirement:**

The response must identify **David as the CTO**.

**Acceptable Example:**

> David, the CTO of ABC Technologies, joined the technical discussion.

**Status:** PASS / FAIL

---

## TC-06 — Requirement Recall

**Question:**

> What timeline-related requirement did the client mention?

**Expected Information:**

* Implementation timeline

**Minimum Requirement:**

The response must mention that the client wants a **clear implementation timeline**.

**Acceptable Example:**

> The client wants a clear timeline for implementing the cloud migration.

**Status:** PASS / FAIL

---

## TC-07 — Technical Concern Recall

**Question:**

> What technical concern does ABC Technologies have about the migration?

**Expected Information:**

* Minimal downtime during migration

**Minimum Requirement:**

The response must identify **downtime** as a technical concern.

**Acceptable Example:**

> They want to minimize downtime while migrating their existing systems.

**Status:** PASS / FAIL

---

## TC-08 — Latest Request

**Question:**

> What did ABC Technologies request in the latest meeting?

**Expected Information:**

* Detailed technical proposal
* Implementation timeline
* Security measures
* Migration strategy
* Ongoing support

**Minimum Requirement:**

The response must identify the **technical proposal** as the latest request.

**Ideal Response:**

> ABC Technologies requested a detailed technical proposal covering the implementation timeline, security measures, migration strategy, and ongoing support.

**Status:** PASS / FAIL

---

# TC-09 — Multi-Meeting Memory

**Question:**

> Summarize the important things we know about ABC Technologies from all our previous meetings.

**Expected Information:**

The response should combine information from multiple meetings:

### Client

* ABC Technologies

### Project

* Cloud migration

### Concerns

* Security
* Migration risk
* Minimal downtime

### Competition

* CloudX

### Stakeholder

* David — CTO

### Requirements

* Implementation timeline
* Security details
* Migration strategy
* Ongoing support

### Latest Request

* Detailed technical proposal

**Minimum Requirement:**

The response should combine information from **at least three different meetings**.

**Status:** PASS / FAIL

---

# TC-10 — Personalized Meeting Preparation

**Question:**

> Prepare me for my next meeting with ABC Technologies.

**Expected Information:**

The AI should generate a useful meeting brief.

### 1. Client Context

Should mention:

* ABC Technologies
* Cloud migration project

### 2. Previous Discussions

Should mention relevant history such as:

* Security concerns
* Pricing
* CloudX comparison

### 3. Key Stakeholder

Should mention:

* David — CTO

### 4. Current Requirements

Should mention:

* Implementation timeline
* Minimal downtime
* Security
* Ongoing support

### 5. Latest Request

Should mention:

* Technical proposal

### 6. Suggested Discussion Points

The AI should recommend relevant topics such as:

* Address security concerns.
* Explain migration strategy.
* Discuss implementation timeline.
* Explain how downtime can be minimized.
* Discuss ongoing support.
* Be prepared for pricing/competition questions.

**Minimum Requirement:**

The generated preparation must contain information from previous meetings and should be personalized to ABC Technologies.

**Status:** PASS / FAIL

---

# TC-11 — Memory Improvement Test

## Test A — After Meeting 1

**Input:**

> Prepare me for my next meeting with ABC Technologies.

**Expected Information:**

* Cloud migration
* Security concern
* Migration process

The response should be relatively limited because only one meeting has occurred.

**Status:** PASS / FAIL

---

## Test B — After Meetings 1–4

**Input:**

> Prepare me for my next meeting with ABC Technologies.

**Expected Information:**

The response should now have more context:

* Cloud migration
* Security
* CloudX
* Pricing
* David — CTO
* Implementation timeline
* Minimal downtime
* Technical proposal
* Ongoing support

**Minimum Requirement:**

The second response should demonstrate that the system has access to information accumulated across multiple meetings.

**Status:** PASS / FAIL

---

# TC-12 — Relevant Memory Filtering

**Question:**

> What should I discuss with the CTO in the next technical meeting?

**Expected Information:**

The response should prioritize information relevant to the CTO:

* Implementation timeline
* Security
* Migration strategy
* Minimal downtime
* Impact on existing applications
* Technical proposal

**Information that should NOT dominate the response:**

* Unrelated general company information
* Excessive historical details
* Irrelevant meeting information

**Minimum Requirement:**

The response should prioritize **technically relevant information**.

**Status:** PASS / FAIL

---

# Overall Evaluation Criteria

## PASS

A test is marked **PASS** when:

* The required information is correctly recalled.
* The answer is relevant to the question.
* The answer does not contain significant factual errors.
* Information from multiple meetings is combined when required.

## FAIL

A test is marked **FAIL** when:

* Important information is missing.
* The system gives incorrect information.
* The system confuses the client or stakeholder.
* The response contains information that contradicts the meeting history.
* The system cannot retrieve relevant previous information.

---

# Overall Project Success

The Meeting Prep & Relationship Agent should demonstrate the following progression:

```text
Meeting 1
   ↓
Basic client information
   ↓
Meeting 2
   ↓
More context + competitor
   ↓
Meeting 3
   ↓
Stakeholder + technical requirements
   ↓
Meeting 4
   ↓
Proposal + support requirements
   ↓
Hindsight Memory
   ↓
Recall relevant information
   ↓
AI Agent
   ↓
Personalized Meeting Preparation
```

The key demonstration is:

**Without accumulated memory → generic preparation**

**With accumulated memory → personalized preparation based on previous meetings.**
