import requests
import json
import time
import sys
import os

API_URL = "http://localhost:8000/api/v1"

def wait_for_server(retries=10, delay=2):
    print("Waiting for server...")
    for i in range(retries):
        try:
            resp = requests.get("http://localhost:8000/")
            if resp.status_code == 200:
                print("Server is up!")
                return True
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(delay)
    print("Server failed to start.")
    return False

def test_parse_resume(file_path):
    url = f"{API_URL}/parse"
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, "rb") as f:
        files = {"file": (os.path.basename(file_path), f, "application/pdf")}
        response = requests.post(url, files=files)
        
    if response.status_code == 200:
        print("\n[SUCCESS] Parse Result:")
        print(json.dumps(response.json(), indent=2))
        return response.json()
    else:
        print(f"\n[ERROR] Parse failed: {response.text}")
        return None

def test_match_job(resume_text):
    url = f"{API_URL}/match"
    job_description = """
    We are looking for a Senior Python Developer with experience in FastAPI, SpaCy, and React.
    Must know PostgreSQL and Docker.
    3+ years of experience required.
    """
    
    data = {"resume_text": resume_text, "job_description": job_description}
    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        print("\n[SUCCESS] Match Result:")
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"\n[ERROR] Match failed: {response.text}")

if __name__ == "__main__":
    if not wait_for_server():
        sys.exit(1)
        
    # Create a dummy PDF if no arg provided
    target_file = "dummy_resume.pdf"
    if len(sys.argv) > 1:
        target_file = sys.argv[1]
    
    # We can't easily create a valid PDF purely in python without libraries installed in THIS environment
    # So we assume the user provides a path or we manually test after server start
    print(f"Testing with file: {target_file}")
    if os.path.exists(target_file):
        result = test_parse_resume(target_file)
        if result:
            test_match_job(result.get("text", ""))
    else:
        print("Please provide a valid PDF path to test.")
