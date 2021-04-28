#!/usr/bin/python
# coding: utf-8

import numpy as np


def cos_sim(v1, v2):
    # コサイン類似度
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))



if __name__ == '__main__':
    # [価格（低）, 価格（中）, 価格（高）, 食べ重視, 飲み重視, 雰囲気重視, サクッと, 一人◯, 一人×]
    user_vec1   = np.array([0, 1, 0, 1, 0.5, 0, 0, 1, 0]) # ユーザインプットから生成される
    user_vec2   = np.array([1, 0, 0, 0, 0, 0, 1, 0, 1])   # ユーザインプットから生成される

    shop_vec1   = np.array([1, 0, 0, 1, 0, 0.5, 0, 0, 1]) # 151A
    shop_vec2   = np.array([1, 0, 0, 0, 1, 0, 0, 1, 0])   # ロカロ
    shop_vec3   = np.array([1, 0, 0, 0, 0, 0, 1, 1, 0])   # BEE
    shop_vec4   = np.array([1, 0, 0, 0, 0, 1, 0.5, 1, 0]) # CAFE AND BAR sweet
    shop_vec5   = np.array([0, 1, 0, 1, 0, 0, 0, 1, 0])   # 北一倶楽部
    shop_vec6   = np.array([1, 0, 0, 1, 0.5, 0, 0, 1, 0]) # CHAP
    shop_vec7   = np.array([0, 1, 0, 0, 1, 0.5, 0, 1, 0]) # KIYOMI
    shop_vec8   = np.array([0, 1, 0, 0, 1, 0.5, 0, 1, 0]) # Gecky
    shop_vec9   = np.array([0, 1, 0, 1, 0, 0.5, 0, 0, 1]) # H
    shop_vec10  = np.array([1, 0, 0, 1, 0, 0, 0, 1, 0])   # maru


    print("user1とのコサイン類似度") # 1に近いほうが類似度が高い
    print(cos_sim(user_vec1, shop_vec1))
    print(cos_sim(user_vec1, shop_vec2))
    print(cos_sim(user_vec1, shop_vec3))
    print(cos_sim(user_vec1, shop_vec4))
    print(cos_sim(user_vec1, shop_vec5))
    print(cos_sim(user_vec1, shop_vec6))
    print(cos_sim(user_vec1, shop_vec7))
    print(cos_sim(user_vec1, shop_vec8))
    print(cos_sim(user_vec1, shop_vec9))
    print(cos_sim(user_vec1, shop_vec10))


    print("user2とのコサイン類似度") # 1に近いほうが類似度が高い
    print(cos_sim(user_vec2, shop_vec1))
    print(cos_sim(user_vec2, shop_vec2))
    print(cos_sim(user_vec2, shop_vec3))
    print(cos_sim(user_vec2, shop_vec4))
    print(cos_sim(user_vec2, shop_vec5))
    print(cos_sim(user_vec2, shop_vec6))
    print(cos_sim(user_vec2, shop_vec7))
    print(cos_sim(user_vec2, shop_vec8))
    print(cos_sim(user_vec2, shop_vec9))
    print(cos_sim(user_vec2, shop_vec10))

