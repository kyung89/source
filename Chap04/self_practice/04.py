# 4. OpenCV이 제공하는, 마우스 이벤트와 트랙바 이벤트를 제어할 콜백 함수를 시스템에 등록하는 함수는 각각 무엇이며, 인수가 어떻게 구성되었는지 자세히 설명하시오.

# 마우스 이벤트 콜백 함수

# onMouse(event, x, y, flags, params=None)

# event: 발생한 마우스 이벤트의 종류
# x, y: 이벤트 발생 시 마우스 포인터의 x, y 좌표
# flags: 마우스 버튼과 동시에 특수키를 눌렀는지 여부 확인
# params: 콜백 함수로 전달하는 추가적인 사용자 정의 인수

# 마우스 이벤트 종류

# cv2.EVENT_MOUSEMOVE
# cv2.EVENT_LBUTTONDOWN
# cv2.EVENT_RBUTTONDOWN
# cv2.EVENT_MBUTTONDOWN
# cv2.EVENT_LBUTTONUP
# cv2.EVENT_RBUTTONUP
# cv2.EVENT_MBUTTONUP
# cv2.EVENT_LBUTTONDBCLK
# cv2.EVENT_RBUTTONDBCLK
# cv2.EVENT_MBUTTONDBCLK
# cv2.EVENT_MOUSEWHEEL
# cv2.EVENT_MOUSEHWHEEL

# flags

# cv2.EVENT_FLAG_LBUTTON
# cv2.EVENT_FLAG_RBUTTON
# cv2.EVENT_FLAG_MBUTTON
# cv2.EVENT_FLAG_CTRLKEY
# cv2.EVENT_FLAG_SHIFTKEY
# cv2.EVENT_FLAG_ALTKEY

# 트랙바 이벤트 콜백 함수

# onChange(pos) -> None

# pos: 트랙바 슬라이더 위치