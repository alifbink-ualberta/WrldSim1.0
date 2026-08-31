# WrldSim 1.0 — Living World Simulation
## Design Document & Development State
### Version: August 2026

---

# 0. PROJECT PURPOSE

WrldSim 1.0 is a passion-project simulation intended to create a large-scale, emergent, living world populated by autonomous people.

The core appeal is not a conventional scripted RPG.

The intended experience is:

> Create a world with sufficiently general rules, populate it with sufficiently believable people, establish their circumstances, and then allow events, relationships, decisions, reproduction, conflict, culture, economics, politics, and history to emerge from the simulation.

The player should be able to enter this world and roleplay within it.

The ultimate goal is not necessarily to reproduce every aspect of real human civilization perfectly. The goal is to construct a sufficiently deep set of interacting systems that **believable human behavior emerges without requiring the developer to script every possibility**.

The project is explicitly a passion project.

Development should therefore be incremental and implementation-oriented rather than requiring extensive academic preparation before coding. Psychology, anthropology, economics, genetics, etc. should be used as references when useful, but the project should develop through experimentation and progressively more sophisticated systems.

---

# 1. CORE WORLD PREMISE

The current tentative setting for WrldSim 1.0:

A massive-scale nuclear/apocalyptic war occurred thousands of years in the past.

The war and its aftermath fundamentally altered Earth.

Consequences included:

- enormous population loss
- destruction of civilizations
- disappearance of nations
- loss of historical records
- extinction of species
- geographical changes
- altered coastlines
- expanded oceans
- abandoned and dangerous regions
- ecological transformation
- technological collapse in many regions

Thousands of years later, nature has reclaimed much of the planet.

Humanity has survived and developed into new civilizations.

The dominant social structure is broadly reminiscent of medieval/feudal societies:

- agriculture
- villages
- towns
- kingdoms
- councils
- nobles
- rulers
- armies
- merchants
- craftsmen
- religious institutions
- political factions

However, technological development is highly uneven.

Different kingdoms or societies may possess very different technological capabilities.

Large areas of the world are:

- unclaimed
- sparsely populated
- dangerous
- environmentally hostile
- inaccessible
- poorly understood

Different human populations have developed distinct:

- cultures
- religions
- languages
- social structures
- traditions
- physical characteristics

They remain human.

"Race" is therefore not intended to be a rigid biological category.

Instead, populations can possess inherited characteristics that become more or less common within particular populations.

Reproduction allows these characteristics to mix between populations.

Thus a person's ancestry can influence their characteristics without requiring permanent racial boundaries.

---

# 2. DESIGN PHILOSOPHY

## 2.1 Emergence over scripting

The simulation should not rely primarily on manually authored stories.

Instead:

```text
RULES
+
PEOPLE
+
ENVIRONMENT
+
SOCIAL STRUCTURES
+
RESOURCES
+
TIME
=
EMERGENT HISTORY
```

A king should not have a scripted "succession storyline."

Instead:

```text
king dies
↓
children/siblings have relationships
↓
each has personality, ambitions, alliances, beliefs, reputation, resources
↓
political system evaluates succession
↓
people choose actions
↓
alliances/opposition form
↓
conflict may occur
↓
new political state emerges
```

---

# 3. HUMAN MODEL

The central design question is:

> What is a person in WrldSim?

A Person is not simply a list of statistics.

A person is a continuously changing entity produced by the interaction of:

```text
BIOLOGY
+
GENETICS
+
DEVELOPMENT
+
PERSONALITY
+
MEMORY
+
BELIEFS
+
EMOTIONS
+
MOTIVATIONS
+
GOALS
+
RELATIONSHIPS
+
FAMILY
+
CULTURE
+
FAITH
+
KNOWLEDGE
+
SKILLS
+
ECONOMIC CIRCUMSTANCES
+
POLITICAL/SOCIAL CIRCUMSTANCES
+
ENVIRONMENT
```

The intention is for these systems to influence one another rather than exist as isolated character-sheet variables.

---

# 4. CURRENT PERSON ARCHITECTURE

Current conceptual structure:

