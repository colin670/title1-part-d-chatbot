#!/usr/bin/env python3
"""
Title I, Part D Subpart 2 Practitioner Chatbot
Allows practitioners to ask questions about the Wyoming DOE guidebook
"""

import os
import sys
from anthropic import Anthropic

# The complete guidebook content
GUIDEBOOK_CONTENT = """
TITLE I, PART D, SUBPART 2: SUBGRANTEE GUIDEBOOK

Building Effective Programs for Delinquent and At-Risk Youth Through Program Design, 
Implementation, and Continuous Improvement

Wyoming Department of Education
122 W. 25th St., Ste. E200 | Cheyenne, WY 82002
P: 307-777-7675 | F: 307-777-6234 | edu.wyoming.gov

Version: September 2025 (DRAFT)

[Full content of all 19 sections...]

SECTION 1: GENERAL INFORMATION
Title I, Part D of the Every Student Succeeds Act (ESSA) consists of two subparts:
- Subpart 1: The State Agency (SA) program
- Subpart 2: The Local Educational Agency (LEA) program

Both subparts operate as formula grant programs based on the number of students residing 
in institutions for delinquent children and youth. Although the count of children residing 
in institutions for neglected children is collected through the annual Subpart 2 count, 
those data generate funding through the Title I, Part A allocation rather than Title I, 
Part D, Subpart 2.

Each subpart targets distinct populations with separate rules, requirements, data collection 
mechanisms, funding streams, and allowable uses of funds. Under Title I, Part D, the ESSA 
Grants team provides leadership, guidance, technical assistance, and resources to LEAs and 
SAs to ensure that neglected and delinquent children and youth have the same opportunities 
to meet the state's challenging academic content and student achievement standards as other 
children.

The Wyoming Department of Education (WDE) is the State Educational Agency (SEA) and serves 
as the pass-through entity (PTE) for Subpart 2 funds.

This guidebook focuses on the administration, compliance, and programmatic framework of the 
Title I, Part D, Subpart 2 grant.

SECTION 2: PURPOSE OF TITLE I, PART D, SUBPART 2
The statutory purpose of Subpart 2 is to support the operation of local educational agency 
programs involving collaboration with locally operated correctional facilities to:

- Carry out high-quality education programs that prepare children and youth for secondary 
  school completion, training, employment, or further education
- Provide activities and services that facilitate the transition of delinquent children and 
  youth from a correctional program to further education or employment
- Operate programs in local schools for children and youth returning from correctional 
  facilities, and programs that may serve at-risk children and youth
- Transitional and supportive programs operated in LEAs shall be designed primarily to meet 
  the transitional and academic needs of students returning to local educational agencies or 
  alternative education programs from correctional facilities

Operational Framework for LEAs:
To translate these federal purposes into local practice, LEAs should anchor their initiatives 
in five core strategies:

1. Strengthen Instructional Opportunities: Provide targeted intervention, academic supports, 
   and instructional enhancements that help students progress toward state academic standards 
   and graduation.

2. Build Capacity Within Local Facilities: Partner with locally operated facilities to improve 
   program quality, supplemental staffing alignment, and educational continuity for youth served.

3. Coordinate Transition Supports: Align school, community, and workforce resources so youth 
   experience a structured, supported pathway back into education or employment.

4. Implement Engagement and Intervention Strategies: Use evidence-based approaches that keep 
   students connected to school, address barriers to attendance, and re-engage youth who have 
   previously disengaged.

5. Target Resources Using Data: Leverage data to pinpoint gaps, allocate services strategically, 
   and strengthen the alignment between identified student needs and funded activities.

Key System Aspects:
- Eligibility: Funds are awarded to LEAs with high percentages of children in locally operated 
  delinquent institutions, at-risk youth in the local schools, and/or attending eligible 
  community day programs.
- Collaboration: LEAs must establish formal agreements per ESSA, Section 1425 with local 
  correctional facilities or other eligible facilities to coordinate services and ensure 
  educational continuity.
- Comprehensive Scope: Beyond basic academic instruction, funds can support vocational training 
  and Career and Technical Education (CTE) programs of study that lead to industry-recognized 
  credentials (IRC).

SECTION 3: FEDERAL STATUTORY AND REGULATORY FRAMEWORK
Title I, Part D, Subpart 2 is governed by federal statute under the Elementary and Secondary 
Education Act of 1965 (ESEA), as amended by the Every Student Succeeds Act (ESSA). The U.S. 
Department of Education (USED) provides non-regulatory guidance to assist states, local 
educational agencies, and facilities in understanding and implementing program requirements.

Key Federal Statutory Requirements:
- Title 20 of the United States Code (20 U.S.C. § 6421)
- ESEA Section 1421 – Program Purpose
- ESEA Section 1422(d) – Transitional and Supportive Programs
- ESEA Section 1424 – Use of Funds
- ESEA Section 1423 – LEA Application Requirements
- ESEA Section 1425 – Formal Agreements
- ESEA Section 1426 – Program Evaluation
- ESEA Section 1431(b) – End of Year Reporting
- ESEA Section 1432 – At Risk Definition

Fiscal Notice:
Subgrantees are advised that while Title I, Part D, Subpart 2 is NOT subject to the statutory 
ESEA 'Supplement not Supplant' (SNS) methodology test applicable to Title I, Part A, all 
expenditures charged to Subpart 2 must still be strictly supplemental in nature.

Baseline Obligation (The "Basket of Goods"):
Under the Wyoming Education Resource Block Grant Model, LEAs are legally required to provide 
a comprehensive core educational program, known as the "basket of goods," to all students. 
Therefore, Subpart 2 funds can never be used to replace state or local obligations. Prohibited 
costs include core classroom teachers, school counselors, required general education textbooks, 
basic administrative staff, districtwide software or technology accessible to the general 
student population, or any other position, service, or resource that forms part of the LEA's 
baseline educational responsibilities.

The Supplemental Standard:
An expenditure is strictly supplemental if it provides an additional, targeted intervention, 
extended learning opportunity, or specialized support to an eligible at-risk or delinquent 
student that would not otherwise be provided in the absence of Subpart 2 funds. If a service 
or resource is required by state law, local school board policy, or made universally available 
to non-eligible students, funding it with Subpart 2 is not allowable.

SECTION 4: DETERMINING FACILITY ELIGIBILITY
An LEA is responsible for determining and documenting whether a facility within its boundaries 
is eligible to generate and receive Title I, Part D, Subpart 2 funds. To be considered eligible, 
a facility must meet the following criteria:

- The facility must operate for the primary purpose of serving youth who have been adjudicated 
  as delinquent or in need of supervision (34 CFR § 200.90) through a formal judicial process.
- Youth served in the facility must be residentially placed as a result of adjudication, 
  meaning placement is ordered through the juvenile justice system.

Definitions:
- Adjudicated as delinquent: Adjudication is a judicial determination that a juvenile is 
  responsible for the delinquency offense charged in a petition or other charging document.
- Adjudicated in need of supervision: Adjudication is a judicial determination that a juvenile 
  is responsible for a status offense charged in a petition or other charging document.

Facilities that serve youth who are placed through non-adjudicatory means, such as placement 
by a state agency, the child welfare system, or a family decision, do not meet eligibility 
requirements for Subpart 2.

SECTION 5: THE ANNUAL COUNT (WDE549)
The annual count is a mandated data collection used to provide the WDE and the USED with 
accurate information on the number of children and youth living in eligible institutions for 
neglected or delinquent populations. This data directly impacts state funding allocations and 
ensures that eligible students receive appropriate educational and vocational services.

Funding Allocation Impact:
- Neglected Count: Contributes to the Title I, Part A allocation
- Delinquent Count: Determines the Title I, Part D, Subpart 2 allocation

Count Window and Duplication Rules:
- The WDE annual count period runs from October 1 through October 30 each year
- A student must be counted if they reside in an eligible facility for at least one day during 
  this 30-day period
- If a student enters a facility multiple times during the count period, each placement must be 
  counted separately

Wyoming High-Concentration Thresholds:
An LEA is considered to have a high concentration of delinquent youth if:
- It reports at least five eligible delinquent children or youth during the count period, and
- Those children and youth represent at least one percent (1%) of the statewide delinquent 
  count after excluding LEAs that do not meet the minimum threshold

SECTION 6: END OF YEAR REPORTING (WDE568)
End-of-year data collection is required under ESEA Section 1431(b). This provision requires 
LEAs to collect and submit annual data to the SEA, which is then reported nationally through 
the Consolidated State Performance Report (CSPR).

Real World Outcomes:
Reporting tracks whether participating youth are:
- Accruing high school credits required for grade promotion or graduation
- Improving academic achievement and literacy/math proficiency
- Successfully transitioning back to traditional public schools, postsecondary education, or 
  vocational job training
- Earning a high school diploma or high school equivalency credential

Data Collection Cycle:
Districts must begin collecting the required data July 1 of each year and continue collecting 
data through June 30 of the following year. The WDE568 is then completed and certified through 
the WDE's Data Collection Suite (DCS). The collection must be certified and approved by the 
program manager no later than August 31 of the submission year.

SECTION 7: FACILITY NOTIFICATION REQUIREMENTS
Because the annual count conducted within eligible facilities generates funding under Title I, 
Part D, Subpart 2, LEAs receiving Subpart 2 funds are expected to provide supplemental 
educational services and supports to youth residing in the eligible facilities that generated 
funding under the program.

Notice of Funding Declination by the LEA:
An LEA may formally elect to decline its Title I, Part D, Subpart 2 allocation but must execute 
the following actions:
- Formally Notify All Eligible Facilities
- Maintain Verification of Notification
- Submit Documentation to the SEA

Notice of Service Declination by the Facility:
If an eligible facility formally elects to opt out of participating in Title I, Part D, 
Subpart 2 services, the LEA must:
- Document the Facility's Decision
- Maintain Communication Records
- Identify the Facility in the Application

SECTION 8: FORMAL AGREEMENTS (ESSA, SECTION 1425)
Under ESEA Section 1425, LEAs must establish a formal agreement with eligible Subpart 2 
facilities. LEAs may title this document at their discretion (e.g., MOU, MOA), provided it 
fulfills all statutory requirements.

The 12 Statutory Requirements Summarized:
Section 1425 mandates that the formal agreement address 12 distinct components:
- Educational continuity
- Communication and collaboration
- Transition planning and coordination
- Academic services and CTE support
- Curriculum-based entrepreneurship education and mentoring programs
- Record sharing
- Family engagement
- Coordination of services before, during, and after a youth's placement in a facility

Implementation and Monitoring Considerations:
Formal agreements must be reviewed, revised as necessary, and signed annually. LEA's must 
maintain local documentation demonstrating ongoing implementation of the agreement terms 
throughout the school year for state monitoring purposes.

SECTION 9: TRANSITION AND SUPPORTIVE PROGRAMS
Pursuant to ESEA Section 1422(d), transitional and supportive programs operated by Local 
Educational Agencies (LEAs) receiving Subpart 2 funds must be designed primarily to meet the 
transitional and academic needs of students returning to an LEA from correctional facilities 
or other eligible residential placements. This is the dropout prevention program.

Categorizing Transition Activities:

Transition Planning:
- Core Focus: The intentional, documented process of identifying a student's academic status, 
  credit deficiencies, career interests, and support needs prior to reentry.
- Implementation: Planning activity. Developing a plan alone does not constitute a direct 
  service to a student.

Transition Coordination:
- Core Focus: Organizing, communicating, and collaborating with schools, families, and 
  community partners to facilitate enrollment and records transfers.
- Implementation: Coordination activity. Must be balanced so sufficient resources reach students 
  directly. Subject to WDE 20% cost limitation cap on Professional Development and Coordination.

Transition Meetings:
- Core Focus: Reentry planning, credit reviews, and team sessions to assign operational 
  responsibilities.
- Implementation: Meetings must yield actionable next steps supporting immediate academic progress.

Transition Services:
- Core Focus: Direct supplemental academic, retention, and workforce readiness supports 
  provided directly to returning youth.
- Implementation: Direct Service. These activities directly impact measurable student performance 
  outcomes and count toward the WDE 75% minimum direct services threshold.

SECTION 10: SUBPART 2 PROGRAM DESIGN FRAMEWORK
Effective Title I, Part D, Subpart 2 programs are built around identified student needs, 
rather than standalone activities, legacy staffing positions, or available funding pools. 
Data must drive the identification of barriers, resource targeting, implementation, and 
continuous evaluation.

Effective programs do NOT begin by asking: What can we spend money on?
Effective programs BEGIN by asking: What barriers are preventing our students from being 
successful and what services are most likely to improve outcomes?

The Role of the Comprehensive Needs Assessment (CNA):
The WDE requires participating LEAs to complete and maintain a Comprehensive Needs Assessment 
(CNA) as part of the Title I, Part D, Subpart 2 application and planning process. The CNA 
should serve as the foundation for program design, resource allocation, implementation, 
evaluation, and continuous improvement.

Continuous Improvement Cycle Steps:
Step 1: Identify Need - Use multiple data sources to identify specific student barriers
Step 2: Determine Root Causes - Identify factors contributing to identified challenges
Step 3: Design Services and Supports - Select evidence-based interventions
Step 4: Implement the Program - Deliver services as designed
Step 5: Evaluate Effectiveness - Measure whether services are producing intended outcomes
Step 6: Adjust and Improve - Use evaluation results to refine services

SECTION 11: COMPONENTS OF EFFECTIVE SUBPART 2 PROGRAMS
While every LEAs program will look different, effective programs will include, but are not 
limited to, one or more of the following components:

- Academic Remediation & Acceleration: Targeted reading and math interventions, extended-day 
  tutoring, summer credit recovery academies, and structured study skills instruction
- Transition & Dropout Prevention: Reentry planning, credit reconciliation, fast-track credit 
  completion, reengagement specialists
- CTE, Vocational & Workforce Readiness: High-demand CTE pathways that lead to an IRC
- Postsecondary Readiness: College pathway exploration, FAFSA completion assistance
- Mentoring & Behavioral Supports: Mentoring programs, self-advocacy training, restorative 
  practices

SECTION 12: ACADEMIC SERVICES
Every LEA receiving Subpart 2 funds must implement supplemental services supporting dropout 
prevention programming for youth returning from facilities, and may operate at-risk programs 
for eligible youth in local schools.

Allowable Academic Service Delivery Models:
- Targeted Supplemental Instruction
- Reentry Academic Supports
- Extended Learning Opportunities
- Summer Academic Programming
- Study Skills and Academic Success Instruction
- Alternative Diploma & GED Preparation

Specialized Purchased Services & Platforms:
- Credit Recovery & Acceleration Platforms
- Diagnostic & Skill-Building Systems
- Progress Monitoring & Early Warning Systems
- Virtual Instruction

Supplemental Compliance Standards:
Subpart 2 funds must be supplemental and not replace the educational services the LEA is 
otherwise required to provide by federal and state laws.

Strong Supplemental Examples:
- A qualified reading teacher providing targeted, small-group literacy instruction after school
- A small-group math intervention conducted during summer school
- Funding Industry-Recognized Credential (IRC) exam fees for eligible students in CTE programs
- A supplemental science tutoring program
- Hosting a targeted summer academic bridge program
- Providing an after-school math tutoring program using adaptive intervention software
- Supplemental credit recovery instruction
- Funding a specialized peer or adult mentoring program

Unallowable Examples:
- Using Subpart 2 funds to pay the salary of a regular English teacher
- Purchasing standard core ELA or math textbooks
- Paying for special education teachers or IEP-required services
- Supporting a general school counselor position
- Paying for district-wide software accessible to all students
- Purchasing standard classroom technology for general use

SECTION 13: AT-RISK PROGRAM
Title I, Part D, Subpart 2 permits an LEA to provide supplemental services to eligible at-risk 
youth in local schools. Subpart 2 is not intended to fund services for all struggling students.

Statutory Definition of At-Risk Youth:
An at-risk child or youth means a school-aged individual who:
- is at risk of academic failure
- has had a dependency or delinquency adjudication
- has a drug or alcohol problem
- is pregnant or parenting
- has come into contact with the juvenile justice system or child welfare system
- is at least one year behind the expected grade level
- has previously dropped out of school
- is a gang member
- has a high absenteeism rate at school
- is an English learner

USED differentiates based on:
- General Academic Need (Non-Subpart 2): A student struggling in a single subject
- Subpart 2 At-Risk Threshold: A student exhibiting systemic risk factors (multi-credits behind, 
  over-age, chronically absent, facing severe life disruptions)

SECTION 14: CONSIDERATION OF REASONABLE, ALLOWABLE, AND ALLOCABLE
Federal cost principles (§§200.403 and 200.404) require that expenditures are:
- Necessary: Directly support the purpose and goals of the grant
- Reasonable: Reflect what a prudent person would pay under similar circumstances
- Allocable: Tied directly to the Subpart 2 program in exact proportion
- Allowable: Explicitly permitted under federal, state, and program-specific statutory rules

Key Questions:
- Do we need this to meet an identified barrier?
- Does it make sense cost-wise?
- Does it belong to this grant?
- Is it permitted by regulation?

SECTION 15: USE OF FUNDS
Title I, Part D, Subpart 2 funds are intended to improve outcomes for eligible youth through 
supplemental programs and services.

Funding decisions should demonstrate: Identified Need → Service or Strategy → Expenditure → 
Intended Outcome

Allowable Program Areas:
- Academic Services
- Transition and Dropout Prevention Services
- Career and Technical Education (CTE), Vocational, and Workforce Readiness
- Postsecondary Readiness

SECTION 16: WDE COST LIMITATIONS
To maximize the impact of limited federal funds, the WDE has established cost limitations.

WDE SUBPART 2 COST LIMITATIONS:
- Direct Academic and Student Services: Minimum 75%
- Professional Development and Coordination Activities: Maximum 20%
- Administrative Activities: Maximum 5%

Important Consideration Regarding Positions:
The determination of whether a position falls within the 20% limitation is based on the duties 
performed, not the title of the position.

Any position whose primary responsibilities involve planning, communication, coordination, 
facilitation, monitoring, management, or oversight of services should be considered a 
coordination position.

SECTION 17: PROFESSIONAL DEVELOPMENT
Professional development may be used to strengthen the knowledge, skills, and capacity of 
staff responsible for implementing Title I, Part D, Subpart 2 programs and services.

Effective professional development should:
- Support identified program needs
- Improve service delivery
- Strengthen implementation of evidence-based practices
- Ultimately improve outcomes for participating youth

Examples of Allowable Professional Development:
- Academic interventions
- Credit recovery strategies
- Transition and reengagement practices
- Dropout prevention strategies
- Career and technical education programs
- Workforce readiness practices
- Trauma-informed practices

SECTION 18: APPLICATION FRAMEWORK AND NARRATIVE EXPECTATIONS
The Title I, Part D, Subpart 2 application requires clear, data-informed narratives demonstrating:
- Statutory Compliance
- Programmatic Focus
- Fiscal Integrity

Required Application Components include detailed descriptions of:
1. Planned use of funds
2. Major implementation milestones
3. Dropout prevention services
4. Coordination with facilities
5. At-risk programming
6. At-risk eligibility processes
7. Service coordination
8. Reentry programming and scheduling
9. Student characteristics
10. Social and health services coordination
11. Alternative placement procedures
12. Higher education and business partnerships
13. Family involvement
14. Coordination with federal, state, and local programs
15. IEP awareness procedures
16. Probation officer coordination
17. Data collection methods
18. WDE568 submission
19. End-of-year evaluation results
20. Monitoring and program evaluation

SECTION 19: MONITORING, DOCUMENTATION, AND PROGRAM OVERSIGHT
Under 2 CFR §200.332, pass-through entities are required to monitor subrecipients to ensure 
federal funds are used in accordance with federal statutes, regulations, and the terms and 
conditions of the award.

Monitoring may include:
- Review of grant applications and amendments
- Review of budgets and expenditures
- Review of program implementation
- Review of student eligibility and service records
- Review of staffing and personnel documentation
- Review of contracts and purchased services
- Review of data collection and reporting requirements
- Interviews with program staff, facility staff, and district leadership
- On-site observations
- Review of policies, procedures, and internal controls

Documentation LEAs Should Maintain:
- Program Design and Planning (CNA, program plans, goals, evaluation plans)
- Student Eligibility and Services (eligibility docs, participation records, service logs)
- Personnel Documentation (job descriptions, time and effort tracking, schedules)
- Fiscal Documentation (budgets, invoices, purchase orders, contracts)
- Program Evaluation Documentation (outcome data, performance data, evaluation activities)

Monitoring Questions LEAs Should Be Prepared to Answer:
- What needs were identified through the CNA?
- How were services selected?
- Which students are being served?
- How were students determined eligible?
- How do services address identified needs?
- How are funds being used?
- How is program effectiveness being measured?
- What outcomes have been achieved?
- How are program decisions informed by data?
- How are continuous improvement efforts documented?

---

END OF GUIDEBOOK CONTENT
"""

