import os
import urllib.request
import json

def load_keys(env_path):
    keys = {}
    if not os.path.exists(env_path):
        return keys
    with open(env_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                keys[k.strip()] = v.strip().strip('"').strip("'")
    return keys

def test_gemini(key):
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models?key={key}"
        with urllib.request.urlopen(url, timeout=5) as resp:
            return resp.status == 200
    except:
        return False

def test_elevenlabs(key):
    try:
        req = urllib.request.Request("https://api.elevenlabs.io/v1/user", headers={"xi-api-key": key})
        with urllib.request.urlopen(req, timeout=5) as resp:
            return resp.status == 200
    except:
        return False

def test_tavily(key):
    try:
        req_data = json.dumps({"api_key": key, "query": "test"}).encode()
        req = urllib.request.Request("https://api.tavily.com/search", data=req_data, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=5) as resp:
            return resp.status == 200
    except:
        return False

def main():
    print("==========================================")
    print("🔍 Free API Harvest Hub Key Verification")
    print("==========================================")
    
    env_path = os.path.expanduser("~/Documents/Codex/.env.all-keys")
    keys = load_keys(env_path)
    print(f"Loaded {len(keys)} keys from {env_path}\n")

    # Sample tests
    for k, v in list(keys.items())[:15]:
        status = "LOADED"
        if "GEMINI" in k:
            status = "HEALTHY (200)" if test_gemini(v) else "FAILED"
        elif "ELEVENLABS" in k:
            status = "HEALTHY (200)" if test_elevenlabs(v) else "FAILED"
        elif "TAVILY" in k:
            status = "HEALTHY (200)" if test_tavily(v) else "FAILED"
        
        print(f"• {k:<30} [{status}]")

if __name__ == "__main__":
    main()
