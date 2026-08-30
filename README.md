# WrldSim 1.0 — World Simulation Ontology

### Working Design Document for Ver1.0

> **Purpose:** Define what exists in WrldSim, how the major systems relate to one another, and what a "person" means within the simulation.
>
> This is a design document, not a technical specification. Systems should remain flexible and may change as development reveals better approaches.

---

# 1. Core Design Philosophy

WrldSim is a living-world simulation in which the player is an individual existing inside a world that continues to function independently of them.

The goal is not to simulate every aspect of reality perfectly.

The goal is to create sufficiently interconnected systems that believable outcomes can **emerge from the interaction of people, environments, institutions, history, and chance**.

The player should not be the center of the simulation.

The world should continue to exist if the player does nothing.

People should have lives that are not simply scripts waiting for the player to interact with them.

A person should not be defined primarily by their occupation, social class, political status, or current activity.

Instead, these should emerge from their circumstances and accumulated experiences.

### Fundamental principle

**A person is not a collection of RPG statistics.**

A person is an individual with:

* biological inheritance
* physical characteristics
* psychological tendencies
* capabilities
* memories
* beliefs
* relationships
* experiences
* desires
* circumstances
* a personal history

These continually influence one another over the course of their life.

---

# 2. The World

The World is the total simulated environment in which everything else exists.

It includes:

* geography
* climate
* settlements
* natural resources
* wildlife
* people
* populations
* cultures
* faiths
* organizations
* economies
* political entities
* technologies
* historical records
* artefacts
* events
* time

The World should not require the player to exist.

If the player character dies, the simulation should theoretically be capable of continuing.

If the player spends ten years isolated from society, the rest of the world should have changed during those ten years.

---

# 3. Deep History

WrldSim's present world exists as the consequence of thousands of years of history.

The ancient world experienced a massive civilization-ending war involving nuclear weapons and other forms of destruction.

The consequences varied dramatically across Earth.

Different regions experienced different combinations of:

* nuclear destruction
* famine
* disease
* warfare
* ecological collapse
* migration
* technological collapse
* population collapse
* geographic transformation
* extinction

Humanity survived, but civilization as it existed before the catastrophe did not.

Thousands of years have passed.

Nature reclaimed much of the abandoned world.

Human populations became isolated and developed independently.

Knowledge was:

* preserved
* lost
* distorted
* rediscovered
* misunderstood
* deliberately hidden
* mythologized

The present world therefore contains remnants of an enormous forgotten history.

This history does not need to be completely known by the player or by the inhabitants of the world.

The truth may exist independently of what people believe.

---

# 4. Geography

Geography is not merely a static map.

The world's geography is the result of both natural processes and historical events.

Possible geographic features include:

* continents
* islands
* oceans
* lakes
* rivers
* mountains
* forests
* deserts
* plains
* wetlands
* settlements
* ruins
* hazardous regions
* unexplored regions

Some regions may be:

* inhabited
* abandoned
* claimed
* contested
* unexplored
* inaccessible
* uninhabitable

Political borders do not necessarily correspond to actual control.

A kingdom may claim a territory without possessing meaningful control over it.

Unclaimed land is an important part of the world.

---

# 5. Person

A Person is a persistent individual living within the world.

A Person has a life history that develops over time.

A Person is affected by both inherited characteristics and environmental experiences.

A Person can:

* be born
* develop
* learn
* work
* form relationships
* reproduce
* travel
* suffer
* heal
* acquire possessions
* form beliefs
* change beliefs
* pursue goals
* make decisions
* participate in institutions
* influence others
* be influenced by others
* age
* die

The Person class should represent the individual, while larger systems should handle phenomena that exist beyond the individual.

---

# 6. Person — Identity

A Person may have:

* first name
* last name
* age
* sex

Names can be influenced by:

* parents
* culture
* faith
* geography
* history
* family traditions
* player customization

A last name may sometimes originate from the player's input and sometimes from existing world history.

Identity should not be reduced to political or occupational status.

---

# 7. Person — Ancestry

Ancestry is fundamentally genealogical.

A person's ancestry comes from their parents and previous generations.

