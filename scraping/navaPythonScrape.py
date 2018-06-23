import requests
import json
import subprocess
 
 
def execute(cmd):
  popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
  for stdout_line in iter(popen.stdout.readline, ""):
    yield stdout_line
  popen.stdout.close()
  return_code = popen.wait()
  if return_code:
    raise subprocess.CalledProcessError(return_code, cmd)
 
baseUrl = "https://nava.hu"
videoId = "3187894"
with requests.session() as s:
  s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'})
  r = s.get("{}/id/{}".format(baseUrl, videoId))
 
  # get m3u base path
  patternForOptions = 'var jwPlayerOptions = '
  patternIndex = r.text.index(patternForOptions)
  nextSemicolonIndex = r.text.index(';', patternIndex + 1)
  optionsJson = r.text[patternIndex + len(patternForOptions): nextSemicolonIndex]
  options = json.loads(optionsJson)
  m3uPath = options['file']
 
  # get rest of the m3u path
  playerTokenData = {
      'prefix': "2",
      'token': '',
      'vid': videoId,
      'm': 'NDYuMTM5LjIzNi4xOTc='
  }
  r = s.post('{}/wp-content/plugins/hms-nava/interface/getPlayerToken.php'.format(baseUrl), data=playerTokenData)
  responseData = json.loads(r.text)
  m3uPath += responseData['vid'] + '?type=m3u8&sessid=' + responseData['token']
  print(m3uPath)
  for path in execute(["ffmpeg", "-i", m3uPath, "-c", "copy", "-bsf:a", "aac_adtstoasc", "{}.mp4".format(videoId)]):
    print(path, end="")
  print("Success.")
  