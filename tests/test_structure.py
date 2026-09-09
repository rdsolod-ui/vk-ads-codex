from pathlib import Path
import subprocess,sys,unittest
class Structure(unittest.TestCase):
 def test_package(self):
  p=Path(__file__).resolve().parents[1]
  r=subprocess.run([sys.executable,str(p/'scripts/validate_package.py')],capture_output=True,text=True)
  self.assertEqual(r.returncode,0,r.stdout+r.stderr)