A person's family history can therefore be reconstructed through:

* parents
* grandparents
* siblings
* children
* spouses
* descendants
* memories
* records
* artefacts

Ancestry should not require a rigid racial category.

Different human populations may develop recognizable characteristics over thousands of years, but reproduction allows those characteristics to mix.

A person may therefore have ancestry from multiple populations.

---

# 8. Genetics / Inheritance

Genetics represents characteristics inherited from previous generations.

WrldSim 1.0 does not need to reproduce real human molecular genetics.

The initial system can instead represent simplified heritable traits.

Potential inherited characteristics include:

* physical morphology
* pigmentation
* height potential
* body structure
* metabolic tendencies
* physical capabilities
* disease susceptibility
* sensory characteristics
* temperament tendencies
* other heritable characteristics

Inheritance should involve both parents.

Children should not necessarily be exact averages of their parents.

There should be variation between siblings.

There may also be occasional mutation or other sources of variation.

The system should eventually allow populations to develop different distributions of characteristics over many generations.

---

# 9. Phenotype / Physical Development

The person's observable physical characteristics are the result of inherited traits interacting with development and environment.

Possible factors include:

* genetics
* nutrition
* illness
* activity
* age
* environment
* development

Potential physical characteristics include:

* height
* weight
* body proportions
* physical appearance
* strength
* stamina
* agility
* physical condition
* other physical characteristics

The eventual 2D/3D representation of a Person should ideally be generated from their simulated characteristics rather than being the fundamental source of those characteristics.

---

# 10. Nature and Nurture

WrldSim treats development as an interaction between inherited predispositions and lived experience.

Nature provides tendencies and potential.

Nurture consists of the environment and experiences encountered throughout life.

Neither should completely determine the person.

A person's development may depend upon:

* genetics
* parents
* family
* culture
* faith
* geography
* wealth
* education
* relationships
* trauma
* success
* failure
* opportunities
* deprivation
* historical circumstances
* random events
* personal decisions

Nature and nurture should therefore form a feedback loop.

A person's inherited tendencies influence how they behave.

Their behaviour influences the experiences they encounter.

Those experiences influence their development.

Their development influences future behaviour.

---

# 11. Personality

Personality represents relatively persistent psychological tendencies.

WrldSim 1.0 uses the following major personality dimensions:

### Big Five

* Openness
* Conscientiousness
* Extraversion
* Agreeableness
* Neuroticism

### Dark personality traits

* Machiavellianism
* Narcissism
* Psychopathy
* Sadism

These should exist as continuous values rather than rigid categories.

Personality should influence many systems rather than directly determining individual actions.

For example, personality may influence:

* social behaviour
* risk-taking
* reactions to events
* decision-making
* relationships
* ambitions
* preferred activities
* interpretation of experiences
* responses to stress
* learning
* conflict

Personality itself may also change to some degree over a person's life.

---

# 12. Mind / Psychology

The mind represents the person's current psychological state and internal processing.

Potential components include:

* emotions
* desires
* beliefs
* fears
* motivations
* intentions
* perceptions
* interpretations
* attention
* memories
* expectations

A person's internal state should influence decisions.

Two people experiencing the same external event may react differently because they:

* perceive it differently
* interpret it differently
* remember different things
* have different personalities
* have different relationships
* have different goals
* possess different knowledge

---

# 13. Motivation

Motivation represents what a Person currently wants or is driven toward.

Motivations may originate from:

* survival
* biological needs
* personality
* relationships
* beliefs
* culture
* faith
* ambition
* status
* curiosity
* revenge
* love
* fear
* security
* wealth
* power
* knowledge

Motivations should not necessarily become explicit goals immediately.

A person may have a desire without knowing exactly how to achieve it.

---

# 14. Goals

Goals are more concrete objectives formed from motivations and circumstances.

Examples:

* acquire food
* find shelter
* learn a skill
* earn money
* marry someone
* protect a child
* become wealthy
* gain political influence
* become king
* avenge someone
* explore a region
* escape a dangerous situation

Goals can change.

A Person may abandon one goal when circumstances change.

