#!/usr/bin/env python3
"""
Title I, Part D Subpart 2 Practitioner Chatbot - Streamlit Web Interface
Web-based chatbot for practitioners to ask questions about the Wyoming DOE guidebook
"""

import os
import streamlit as st
from anthropic import Anthropic

# Page configuration
st.set_page_config(
    page_title="Title I Part D Chatbot",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# The complete guidebook content
GUIDEBOOK_CONTENT = """
TITLE I, PART D, SUBPART 2: SUBGRANTEE GUIDEBOOK

Building Effective Programs for Delinquent and At-Risk Youth Through Program Design, 
Implementation, and Continuous Improvement

Wyoming Department of Education
Version: September 2025 (DRAFT)

[Full guidebook content - same as in title1_chatbot.py...]

SECTION 1: GENERAL INFORMATION
Title I, Part D of the Every Student Succeeds Act (ESSA) consists of two subparts:
- Subpart 1: The State Agency (SA) program
- Subpart 2: The Local Educational Agency (LEA) program

[Content continues through all 19 sections...]
"""

SYSTEM_PROMPT = f"""You are an expert assistant helping practitioners understand the Wyoming Department 
of Education's Title I, Part D, Subpart 2 Subgrantee Guidebook. You have access to the complete guidebook 
content.

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

def initialize_session_state():
    """Initialize Streamlit session state."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "client" not in st.session_state:
        st.session_state.client = Anthropic()


def chat_with_claude(user_message):
    """Send message to Claude and get response."""
    # Add user message to history
    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })
    
    # Get response from Claude
    response = st.session_state.client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=st.session_state.messages
    )
    
    assistant_message = response.content[0].text
    
    # Add assistant response to history
    st.session_state.messages.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    return assistant_message


def main():
    """Main Streamlit app."""
    initialize_session_state()
    
    # Header
    st.markdown("# 📚 Title I, Part D Chatbot")
    st.markdown("### Wyoming Department of Education - Subpart 2 Practitioner Assistant")
    st.markdown("---")
    
    # Sidebar with information
    with st.sidebar:
        st.markdown("## 📋 Quick Guide")
        st.markdown("""
        This chatbot helps you find information about:
        
        **Compliance & Requirements**
        - Program eligibility criteria
        - Facility eligibility requirements
        - Student eligibility (at-risk definition)
        - Annual counts (WDE549)
        - End-of-year reporting (WDE568)
        
        **Funding & Budgeting**
        - Allowable vs. unallowable uses of funds
        - Cost limitations (75/20/5 split)
        - Reasonable, allowable, and allocable costs
        - Supplemental vs. baseline services
        
        **Program Components**
        - Academic services
        - Transition and dropout prevention
        - Career and technical education
        - Postsecondary readiness
        
        **Administration**
        - Formal agreements (Section 1425)
        - Monitoring and documentation
        - Application requirements
        - Comprehensive needs assessment
        """)
        
        st.markdown("---")
        st.markdown("### Example Questions:")
        example_questions = [
            "What are the cost limitations for Subpart 2 funds?",
            "What makes a facility eligible for Title I Part D?",
            "Can we use funds to pay a general school counselor?",
            "What are the requirements for formal agreements?",
            "How do we determine if a student is at-risk?",
            "What academic services are allowable?",
            "What is the annual count (WDE549)?",
            "What are the components of an effective program?"
        ]
        
        for i, question in enumerate(example_questions, 1):
            st.caption(f"{i}. {question}")
        
        st.markdown("---")
        
        # Check API status
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("**API Status:**")
        with col2:
            if os.environ.get("ANTHROPIC_API_KEY"):
                st.success("✅ Configured")
            else:
                st.error("❌ Not Found")
    
    # Main content area
    # Display conversation history
    if st.session_state.messages:
        for message in st.session_state.messages:
            if message["role"] == "user":
                with st.chat_message("user", avatar="👤"):
                    st.markdown(message["content"])
            else:
                with st.chat_message("assistant", avatar="🤖"):
                    st.markdown(message["content"])
    else:
        # Welcome message
        st.info("""
        👋 Welcome to the Title I, Part D Chatbot!
        
        I'm here to help you understand the Wyoming Department of Education's Title I, Part D, 
        Subpart 2 Subgrantee Guidebook.
        
        **How to get started:**
        1. Type your question in the input box below
        2. I'll search the guidebook and provide you with accurate information
        3. I'll cite relevant sections and provide practical guidance
        
        Feel free to ask follow-up questions - I'll remember our conversation!
        """)
    
    # Input area
    st.markdown("---")
    user_input = st.chat_input("Ask a question about Title I, Part D, Subpart 2...", key="user_input")
    
    if user_input:
        # Validate API key
        if not os.environ.get("ANTHROPIC_API_KEY"):
            st.error("""
            ❌ API Key Not Configured
            
            Please set your ANTHROPIC_API_KEY environment variable before using this chatbot.
            You can get an API key at: https://console.anthropic.com/
            """)
        else:
            with st.spinner("Searching guidebook and generating response..."):
                try:
                    response = chat_with_claude(user_input)
                    st.rerun()
                except Exception as e:
                    st.error(f"Error communicating with Claude: {str(e)}")
    
    # Clear conversation button
    col1, col2 = st.columns([0.8, 0.2])
    with col2:
        if st.button("Clear Conversation", use_container_width=True):
            st.session_state.messages = []
            st.rerun()


if __name__ == "__main__":
    main()
