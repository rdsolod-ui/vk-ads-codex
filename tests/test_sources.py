from pathlib import Path
import json,subprocess,sys,unittest
root=Path(__file__).resolve().parents[1]/'skills/vk-ads-codex'
class Sources(unittest.TestCase):
 def test_unique_official(self):
  a=json.loads((root/'references/sources.json').read_text(encoding='utf-8'))['sources']
  self.assertGreater(len(a),500);self.assertEqual(len(a),len({x['url'] for x in a}));self.assertTrue(all(x['url'].startswith('https://ads.vk.ru/') for x in a))
 def test_retrieval_evidence(self):
  a=json.loads((root/'references/sources.json').read_text(encoding='utf-8'))['sources'];self.assertTrue(all(x['status']=='retrieved' and len(x['text_sha256'])==64 for x in a))
 def test_lookup(self):
  r=subprocess.run([sys.executable,str(root/'scripts/find_sources.py'),'LeadForm','--limit','2'],capture_output=True,text=True);self.assertEqual(r.returncode,0);d=json.loads(r.stdout);self.assertGreater(d['matched'],2);self.assertEqual(len(d['items']),2)
