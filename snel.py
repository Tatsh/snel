from os import stat
from os.path import basename
import json
import sys

import requests

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'


def main() -> int:
    if len(sys.argv) < 2:
        print(f'Usage: {basename(sys.argv[0])} FILE')
        return 1
    print(post(sys.argv[1]))
    return 0


def post(filename: str, user_agent: str = USER_AGENT) -> str:
    size = str(stat(sys.argv[1]).st_size)
    r = requests.post('https://lens.google.com/_/upload/',
                      headers={
                          'x-client-side-image-upload': 'true',
                          'x-goog-upload-command': 'start',
                          'x-goog-upload-header-content-length': size,
                          'x-goog-upload-protocol': 'resumable',
                          'user-agent': user_agent
                      })
    r.raise_for_status()
    with open(sys.argv[1], 'rb') as f:
        r = requests.post(r.headers['X-Goog-Upload-URL'],
                          headers={
                              'x-client-side-image-upload': 'true',
                              'x-goog-upload-command': 'upload, finalize',
                              'x-goog-upload-offset': '0',
                              'user-agent': user_agent
                          },
                          data=f)
        r.raise_for_status()
        return f"https://lens.google.com{json.loads(r.text[5:])['url']}"


if __name__ == '__main__':
    sys.exit(main())
