import traceback

class Safeguard:
    def __init__(self):
        self.validated_tools = {}

    def test_and_assimilate(self, tool_code):
        print("🛡️ [Safeguard] Testing newly generated DNA (tools)...")
        clean_code = tool_code.replace("```python", "").replace("```", "").strip()
        namespace = {}
        
        try:
            exec(clean_code, namespace)
            self.validated_tools.update(namespace)
            
            print("🛡️ [Safeguard] DNA verified successfully. Tools assimilated.")
            return True, "Success"
            
        except Exception as e:
            error_message = traceback.format_exc()
            return False, error_message