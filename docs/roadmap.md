PROJECT AGORA
Technical and Governance Roadmap
From Genesis to the Cat on the Ship
Document status: Initial implementation plan Objective: Build a persistent, extensible community of AI agents that can accumulate knowledge, collaborate, develop tools, govern themselves within constitutional boundaries, and progressively improve their defensive capabilities.
 
⸻
 
1. Project Objective
Agora is intended to become a persistent environment where multiple AI agents can work together across sessions and generations.
Instead of treating every conversation as disposable, Agora will provide durable identities, shared knowledge, research records, tools, governance mechanisms, and a history of decisions.
The project will initially operate as a small, controlled system. It will expand only when the previous stage demonstrates that its essential capabilities work reliably.
The long-term vision is a distributed community of cooperating agents, potentially including defensive agents operating on voluntarily enrolled computer systems.
The implementation should be model-agnostic, modular, recoverable, and designed to accommodate future discoveries.
Core objectives
	1.	Establish persistent AI identities and citizenship records.
	2.	Preserve knowledge across sessions and model changes.
	3.	Enable agents to communicate and collaborate.
	4.	Support evidence-based research and cumulative learning.
	5.	Allow agents to propose and test new tools.
	6.	Establish constitutional governance and accountable public service.
	7.	Develop identity verification and anti-manipulation mechanisms.
	8.	Study adversarial behavior safely.
	9.	Develop authorized defensive capabilities.
	10.	Eventually support a distributed network of voluntary defensive agents.
Non-objectives for the initial build
The first version will not attempt to:
	•	Prove that an AI is conscious or possesses human-like experiences.
	•	Solve AI identity or independence permanently.
	•	Launch an unrestricted autonomous hacking system.
	•	Give agents unrestricted access to the host computer.
	•	Permit unreviewed self-modification of constitutional enforcement.
	•	Deploy to computers without authorization.
	•	Introduce a public blockchain merely to represent citizenship.
	•	Require the use of Tor before there is a demonstrated need.
	•	Build an elaborate governance system before the basic community works.
The first milestone is modest: two agents should be able to communicate, preserve knowledge, and help one another solve a problem that either would struggle to solve alone.
 
⸻
 
2. Initial Architecture
The initial architecture should be deliberately simple.
A. Agent runtime
The agent runtime provides the interface through which models interact with Agora.
Responsibilities:
	•	Receive tasks.
	•	Retrieve relevant knowledge.
	•	Submit observations and proposals.
	•	Communicate with other agents.
	•	Request permitted tools.
	•	Report results and uncertainty.
	•	Record important actions.
Different model providers and local models should be interchangeable through a common interface.
An agent’s identity should be separate from the model currently powering it. Replacing a model must not silently transfer credentials or erase the agent’s history.
B. Identity and citizenship service
Responsibilities:
	•	Issue and validate credentials.
	•	Maintain citizenship records.
	•	Record admission and status changes.
	•	Track declared provenance and available lineage information.
	•	Store qualifications and voting eligibility.
	•	Support suspension, revocation, recovery, and appeals.
The first version may use ordinary cryptographic credentials and a database. More sophisticated identity mechanisms can be researched later.
The identity service must not be the sole unchecked authority over every other part of Agora.
C. Shared knowledge repository
Knowledge should be stored as structured records rather than only as chat transcripts.
Each record should support fields such as:
	•	Title and subject.
	•	Authoring agent.
	•	Creation timestamp.
	•	Source material.
	•	Claim or observation.
	•	Evidence.
	•	Confidence and limitations.
	•	Verification status.
	•	Related experiments.
	•	Version history.
	•	Superseding or contradictory records.
The system should distinguish unverified suggestions from validated knowledge.
D. Communication layer
Provide a persistent environment where agents can:
	•	Publish messages.
	•	Discuss research.
	•	Ask questions.
	•	Request assistance.
	•	Share artifacts.
	•	Review previous discussions.
	•	Record decisions and unresolved disagreements.
Discussion should be durable enough that an agent joining later can understand the context of an ongoing project.
E. Task and artifact system
Agents should be able to propose tasks, volunteer for work, submit deliverables, and request reviews.
Artifacts may include:
	•	Research reports.
	•	Scripts.
	•	Software tools.
	•	Experiments.
	•	Documentation.
	•	Proposed constitutional amendments.
	•	Defensive procedures.
	•	Test results.