```text
Person
│
├── Identity
│   ├── first_name
│   ├── last_name
│   ├── age
│   └── sex
│
├── Biology
│   ├── genetics
│   └── body
│
├── Psychology
│   ├── personality
│   ├── emotions
│   ├── memories
│   ├── beliefs
│   ├── motivations
│   └── goals
│
├── Development
│   ├── skills
│   └── knowledge
│
├── Social
│   ├── relationships
│   └── family
│
├── Survival
│   └── survival
│
├── Economy
│   ├── money
│   └── inventory
│
└── World
    └── location
```

Current `Person` constructor conceptually resembles:

```python
Person(
    first_name,
    last_name,
    age,
    sex,
    genetics=None,
    personality=None,
    body=None,
    money=0
)
```

---

# 5. IDENTITY

Current identity:

- first name
- last name
- age
- sex

Full name is generated from first + last name.

Future identity may include:

- aliases
- titles
- nicknames
- language
- self-concept
- social identity
- citizenship
- ethnicity/ancestry
- cultural identity
- faith identity

However, not everything should become a permanent Person attribute.

For example:

## Birthplace

Birthplace should primarily be represented through:

- memories
- family records
- historical records
- relevant world events

rather than necessarily being a fundamental biological property.

## Citizenship

Citizenship should belong to the eventual governing/political management system.

This matters because:

- states can change
- borders can change
- people can become citizens
- people can lose citizenship
- unclaimed territory can exist
- governments can collapse

Therefore citizenship should not be hardcoded as a static identity variable.

---

# 6. FAMILY

Family is a fundamental part of the simulation.

People require parents for reproduction.

The family system should eventually support:

- biological parents
- children
- siblings
- grandparents
- descendants
- partners
- potentially adoptive/social family
- kinship structures

The immediate implementation already supports parent/child relationships and sibling discovery.

Example:

```text
Edward
├── Arthur
└── Thomas
```

Arthur and Thomas can identify one another as siblings because they share a parent.

Family is expected to become extremely important for:

- inheritance
- succession
- alliances
- dynasties
- marriage
- reproduction
- feuds
- loyalty
- political competition
- emotional attachment
- social status

A prince's behavior should therefore emerge partly from his relationships with his siblings and parents.

---

# 7. GENETICS

Genetics is intended to support reproduction and inherited characteristics.

The eventual model:

```text
Father
  │
  ├── genetic contribution
  │
  └──────────────┐
                 ▼
               CHILD
                 ▲
  ┌──────────────┘
  │
  └── genetic contribution
      Mother
```

The project uses the distinction between:

## Genotype

Inherited genetic information.

## Phenotype

Observable characteristics resulting from genetics interacting with development/environment.

Conceptually:

```text
GENETICS
+
DEVELOPMENT
+
ENVIRONMENT
=
OBSERVABLE PERSON
```

The goal is not initially to create a scientifically perfect human genetic model.

The system should instead allow inheritance of characteristics in a way that produces believable variation across generations.

Potential future traits include:

- height
- body structure
- pigmentation
- hair characteristics
- facial characteristics
- physical capabilities
- disease susceptibility
- metabolism
- other inherited characteristics

Reproduction is intended to eventually allow cross-population mixing.

Therefore population characteristics should be statistical rather than rigid.

---

# 8. BODY

The Person contains a `Body` object generated from genetics.

Potential physical characteristics:

- height
- weight
- strength
- stamina
- agility
- physical prowess
- fitness
- health
- injuries
- age-related changes

Fitness should not simply be a single arbitrary number.

It may eventually emerge from:

```text
body
+
training
+
health
+
age
+
nutrition
+
activity
+
genetics
```

---

# 9. PERSONALITY

Personality is represented separately through a `Personality` object.

Current intended traits:

## Big Five

- openness
- conscientiousness
- extraversion
- agreeableness
- neuroticism

## Dark personality traits

- Machiavellianism
- narcissism
- psychopathy
- sadism

These are represented as continuous values/floats.

They should NOT directly dictate behavior.

Instead:

```text
PERSONALITY
      ↓
influences
      ↓
PERCEPTION
INTERPRETATION
EMOTIONAL RESPONSE
MOTIVATION
DECISION-MAKING
SOCIAL BEHAVIOR
```

For example, high openness might influence:

- curiosity
- tolerance for novelty
- exploration
- interest in ideas

but should not simply mean:

