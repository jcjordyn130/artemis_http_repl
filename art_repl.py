import sys
import requests

def main():
    print("=== Artemis Multi-line Lua REPL ===")
    ip = input("Enter console IP address: ").strip()
    if not ip:
        print("Error: IP address cannot be empty.")
        return

    url = f"http://{ip}:8080/eval"
    print(f"Target URL set to: {url}")
    
    # --- MODIFICATION START: Initial Pointer Check ---
    print("\n--- Running Initial Native Pointer Scan... ---")
    try:
        # We execute the pointer check immediately upon startup
        # This ensures n2h is loaded and its values are available before user input starts.
        check_payload = """
            if n2h then 
                print("=== Querying Active Native Pointers ===") 
                print("Platform Check: ", n2h.platform) 
                print("Main Base Address: ", n2h.main_base) 
                print("SDK Base Address: ", n2h.sdk_base) 
            else 
                print("Error: The 'n2h' table is not found in the global space.") 
            end
        """
        # Send the check payload immediately
        response = requests.post(url, data=check_payload.encode('utf-8'), timeout=5)
        
        # Print the response from the console (the pointers)
        print("=== Initial Pointer Scan Response ===")
        print(response.text)
        print("========================================\n")

    except requests.exceptions.RequestException as e:
        print(f"Network Error during initial scan: {e}")
        print("Please ensure the console is running and accessible at the specified IP.")
        print("========================================\n")
    # --- MODIFICATION END ---


    print("\nInstructions:")
    print("1. Paste or type your multi-line Lua code.")
    print("2. To execute: Press Ctrl+D (Linux/Mac) or Ctrl+Z then Enter (Windows).")
    print("3. To exit the program entirely: Press Ctrl+C.\n")

    while True:
        try:
            print("--- Enter Lua Code ---")
            # Read all lines from standard input until EOF (Ctrl+D / Ctrl+Z)
            payload = sys.stdin.read()
            
            if not payload.strip():
                print("Empty input. Try again.")
                continue

            print("\nSending payload...")
            # Send the user's code via POST request
            response = requests.post(url, data=payload.encode('utf-8'), timeout=5)
            
            # Print the server response cleanly
            print("=== Response ===")
            print(response.text)
            print("================================\n")

        except KeyboardInterrupt:
            # Clean exit on Ctrl+C
            print("\nExiting REPL. Goodbye!")
            sys.exit(0)
        except requests.exceptions.RequestException as e:
            print(f"\nNetwork Error during execution loop: {e}")
            print("================================\n")

if __name__ == "__main__":
    main()
