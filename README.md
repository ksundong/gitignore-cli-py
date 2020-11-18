# gitignore cli python(giig)

## milestone

- [x] gitignore api 호출해서 gitignore 출력
- [x] gitignore api 호출해서 `.gitignore` 파일 생성
- [x] 검색 기능
- [x] 리스트 출력 기능
- [ ] default 추가 기능

## installation

```shell
git clone https://github.com/ksundong/gitignore-cli-py.git
python3 setup.py install
```

또는

```shell
pip3 install giigd
```

## update

```
pip3 install giigd --upgrade
```

## how to use

`giig [-h|--help]`로 도움말을 볼 수 있습니다.

```shell script
$ giig --help
Usage: giig [OPTIONS] COMMAND [ARGS]...

Options:
  -v, --version  Show version
  -h, --help     Show this message and exit.

Commands:
  list    Show a list of the ignorable items
  make    Make .gitignore
  search  Fuzzy search in ignorable items
  show    Show api results
```

### option

- `-h`, `--help` 옵션은 도움말을 보여줍니다.
- `-v`, `--help` 옵션을 사용하면 버전을 알 수 있습니다.

### command

#### list

이 커맨드는 gitignore.io의 적용가능한 목록들을 불러옵니다. (출력 엄청 많음)

#### search

이 커맨드는 검색 키워드(1개)를 인자로 받아 관련성이 높은 item들을 보여줍니다. 

```shell
$ giig search py
Finding... py
['jupyternotebooks', 'pycharm', 'pycharm+all', 'pycharm+iml', 'pydev']
```

#### show

이 커맨드는 인자로 item들을 받아서 터미널에 내용을 출력해줍니다.

```shell
$ giig show java

# Created by https://www.toptal.com/developers/gitignore/api/java
# Edit at https://www.toptal.com/developers/gitignore?templates=java

### Java ###
# Compiled class file
*.class

# Log file
*.log

# BlueJ files
*.ctxt

# Mobile Tools for Java (J2ME)
.mtj.tmp/

# Package Files #
*.jar
*.war
*.nar
*.ear
*.zip
*.tar.gz
*.rar

# virtual machine crash logs, see http://www.java.com/en/download/help/error_hotspot.xml
hs_err_pid*

# End of https://www.toptal.com/developers/gitignore/api/java

```

#### make

이 커맨드는 인자로 item들을 받아서 `.gitignore` 파일을 만들어줍니다.

```shell
$ giig make macos kotlin intellij
Making... ['macos', 'kotlin', 'intellij']
Done!! ['macos', 'kotlin', 'intellij']
```

##### make option

`-a` 로 기존 파일에 덧붙일 수 있습니다.