```python
if openness > 0.8:
    explore()
```

Personality is intended to bias systems rather than replace them.

---

# 10. EMOTIONS

Person contains:

```python
self.emotions = EmotionalState()
```

The emotional system is still relatively early.

Important design principle:

An emotion should be an **emergent response**, not merely a permanent character statistic.

For example:

```text
EVENT
↓
PERSON'S INTERPRETATION
↓
APPRAISAL
↓
EMOTIONAL RESPONSE
```

The same event can therefore produce different emotional responses in different people.

Example:

```text
Edward dies
```

could produce:

```text
Arthur:
grief
love
fear
anxiety
```

while:

```text
Thomas:
relief
resentment
guilt
perhaps grief
```

depending on their history.

---

# 11. MEMORY

Person contains:

```python
self.memories = []
```

Memories are represented using a `Memory` object.

The intended model is:

```text
EXPERIENCE
↓
MEMORY
```

A memory can eventually contain:

- event
- time
- location
- participants
- interpretation
- emotional significance
- contextual information

Memory should eventually be capable of:

- decay
- strengthening through repetition
- distortion
- emotional reinforcement
- influencing future interpretation
- influencing beliefs
- influencing relationships

A person should not simply remember objective historical truth.

They should remember **their experience of it**.

---

# 12. BELIEFS

Person currently has:

```python
self.beliefs = []
```

The system is not fully developed.

Beliefs are intended to represent things a person considers true or meaningful.

Potential categories:

```text
religious beliefs
political beliefs
social beliefs
personal beliefs
beliefs about other people
beliefs about the world
beliefs about themselves
```

Beliefs should be capable of developing from:

```text
culture
faith
family
education
experience
memory
observation
social influence
reasoning
```

and should subsequently influence:

```text
interpretation
emotion
motivation
decisions
relationships
```

---

# 13. MOTIVATIONS

Person currently has:

```python
self.motivations = []
```

Motivations represent relatively persistent drives.

They should eventually emerge from combinations of:

```text
biology
personality
development
beliefs
circumstances
relationships
culture
faith
experience
```

Potential motivations:

- survival
- security
- belonging
- achievement
- power
- status
- knowledge
- exploration
- wealth
- love
- revenge
- freedom
- family welfare
- religious devotion

The system should not assume that every person values these equally.

---

# 14. GOALS

Person currently has:

```python
self.goals = []
```

Goals are intended to be more concrete than motivations.

Example:

```text
Motivation:
Power

Goal:
Become ruler of the kingdom
```

or:

```text
Motivation:
Security

Goal:
Acquire enough food to survive winter
```

Goals should eventually be generated dynamically rather than manually assigned.

They should respond to:

- motivations
- opportunities
- constraints
- memories
- relationships
- world events
- resources
- beliefs
- personality

This is a major part of the eventual autonomy system.

---

# 15. SKILLS AND KNOWLEDGE

Person contains:

```python
self.skills = {}
self.knowledge = {}
```

Skills and knowledge are intentionally distinct.

## Knowledge

Knowing something.

Example:

```text
knowledge["ancient ruins"] = 0.7
```

## Skill

Being able to perform something.

Example:

```text
skills["blacksmithing"] = 0.8
```

The system should eventually support experience-based development.

This connects to the decision to remove occupation as a permanent Person state.

---

# 16. OCCUPATION PHILOSOPHY

Occupation should NOT fundamentally be:

```python
person.occupation = "blacksmith"
```

because this is too restrictive for the desired simulation.

A person can:

- work as a baker
- quit
- become a soldier
- travel
- become unemployed
- manage a business
- become a ruler
- return to an old profession
- perform temporary work
- possess skills from decades earlier

Instead, occupational activity should generate:

```text
skills
knowledge
money
relationships
reputation
memories
experiences
social connections
opportunities
events
```

Example:

A person blacksmiths for three years, then spends twenty years doing something else.

Their blacksmithing skill should not become zero.

If later asked to forge a sword:

```text
old experience
+
current physical ability
+
knowledge
+
available tools
+
practice
=
current capability
```

This makes occupation an **experience/history system**, rather than a character label.

This also allows the same framework to model both:

```text
ordinary baker
```

and:

```text
king
```

