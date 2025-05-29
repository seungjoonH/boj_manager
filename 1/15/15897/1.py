def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1  # i는 약수
            if i != n // i:
                count += 1  # n // i도 약수 (i와 다를 경우)
    return count

n = int(input("숫자를 입력하세요: "))
print(f"{n}의 약수 개수는 {count_divisors(n)}개 입니다.")
