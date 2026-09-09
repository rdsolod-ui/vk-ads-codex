"""Validate installable structure and relative Markdown links, without network."""
from pathlib import Path
import re, sys
root=Path(__file__).resolve().parents[1]
errors=[]
skills=list((root/'skills').glob('*/SKILL.md'))
if len(skills)!=1: errors.append('Expected one skill')
for p in skills:
 text=p.read_text(encoding='utf-8')
 if not text.startswith('---\n'): errors.append('Missing frontmatter')
 name=re.search(r'^name: ([a-z0-9-]+)$',text,re.M)
 if not name or name.group(1)!=p.parent.name: errors.append('Name/folder mismatch')
 if not re.search(r'^description: .+',text,re.M):errors.append('Missing description')
 if not (p.parent/'agents/openai.yaml').is_file():errors.append('Missing UI metadata')
for p in root.rglob('*.md'):
 text=p.read_text(encoding='utf-8')
 for target in re.findall(r'\]\(([^)]+)\)',text):
  if '://' in target or target.startswith('#'):continue
  if not (p.parent/target.split('#')[0]).exists():errors.append(str(p)+': missing '+target)
for p in root.rglob('*'):
 if p.is_symlink():errors.append('Symlink: '+str(p))
 if p.name=='.env':errors.append('Unexpected environment file')
print('PASS' if not errors else '\n'.join(errors))
sys.exit(bool(errors))