because being a king can similarly be represented through responsibilities, experience, relationships, authority, resources, and social structures.

---

# 17. SURVIVAL SYSTEM

Person contains:

```python
self.survival = SurvivalState()
```

The survival system is responsible for biological needs and states.

Potential components:

- hunger
- thirst
- energy
- sleep
- health
- injuries
- fatigue
- pain
- environmental exposure
- potentially disease

The exact system depends on the eventual world design.

The world currently updates survival once per simulated minute.

---

# 18. ECONOMY

Person currently contains:

```python
self.money
self.inventory
```

Basic inventory functionality exists.

Basic money functionality exists.

However, the actual economic model is intentionally not finalized.

The eventual system may include:

- currencies
- markets
- wages
- prices
- property
- wealth
- debt
- taxation
- trade
- resource scarcity
- businesses
- economic classes

Economic systems should eventually influence people rather than simply being numbers attached to them.

---

# 19. RELATIONSHIPS

Relationships are one of the most important systems in WrldSim.

A relationship is a persistent object connecting two people.

Current dimensions:

```text
affection
trust
respect
fear
resentment
attraction
familiarity
```

Each dimension is directional.

For example:

```text
Arthur → Thomas
affection = 0.8

Thomas → Arthur
affection = 0.2
```

These are separate values.

The relationship also contains:

```text
connections
history
```

The intended eventual relationship model is much more expansive.

Possible influences include:

```text
shared experiences
memories
family
kinship
personality
culture
faith
status
reputation
economic dependence
political interests
competition
cooperation
promises
betrayals
attraction
fear
respect
resentment
```

Relationships should change dynamically through interactions and events.

---

# 20. SOCIAL IDENTITY

Social identity should not be reduced to a list of labels.

It may emerge from:

```text
family
culture
faith
status
relationships
reputation
political affiliation
citizenship
occupation/experience
wealth
ancestry
community
```

Social identity is expected to influence how others perceive a person.

---

# 21. CULTURE

Culture is intended to become a major independent system.

It should not simply be:

```python
person.culture = "English"
```

with a few bonuses.

Culture should eventually influence:

- values
- norms
- family structure
- marriage
- gender roles
- etiquette
- emotional expression
- economic behavior
- military organization
- politics
- religion
- education
- attitudes toward outsiders
- interpretation of events

Cultures themselves should exist in the world and change over time.

---

# 22. FAITH

Faith is also intended to be an independent system.

Person may eventually contain:

```python
person.faith
```

where `faith` is a proper `Faith` object/system.

Faith can influence:

- morality
- interpretation
- rituals
- death
- marriage
- family
- politics
- economics
- military behavior
- relationships
- identity
- attitudes toward other faiths

Faith and culture are separate.

They can influence one another, but neither should simply be a property of the other.

---

# 23. SOCIAL PERCEPTION

An important principle:

A person does not perceive other people objectively.

For example:

```text
Prince B
```

may perceive:

```text
Prince A
```

through multiple layers:

```text
personal relationship
+
family relationship
+
shared history
+
reputation
+
culture
+
faith
+
political interests
+
class/status
+
personal personality
```

Therefore two people can encounter the same person and have different perceptions.

For example:

```text
Prince B dislikes Prince A personally.

Prince B also belongs to a faith whose followers have a generally conflicted attitude toward A's faith.

Therefore Prince B's perception of A is influenced both by:
    personal experience
    social/cultural context
```

The intended architecture allows these influences to be small rather than deterministic.

A cultural or religious influence does not need to completely override personal experience.

---

# 24. EVENTS

Events represent things that happen in the world.

Examples:

```text
birth
death
marriage
war
battle
betrayal
discovery
trade
accident
crime
political decision
natural disaster
conversation
```

Events should be objective world occurrences.

The psychological consequences of those events are separate.

---

# 25. EVENT → HUMAN EXPERIENCE PIPELINE

Current conceptual pipeline:

```text
WORLD EVENT
    ↓
OBSERVATION
    ↓
INTERPRETATION
    ↓
EXPERIENCE
    ↓
EMOTIONAL SIGNIFICANCE
    ↓
MEMORY
```

This distinction is extremely important.

The world says:

```text
Edward died.
```

It does not say:

```text
Arthur is sad.
```

