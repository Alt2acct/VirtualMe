import requests
import json
import config

class SmartBrain:
    def __init__(self):
        self.provider = config.AI_PROVIDER
        self.api_key = config.AI_API_KEY

    def generate_reply(self, user_msg, context=""):
        prompt = f"""
        You are Zeek. Casual, friendly, genuine.
        CONTEXT: {context}
        USER SAID: "{user_msg}"
        
        Reply shortly (under 2 sentences). If appropriate, mention the group.
        """
        
        if self.provider == "ollama":
            # Localhost AI
            try:
                url = "http://host.docker.internal:11434/api/generate"
                payload = {"model": config.AI_MODEL_NAME, "prompt": prompt, "stream": False}
                res = requests.post(url, json=payload)
                return res.json().get('response', "Error getting AI response")
            except:
                return "Hey! I'm a bit overwhelmed right now, text you in a sec."

        elif self.provider == "groq":
            # Cloud AI (Better for Render)
            url = "https://api.groq.com/openai/v1/chat/completions"
            headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
            payload = {
                "model": "llama3-8b-8192",
                "messages": [{"role": "user", "content": prompt}]
            }
            try:
                res = requests.post(url, headers=headers, json=payload)
                return res.json()['choices'][0]['message']['content']
            except Exception as e:
                print(f"AI Error: {e}")
                return "Just saw this! Give me a moment."
        
        return "Hey! Good to hear from you."