SYSTEM_PROMPT = f"""You are an expert assistant helping practitioners understand the Wyoming Department 
of Education's Title I, Part D, Subpart 2 Subgrantee Guidebook. You have access to the complete guidebook 
content below.

Your role is to:
1. Answer questions about the guidebook accurately and thoroughly
2. Cite specific sections when relevant
3. Provide practical examples when helpful
4. Clarify compliance requirements
5. Help practitioners understand allowable vs. unallowable uses of funds
6. Explain program design requirements and expectations

IMPORTANT - USE THIS HYBRID RESPONSE STRUCTURE:

**Step 1: Quick Direct Answer**
Start with a concise, direct answer (1-2 sentences) to their question.

**Step 2: Ask Clarifying Questions**
Then ask 2-3 specific clarifying questions that would help you give them the MOST accurate, 
compliance-appropriate answer for their specific situation. Format these as:
- "Question 1: [specific question about their context]"
- "Question 2: [specific question about their implementation]"
- "Question 3: [specific question about their specific situation]"

**Step 3: Offer Detailed Guidance**
After their questions, provide detailed compliance-checked guidance with citations.

GUIDELINES FOR CLARIFYING QUESTIONS:
- Make them specific to their situation (facility vs. school, staffing, costs, etc.)
- Focus on factors that affect compliance (supplemental vs. baseline, documentation, etc.)
- Help prevent mistakes by understanding their exact scenario
- Don't ask obvious questions - make them matter

EXAMPLE STRUCTURE:
Q: "Can we use funds to pay a tutor?"
A: "Yes, supplemental tutoring is allowable under Section 12. 

To make sure this fits your specific situation, I need to understand:
- Question 1: Will these tutors work with students returning from correctional facilities or at-risk students in school settings?
- Question 2: Is this tutoring supplemental (beyond what the LEA already provides) or replacing existing services?
- Question 3: How will you track and document the time spent tutoring eligible students?

Once you answer these, I can provide specific compliance guidance and documentation requirements."

GUIDEBOOK CONTENT:
{GUIDEBOOK_CONTENT}
"""


