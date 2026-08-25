print("나만의 프롬프트 관리 프로그램")
prompts = [
    {
        "title": "로판 캐릭터 이미지 생성",
        "content": "로맨스 판타지풍의 캐릭터를 생성해주세요.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "SYNESTHESIA 광고 영상",
        "content": "소리가 빛과 예술로 변화하는 10초 광고 영상을 제작해주세요.",
        "category": "영상 생성",
        "favorite": False
    },
    {
        "title": "만족도 조사 자동화",
        "content": "설문 응답 결과를 확인하고 조건에 따라 자동으로 처리해주세요.",
        "category": "자동화",
        "favorite": False
    }
]
def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")

show_menu()
