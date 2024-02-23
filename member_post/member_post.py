import hashlib


class Member:

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f"이름: {self.name}, ID: {self.username}")


class Post:

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


members = []
posts = []
members_username = []  # 회원 ID만 따로 저장

# 숫자 제한 없이 회원 추가
while 1:
    name = input("이름을 입력해주세요: ").strip()
    username = input("ID를 입력해주세요: ").strip()
    if username in members_username:
        print("해당 ID는 사용중입니다. 다른 ID를 사용해주세요.")
        continue
    password = input("패스워드를 입력해주세요: ").strip()
    password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()

    members.append(Member(name, username, password_hash))
    members_username.append(username)

    if input("회원을 계속 추가하시겠습니까? (y/n): ").lower() == "y":
        print()  # 프롬프트에서 가독성을 위해 사용
        continue
    else:
        break
print()

# 숫자 제한 없이 게시물 추가
while 1:
    title = input("게시글 제목을 입력해주세요: ").strip()
    content = input("게시글 내용을 입력해주세요: ").strip()
    author = input("게시글 작성자를 입력해주세요: ").strip()

    if author in members_username:
        posts.append(Post(title, content, author))
    else:
        print("해당 ID를 가진 회원이 존재하지 않습니다. ID를 다시 확인해주세요.")
        continue

    if input("게시물을 계속 추가하시겠습니까? (y/n): ").lower() == "y":
        print()
        continue
    else:
        break
print()

# 전체 회원의 이름 출력
print(f"회원 리스트(총 인원: {len(members)}명)")
for member in members:
    member.display()
print()

# 특정 유저의 게시물 검색
while 1:
    cnt = 0
    list_num = 1
    search_username_post = input("검색하고 싶은 ID를 입력하세요: ")
    if search_username_post in members_username:
        for post in posts:
            if post.author == search_username_post:
                print(f"{list_num} {post.title}")
                list_num += 1
                cnt += 1
        if cnt == 0:
            print("해당 회원님이 작성한 게시물이 존재하지 않습니다.")
    else:
        print("해당 ID를 가진 회원이 존재하지 않습니다.")

    if input("ID 검색을 계속 하시겠습니까? (y/n): ").lower() == "y":
        print()
        continue
    else:
        break
print()

# 특정 단어가 포함된 게시물 검색
while 1:
    cnt = 0
    list_num = 1
    search_word = input("검색하고 싶은 단어를 입력하세요: ")
    for post in posts:
        if search_word in post.content:
            print(f"{list_num} {post.title}")
            list_num += 1
            cnt += 1

    if cnt == 0:
        print("해당 단어를 포함하는 게시물이 존재하지 않습니다.")

    if input("단어 검색을 계속 하시겠습니까? (y/n): ").lower() == "y":
        print()
        continue
    else:
        break
