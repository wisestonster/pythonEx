# 원화(￦)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    return krw / 1000


# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    return (usd / 8) * 1000


# 원화(￦)으로 각각 얼마인가요?
prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(prices))
 
i = 0
while i < 8:
    prices[i] = krw_to_usd(prices[i]);
    i += 1
print("미국 화폐: " + str(prices));

i = 0
while i < 8:
    prices[i] = usd_to_jpy(prices[i]);
    i += 1
print("일본 화폐: " + str(prices));
