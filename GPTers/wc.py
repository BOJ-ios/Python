from wordcloud import WordCloud
import matplotlib.pyplot as plt

font_path = "C:/Users/LoewllZoe/Downloads/NanumGothicBold.ttf"

# Input your article text here
article = """
LG CNS가 미래의 DX 전문가로 성장해 나갈 인재를 확보하기 위해 세 자릿수 규모의 하반기 신입사원 채용을 시작했다고 11일 밝혔다.

이번 채용은 ▲인공지능(AI) ▲데이터 ▲클라우드 애플리케이션 현대화(AM) ▲클라우드 아키텍처 ▲스마트 물류 ▲컨설팅 ▲DX 엔지니어 총 7개 분야를 모집한다.

AI 분야는 머신러닝, 딥러닝, 생성형 AI 등의 기술을 연구개발하고 고객사에 제공할 AI 모델과 서비스를 설계, 구축, 운영하는 역할을 수행한다.


상반기 LG CNS 신입사원(이미지=LG CNS)

초거대 AI 기반의 대규모언어모델(LLM) 튜닝, 이미지 생성형 AI 모델 개발 업무도 진행하게 된다. 데이터 분야는 금융, 제조, 물류, 유통 등 여러 산업 분야에서 발생하는 핵심 데이터를 분석하고, 고객 비즈니스에 가치 있는 서비스를 만들어낼 수 있다.

클라우드 AM은 기존 방식으로 개발된 애플리케이션을 미래 비즈니스 목적에 맞게 최신 클라우드 기술을 통해 재구성하는 역할을 담당한다.

클라우드 아키텍처는 건축물의 뼈대와 같이 클라우드 환경 내 시스템을 구성하고 있는 소프트웨어, 네트워크, 서버 등 기본 구성요소를 설계, 구축하는 분야다. LG CNS 아키텍처 조직은 코로나19 펜데믹 당시 EBS 온라인 강의, 백신예약 시스템 등 대국민 IT서비스 개선 작업을 주도하기도 했다.

스마트 물류는 고객사 물류센터에 AI, 데이터 등 DX 기술을 접목해 디지털 물류센터로의 전환 업무를 수행하는 곳이다. LG CNS는 SSG, 쿠팡, 마켓컬리 등 고객사의 디지털 물류센터를 구축해 운영하고 있다.

컨설팅은 고객 페인포인트, 시장 전망 등의 환경을 분석해 고객사의 DX와 신규 비즈니스 전략을 수립하는 역할이다. LG CNS는 컨설팅 전문조직 ‘엔트루(Entue)’를 운영하고 있다. DX 엔지니어는 디지털 금융, 스마트시티, 스마트팩토리 등 분야에서 시스템과 솔루션을 구축, 운영하게 된다.

이번 신입사원 채용은 전공 무관이며, DX 전문가로 성장을 원하는 대졸자, 대졸예정자라면 누구나 지원 가능하다. 컴퓨터공학, 정보통신공학, 산업공학, 통계학 등 이공계열 전공자와 코딩 동아리 활동, 앱 개발 경험 등 IT 역량을 보유한 지원자는 우대한다.

채용 절차는 서류전형, 필기전형, 실무면접, 최종면접 순으로 진행된다. 서류 접수는 이번 달 19일 까지며, 추후 일정은 서류전형 결과 발표 후 안내할 예정이다.

LG CNS는 최종 합격자들을 대상으로 8주간 각자의 직무, 역량에 맞는 ‘신입사원 맞춤형 DX 커리어’ 교육을 제공한다. 신입사원이 DX 전문가로서의 장기 로드맵을 그려 나갈 수 있도록 지속 투자하고 있다. 기술, 어학, 인문 등 다양한 분야의 4천 개가 넘는 온라인 교육 콘텐츠를 보유해 직원들을 육성하고 있으며 클라우드, AI 등 자격증 응시료도 지원한다.

입사 후 일정 기간이 지나면 가고 싶은 팀을 스스로 선택할 수 있는 경력개발 프로그램 ‘마이 커리어 업(MCU)’를 운영 중이다. 2021년 9월부터 시작했던 MCU에는 현재까지 약 1천150명이 지원해 약 650명이 원하는 팀에 합격했다.

지원자는 현재 속해 있는 조직의 리더와 합의하지 않더라도 합격 후 2개월 내 조직 이동이 완료되며, 최종 합격시까지 비밀이 보장된다.

LG CNS는 DX 역량이 뛰어나면 인정하고 높은 급여를 제공하는 ‘역량중심’ 문화가 자리잡고 있다. 연공서열 중심에서 역량서열 중심으로 보상구조를 빠르게 전환했다. 역량레벨은 평가에 따라 1부터 최고 5까지 나눠진다. 레벨4 이상 직원들은 추가 테스트를 통해 ▲포텐셜 엑스퍼트 ▲엑스퍼트 ▲마이스터 ▲연구/전문위원 등 4단계로 구성된 전문가에 선발돼 추가 수당을 받을 수 있다.

역량이 상승해 높은 레벨을 획득한 사원, 선임(대리)급은 나이와 직급에 상관없이 더 많은 보상을 받을 수 있도록 고정급을 추가 인상해주는 ‘패스트 트랙(Fast Track)’ 제도를 시행 중이다.

LG CNS는 역량중심 공정채용, 역량중심 임금체계 개편 등의 활동을 높게 평가받아 지난 4일 고용노동부에서 선정하는 ‘2023 대한민국 일자리 으뜸기업’에 선정되기도 했다.

LG CNS는 이번 세 자릿수 규모 채용을 완료하고 나면, 전체 임직원 수 7,000명을 돌파할 예정이다. LG CNS는 어려운 시장상황 속에서도 DX 인재 확보와 육성을 위해 올해만도 500여명의 직원을 신규 채용했다. 인재 확보와 육성은 성과로 이어지며, 2018년부터 5년 연속 연간 매출액 최고기록을 경신했다.

LG CNS 신입사원 채용 ‘DX 리더십 아카데미’ 대한 자세한 내용은 LG CNS 채용사이트와 LG그룹 채용사이트에서 확인할 수 있다.

LG CNS 인사담당 고영목 상무는 “AI, 클라우드, 스마트 물류 등 DX 신기술 영역에서 우수한 인재들을 확보해, 고객사의 비즈니스 가치를 더욱 혁신해 나가겠다”고 강조했다.
"""

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white',
                      font_path=font_path).generate(article)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
