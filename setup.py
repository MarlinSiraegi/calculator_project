from setuptools import setup, find_packages

setup(
    name="calculator",  # 패키지 이름
    version="0.1.0",  # 현재 패키지 버전
    packages=find_packages(),  # 패키지 자동 탐색
    author="MarlinSiraegi",  # 저작자 이름
    author_email="shun2959@gmail.com",  # 저작자 이메일
    description="A basic and engineering calculator package",  # 짧은 패키지 설명
    long_description=open('README.md').read(),  # 상세 패키지 설명 (README.md 파일 내용)
    long_description_content_type='text/markdown',  # README 형식 지정
    license="Apache License 2.0",  # 라이선스 종류
    url="https://github.com/MarlinSiraegi/calculator_project",  # 프로젝트 URL (GitHub URL 등)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],  # 필요한 외부 패키지 (예: ["numpy", "pandas"] 등)
    python_requires='>=3.6',  # 패키지를 설치할 수 있는 최소 Python 버전
)