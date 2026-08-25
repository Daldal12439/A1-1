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


def add_prompt():
    print("\n=== 프롬프트 추가 ===")

    while True:
        title = input("제목: ")
        if title:
            break
        print("제목을 입력해주세요.")

    while True:
        content = input("내용: ")
        if content:
            break
        print("내용을 입력해주세요.")

    while True:
        category = input("카테고리: ")
        if category:
            break
        print("카테고리를 입력해주세요.")

    prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(prompt)

    print("프롬프트가 추가되었습니다!")

def show_list():
    print("\n=== 프롬프트 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(prompts, start=1):
        favorite = " ⭐" if prompt["favorite"] else ""
        print(f"{i}. [{prompt['category']}] {prompt['title']}{favorite}")

    print(f"\n총 {len(prompts)}개의 프롬프트")

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

    choice = input("선택: ")

    if choice == "1":
        add_prompt()
    elif choice == "2":
        show_list()
    elif choice == "0":
        print("프로그램을 종료합니다.")


show_menu()