
import requests  

searchurl = 'https://www.baidu.com'

githuburl = 'https://api.github.com/repos/requests/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad';
r = requests.get(githuburl);

if (r.status_code == requests.codes.all_ok):
    print (r.headers['content-type'])
commit_data = r.json()
print(commit_data)
print(commit_data.keys())
print("\n")
print(commit_data.values())


verbs = requests.options(r.url)
print(verbs)
print(verbs.status_code)

verbs1 = requests.options('http://a-good-website.com/api/cats')
print(verbs1.headers['Server'])

print("test")
    