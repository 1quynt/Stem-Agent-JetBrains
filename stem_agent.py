import os
import json
from openai import OpenAI
from safeguard import Safeguard

class StemCell:
    def __init__(self, api_key=None):
        self.client = OpenAI(api_key=api_key or os.environ.get("OPENAI_API_KEY"))
        self.model = "gpt-4o"
        self.safeguard = Safeguard() 

    def differentiate(self, task_environment, max_retries=3):
        print(f"🔬 [Stem Cell] Sensing environment: {task_environment}")
        print("🧬 [Stem Cell] Starting differentiation process...")

        system_prompt = """
        You are a Stem Cell AI. You must differentiate into a highly specialized AI agent based on the given task.
        
        You MUST respond in raw JSON format with exactly this structure:
        {
            "agent_name": "Name of the agent",
            "system_prompt": "Instructions for the agent on how to use its tools",
            "tool_code": "Valid Python code. MUST include all imports. DO NOT wrap code in a class! Write ONLY standalone functions."
        }
        """

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"ENVIRONMENT/TASK:\n{task_environment}"}
        ]

        attempt = 1
        while attempt <= max_retries:
            print(f"🔄 [Evolution Loop] Attempt {attempt} of {max_retries}...")
            
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    response_format={"type": "json_object"}
                )
                
                differentiation_data = json.loads(response.choices[0].message.content)
                tool_code = differentiation_data['tool_code']
                
                # pass the code to safeguard for testing
                is_valid, feedback = self.safeguard.test_and_assimilate(tool_code)
                
                if is_valid:
                    print(f"✅ [Stem Cell] Differentiated into: {differentiation_data['agent_name']}")
                    return differentiation_data, self.safeguard.validated_tools
                else:
                    print("⚠️ [Stem Cell] Genetic mutation failed. Sending error feedback to rebuild...")
                    print(f"   -> Error detected: {feedback.splitlines()[-1]}") 
                    
                    messages.append({"role": "assistant", "content": response.choices[0].message.content})
                    messages.append({
                        "role": "user", 
                        "content": f"Your generated 'tool_code' failed during execution with this error:\n{feedback}\nPlease fix the code. Do NOT use markdown blocks like ```python. Just output raw code."
                    })
                    attempt += 1

            except Exception as e:
                print(f"❌ API Error: {e}")
                return None, None
                
        print("❌ [Stem Cell] Exhausted all evolution attempts. Cell died.")
        return None, None

# Test area
if __name__ == "__main__":
    api_key = "YOUR_API_KEY_HERE"
    stem = StemCell(api_key=api_key)
    task = "Read a messy CSV file named 'sales.csv' containing columns 'Date', 'Product', and 'Revenue'. Clean missing or non-numeric values in 'Revenue', and calculate the total sum of the revenue."
    data, tools = stem.differentiate(task)
    if data:
        print("\nFinal JSON result")
        print(json.dumps(data, indent=4))
        
        print("\nTools(Safeguard)")
        print(tools.keys())
        
        print(f"\n🚀Final phase: exec with agent {data['agent_name']}!")
        tool_function = None
        for key, val in tools.items():
            if callable(val):
                tool_function = val
                break
                
        if tool_function:
            print(f"Exec tool: {tool_function.__name__} on 'sales.csv'...")
            try:
                rezultat = tool_function("sales.csv")
                print(f"\nSUCCESSFULL: result calculated by the agent is: {rezultat} $")
            except Exception as e:
                print(f"Error on exec of function {e}")