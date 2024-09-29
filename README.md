# Slackbot Sample
### 이 저장소는 Slackbot을 사용하기 위한 기본 샘플 코드와 설명을 제공합니다.

이 샘플은 **Docker**를 사용하여 손쉽게 Slackbot을 배포할 수 있도록 구성되었습니다. Docker 환경을 이용하면 복잡한 설정 없이도 빠르게 Slackbot을 실행할 수 있습니다.

---

## 시작하기

### 1. **사전 준비**
- **Docker**: 먼저, [Docker](https://docs.docker.com/get-docker/)가 설치되어 있어야 합니다.
- **Slack 앱 생성**: Slack 개발자 페이지에서 Slack 앱을 생성하고 **Bot Token**과 **App Token**을 발급받아야 합니다.
  
  - **Bot Token**: `xoxb-`로 시작하는 토큰
  - **App Token**: `xapp-1`로 시작하는 토큰

  Slack 앱을 생성하고 토큰을 발급받는 방법에 대해서는 [Slack API 문서](https://api.slack.com/authentication/basics)를 참조하세요.

### 2. **소스 내려받기**
1. Git을 사용하여 저장소를 클론합니다:
   ```bash
   git clone https://github.com/kimkitae/slackbot-sample.git
   ```
   
2. 클론한 저장소 디렉토리로 이동합니다:
   ```bash
   cd slackbot-sample
   ```

### 3. **환경 설정**
1. `docker-compose.yml` 파일을 열어 **SLACK_BOT_TOKEN**과 **APP_TOKEN** 값을 입력합니다.
   ```yaml
   environment:
     - SLACK_BOT_TOKEN=xoxb-your-bot-token
     - APP_TOKEN=xapp-your-app-token
   ```
   - **SLACK_BOT_TOKEN**: `xoxb-`로 시작하는 봇 토큰
   - **APP_TOKEN**: `xapp-1`로 시작하는 앱 토큰

2. 저장 후 파일을 닫습니다.

---

## Docker를 통한 Slackbot 구동

### 1. **이미지 빌드**
Slackbot을 Docker 이미지로 빌드합니다. 해당 명령어를 실행하여 이미지를 생성합니다:
```bash
docker build -t slackbot .
```

### 2. **컨테이너 실행**
이미지가 빌드된 후, 아래 명령어로 컨테이너를 실행합니다:
```bash
docker-compose up -d
```
- `-d` 옵션은 컨테이너를 백그라운드에서 실행시킵니다.
- 실행 후, 컨테이너가 정상적으로 구동되었는지 확인하려면 `docker ps` 명령어로 컨테이너 상태를 확인하세요.

---

## 문제 해결 (Troubleshooting)

### 1. **로그 확인**
만약 Slackbot이 정상적으로 작동하지 않는다면, 다음 명령어로 컨테이너 로그를 확인하여 원인을 파악할 수 있습니다:
```bash
docker logs slackbot
```

### 2. **토큰 오류**
- **SLACK_BOT_TOKEN** 또는 **APP_TOKEN**이 올바르지 않으면 Slack에서 봇이 제대로 작동하지 않습니다. Slack API 페이지에서 정확한 토큰을 확인하고 다시 입력하세요.

### 3. **포트 충돌**
기본적으로 사용되는 포트가 다른 애플리케이션과 충돌하는 경우, `docker-compose.yml` 파일 내에서 포트를 수정하여 문제를 해결할 수 있습니다.

---

## 참고 링크
- [Slack API 문서](https://api.slack.com/)
- [Docker 공식 문서](https://docs.docker.com/)

---

이 설명서를 참고하여 Slackbot을 빠르고 쉽게 실행할 수 있습니다. 질문이 있거나 문제가 발생한 경우 GitHub 이슈를 통해 문의해 주세요.

---
