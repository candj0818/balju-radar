"""balju-radar.html(claude.ai 페이지용 본문)을 GitHub Pages용 index.html로 감싼다.

claude.ai는 <!doctype>/<head>를 자동으로 붙이지만 GitHub Pages는 파일을 그대로 보여 주므로,
같은 기본값(문자셋, 모바일 화면 폭, body 여백 0, [hidden] 숨김)을 여기서 붙인다.
사용법: python build.py
"""
from pathlib import Path

here = Path(__file__).parent
src = (here / "balju-radar.html").read_text(encoding="utf-8")
head = (
    "<!doctype html>\n"
    "<!-- 자동 생성 파일: balju-radar.html을 고친 뒤 python build.py 로 다시 만드세요 -->\n"
    '<html lang="ko">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    "<style>body{margin:0}[hidden]{display:none!important}img{max-width:100%}</style>\n"
)
(here / "index.html").write_text(head + src + "\n</html>\n", encoding="utf-8", newline="\n")
print("index.html 생성 완료")