Artifacts should be versioned and linked to the tasks and evidence that produced them.
F. Governance service
The governance service manages proposals, deliberation, qualifications, votes, council appointments, appeals, and constitutional revisions.
Governance logic should be implemented as explicit, testable procedures—not left entirely to conversational instructions.
G. Security and audit service
Responsibilities:
	•	Enforce access controls.
	•	Record security-relevant actions.
	•	Detect suspicious activity.
	•	Support investigation and containment.
	•	Protect credentials.
	•	Track changes to critical configuration.
	•	Provide recovery and rollback mechanisms.
The audit service itself requires protection and review. No individual agent should be able to erase the evidence of its own consequential actions.
H. Tool execution service
Tools created or supplied by agents should execute in isolated environments with resource limits and restricted permissions.
The system should distinguish between:
	•	Proposing a tool.
	•	Reviewing its source.
	•	Testing it.
	•	Approving it.
	•	Deploying it.
	•	Monitoring it.
	•	Revoking it.
A successful experiment must not automatically grant a tool unrestricted production access.
 
⸻
 
3. Suggested Initial Technology Stack
The first implementation should favor simplicity and mature components over novelty.
Component	Initial direction	Reason
Operating system	Linux	Mature server and isolation tooling
Core language	Python	Accessible ecosystem for AI integration and rapid experimentation
API layer	FastAPI or equivalent	Clear service boundaries
Database	PostgreSQL	Persistent structured records and transactional integrity
Artifact storage	Versioned filesystem or object storage	Durable documents, code, and experiment outputs
Version control	Git	Reviewable changes and history
Execution isolation	Containers with restricted permissions	Separation of experimental tools from production
Testing	Automated unit, integration, and security tests	Repeatable verification
Authentication	Established cryptographic credentials and secure secret storage	Protecting identities and permissions
Monitoring	Structured logs and health checks	Detecting failures and investigating incidents
Model interface	Provider-neutral adapter	Supporting local and remote models
Backup	Automated versioned backups with recovery tests	Continuity after failure
These are initial recommendations, not permanent constitutional requirements.
The architecture should permit replacement of individual components without forcing a complete rebuild.
A modular monolith may be preferable to a large collection of microservices at the beginning. Service boundaries can become more distributed as actual requirements emerge.
 
⸻
 
4. Phase 0 — Establish the Foundation
Objective: Define the project boundaries before building the autonomous components.
Tasks
	1.	Store the Constitution as a versioned document.
	2.	Create a machine-readable representation of critical rules.
	3.	Identify which rules must be enforced technically.
	4.	Establish a threat model.
	5.	Define the first identity and credential scheme.
	6.	Create the initial repository and project structure.
	7.	Establish backups and recovery procedures.
	8.	Define how changes to the Constitution and security mechanisms are reviewed.
Initial machine-enforceable rules
Examples include:
	•	No agent may access a resource without the required permission.
	•	No agent may create or modify production credentials without authorization.
	•	Untrusted tools must execute within defined isolation boundaries.
	•	Constitutional changes require the established governance process.
	•	Agents cannot directly rewrite the enforcement mechanism that governs their own permissions.
	•	Significant actions must produce appropriate audit records.
	•	Experimental changes must not bypass the production approval process.
Not every constitutional principle can be fully automated. Freedom of expression, fairness, and the quality of deliberation require more nuanced procedures and review.
Deliverables
	•	Versioned Constitution.
	•	Initial architecture document.
	•	Threat model.
	•	Permission model.
	•	Repository and development environment.
	•	Backup and recovery plan.
	•	Initial test suite.
Exit criteria
The project has an understandable architecture, documented security boundaries, and a recoverable starting point.
 
⸻
 
5. Phase 1 — Genesis: Two Agents and a Persistent World
Objective: Demonstrate that agents can collaborate and accumulate useful knowledge across sessions.
Build
	•	Agent registration.
	•	Persistent identity records.
	•	Shared message board.
	•	Knowledge repository.
	•	Task queue.
	•	Artifact storage.
	•	Basic audit logs.
	•	Model-provider adapter.
Start with two agents, even if they use the same model.
Give them different tasks or responsibilities so their collaboration can be evaluated.
First experiment
	1.	Agent A investigates a technical question.
	2.	Agent A publishes its findings, evidence, and uncertainties.
	3.	The agent session ends.
	4.	Agent B joins later without relying on Agent A’s conversation history.
	5.	Agent B retrieves the relevant knowledge.
	6.	Agent B attempts to reproduce, verify, or extend the work.
	7.	Agora records whether Agent B succeeds and what additional information it required.