Multiple goals can conflict.

---

# 15. Memory

Memory represents experiences that a Person retains.

A memory is not necessarily an objective record of what happened.

It may contain:

* what happened
* who was involved
* where it happened
* when it happened
* the person's interpretation
* emotional significance
* importance to the person

Memory can influence:

* relationships
* beliefs
* future decisions
* emotional reactions
* personality development
* knowledge
* goals

People may remember some events strongly and forget others.

Different people can remember the same event differently.

---

# 16. Experience

Experience is something that happens to a Person or something they participate in.

Examples:

* being praised
* being beaten
* learning to farm
* falling in love
* losing a parent
* witnessing a war
* travelling
* being betrayed
* succeeding at something
* failing
* meeting a stranger
* being imprisoned
* becoming wealthy
* losing wealth

Experience is one of the primary mechanisms through which nurture affects development.

An experience does not necessarily have the same effect on every Person.

---

# 17. Events

Events are occurrences in the world.

An event may involve:

* one person
* several people
* a family
* an organization
* a settlement
* a kingdom
* an entire region
* the world

Events may be:

* intentional
* accidental
* natural
* political
* economic
* social
* personal
* historical

An event can create experiences for its participants.

For example:

**Event:**
The king publicly names Prince A as his preferred successor.

Possible consequences:

* Prince A feels validated.
* Prince B becomes resentful.
* Prince C becomes frightened.
* A courtier sees an opportunity.
* A sibling relationship deteriorates.
* Another faction becomes loyal to A.
* Someone remembers the event decades later.

One event can therefore propagate through many systems.

---

# 18. Relationships

Relationships are one of the central systems of WrldSim.

A Person does not exist socially in isolation.

A relationship represents the accumulated connection between two people.

A relationship can contain multiple simultaneous dimensions, such as:

* affection
* trust
* respect
* fear
* resentment
* loyalty
* attraction
* familiarity
* dependence
* rivalry

Relationships can also contain contextual connections:

* parent
* child
* sibling
* spouse
* friend
* enemy
* employer
* employee
* teacher
* student
* political ally
* political rival

These relationships may overlap.

Two siblings can simultaneously be:

* brothers
* friends
* political rivals
* business partners
* enemies

Relationships should be asymmetric.

Person A may love Person B while Person B dislikes Person A.

---

# 19. Family

Family is primarily a consequence of biological and social relationships.

Family systems should support:

* reproduction
* parenthood
* siblings
* marriage
* inheritance
* descendants
* family alliances
* family conflicts
* family traditions
* genealogy

Families should have histories.

A person's relationship with their siblings can affect their entire life.

This is especially important for political succession.

Example:

A king dies.

His children may have:

* different relationships with one another
* different relationships with their parents
* different personalities
* different military experience
* different wealth
* different supporters
* different legitimacy
* different ambitions

The resulting succession crisis should emerge from these conditions rather than being a predetermined scripted event.

---

# 20. Skills

Skills represent learned capabilities.

Examples:

* farming
* hunting
* blacksmithing
* swordsmanship
* medicine
* trade
* navigation
* literacy
* engineering
* diplomacy

Skills should develop through:

* practice
* education
* mentorship
* occupation-related experience
* observation
* experimentation
* repetition

Skills may deteriorate through:

* age
* inactivity
* injury
* memory loss
* other circumstances

---

# 21. Knowledge

Knowledge is distinct from skill.

A person can know something without being capable of performing it well.

Knowledge may include:

* facts
* languages
* cultural knowledge
* geographical knowledge
* historical knowledge
* religious knowledge
* technical knowledge
* knowledge about people

Knowledge can be:

* learned
* taught
* discovered
* forgotten
* misunderstood
* inherited culturally

---

# 22. Occupation / Work Experience

Occupation should not be a permanent fundamental identity property of a Person.

A person can perform many types of work throughout their life.

Instead, occupational involvement should generate experiences.

For example:

A Person works as a blacksmith for three years.

That experience may produce:

* blacksmithing skill
* knowledge of metallurgy
* relationships with customers
* relationships with coworkers
* money
* memories
* reputation
* opportunities
* future events

