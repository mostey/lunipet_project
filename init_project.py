"""
이 파일은 루니펫 프로젝트를 처음 실행할 때 필요한 모든 환경을 자동으로 구성하는 스크립트임
- OS 종류 자동 인식 (Windows / Linux / macOS)
- Python 버전 확인 (최소 3.10.9 이상)
- 가상환경 생성 (venv 폴더)
- requirements.txt에 정의된 라이브러리 자동 설치

사용자는 단 한 번만 python init_project.py를 실행하면 모든 개발 환경이 구성됨
"""

import os
import platform
import subprocess
import sys

# 프로젝트에 필요한 최소 Python 버전 정의
REQUIRED_PYTHON = (3, 10, 9)

def check_python_version():
    """
    현재 실행 중인 Python 버전이 최소 요구 사항을 만족하는지 확인함
    """
    current = sys.version_info
    required_str = ".".join(map(str, REQUIRED_PYTHON))

    if current < REQUIRED_PYTHON:
        print(f"! Python {required_str} 이상이 필요함. 현재 버전: {platform.python_version()}")
        sys.exit(1)
    else:
        print(f"Python 버전 확인 완료: {platform.python_version()}")

def create_venv():
    """
    venv 디렉토리가 없다면 가상환경을 새로 생성함
    """
    if os.path.exists("venv"):
        print("가상환경 이미 존재함 (venv/)")
    else:
        print("가상환경 생성 중...")
        subprocess.run([sys.executable, "-m", "venv", "venv"])
        print("가상환경 생성 완료")

def install_requirements():
    """
    생성된 가상환경 내에서 필요한 패키지를 requirements.txt 기반으로 설치함
    OS 종류에 따라 pip 경로가 다름
    """
    pip_exe = (
        "venv\\Scripts\\pip.exe" if os.name == "nt"  # Windows
        else "./venv/bin/pip"                        # macOS/Linux
    )

    print("requirements.txt 기반 패키지 설치 중...")
    subprocess.run([pip_exe, "install", "--upgrade", "pip"])
    subprocess.run([pip_exe, "install", "-r", "requirements.txt"])
    print("패키지 설치 완료")

def activate_info():
    """
    가상환경을 수동으로 활성화하고 싶은 사용자를 위한 안내 문구 출력
    """
    if os.name == "nt":
        activate_cmd = "venv\\Scripts\\activate"
    else:
        activate_cmd = "source ./venv/bin/activate"

    print("\n수동으로 가상환경을 활성화하려면 아래 명령어 사용:")
    print(f"• {activate_cmd}\n")

def main():
    print("루니펫 프로젝트 초기 환경 구성 자동 실행 시작")

    check_python_version()     # Python 버전 확인
    create_venv()              # 가상환경 생성
    install_requirements()     # 라이브러리 설치
    activate_info()            # 활성화 안내

    print("모든 준비 완료됨! 이제 run_create.py 또는 run_tests.py를 실행하면 됨.")

# 이 파일이 단독 실행될 때만 main() 함수 호출됨
if __name__ == "__main__":
    main()