import requests

def get_user_input():
    """사용자로부터 입력을 받는 함수"""
    try:
        possession = int(input("Ball Possession: "))
        shootHeading = int(input("Shoot Heading: "))
        goalInPenalty = int(input("Goals in Penalty: "))
        goalHeading = int(input("Goals Heading: "))
        goalTotal = int(input("Total Goals: "))
        bouncingLobPassSuccess = int(input("Bouncing Lob Pass Success: "))
        goalTotalDisplay = int(input("Goal Total Display: "))
        bouncingLobPassTry = int(input("Bouncing Lob Pass Try: "))
        current_rank = int(input("Current Rank: "))
        
        return {
            "possession": possession,
            "shootHeading": shootHeading,
            "goalInPenalty": goalInPenalty,
            "goalHeading": goalHeading,
            "goalTotal": goalTotal,
            "bouncingLobPassSuccess": bouncingLobPassSuccess,
            "goalTotalDisplay": goalTotalDisplay,
            "bouncingLobPassTry": bouncingLobPassTry,
            "current_rank": current_rank,
        }
    except ValueError:
        print("잘못된 입력입니다. 숫자를 입력해주세요.")
        return None

def send_request(data):
    """API 요청을 보내는 함수"""
    try:
        response = requests.post('http://localhost:8000/predict', json=data)
        response.raise_for_status()  # HTTP 오류 발생 시 예외 발생
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"요청 실패: {e}")
        return None

def main():
    """메인 함수"""
    data = get_user_input()
    if data:
        result = send_request(data)
        if result:
            print("예측 결과:", result['message'])

if __name__ == "__main__":
    main()