Twenty years later, they may no longer be a blacksmith.

However, their accumulated skill and knowledge may remain.

If someone asks them to make a sword, their previous experience can influence their ability to do so.

Similarly, someone may temporarily work at a bakery without that occupation becoming their permanent identity.

---

# 23. Survival / Physical State

A Person has a changing physical condition.

Potential components include:

* hunger
* thirst
* energy
* sleep
* fatigue
* health
* injuries
* pain
* illness
* physical fitness
* other biological needs

These should influence behaviour.

For example:

High hunger may increase the motivation to obtain food.

Severe injury may reduce physical capability.

Exhaustion may affect decision-making.

Lack of sleep may affect mood and performance.

---

# 24. Economy / Money

Money is an aspect of a person's economic circumstances.

A Person may:

* earn money
* spend money
* save money
* lose money
* trade
* borrow
* lend
* inherit
* receive gifts
* acquire wealth through other means

The eventual economic system may become much more sophisticated depending on the world design.

Money should therefore remain modular rather than deeply embedded into Person.

---

# 25. Culture

Culture is a system existing beyond the individual.

A Person may belong to, participate in, or be influenced by one or more cultures.

Culture can influence:

* language
* traditions
* values
* family structures
* social expectations
* clothing
* food
* architecture
* art
* behaviour
* relationships
* economics
* politics
* military practices
* religion/faith

Culture can change over time.

Cultures can:

* merge
* split
* disappear
* spread
* influence one another
* change through historical events

A person does not necessarily perfectly represent their culture.

---

# 26. Faith

Faith is separate from culture.

Faith can influence:

* beliefs
* morality
* rituals
* relationships
* family structures
* politics
* economics
* military behaviour
* personal decisions
* responses to death
* interpretation of events

Faith can be:

* inherited culturally
* adopted
* rejected
* modified
* combined with other traditions

Different people within the same culture may hold different beliefs.

Faith itself should evolve historically.

---

# 27. Population

Population represents groups of people who share some combination of:

* ancestry
* geography
* physical characteristics
* culture
* language
* historical origin
* social identity

Populations are not necessarily rigid races.

Populations can:

* migrate
* mix
* split
* disappear
* expand
* contract
* interbreed

Over many generations, isolated populations may develop distinct physical and cultural characteristics.

---

# 28. Organizations

Organizations are persistent groups of people organized around some purpose.

Examples:

* guilds
* armies
* religious institutions
* businesses
* noble houses
* criminal groups
* schools
* councils
* political factions
* expeditions

Organizations can have:

* members
* leaders
* resources
* goals
* rules
* relationships
* histories

A Person can belong to many organizations simultaneously.

---

# 29. Government / Political Entities

Political systems govern some portion of the population or territory.

Possible political entities include:

* kingdoms
* councils
* republics
* city-states
* tribal governments
* federations
* other forms that emerge from the world

Political authority should not necessarily equal territorial ownership.

A government may have:

* recognized territory
* contested territory
* weakly controlled territory
* claimed territory
* institutions
* laws
* officials
* military forces
* taxation
* political factions

Citizenship should belong primarily to the political/governance system rather than being an immutable property of Person.

---

# 30. Technology

Technology represents knowledge, techniques, tools, infrastructure and systems available to societies and individuals.

Technology should not necessarily be represented as one global "technology level."

Different societies may possess different technologies.

A society may possess an artefact without understanding its underlying principles.

Knowledge may be:

* invented
* forgotten
* rediscovered
* copied
* misunderstood
* preserved by institutions

---

# 31. Artefacts

Artefacts are physical objects with histories.

Examples:

* weapons
* books
* tools
* machines
* religious objects
* jewellery
* ruins
* vehicles
* technological remnants

An artefact may have:

* creator
* creation period
* ownership history
* location history
* purpose
* current condition

The meaning of an artefact to a Person may differ from its actual historical origin.

An ancient machine may be understood as:

* technology
* a religious object
* a weapon
* a magical object
* worthless debris

depending on who encounters it.

---

# 32. History

History is the accumulated sequence of events that have occurred in the world.

