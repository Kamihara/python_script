#from oaiso.models import Shop_test, Label_first
import numpy as np

def sample():
	id_list = Label_first.objects.values_list('id', flat=True).order_by('id')
	return id_list

# 何らかの計算結果の降順(大きい順)に飲食店のidを返す関数
def return_id(sim_list):
	sim_list_sort = sorted(sim_list, key=lambda x:x[1], reverse=True)
	sim_array = np.array(sim_list_sort)
	id_list = list(map(int, list(sim_array[:, 0])))
	return id_list

def cos_sim(v1, v2):
	# コサイン類似度
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


# 内容ベースフィルタリング関数
def contents_filter(uvec):
	sim_list = []	#cos類似度の計算結果リストの初期化
	user_vec = np.array(uvec)	#ユーザベクトル(user_vec)をNumPy配列で受け取り

	#飲食店のラベリングテーブル(oaiso.oaiso_label_first)の呼び出し
	for label in Label_first.objects.all().values_list().order_by('id'):
		list_label = list(label)

		shop_id = list_label[0]	#飲食店のid
		shop_vec = np.array(list_label[1:])	#飲食店の特徴ベクトル(NumPy配列)

		sim_score = cos_sim(user_vec, shop_vec)

		sim_list.append([shop_id, sim_score])	#飲食店のidとそのお店のcos類似度が入った二次元リストを作成

	return return_id(sim_list)	#cos類似度順に並び替えたidを返す



if __name__ == '__main__':
	user_vec = np.array([0, 1, 0, 1, 0.5, 0, 0, 1, 0])
	list_labels = [[1, 1, 0, 0, 1, 0, 0.5, 0, 0, 1],
				   [2, 1, 0, 0, 0, 1, 0, 0, 1, 0],
				   [3, 1, 0, 0, 0, 0, 0, 1, 1, 0],
				   [4, 1, 0, 0, 0, 0, 1, 0.5, 1, 0],
				   [5, 0, 1, 0, 1, 0, 0, 0, 1, 0],
				   [6, 1, 0, 0, 1, 0.5, 0, 0, 1, 0],
				   [7, 0, 1, 0, 0, 1, 0.5, 0, 1, 0],
				   [8, 0, 1, 0, 0, 1, 0.5, 0, 1, 0],
				   [9, 0, 1, 0, 1, 0, 0.5, 0, 0, 1],
				   [10, 1, 0, 0, 1, 0, 0, 0, 1, 0]
				   ]
	sim_list = []

	for list_label in list_labels:

		shop_id = list_label[0]	#飲食店のid
		shop_vec = np.array(list_label[1:])	#飲食店の特徴ベクトル(NumPy配列)

		sim_score = cos_sim(user_vec, shop_vec)

		sim_list.append([shop_id, sim_score])	#飲食店のidとそのお店のcos類似度が入った二次元リストを作成
		print(shop_id, sim_score)

	for id in return_id(sim_list):	#cos類似度順に並び替えたidを返す
		print(id)