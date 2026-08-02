from config import config_manager
import getpass

def setup():
    print("--- SOC Engine Production Setup ---")
    vt_key = input("Enter VirusTotal API Key: ")
    abuse_key = input("Enter AbuseIPDB API Key: ")
    
    config_manager.save_api_key("virustotal", vt_key)
    config_manager.save_api_key("abuseipdb", abuse_key)
    
    print("\n[+] Configuration encrypted and saved successfully.")
    print("[+] Run 'python main.py' to start the dashboard.")

if __name__ == "__main__":
    setup()