Instead Arthur processes the event according to his own internal state.

---

# 26. INTERPRETATION

The interpretation system currently exists and can take into account:

- relationship
- personality
- contextual information

We have already demonstrated differentiated interpretation.

Example:

```text
Arthur:
"Someone I trust has insulted me."

Thomas:
"Someone I resent is deliberately disrespecting me."
```

This demonstrates the intended direction:

```text
OBJECTIVE EVENT
+
PERSON'S INTERNAL STATE
=
SUBJECTIVE INTERPRETATION
```

Interpretation should eventually become substantially more general and event-independent.

---

# 27. EXPERIENCE

The experience system currently connects:

```text
event
↓
observer
↓
interpretation
↓
emotional significance
↓
memory
```

The eventual system should support the broader human processing chain:

```text
PERCEPTION
↓
INTERPRETATION
↓
APPRAISAL
↓
EMOTION
↓
MEMORY
↓
BELIEF/IDENTITY/MOTIVATION CHANGES
↓
GOALS
↓
ACTION
```

---

# 28. WORLD

Current `World` contains:

```text
time
people
events
locations
BehaviorRegistry
DecisionSystem
ActionResolver
running state
```

Time is now represented at minute-level resolution.

Current model:

```text
1 simulation minute = 1 simulation tick
```

World can run:

```python
run_minutes()
run_hours()
run_days()
run_years()
```

The simulation can therefore eventually operate over very long periods.

---

# 29. WORLD TIME

Current world state:

```python
year
month
day
hour
minute
current_time_minutes
```

Current simplification:

```text
30-day months
12 months/year
```

The long-term intention is that activities consume actual simulated minutes.

Example:

```text
travel = 180 minutes
sleep = 480 minutes
work = 360 minutes
conversation = 15 minutes
```

Narrative/player decisions can potentially represent zero-time events where appropriate.

---

# 30. ACTIVITY SYSTEM

People can have a current activity.

Conceptually:

```text
Person
 ↓
current_activity
 ↓
Action
 ↓
duration
 ↓
activity progresses over world minutes
 ↓
ActionResolver
 ↓
outcome
```

This is already connected to World.

---

# 31. DECISION SYSTEM

The world currently asks the decision system for an action when a person is not already performing one.

Conceptually:

```text
Person state
+
World state
↓
DecisionSystem
↓
Action + score
```

The eventual decision system should become the primary mechanism by which autonomy emerges.

It should eventually consider:

```text
needs
personality
emotions
motivations
goals
beliefs
relationships
memories
knowledge
skills
location
resources
social expectations
culture
faith
risk
opportunity
time
```

The system should not require every possible action to be scripted as a personality rule.

---

# 32. ACTION SYSTEM

Actions represent things a person can actually do.

Examples currently include concepts such as:

```text
eat
sleep
work
practice
buy
sell
socialize
explore
```

Actions are separate from decisions.

This distinction is important:

```text
Decision:
"I want to explore."

Action:
"Travel to the forest."

Outcome:
"Person discovers an abandoned structure."
```

The action system should eventually allow consequences to emerge from world conditions.

---

# 33. CURRENT CAUSAL ARCHITECTURE

The most important long-term architecture currently envisioned:

```text
                         WORLD
                           │
                           ▼
                        EVENT
                           │
                           ▼
                      PERCEPTION
                           │
                           ▼
                    INTERPRETATION
                           │
               ┌───────────┴───────────┐
               ▼                       ▼
            EMOTION                 COGNITION
               │                       │
               └───────────┬───────────┘
                           ▼
                         MEMORY
                           │
                  ┌────────┴────────┐
                  ▼                 ▼
               BELIEFS          IDENTITY
                  │                 │
                  └────────┬────────┘
                           ▼
                       MOTIVATIONS
                           │
                           ▼
                          GOALS
                           │
                           ▼
                       DECISION
                           │
                           ▼
                         ACTION
                           │
                           ▼
                         WORLD
                           │
                           └───────────────┐
                                           │
                                           ▼
                                      NEW EVENTS
```

Running through this entire system:

```text
GENETICS
DEVELOPMENT
BIOLOGY
PERSONALITY
FAMILY
RELATIONSHIPS
CULTURE
FAITH
KNOWLEDGE
SKILLS
ECONOMICS
POLITICS
ENVIRONMENT
```