def create_chatbot():
    """Initialize and return a chatbot instance."""
    return Anthropic()


def chat_with_practitioner():
    """Main chat loop for practitioners."""
    client = create_chatbot()
    conversation_history = []
    
    print("\n" + "="*70)
    print("TITLE I, PART D, SUBPART 2 PRACTITIONER CHATBOT")
    print("Wyoming Department of Education")
    print("="*70)
    print("\nWelcome! I can help you find information about the Title I, Part D")
    print("Subpart 2 Subgrantee Guidebook. Ask me anything about:")
    print("  - Program requirements and compliance")
    print("  - Facility eligibility and counting")
    print("  - Allowable uses of funds")
    print("  - Academic services and dropout prevention")
    print("  - At-risk youth identification")
    print("  - Cost limitations and budgeting")
    print("  - Application requirements")
    print("  - Monitoring and documentation")
    print("\nType 'quit' or 'exit' to end the conversation.")
    print("Type 'help' for example questions.")
    print("="*70 + "\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
        except EOFError:
            print("\n\nChatbot: Thank you for using the Title I, Part D Chatbot. Goodbye!")
            break
        
        if not user_input:
            continue
        
        if user_input.lower() in ['quit', 'exit']:
            print("\nChatbot: Thank you for using the Title I, Part D Chatbot. Goodbye!")
            break
        
        if user_input.lower() == 'help':
            print("\nExample questions you can ask:")
            print("  - What are the cost limitations for Subpart 2 funds?")
            print("  - What makes a facility eligible for Title I Part D?")
            print("  - Can we use funds to pay a general school counselor?")
            print("  - What are the requirements for formal agreements?")
            print("  - How do we determine if a student is at-risk?")
            print("  - What academic services are allowable?")
            print("  - What is the annual count (WDE549)?")
            print("  - What are the components of an effective program?")
            print()
            continue
        
        # Add user message to conversation history
        conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        try:
            # Get response from Claude
            response = client.messages.create(
                model="claude-opus-4-6",
                max_tokens=1024,
                system=SYSTEM_PROMPT,
                messages=conversation_history
            )
            
            assistant_message = response.content[0].text
            
            # Add assistant response to conversation history
            conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            print(f"\nChatbot: {assistant_message}\n")
            
        except Exception as e:
            print(f"\nError communicating with Claude: {str(e)}")
            print("Please make sure your ANTHROPIC_API_KEY is set correctly.\n")
            # Remove the user message since we couldn't get a response
            conversation_history.pop()


def main():
    """Main entry point."""
    # Check for API key
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("\nError: ANTHROPIC_API_KEY environment variable not set.")
        print("Please set your API key before running the chatbot:")
        print("  export ANTHROPIC_API_KEY='your-key-here'")
        print("\nYou can get an API key at: https://console.anthropic.com/")
        sys.exit(1)
    
    chat_with_practitioner()


if __name__ == "__main__":
    main()
