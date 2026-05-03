================================================================
Project Stem: Self-Differentiating AI Agent
Applicant: Alexandru Racovita
Position: AI Engineer Intern
================================================================

OVERVIEW
This project demonstrates a "Stem Cell" AI agent that dynamically generates, tests, and assimilates its own Python tools based on a given task environment before executing it. It includes a built-in "Safeguard" feedback loop to handle LLM hallucinations and execution errors.

PREREQUISITES
- Python 3.8 or higher
- An active OpenAI API Key

SETUP INSTRUCTIONS
1. Clone this repository or download it to your local machine.
2. Open a terminal or command prompt inside that project folder.
3. Install the required Python libraries by running:
   `pip install openai pandas`

CONFIGURATION
1. Open the file `stem_agent.py` in your code editor.
2. Scroll to the very bottom of the file (in the "Testing Area" section).
3. Replace the placeholder string with your actual OpenAI API key:
   api_key = "YOUR_API_KEY_HERE"

HOW TO RUN
1. In the terminal, ensure you are in the project directory.
2. Run the main script by typing:
   python stem_agent.py
3. Watch the terminal output. You will see the agent sense the task, attempt to generate its tools, pass them through the Safeguard for testing, and finally execute the data cleaning task on the provided `sales.csv` file.

FILE STRUCTURE
- stem_agent.py : The core engine, handling the prompt engineering and the evolution loop.
- safeguard.py  : The dynamic execution environment that isolates, tests, and validates the generated code.
- sales.csv     : A purposefully messy dataset used to test the matured agent's data-cleaning capabilities.
- write-up.pdf  : The detailed 4-page explanation of the architecture, experiments, and failure handling.