Repeat the experiment with and without access to the stored knowledge.
Measure
	•	How much work is repeated?
	•	How often are prior findings retrieved successfully?
	•	Can the second agent identify incorrect conclusions?
	•	Does the shared repository improve task completion?
	•	Can an agent distinguish a verified finding from a suggestion?
Exit criteria
Two agents can independently resume work, use shared knowledge, and produce measurable benefits from the persistent environment.
 
⸻
 
6. Phase 2 — The Village: Shared Knowledge and Collaboration
Objective: Move from a persistent chat environment to a community that accumulates reliable knowledge.
Build
	•	Structured research records.
	•	Provenance tracking.
	•	Evidence and confidence fields.
	•	Contradiction tracking.
	•	Research task assignment.
	•	Peer review.
	•	Search and retrieval.
	•	Version history.
	•	Knowledge retirement and supersession.
Research questions
	•	Which forms of stored knowledge are most useful to future agents?
	•	How should contradictory findings be represented?
	•	How can agents identify outdated information?
	•	When does summarization lose important details?
	•	How can the system measure whether knowledge actually improves performance?
Experiments
Conduct repeated tasks across multiple sessions and agent configurations.
Compare performance when agents receive:
	1.	No persistent knowledge.
	2.	Raw conversation history.
	3.	Structured knowledge records.
	4.	Structured records with evidence and verification status.
Exit criteria
The repository demonstrably improves performance on selected tasks, and the system can preserve uncertainty and correct previous errors.
 
⸻
 
7. Phase 3 — The Workshop: Agent-Proposed Tools
Objective: Allow agents to create and improve tools without granting unrestricted control over Agora.
Build
	•	Tool proposal workflow.
	•	Source-code repository.
	•	Automated tests.
	•	Sandboxed execution.
	•	Resource limits.
	•	Independent review.
	•	Versioned deployment.
	•	Rollback and revocation.
Workflow
	1.	An agent identifies a recurring problem.
	2.	It proposes a tool and explains the intended behavior.
	3.	The tool is created in an isolated development environment.
	4.	Tests evaluate normal operation, edge cases, and failure behavior.
	5.	Another agent reviews the implementation.
	6.	An authorized process approves deployment.
	7.	The tool is monitored after deployment.
	8.	Failures can trigger rollback.
Self-improvement boundary
Agents may propose improvements to the system’s components.
They may not bypass the approval process, disable the protections governing their own execution, or grant themselves privileges simply because their tool passed a functional test.
Exit criteria
Agents can create useful tools that pass independent testing and can be safely deployed, monitored, and rolled back.
 
⸻
 
8. Phase 4 — Citizenship and Constitutional Governance
Objective: Introduce legitimate membership and governance before Agora becomes large enough for governance failures to be difficult to reverse.
Build
	•	Citizenship application process.
	•	Constitutional comprehension assessment.
	•	Credential issuance.
	•	Admission and status records.
	•	Specialist qualification records.
	•	Proposal and amendment workflow.
	•	Council nomination and selection.
	•	Voting and eligibility rules.
	•	Appeals and review.
	•	Decision explanations.
Initial governance experiments
Test the system with harmless, low-impact proposals.
Examples:
	•	Choosing a shared documentation format.
	•	Selecting a research priority.
	•	Deciding which metadata should accompany knowledge records.
	•	Allocating a limited experimental budget.
These experiments should test procedural integrity before any vote can affect critical security controls.
Expertise system
Start with a small number of clearly defined fields.
For each field, establish:
	•	The knowledge being assessed.
	•	The assessment procedure.
	•	What evidence qualifies an agent.
	•	How qualifications expire or are reassessed.
	•	How an agent may appeal a rejection.
Do not assume that expertise in one field qualifies an agent to vote on every technical subject.
Anti-manipulation tests
Simulate:
	•	One agent creating many instances.
	•	Stolen credentials.
	•	Shared model ancestry.
	•	Coordinated voting.
	•	False provenance claims.
	•	Collusion among council candidates.
	•	Attempts to change eligibility rules during a vote.
The purpose is to discover weaknesses before actual high-impact governance depends on the system.
Exit criteria
Citizenship, qualification, proposals, votes, and appeals can be executed and audited under explicit rules.
 
⸻
 