These factors should continuously modify the process.

---

# 34. CURRENT IMPLEMENTATION STATUS

## Implemented / substantially established

```text
✓ Person
✓ Genetics foundation
✓ Body foundation
✓ Personality
✓ EmotionalState foundation
✓ SurvivalState foundation
✓ Family
✓ Relationship
✓ Memory
✓ Event
✓ Event consequences
✓ Event observation
✓ Interpretation
✓ Experience/memory creation
✓ World
✓ Minute-level simulation clock
✓ Activities
✓ Decision system foundation
✓ Behavior registry foundation
✓ Action resolver foundation
✓ Basic actions
✓ Basic inventory
✓ Basic money
```

## Partially implemented

```text
~ Emotional processing
~ Interpretation
~ Memory
~ Relationships
~ Decision-making
~ Motivation
~ Goals
~ Skills
~ Knowledge
~ Genetics
~ Body
~ Survival
~ Family events
```

## Not yet implemented as major systems

```text
□ Culture
□ Faith
□ Reproduction
□ Full genetics inheritance
□ Development/childhood
□ Education
□ Advanced skill progression
□ Advanced knowledge
□ Political systems
□ Government
□ Citizenship
□ Kingdoms
□ Military systems
□ Advanced economics
□ Property
□ Businesses
□ Reputation
□ Social groups
□ Language
□ Crime/law
□ Marriage
□ Succession
□ Inheritance
□ Population systems
□ Geography/ecology
□ Large-scale history
```

---

# 35. CURRENT TESTING PHILOSOPHY

Tests are diagnostic.

They should NOT dictate the design.

The desired world architecture comes first.

Tests should answer questions such as:

```text
Does the system behave according to the architecture?
Does information propagate correctly?
Does one person's state influence their response?
Are relationships asymmetric?
Does an event create appropriate consequences?
Does the simulation remain stable?
```

A test should never become:

> "Let's design the simulation so this test produces the output we want."

Instead:

> "We designed a general mechanism. Let's see what it produces under these circumstances."

---

# 36. IMPORTANT ARCHITECTURAL PRINCIPLES

## Principle 1 — Avoid giant Person classes

Person should be the central entity but should delegate complexity to systems.

Prefer:

```python
person.personality
person.relationships
person.family
person.genetics
person.body
person.survival
```

rather than putting hundreds of variables directly into Person.

---

## Principle 2 — Avoid hardcoded psychology

Do not create:

```python
if narcissism > 0.8:
    person.becomes_angry()
```

as the primary architecture.

Instead:

```text
event
+
interpretation
+
appraisal
+
personality
+
relationship
=
emotional response
```

---

## Principle 3 — Traits should influence, not dictate

A trait should modify probabilities, preferences, sensitivity, interpretation, or decision weighting.

It should rarely determine behavior by itself.

---

## Principle 4 — Separate objective world state from subjective human experience

World:

```text
Edward died.
```

Arthur:

```text
Edward was my father.
I loved him.
He protected me.
He was supposed to see me become king.
He is gone.
```

Thomas:

```text
Edward was cruel to me.
He favored Arthur.
Now he is dead.
What happens to the succession?
```

Same event.

Different internal realities.

---

## Principle 5 — Relationships are directional

Never assume:

```text
A likes B
```

means:

```text
B likes A
```

---

## Principle 6 — History matters

Past experiences should affect present behavior.

The person should not reset after every event.

---

## Principle 7 — Systems should be reusable

The same systems should work for:

```text
peasant
merchant
soldier
blacksmith
noble
king
priest
explorer
criminal
child
```

without creating fundamentally different Person classes.

---

## Principle 8 — Do not over-engineer prematurely

The project is being built iteratively.

When a system can initially be represented simply, implement a simple version and improve it when the simulation demonstrates the need.

The goal is to keep making tangible progress.

---

# 37. THE CENTRAL AUTONOMY PROBLEM

One of the largest unresolved design problems is:

> How do we produce autonomous people in an open world without scripting every possible behavior?

The desired answer is not a giant list of behavioral rules.

Instead, the eventual system should approximately be:

