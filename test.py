from crewai import Agent, Task, Crew

# 1. 역할별 에이전트 정의
researcher = Agent(
    role="리서처",
    goal="최신 AI 트렌드를 조사한다",
    backstory="10년 경력의 AI 리서처",
    tools=[search_tool]
)

writer = Agent(
    role="작가",
    goal="조사 결과를 블로그 글로 작성한다",
    backstory="기술 블로그 전문 작가"
)

# 2. 태스크 정의
research_task = Task(
    description="2025년 에이전트 AI 트렌드 조사",
    agent=researcher,
    expected_output="주요 트렌드 5가지 정리"
)

write_task = Task(
    description="조사 결과로 블로그 글 작성",
    agent=writer,
    expected_output="1000자 분량의 블로그 포스트"
)

# 3. 크루 실행
crew = Crew(agents=[researcher, writer], tasks=[research_task, write_task])
result = crew.kickoff()