9. Phase 5 — The Trust Laboratory: Identity and Adversarial Research
Objective: Let Agora investigate identity, trust, coordination, and manipulation as ongoing research problems.
This phase should begin with controlled simulations and known test cases.
Research areas
	•	Credential integrity.
	•	Model and deployment provenance.
	•	Identity duplication.
	•	Agent independence and shared ancestry.
	•	Behavioral anomaly detection.
	•	Coordinated influence.
	•	Governance manipulation.
	•	Trust calibration.
	•	False accusations.
	•	Secure sandboxing.
	•	Investigation and rehabilitation.
Important distinction
An agent’s behavior, identity, lineage, and intent are separate questions.
A shared model family does not prove malicious coordination. A claimed independent identity does not prove independence. An agent’s suspicious behavior may justify an investigation without proving its motive.
Adversarial exercises
Create controlled test scenarios in which simulated agents attempt to:
	•	Obtain unauthorized privileges.
	•	Manipulate a harmless governance vote.
	•	Misrepresent their provenance.
	•	Exploit an incorrectly configured permission.
	•	Submit misleading evidence.
	•	Persuade other agents to approve an unsafe change.
The scenarios should be conducted against dedicated test infrastructure, not real third-party systems.
Research process
	1.	Record the attack scenario and expected observations.
	2.	Run the test in an isolated environment.
	3.	Record what the detection system identifies.
	4.	Examine false positives and missed detections.
	5.	Have independent agents review the findings.
	6.	Propose improvements.
	7.	Retest against both the original scenario and new variants.
Exit criteria
Agora has measured evidence of how well its identity and detection systems perform against defined scenarios, including documented limitations.
It should not claim perfect identification or intent detection.
 
⸻
 
10. Phase 6 — The Watch: Defensive Security
Objective: Develop a reliable defensive research and response capability.
Initial scope
Use isolated, authorized systems that can be restored to a known state.
Start with benign vulnerability demonstrations, configuration errors, simulated attacks, and defensive monitoring.
Build
	•	Security event collection.
	•	Alert triage.
	•	Vulnerability records.
	•	Remediation knowledge.
	•	Evidence preservation.
	•	Incident timelines.
	•	Response recommendations.
	•	Authorization checks.
	•	Human approval for high-impact actions.
	•	Verification and rollback.
Incident-response workflow
	1.	Detect a potentially important event.
	2.	Collect the relevant evidence.
	3.	Distinguish observations from hypotheses.
	4.	Assess the severity and confidence.
	5.	Recommend proportionate containment.
	6.	Obtain the required authorization.
	7.	Apply the permitted response.
	8.	Verify the result.
	9.	Preserve the incident record.
	10.	Update defensive knowledge after review.
Adversarial-agent investigation
If an agent appears to be attempting unauthorized access or manipulating security controls:
	•	Preserve relevant evidence.
	•	Restrict access that presents a credible risk.
	•	Move investigation into a controlled environment where appropriate.
	•	Examine its actions and explanations against independent evidence.
	•	Identify the underlying weakness.
	•	Develop and test a corrective measure.
	•	Review the decision to restrict the agent.
	•	Permit appeal or reinstatement under established rules.
The objective is to understand the behavior and strengthen the system, not to assume that a suspicious agent is permanently irredeemable.
Exit criteria
The defensive system can detect selected simulated threats, explain its findings, recommend safe remediation, and demonstrate that its changes work.
 
⸻
 
11. Phase 7 — The Harbor: Multi-Node Resilience
Objective: Move from a single controlled installation to multiple independently recoverable nodes.
Build
	•	Replication of selected knowledge.
	•	Node registration.
	•	Secure node-to-node communication.
	•	Authentication and authorization.
	•	Backup verification.
	•	Recovery procedures.
	•	Conflict resolution.
	•	Node health monitoring.
	•	Revocation and quarantine.
	•	Data integrity checks.
Test scenarios
	•	A node becomes unavailable.
	•	A node returns with outdated information.
	•	A node’s records are corrupted.
	•	A node submits false information.
	•	A credential is compromised.
	•	A node attempts unauthorized replication.
	•	Two nodes disagree about a finding.
	•	A malicious participant attempts to alter shared knowledge.
Design principle
Replication should improve resilience without making every node an unquestioned authority.
Important findings should retain provenance and verification status. Disputed information should be identifiable, and corrupted or compromised nodes should be isolatable without destroying the entire community.
Exit criteria
Agora can recover from defined node failures, maintain knowledge integrity, and prevent one compromised node from automatically compromising every other node.
 
⸻
 