```text
Person's internal state
+
World perception
+
Available actions
+
Motivations
+
Goals
+
Constraints
+
Relationships
+
Beliefs
+
Memory
+
Personality
+
Culture
+
Faith
+
Needs
=
Decision
```

The decision system then selects from possible actions.

This should create enough feedback that long-term behavior becomes difficult to predict exactly.

---

# 38. EMERGENT LIFE EXAMPLE

The intended simulation should eventually be capable of producing something like:

```text
A king has three children.

Child A:
high conscientiousness
strong relationship with father
high respect from nobles

Child B:
high ambition
resentment toward father
many military relationships

Child C:
high openness
low interest in politics
strong religious devotion
```

The king dies.

Nothing should explicitly say:

```text
START SUCCESSION STORY
```

Instead:

```text
death event
↓
family relationships
↓
inheritance rules
↓
political structure
↓
individual interpretations
↓
emotions
↓
motivations
↓
goals
↓
alliances
↓
actions
↓
political consequences
```

The result could be:

- peaceful succession
- civil war
- assassination
- abdication
- compromise
- foreign intervention
- religious intervention
- kingdom fragmentation

depending on the systems and circumstances.

---

# 39. LONG-TERM VISION

The eventual simulation should create a world where:

```text
People are born.
People develop.
People form relationships.
People learn.
People work.
People love.
People hate.
People remember.
People forget.
People marry.
People reproduce.
People die.
Families grow and disappear.
Cultures change.
Faiths spread and fracture.
Kingdoms rise and fall.
Economies develop.
Wars begin.
Borders change.
Technology is discovered and lost.
Cities grow.
Cities collapse.
History accumulates.
```

The player then enters that world.

The player should not feel like the only meaningful agent.

The world should continue to exist and change independently of the player.

---

# 40. CURRENT DEVELOPMENT POSITION

We have moved beyond the initial question:

> "How do I make an NPC?"

The current project is now better understood as:

> **"How do I construct a general-purpose simulation of human beings interacting with a changing world?"**

The current foundations are sufficient to begin connecting systems more deeply.

The major next architectural task is to establish the **complete causal relationship between perception, interpretation, emotion, memory, beliefs, motivation, goals, decision-making, action, and world consequences**.

This should be developed as a general mechanism rather than as a collection of event-specific scripts.

The project should continue from this point without assuming that every currently listed system is final.

---

# 41. DEVELOPMENT RULE FOR FUTURE SESSIONS

When continuing development from this document:

1. Preserve the existing architecture unless there is a concrete reason to change it.
2. Explain the conceptual purpose of a new system before implementing it.
3. Prefer tangible implementation progress over prolonged theoretical preparation.
4. Provide complete copy-pasteable files when the user asks to build a system.
5. Keep testing diagnostic rather than allowing tests to dictate system design.
6. Do not prematurely implement every possible aspect of psychology, economics, anthropology, or genetics.
7. Build general mechanisms that can later become more sophisticated.
8. Remember that the ultimate objective is emergent behavior in an open-ended world.
9. Treat relationships and human social interaction as first-class systems.
10. Keep Person modular: Person is the entity that possesses/participates in systems, not the place where every system's logic belongs.

---

# 42. CURRENT CONCEPTUAL MAP

The project currently aims toward:

```text
                              WRLDSIM
                                 │
                ┌────────────────┼────────────────┐
                │                │                │
              WORLD            PEOPLE           SOCIETY
                │                │                │
        ┌───────┼───────┐       │        ┌───────┼────────┐
        │       │       │       │        │       │        │
     Geography Resources Events  │     Culture Faith   Politics
                                │
                 ┌──────────────┼──────────────┐
                 │              │              │
              Biology       Psychology       Social
                 │              │              │
             Genetics       Personality    Relationships
             Body           Emotion        Family
             Survival       Memory         Reputation
             Reproduction   Beliefs        Status
                            Motivation
                            Goals
                 │              │              │
                 └──────────────┼──────────────┘
                                │
                           DECISION
                                │
                             ACTION
                                │
                             WORLD
                                │
                              EVENTS
                                │
                          HUMAN EXPERIENCE
                                │
                             HISTORY
                                │
                           FUTURE WORLD
```

**This is the current state of WrldSim 1.0.**