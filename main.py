import os
import asyncio
from slack_bolt.async_app import AsyncApp
from slack_bolt.adapter.socket_mode.aiohttp import AsyncSocketModeHandler

# 비동기 Slack 앱
app = AsyncApp(token=os.getenv("SLACK_BOT_TOKEN"))

# 'app_mention' 이벤트를 처리하는 비동기 핸들러
@app.event("app_mention")
async def handle_app_mention(event, say):
    await say(f"Hello, <@{event['user']}>!")  # 비동기 핸들러에서는 await 사용


# 비동기 SocketModeHandler 시작
async def main():
    handler = AsyncSocketModeHandler(app, os.getenv("APP_TOKEN"))
    await handler.start_async()

if __name__ == "__main__":
    asyncio.run(main())  # 비동기 메인 함수 실행
