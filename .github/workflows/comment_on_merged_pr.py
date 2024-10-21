import os
import requests

def comment_on_pr(repo, pr_number, token):
    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "body": "🎉 This PR has been successfully merged. Thank you for your contribution!"
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 201:
        print(f"Successfully commented on PR #{pr_number}")
    else:
        print(f"Failed to comment on PR #{pr_number}: {response.status_code}, {response.text}")

if __name__ == "__main__":
    github_token = os.getenv('GITHUB_TOKEN')
    repo = os.getenv('REPO')
    pr_number = os.getenv('PR_NUMBER')

    if github_token and repo and pr_number:
        comment_on_pr(repo, pr_number, github_token)
    else:
        print("Missing environment variables!")