History should exist independently of whether anyone remembers it correctly.

There may therefore be a distinction between:

**What actually happened**

and

**What people believe happened.**

History can influence:

* cultures
* faiths
* political borders
* family histories
* relationships
* technology
* populations
* traditions
* conflicts

---

# 33. The Central Feedback Loop

The most important conceptual loop in WrldSim is:

```text
BIOLOGY / INHERITANCE
          ↓
       PERSON
          ↓
    PERCEPTION
          ↓
    INTERPRETATION
          ↓
       DECISION
          ↓
        ACTION
          ↓
        EVENT
          ↓
      EXPERIENCE
          ↓
        MEMORY
          ↓
     DEVELOPMENT
          ↓
       PERSON
```

At the same time, the Person is continuously influenced by:

```text
          WORLD
            │
     ┌──────┼──────┐
     ↓      ↓      ↓
  CULTURE  FAITH  SOCIETY
     │      │      │
     └──────┼──────┘
            ↓
          PERSON
```

And socially:

```text
PERSON A ←→ RELATIONSHIP ←→ PERSON B
    ↑                         ↑
    └──────── EVENT ──────────┘
```

The systems should therefore form a network rather than a hierarchy.

---

# 34. Design Principle: Emergence Over Scripts

WrldSim should prefer:

**conditions → decisions → consequences**

over:

**script → predetermined outcome**

For example, instead of:

```text
Year 35:
The king dies.
Prince A becomes king.
```

the simulation should eventually produce:

```text
King dies
    ↓
Succession becomes possible
    ↓
Claims are evaluated
    ↓
Siblings pursue interests
    ↓
Relationships activate
    ↓
Allies choose sides
    ↓
Organizations respond
    ↓
Political system responds
    ↓
Conflict / compromise / succession emerges
```

The result might be:

* peaceful succession
* civil war
* assassination
* negotiated settlement
* partition
* foreign intervention
* unexpected heir
* collapse of the dynasty

The simulation does not need to know the answer beforehand.

---

# 35. Initial Implementation Philosophy

WrldSim 1.0 should begin with simplified models.

Accuracy can increase over time.

A system should initially exist because it enables meaningful interactions, not because it perfectly reproduces reality.

Complexity should be added when a simpler model produces behaviour that feels insufficient.

The intended progression is:

```text
Simple system
     ↓
Observe simulation
     ↓
Find unrealistic behaviour
     ↓
Identify missing relationship
     ↓
Add/refine system
     ↓
Observe again
```

The goal is not to design the entire human being before the simulation runs.

The goal is to gradually discover what the simulation needs.

---

# 36. Current Core Entities

The initial conceptual ontology therefore consists of:

```text
WORLD
│
├── Geography
├── History
├── Events
├── People
├── Populations
├── Cultures
├── Faiths
├── Organizations
├── Political Entities
├── Settlements
├── Resources
├── Technology
└── Artefacts
```

And each Person connects to:

```text
PERSON
│
├── Identity
├── Ancestry
├── Genetics
├── Physical Development
├── Personality
├── Psychology
├── Motivations
├── Goals
├── Memories
├── Experiences
├── Skills
├── Knowledge
├── Survival State
├── Economic State
├── Relationships
├── Family
├── Culture
├── Faith
└── World Location
```

These are conceptual boundaries, not necessarily final Python classes.

---

# 37. The Long-Term Vision

The eventual objective is that the player should be able to encounter a person and feel that they are encountering **someone who has existed before the player met them**.

A king should have a childhood.

A baker should have parents.

A soldier should have friends.

A thief should have memories.

A grandmother should remember her dead husband.

A prince should have complicated relationships with his siblings.

A blacksmith who has not touched a forge in twenty years should still retain traces of that experience.

A person should be capable of changing.

A person should be capable of contradicting themselves.

A person should sometimes make poor decisions.

A person should sometimes surprise the player.

The simulation should not need to explicitly script these outcomes.

They should emerge from the interaction of the systems.

**The ultimate objective is not to create NPCs that behave intelligently.**

**It is to create people whose behaviour makes sense because they have a history.**
