class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

if __name__ == "__main__":  # thailand.py 에서 실행시켯을 때는 이문장이 실행됨
    print("Thailand 모듈을 직접 실행")
    # 이문장은 모듈을 직접 실행할 때만 실행된다
    trip_to = ThailandPackage()
    trip_to.detail()
else:   # 만약 practice에서 thailand.py를 갖다쓸때는 이문장이 실행됨
    print("Thailand 외부에서 모듈 호출")