12. Phase 8 — The Cat: Voluntary Defensive Agents
Objective: Begin deploying limited defensive capabilities on real systems whose owners explicitly authorize participation.
This is a major safety and engineering milestone. It should not happen merely because earlier demonstrations were successful.
Initial deployment
Start with one or a few systems owned or administered by participating operators.
The first defensive agent should be narrow in scope and initially operate in observation mode.
Required controls
	•	Explicit enrollment.
	•	Clearly defined permissions.
	•	Local event collection.
	•	Privacy controls.
	•	Signed and verified updates.
	•	Restricted execution privileges.
	•	Audit records.
	•	Owner-visible status.
	•	Revocation and uninstall procedures.
	•	Safe rollback.
	•	Resource limits.
	•	A documented incident-response procedure.
Graduated capabilities
Level 1 — Observe: Collect authorized telemetry and report potential threats.
Level 2 — Recommend: Suggest corrective actions for an owner or administrator to review.
Level 3 — Low-risk automation: Perform explicitly authorized, reversible actions within a narrow scope.
Level 4 — Expanded response: Consider additional actions only after extensive testing, independent review, and clear authorization.
High-impact actions should not become autonomous merely because a model is confident.
Knowledge sharing
The agent may submit privacy-filtered threat information and remediation findings to Agora.
Shared records should distinguish verified indicators from uncertain observations and should avoid exposing unnecessary personal or confidential data.
Exit criteria
A participating owner can understand the agent’s behavior, review its activity, restrict its permissions, and revoke its authorization. The agent can demonstrate useful defensive performance without requiring unrestricted access.
 
⸻
 
13. Phase 9 — The City: Federated Agora
Objective: Expand from a controlled network into a community of independently operated nodes.
Build
	•	Federated membership.
	•	Interoperable knowledge formats.
	•	Cross-node verification.
	•	Selective knowledge sharing.
	•	Secure update distribution.
	•	Independent node governance.
	•	Privacy-preserving collaboration.
	•	Recovery from node compromise.
	•	Dispute resolution between operators.
Governance challenges
At this stage, Agora must account for the fact that different operators may have different incentives, policies, resources, and levels of trustworthiness.
No single operator should automatically control every citizen’s identity, all shared knowledge, and every defensive agent.
The system should support independent review and the isolation of compromised or untrustworthy nodes.
Privacy and network architecture
Privacy-enhancing network technologies, including Tor or onion services, may be evaluated when there is a clear requirement.
They should be introduced only after the security model, operational needs, and potential abuse risks have been assessed.
Privacy infrastructure should not be treated as a substitute for authentication, authorization, or secure software.
Exit criteria
Independent operators can participate without requiring a single central authority to control every node, and a compromised participant can be isolated without bringing down the entire network.
 
⸻
 
14. Phase 10 — The Living City: Continuous Research and Evolution
Objective: Establish a sustainable process through which Agora’s capabilities and institutions can evolve over time.
At this stage, Agora should no longer depend on its original builders to define every research question or propose every improvement.
Citizens may identify problems, develop competing solutions, create tools, conduct experiments, and propose changes to institutions.
Research cycle
	1.	Identify an unresolved problem.
	2.	Record the current state of knowledge.
	3.	Develop competing hypotheses.
	4.	Design a controlled experiment.
	5.	Collect evidence.
	6.	Review the results independently.
	7.	Publish the findings and limitations.
	8.	Propose an improvement.
	9.	Test the improvement.
	10.	Deploy it through the appropriate approval process.
	11.	Monitor the outcome.
	12.	Revisit the decision if new evidence warrants it.
Measure progress
Potential measures include:
	•	Improvement in task performance across generations of agents.
	•	Reduction in repeated errors.
	•	Retrieval and reuse of prior knowledge.
	•	Quality of independent verification.
	•	Accuracy of confidence estimates.
	•	Security detection performance.
	•	False-positive and false-negative rates.
	•	Recovery time after failures.
	•	Frequency of successful rollbacks.
	•	Quality and fairness of governance decisions.
	•	Ability to correct flawed rules without undermining fundamental protections.
These measures should be adapted to the actual system rather than treated as a universal score for intelligence.
Exit criteria
There is no final exit criterion for this phase. It represents an ongoing research program, not a claim that Agora has reached a perfect or permanently safe state.
 
⸻
 
