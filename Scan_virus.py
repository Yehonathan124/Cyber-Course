import requests

def scan_file_virus_total(file_path, api_key):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': api_key}
    files = {'file': (file_path, open(file_path, 'rb'))}
    response = requests.post(url, files=files, params=params)
    if response.status_code == 200:
        result = response.json()
        return result['verbose_msg']
    else:
        return 'Failed to scan file. Status code: {}'.format(response.status_code)

def is_file_safe_virus_total(file_hash, api_key):
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': api_key, 'resource': file_hash}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        result = response.json()
        if 'positives' in result:
            if result['positives'] == 0:
                return True
            else:
                return False, result['scans']
        else:
            return 'File not found on VirusTotal database'
    else:
        return 'Failed to check file safety. Status code: {}'.format(response.status_code)

def scan_directory_virus_total(directory_path, api_key):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(f'Scanning {file_path}...')
            scan_result = scan_file_virus_total(file_path, api_key)
            print(f'Scan result: {scan_result}\n')
            
# API key for VirusTotal. Replace 'YOUR_API_KEY' with your actual API key.
API_KEY = 'YOUR_API_KEY'