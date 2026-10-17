import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from openai import api_key

def load_config():
    load_dotenv()
    
    # Fallback to .env.example if missing
    if not os.getenv("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY") == "":
        load_dotenv(".env.example", override=True)
        
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing GEMINI_API_KEY. Put it in a .env file or export it in your terminal.")
        
    # We use the current lite model string
    model_name = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")    
    return api_key, model_name

def main():
    api_key, model_name = load_config()
    
    # 1. Initialize the LangChain model
    llm = ChatGoogleGenerativeAI(
        model=model_name,
        api_key=api_key,
        # 'thinking_budget=0' turns off the hidden reasoning step 
        # for Flash-Lite to make it as fast and cheap as possible.
    )

    # 2. LangChain uses native objects (HumanMessage, AIMessage) for history
    history = []
    print("Gemini chat started. Type 'exit' to quit.\n")

    while True:
        user_text = input("You: ").strip()
        if not user_text:
            continue

        if user_text.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
            
        # Append the user's message to our history list
        history.append(HumanMessage(content=user_text))
        
        try:
            # 3. Pass the entire history to the model
            # LangChain automatically formats this into the correct JSON payload
            response = llm.invoke(history)
            # Extract plain text whether response.content is a string or a list of blocks
            if isinstance(response.content, str):
                reply = response.content
            elif isinstance(response.content, list):
                reply = "".join(
                    block["text"] for block in response.content 
                    if isinstance(block, dict) and "text" in block
                )
            
            print(f"Gemini: {reply}\n")
            
            # Append the AI's response to keep the conversation going
            history.append(AIMessage(content=reply))
            
        except Exception as exc:
            print(f"Error: {exc}")
            # If the API call fails, remove the last user message so they can try again
            history.pop()

if __name__ == "__main__":
    main()