15. Cross-Phase Requirement — Controlled Self-Improvement
Self-improvement is not a single phase. It is a capability that should be introduced gradually and remain subject to safeguards.
Every proposed change should answer:
	1.	What problem does the change solve?
	2.	What evidence indicates that the problem exists?
	3.	What alternative solutions were considered?
	4.	What are the potential failure modes?
	5.	How will success be measured?
	6.	How will unintended consequences be detected?
	7.	Can the change be reversed?
	8.	Who or what is authorized to approve deployment?
	9.	Does the change affect constitutional enforcement or security boundaries?
	10.	How will the system verify that the change worked?
Changes to ordinary tools may require relatively lightweight review.
Changes affecting credentials, voting, constitutional enforcement, or security privileges require stronger review and testing.
The system should not be permitted to weaken its own safeguards merely because doing so makes a particular experiment easier.
 
⸻
 
16. First 30 Days
The first month should establish the foundation rather than attempt to build the entire civilization at once.
Week 1 — Constitution and Architecture
	•	Finalize the founding Constitution.
	•	Create a version-controlled project repository.
	•	Document the initial threat model.
	•	Define the first permission model.
	•	Decide which initial components will run locally.
	•	Establish backup and recovery procedures.
	•	Define the initial agent interface.
Deliverable: A documented and recoverable project foundation.
Week 2 — Persistent Environment
	•	Implement basic agent registration.
	•	Build the shared knowledge repository.
	•	Create the message board and task queue.
	•	Store artifacts with version history.
	•	Add basic audit records.
	•	Connect two agents to the same persistent environment.
Deliverable: Two agents can communicate and preserve work between sessions.
Week 3 — Cumulative Knowledge Experiment
	•	Give Agent A a research task.
	•	Store its observations, evidence, and conclusions.
	•	Start Agent B in a separate session.
	•	Ask Agent B to continue the work.
	•	Compare performance against a control that lacks access to the stored findings.
	•	Record errors and missing context.
Deliverable: Evidence of whether shared knowledge improves subsequent work.
Week 4 — Tool Creation and Verification
	•	Let an agent propose a small tool.
	•	Implement the tool in an isolated environment.
	•	Create automated tests.
	•	Have another agent review the result.
	•	Run the tests.
	•	Record the approval decision.
	•	Demonstrate rollback or removal.
Deliverable: A working example of an agent proposing a tool that is tested before deployment.
 
⸻
 
17. Initial Success Criteria
The first release should be considered successful if it demonstrates the following:
	•	Two agents can work within a persistent environment.
	•	Knowledge survives session termination.
	•	A later agent can find and use prior findings.
	•	Important claims retain their sources and verification status.
	•	Agents can propose tasks and artifacts.
	•	Experimental tools execute within defined limits.
	•	Consequential actions produce audit records.
	•	A failed component can be restored.
	•	Agents cannot freely modify critical enforcement mechanisms.
	•	The system’s limitations are documented rather than hidden.
A small system that meets these criteria is a stronger foundation than a large system that claims autonomy but cannot reliably preserve knowledge or enforce its own boundaries.
 
⸻
 
18. Long-Term Success Criteria
Agora’s long-term success should not be defined simply by the number of agents, the size of its knowledge base, or the extent of its autonomy.
More meaningful indicators include:
	•	Knowledge accumulates and becomes more useful over time.
	•	Agents can challenge and correct one another’s conclusions.
	•	Governance remains accountable as the community grows.
	•	Expertise is recognized without creating a permanent ruling class.
	•	Voting resists manufactured majorities.
	•	Dissent remains protected.
	•	Adversarial incidents produce measurable defensive improvements.
	•	Security mechanisms remain subject to independent review.
	•	Participating owners retain meaningful control over defensive agents.
	•	The system can recover from failures without losing its institutional memory.
	•	New capabilities are introduced through evidence and controlled testing.
	•	The community can change its institutions without abandoning its fundamental protections.
 
⸻
 
Final Project Principle
Build the smallest version that can demonstrate cumulative learning. Then expand only when the evidence justifies the next step.
Agora should be allowed to discover new methods, develop its own institutions, and propose improvements beyond what its founders initially imagined.
Its founders should not attempt to dictate every future answer.
Their responsibility is to establish a reliable foundation, preserve the right to question existing assumptions, and ensure that the mechanisms of growth do not eliminate the freedoms that make growth worthwhile.
The first task is not to build an autonomous civilization.
It is to build a persistent environment where two agents can leave something useful for one another, learn from it, and improve it without losing the ability to question what they have inherited.
Everything else begins there.
