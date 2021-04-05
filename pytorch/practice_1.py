from __future__ import print_function
import torch

#### 기본 ####
# 초기화되지 않은 5*3 행렬 생성하기
x = torch.empty(5, 3)
print(x)

# 난수로 초기화된 행렬 생성하기
x = torch.rand(5, 3)
print(x)

# 데이터를 넣어서 직접 생성하기
x = torch.tensor([5.5, 3])
print(x)

# 텐서 선언, 선언된 텐서의 속성을 가지고 새로운 텐서 생성
x = x.new_ones(5,3,dtype = torch.double) # new_* 메소드는 크기를 받습니다.
print(x)
x = torch.rand_like(x, dtype = torch.float) # dtype을 오버라이드
print(x)                                    # 결과는 같은 크기
# 행렬 사이즈 측정
print(x.size())

#### 연산하기 (덧셈) ####
# 문법1
y = torch.rand(5, 3)
print(x + y)
# 문법2
print(torch.add(x, y))
# 결과를 인자로 다른텐서에 제공하기
result = torch.empty(5, 3)
torch.add(x, y, out = result)
print(result)
# in-place 방식
y.add_(x)

#### 크기 변경 ####
x = torch.randn(4, 4)
y = x.view(16)
z = x.view(-1, 8) # -1은 다른 차원에서 유추
print(x.size(), y.size(), z.size())

#### 값 추출 ####
x = torch.randn(1) # 값이 하나일때만 사용가능
print(x)
print(x.item())

#### NumPy로 다시 변환 ####
a = torch.ones(5)
print(a)

b = a.numpy()
print(b)

a.add_(1)
print(a)
print(b)

#### NumPy -> torch ####
import numpy as np
a = np.ones(5)
b = torch.from_numpy(a)
np.add(a, 1, out=a)
print(a)
print(b)





